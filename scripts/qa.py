#!/usr/bin/env python3
"""Build output static SEO and safety QA; run after scripts/build.py."""
import json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse,parse_qs
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/'dist'
meta=json.loads((DIST/'build-report.json').read_text())
errors=[]
publisher=meta.get('adsense_verification_publisher')
ad_pages=[]
analytics_pages=[]
def check(condition,msg):
    if not condition:errors.append(msg)
for f in DIST.rglob('index.html'):
    relative_parent=f.relative_to(DIST).parent
    p='/' if str(relative_parent)=='.' else '/'+str(relative_parent).replace('\\','/').strip('/')+'/'
    html=f.read_text(encoding='utf-8'); soup=BeautifulSoup(html,'html.parser')
    check(bool(soup.title and soup.title.get_text(strip=True)),p+': missing title')
    check(bool(soup.find('meta',attrs={'name':'description'})),p+': missing description')
    check(bool(soup.find('meta',attrs={'name':'robots'})),p+': missing robots')
    if meta['site_url']:
        canonical=soup.find('link',rel='canonical')
        check(bool(canonical) and canonical.get('href')==meta['site_url']+p,p+': canonical does not match site URL')
    check(bool(soup.find('h1')),p+': missing h1')
    if p.startswith('/tools/'):
        check(bool(soup.select('.wl-guide h2')),p+': missing static usage guide')
        check(bool(soup.select('.wl-header')),p+': missing shared navigation')
        check(bool(soup.select('button')),p+': tool lacks buttons')
        check(bool(soup.find('meta',attrs={'property':'og:title'})),p+': missing OG title')
        check(bool(soup.find('script',attrs={'type':'application/ld+json'})),p+': missing structured data')
        check(bool(soup.find('script',attrs={'type':None})),p+': missing interactive JS')
    if p in meta['indexable_paths']:
        check(bool(soup.find('link',rel='canonical')),p+': indexable lacks canonical')
        check('noindex' not in str(soup.find('meta',attrs={'name':'robots'})),p+': conflicting noindex')
        check(meta['mode']=='production',p+': preview became indexable')
    else:
        check('noindex' in str(soup.find('meta',attrs={'name':'robots'})),p+': draft inadvertently indexable')
    verification=soup.find_all('meta',attrs={'name':'google-adsense-account'})
    analytics=soup.find_all('script',id='wl-analytics-config')
    check(len(analytics)==(1 if meta.get('analytics_enabled') else 0),p+': analytics configuration mismatch')
    loaders=soup.find_all('script',src='/assets/usage-analytics.js')
    check(len(loaders)==(1 if meta.get('analytics_enabled') else 0),p+': consent controller count mismatch')
    if analytics:
        analytics_pages.append(p)
        settings=json.loads(analytics[0].get_text())
        check(settings['hostname']==urlparse(meta['site_url']).hostname and settings['path']==p,p+': analytics path or host mismatch')
        check(not soup.find('script',src='https://cloud.umami.is/script.js'),p+': third-party tracker bypasses consent controller')
    check(len(verification)==(1 if publisher else 0),p+': verification tag count mismatch')
    if publisher:
        check(all(v.get('content')==publisher and v.parent.name=='head' for v in verification),p+': verification publisher mismatch')
    ad_scripts=[s for s in soup.find_all('script') if 'googlesyndication.com' in s.get('src','') or 'adsbygoogle' in s.get_text()]
    if ad_scripts:
        ad_pages.append(p)
        check(meta['ads_enabled'] and p in meta['indexable_paths'],p+': ad script without approval or on draft')
        for s in ad_scripts:
            src=urlparse(s.get('src',''))
            check(src.scheme=='https' and src.netloc=='pagead2.googlesyndication.com' and src.path=='/pagead/js/adsbygoogle.js' and parse_qs(src.query).get('client')==[publisher],p+': unexpected ad loader/publisher')
check((DIST/'sitemap.xml').exists(),'Missing sitemap')
check((DIST/'robots.txt').exists(),'Missing robots.txt')
not_found=DIST/'404.html'
check(not_found.is_file(),'Missing root 404.html; Pages may serve unknown URLs as HTTP 200')
if not_found.is_file():
    missing=BeautifulSoup(not_found.read_text(encoding='utf-8'),'html.parser')
    check('noindex' in str(missing.find('meta',attrs={'name':'robots'})),'404 page must remain noindex')
    check(not missing.find_all('script'),'404 page must not load advertising or interactive scripts')
ET.parse(DIST/'sitemap.xml')
check(bool(ad_pages)==meta['ads_enabled'],'Ad serving report does not match emitted scripts')
check(bool(analytics_pages)==meta.get('analytics_enabled',False),'Analytics report does not match emitted controller')
check((DIST/'assets/usage-analytics.js').exists()==meta.get('analytics_enabled',False),'Analytics asset activation mismatch')
check((DIST/'ads.txt').exists() == meta.get('ads_txt_enabled',False),'ads.txt activation mismatch')
if publisher:
    check((DIST/'ads.txt').read_text()==f'google.com, {publisher.removeprefix("ca-")}, DIRECT, f08c47fec0942fa0\n','ads.txt publisher mismatch')
robots=RobotFileParser()
robots.parse((DIST/'robots.txt').read_text().splitlines())
for agent in ('Mediapartners-Google','Google-Display-Ads-Bot'):
    check(robots.can_fetch(agent,'/') == (bool(publisher) or meta['mode']=='production'),'Review crawler access mismatch: '+agent)
check(robots.can_fetch('Googlebot','/'),'Search crawler cannot read page indexing directives')
catalog=json.loads((ROOT/'content/catalog.json').read_text(encoding='utf-8'))
for tool in catalog['tools']:
    slug=tool['slug']
    check((DIST/'tools'/slug/'index.html').is_file(),'Missing catalog app '+slug)
check(len(catalog['tools'])==meta['tools_total'],'Catalog total does not match build')
print(('QA FAILED: '+', '.join(errors)) if errors else f'QA PASS: SEO safety, tool routes, sitemap, publisher-code gating and {meta["tools_total"]} app pages.')
sys.exit(1 if errors else 0)
