#!/usr/bin/env python3
"""Build Worklane Tools into dist/; safe preview defaults to noindex and no advertising."""
import argparse, datetime, html, json, os, re, shutil
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'content/catalog.json'
MONETIZATION = ROOT / 'content/monetization.json'
ANALYTICS = ROOT / 'content/analytics.json'
DIST = ROOT / 'dist'


def h(v): return html.escape(str(v), quote=True)

def url_path(host, path): return host.rstrip('/') + path if host else ''


def analytics_config(site_url, override=None):
    c = override if override is not None else (json.loads(ANALYTICS.read_text()) if ANALYTICS.exists() else {})
    enabled = c.get('enabled', False)
    if not isinstance(enabled, bool): raise ValueError('Analytics enabled must be boolean')
    if enabled:
        if c.get('provider') != 'umami' or c.get('consent_required') is not True or c.get('privacy_ready') is not True:
            raise ValueError('Analytics requires reviewed Umami configuration and explicit consent')
        if not re.fullmatch(r'[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}', c.get('website_id','')):
            raise ValueError('Analytics requires the real website UUID')
        if c.get('script_url') != 'https://cloud.umami.is/script.js':
            raise ValueError('Analytics script must be the reviewed Umami Cloud endpoint')
        if c.get('data_region') not in ('EU','US') or not c.get('operator_name','').strip():
            raise ValueError('Analytics requires verified storage region and operator')
        if not re.fullmatch(r'[a-z0-9.-]+',c.get('site_hostname','')):
            raise ValueError('Analytics requires the reviewed website hostname')
        if not re.fullmatch(r'[^\s<>@]+@[^\s<>@]+\.[^\s<>@]+', c.get('privacy_contact','')):
            raise ValueError('Analytics requires a public privacy contact')
    return {**c, 'configured': enabled, 'enabled': enabled and bool(site_url) and urlparse(site_url).hostname==c.get('site_hostname'),
            'hostname': urlparse(site_url).hostname if site_url else ''}


def analytics_markup(c, path, title, tool, html_source):
    actions = sorted(set(re.findall(r'<button\b[^>]*\bid=[\"\']([A-Za-z][\w-]{0,63})[\"\']', html_source))) if tool else []
    public = {k:c[k] for k in ('enabled','website_id','script_url','hostname')}
    public.update(path=path, title=title, tool=tool, actions=actions)
    data = json.dumps(public, ensure_ascii=False).replace('<','\\u003c')
    return '<script id="wl-analytics-config" type="application/json">'+data+'</script>\n<script defer src="/assets/usage-analytics.js"></script>'

def css():
    return '''<style id="worklane-ui">
.wl-header,.wl-footer,.wl-guide,.wl-main,.wl-disclosure{font-family:Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;color:#193446;box-sizing:border-box}
.wl-header *,.wl-footer *,.wl-guide *,.wl-main *,.wl-disclosure *{box-sizing:border-box}
.wl-header{background:white;border-bottom:1px solid #dce7e9;position:relative;z-index:12}
.wl-container{max-width:1160px;margin:auto;padding-left:20px;padding-right:20px}
.wl-top{min-height:64px;display:flex;align-items:center;justify-content:space-between;gap:18px}
.wl-logo{font-size:19px;font-weight:900;text-decoration:none!important;color:#0b6c6a!important;letter-spacing:-.5px}
.wl-links{display:flex;gap:18px;flex-wrap:wrap}.wl-links a{font-size:13px;color:#526b78!important;font-weight:700;text-decoration:none}
.wl-guide{background:#f5f9f8;padding:40px 0 55px;border-top:1px solid #e0e9ea}
.wl-guide h2{font-size:26px;margin:0 0 8px;color:#143344;letter-spacing:-.5px}.wl-guide h3{font-size:18px;color:#143344;margin:12px 0}.wl-guide p,.wl-guide li{color:#425f6b;line-height:1.65}
.wl-guide li{margin:8px 0}.wl-columns{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.wl-panel{background:#fff;border:1px solid #deebeb;padding:22px;border-radius:17px;min-width:0}
.wl-disclosure{font-size:13px;background:#eaf4f1;padding:12px 0;border-bottom:1px solid #d6e8e3;color:#3d625e}
.wl-footer{background:#12303b;padding:33px 0;color:#c4d6dc!important;font-size:13px}
.wl-footer a{color:#dbe8eb!important;text-decoration:none;margin-right:17px}.wl-footer p{margin:14px 0 0;color:#b6cfd5}
.wl-pill{display:inline-block;background:#e3f3ee;color:#0c635d!important;font-size:12px;font-weight:800;border-radius:50px;padding:5px 10px}
@media(max-width:640px){.wl-links{gap:10px}.wl-links a{font-size:12px}.wl-columns{grid-template-columns:1fr}}
@media print{.wl-header,.wl-guide,.wl-footer,.wl-disclosure{display:none!important}}
</style>'''


def head_base(title, description, canonical='', robots='noindex,follow', ads='', verification_publisher=''):
    tags = [f'<meta name="robots" content="{robots}">',
            '<meta name="color-scheme" content="light">',
            '<meta name="theme-color" content="#0b6c6a">']
    if canonical:
        tags.extend([f'<link rel="canonical" href="{h(canonical)}">',
                     f'<meta property="og:url" content="{h(canonical)}">',
                     '<meta property="og:type" content="website">'])
    if verification_publisher:
        tags.append(f'<meta name="google-adsense-account" content="{h(verification_publisher)}">')
    if ads:
        tags.append(f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={h(ads)}" crossorigin="anonymous"></script>')
    return '\n'.join(tags)


def frame_header(brand):
    return f'''<div class="wl-header"><div class="wl-container wl-top">
<a class="wl-logo" href="/">{h(brand)}</a>
<nav class="wl-links" aria-label="Main navigation"><a href="/#tools">Browse tools</a><a href="/about/">About</a><a href="/privacy/">Privacy</a></nav>
</div></div>'''


def frame_footer(brand):
    return f'''<footer class="wl-footer"><div class="wl-container">
<strong>{h(brand)}</strong> — Practical, lightweight browser tools.<div style="margin-top:11px">
<a href="/">Home</a><a href="/about/">About</a><a href="/privacy/">Privacy</a><a href="/terms/">Terms</a></div>
<p>These tools are independent prototypes. Export important records; browser storage may be cleared. No cloud backup is offered.</p>
</div></footer>'''


def guide(tool, siblings):
    howto = ''.join('<li>'+h(step)+'</li>' for step in tool['howto'])
    related = ''.join(f'<li><a href="/tools/{h(t["slug"])}/">{h(t["name"])} — {h(t["headline"])}</a></li>' for t in siblings)
    return f'''<section class="wl-guide" aria-labelledby="wl-guide-title"><div class="wl-container">
<span class="wl-pill">Free web tool · No account required</span>
<h2 id="wl-guide-title">How to use {h(tool['name'])}</h2>
<p>{h(tool['best_for'])}</p><div class="wl-columns">
<div class="wl-panel"><h3>Step-by-step workflow</h3><ol>{howto}</ol></div>
<div class="wl-panel"><h3>Important limits</h3><p>{h(tool['limitations'])}</p><h3>{h(tool['faq_question'])}</h3><p>{h(tool['faq_answer'])}</p></div>
</div><div class="wl-panel" style="margin-top:18px"><h3>Explore other free tools</h3><ul>{related}</ul></div>
</div></section>'''


def home_html(catalog, site_url, prod, ads, verification_publisher=''):
    brand = catalog['brand']; title = 'Worklane Tools | Free Browser Tools for Independent Professionals'
    desc = catalog['description']
    cards=[]
    for t in catalog['tools']:
        cards.append(f'''<a class="toolcard" data-category="{h(t['category'])}" data-search="{h(' '.join([t['headline'],t['audience']]+t['keywords']).lower())}" href="/tools/{h(t['slug'])}/">
<div class="toolbadge">{t['emoji']} &nbsp;{h(t['audience'])}</div><h3>{h(t['headline'])}</h3><p>{h(t['description'])}</p>
<div class="visit">Open free tool <span aria-hidden="true">↗</span></div></a>''')
    schema={'@context':'https://schema.org','@type':'WebSite','name':brand,'url':site_url} if site_url else None
    schema_tag='<script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False).replace('</','<\\/')+'</script>' if schema else ''
    home_style='''<style>*{box-sizing:border-box}body{margin:0;background:#f6faf9;color:#183746;font-family:Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;line-height:1.6}a{color:#08766d}.hero{background:radial-gradient(ellipse at 88% 5%,#d3ede7,transparent 48%),linear-gradient(125deg,#f3faf7,#fff);padding:74px 0 70px}.eyebrow{color:#0e7770;text-transform:uppercase;letter-spacing:2px;font-size:12px;font-weight:900}.hero h1{font-size:clamp(36px,5.5vw,68px);max-width:850px;letter-spacing:-2.5px;line-height:1.04;margin:14px 0 18px}.hero p{max-width:760px;font-size:19px;color:#506c76;margin:0}.stats{display:flex;gap:9px;margin-top:25px;flex-wrap:wrap}.stats span{padding:8px 13px;border:1px solid #cadfdb;border-radius:99px;color:#225f5b;background:white;font-size:12px;font-weight:750}.section{padding:52px 0 70px}.section h2{font-size:31px;letter-spacing:-.7px;margin:0 0 7px}.lead{color:#5b7480;margin:0 0 25px}.bar{display:flex;gap:12px;margin:18px 0 28px;align-items:center;flex-wrap:wrap}.bar input{max-width:480px;flex:1;min-width:200px;border:1px solid #cbdedc;border-radius:10px;padding:13px;font:inherit;background:#fff}.filters{display:flex;flex-wrap:wrap;gap:8px}.filters button{padding:10px 13px;background:white;border:1px solid #cfdddb;border-radius:99px;color:#2a5a5a;cursor:pointer}.filters button[aria-pressed=true]{background:#0b716a;color:white}.cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}.toolcard{display:flex;flex-direction:column;gap:6px;padding:25px;border:1px solid #d9e6e5;background:#fff;border-radius:18px;box-shadow:0 10px 24px rgba(19,65,64,.04);color:inherit;text-decoration:none;transition:transform .15s}.toolcard:hover{transform:translateY(-3px)}.toolcard h3{font-size:21px;line-height:1.22;margin:7px 0;letter-spacing:-.3px}.toolcard p{font-size:14px;line-height:1.58;color:#59717b;margin:2px 0 9px;flex:1}.toolbadge{color:#0b706b;font-size:12px;font-weight:800;text-transform:uppercase;letter-spacing:.4px}.visit{font-size:13px;font-weight:800;color:#0c6c67}.who{padding:42px 0 60px;background:#eaf5f1}.who p{max-width:760px;color:#4f6b72}.notice{font-size:13px;color:#5d7480}.hidden{display:none!important}@media(max-width:980px){.cards{grid-template-columns:repeat(2,1fr)}}@media(max-width:640px){.cards{grid-template-columns:1fr}.hero{padding:45px 0}.section{padding:35px 0}.hero h1{letter-spacing:-1.3px}} </style>'''
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{h(title)}</title><meta name="description" content="{h(desc)}">
<meta property="og:title" content="{h(title)}"><meta property="og:description" content="{h(desc)}">
{head_base(title,desc,url_path(site_url,'/'), 'index,follow' if prod else 'noindex,follow',ads,verification_publisher)}
{css()}{home_style}{schema_tag}</head><body>
{frame_header(brand)}<main>
<section class="hero"><div class="wl-container"><div class="eyebrow">Tools built for real work</div>
<h1>Small tools. Less busywork.</h1><p>Free, focused browser tools for independent professionals. Estimate a job, organize rental records, define photography usage or price your freelance work—without creating an account.</p>
<div class="stats"><span>{len(catalog["tools"])} practical tools</span><span>Browser-first</span><span>No account for free features</span><span>Mobile friendly</span></div></div></section>
<section class="section wl-container" id="tools"><h2>Explore free work tools</h2><p class="lead">Pick a job, complete it quickly, and export what you create.</p>
<div class="bar"><input id="toolSearch" type="search" placeholder="Search tools or your profession" aria-label="Search tools">
<div class="filters" id="filters"><button data-cat="all" aria-pressed="true">All</button><button data-cat="contractors">Contractors</button><button data-cat="landlords">Landlords</button><button data-cat="photographers">Photographers</button><button data-cat="freelancers">Freelancers</button><button data-cat="notaries">Notaries</button><button data-cat="cleaning">Cleaning</button></div></div>
<div class="cards" id="catalogCards">{''.join(cards)}</div><p id="noResults" class="notice hidden">No matching tools found. Try a different search.</p></section>
<section class="who"><div class="wl-container"><h2>Tools that respect your time</h2><p>The free core features run in your browser. Some tools store records on your device; others use temporary browser memory. We do not offer account sync, server storage, automated email sending or payment processing in these demos. Export records you need to keep.</p><p>These tools are intentionally narrow: finish a real task first, without learning a complicated dashboard.</p></div></section>
</main>{frame_footer(brand)}
<script>const q=document.getElementById('toolSearch');const cards=[...document.querySelectorAll('.toolcard')];let category='all';
function filter(){{let val=q.value.trim().toLowerCase(),n=0;cards.forEach(c=>{{let ok=(category==='all'||c.dataset.category===category)&&c.dataset.search.includes(val);c.classList.toggle('hidden',!ok);if(ok)n++}});document.getElementById('noResults').classList.toggle('hidden',n>0)}}
q.addEventListener('input',filter);document.getElementById('filters').addEventListener('click',e=>{{if(e.target.matches('button')){{category=e.target.dataset.cat;document.querySelectorAll('[data-cat]').forEach(b=>b.setAttribute('aria-pressed',b===e.target?'true':'false'));filter()}}}});
</script></body></html>'''


def info_page(title, paragraphs, brand, site_url, path, prod, ads='', verification_publisher=''):
    body = ''.join(f'<p>{p}</p>' for p in paragraphs)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{h(title)} | {h(brand)}</title><meta name="description" content="{h(re.sub('<[^>]*>', '', paragraphs[0])[:156])}">
{head_base(title,paragraphs[0],url_path(site_url,path), 'index,follow' if prod else 'noindex,follow',ads,verification_publisher)}
{css()}<style>body{{margin:0;background:#f6faf9;font-family:system-ui,sans-serif;line-height:1.7;color:#274454}}.wl-article{{max-width:780px;margin:60px auto 90px;padding:0 20px}}.wl-article h1{{font-size:40px;letter-spacing:-1px}}.wl-article p{{color:#536a78}}.wl-article a{{color:#08766d}}</style></head><body>{frame_header(brand)}
<main class="wl-article"><h1>{h(title)}</h1>{body}</main>{frame_footer(brand)}</body></html>'''


def build(production=False, site_url='', adsense='', ads_approved=False, privacy_ready=False, verification_publisher=None):
    cfg=json.loads(CATALOG.read_text(encoding='utf-8'))
    if verification_publisher is None:
        monetization=json.loads(MONETIZATION.read_text(encoding='utf-8')) if MONETIZATION.exists() else {}
        verification_publisher=monetization.get('adsense_verification_publisher','')
    site_url=site_url.strip().rstrip('/')
    if site_url:
        parsed=urlparse(site_url)
        if (parsed.scheme!='https' or not parsed.hostname or parsed.hostname.endswith(('.example','.invalid','.test'))
                or 'localhost' in parsed.hostname or parsed.path or parsed.query or parsed.fragment or parsed.username):
            raise ValueError('SITE_URL must be a real HTTPS origin (no placeholder or path)')
    elif production:
        raise ValueError('Production requires --site-url with a real HTTPS origin')
    analytics=analytics_config(site_url)
    if not isinstance(verification_publisher,str) or (verification_publisher and not re.fullmatch(r'ca-pub-\d{16}',verification_publisher)):
        raise ValueError('Verification publisher must match ca-pub- followed by 16 digits')
    if adsense and not re.fullmatch(r'ca-pub-\d{16}',adsense):
        raise ValueError('AdSense ID must match ca-pub- followed by 16 digits')
    if adsense and not (production and ads_approved and privacy_ready):
        raise ValueError('AdSense requires --production --ads-approved --privacy-ready; no ads served before review')
    if adsense and verification_publisher and adsense!=verification_publisher:
        raise ValueError('Advertising and verification publishers must match')
    publisher=verification_publisher or adsense
    slugs=[t['slug'] for t in cfg['tools']]
    if len(set(slugs))!=len(slugs) or not all(re.fullmatch(r'[a-z][a-z0-9-]+',s) for s in slugs):
        raise ValueError('Invalid/duplicate slugs')
    if DIST.exists(): shutil.rmtree(DIST)
    DIST.mkdir(parents=True)
    approved_count=sum(bool(t.get('approved_for_index') and t.get('evidence_reviewed') and t.get('qa_verified')) for t in cfg['tools'])
    homepage_indexable=production and approved_count>0
    ads_enabled=bool(adsense and homepage_indexable)
    (DIST/'index.html').write_text(home_html(cfg,site_url,homepage_indexable,adsense if homepage_indexable else '',publisher),encoding='utf-8')
    # A root 404.html prevents Pages from serving the homepage with HTTP 200
    # for every unknown route under its default single-page-app fallback.
    (DIST/'404.html').write_text(info_page('Page not found',
        ['This page could not be found. <a href="/">Browse the available tools</a>.'],
        cfg['brand'],site_url,'/404.html',False,verification_publisher=publisher),encoding='utf-8')
    sitemap=['/'] if homepage_indexable else []
    for t in cfg['tools']:
        dest=DIST/'tools'/t['slug'];dest.mkdir(parents=True,exist_ok=True)
        base=(ROOT/'apps'/t['slug']/'index.html').read_text(encoding='utf-8')
        published=production and t.get('approved_for_index',False) and t.get('evidence_reviewed',False) and t.get('qa_verified',False)
        canonical=url_path(site_url,f'/tools/{t["slug"]}/')
        meta=head_base(t['headline'],t['description'],canonical,'index,follow' if published else 'noindex,follow',adsense if published else '',publisher)
        base=base.replace('</head>', '\n'+meta+css()+'</head>',1)
        base=base.replace('<body>','<body>'+frame_header(cfg['brand']),1)
        # Attach genuine, static instructions and disclosure; do not replace the tool functionality.
        next_tools=sorted([x for x in cfg['tools'] if x['slug']!=t['slug']], key=lambda x: (x['category']!=t['category'], x['slug']))[:3]
        base=base.replace('</body>',guide(t,next_tools)+frame_footer(cfg['brand'])+'</body>',1)
        (dest/'index.html').write_text(base,encoding='utf-8')
        if published: sitemap.append(f'/tools/{t["slug"]}/')
    about=[
        'Worklane Tools is a small collection of focused web utilities for independent professionals, including contractors, landlords, photographers and freelancers.',
        'Our approach: make the free core workflow functional without requiring an account. Tools are intentionally lightweight rather than full business management services.',
        'Important: This project is an early-stage prototype collection. Some ideas and paid features are still research hypotheses. The tools are not professional legal, tax or accounting advice.',
        'We do not claim to offer cloud backups. If you use a tool to create important records, export them and keep independent copies.'
    ]
    ad_notice = (
        'Advertising and cookies: Google AdSense is configured for this site. Third-party vendors, including Google, may use cookies to serve ads based on visits to this and other websites. Learn about ad personalization at <a href="https://adssettings.google.com/">Google Ads Settings</a>. Required region-specific consent and opt-out mechanisms must be implemented and tested before serving ads where applicable.'
        if ads_enabled else
        ('Advertising setup: this site publishes a Google AdSense ownership-verification meta tag and an ads.txt seller record. These static records do not load advertising scripts or serve ads. Advertising is not enabled in this build. Before ads are enabled, this policy and the applicable consent and opt-out controls must be updated and tested.'
         if publisher else
         'Analytics and advertising: paid advertising is not enabled in this build. If Google AdSense or analytics are activated later, this policy must be updated to describe actual data collection, cookies, ad personalization and user choices.')
    )
    privacy=[
        'Privacy overview: the current free tools perform their core tasks locally in your browser. We do not run a central account database or intentionally receive your project photos, invoices or trip records through these forms.',
        'Local storage: some tools save entries in the browser localStorage; others use temporary browser memory. You can clear this data with your browser controls. Export your work before clearing site data.',
        ad_notice,
        'Never enter highly sensitive information into prototypes. Review privacy disclosures, legal obligations and contact information before taking this project live as a commercial service.'
    ]
    if analytics['enabled']:
        privacy += [
            'Optional usage analytics: only after you accept, we load Umami Cloud to measure page paths, referring site origins and fixed event names such as tool_start, tool_complete, tool_error and export_generated. Button actions record a reviewed static identifier. Completion is instrumented for Linear Cut Planner; an action click on other tools is not proof of successful completion.',
            'We do not send form values, photographs, filenames, customer details, URL search parameters or fragments. The analytics service still processes connection information (including IP address and browser headers) to receive and derive aggregate visit information. Analytics is optional; rejecting it does not affect tools.',
            'The selected Umami Cloud analytics storage region is '+h(analytics['data_region'])+'. Cloud retention is six months on the free Hobby plan; CDN, security and operational processing can involve other regions. See <a href="https://umami.is/privacy">Umami privacy information</a>. No session replay or advertising personalization is enabled.',
            'Use Analytics choices in the footer to reject or withdraw. We save only that choice and its timestamp on your device for up to 180 days. Withdrawal stops future events; it does not automatically erase previously collected records. Browser privacy signals keep analytics off. Consent-based statistics omit visitors who decline or block collection and are not a complete count of all traffic.',
            'Operator: '+h(analytics['operator_name'])+'. For privacy questions or rights requests, contact <a href="mailto:'+h(analytics['privacy_contact'])+'">'+h(analytics['privacy_contact'])+'</a>. Do not post personal records in public repository issues.'
        ]
    terms=[
        'These free tools are provided as prototypes, on an as-is and as-available basis, without guaranteed accuracy, retention, continuity or availability.',
        'You are responsible for checking the accuracy, completeness and suitability of generated reports, invoice reminders, estimates and other records before relying on them.',
        'Do not use prototype exports as the sole record for legal disputes, financial reporting, tax compliance or other high-impact decisions.',
        'The project does not yet support accounts, cloud backups or paid subscriptions. Any displayed Pro pricing is an exploratory hypothesis, not a current offer for sale.'
    ]
    for slug,title,paras in [('about','About Us',about),('privacy','Privacy Policy',privacy),('terms','Terms & Limitations',terms)]:
        dest=DIST/slug;dest.mkdir(exist_ok=True)
        # Legal templates are available for human review; do not index as marketing pages in the initial release.
        (dest/'index.html').write_text(info_page(title,paras,cfg['brand'],site_url,f'/{slug}/',False,verification_publisher=publisher),encoding='utf-8')
    review_crawlers=('User-agent: Mediapartners-Google\nAllow: /\n\nUser-agent: Google-Display-Ads-Bot\nAllow: /\n\n') if publisher else ''
    if production:
        urls=''.join(f'<url><loc>{h(site_url+p)}</loc></url>' for p in sitemap)
        (DIST/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+urls+'</urlset>',encoding='utf-8')
        (DIST/'robots.txt').write_text(review_crawlers+'User-agent: *\nAllow: /\nSitemap: '+site_url+'/sitemap.xml\n',encoding='utf-8')
    else:
        # Public preview pages must be crawlable for their noindex directives to be read.
        # Private content requires authentication; robots.txt is never access control.
        (DIST/'robots.txt').write_text(review_crawlers+'User-agent: *\nAllow: /\n',encoding='utf-8')
        (DIST/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"/>',encoding='utf-8')
    if publisher:
        (DIST/'ads.txt').write_text(f'google.com, {publisher.removeprefix("ca-")}, DIRECT, f08c47fec0942fa0\n',encoding='utf-8')
    if analytics['enabled']:
        (DIST/'assets').mkdir(exist_ok=True)
        shutil.copyfile(ROOT/'assets/usage-analytics.js', DIST/'assets/usage-analytics.js')
        by_path={f'/tools/{t["slug"]}/':t for t in cfg['tools']}
        for page in DIST.rglob('index.html'):
            relative=page.relative_to(DIST).parent.as_posix()
            path='/' if relative=='.' else '/'+relative+'/'
            tool=by_path.get(path)
            source=page.read_text(encoding='utf-8')
            source=source.replace('No analytics, advertising pixels, server-side storage, or account system in this MVP.', 'Optional usage analytics runs only after your consent. No advertising pixels, server-side storage of form records, or account system is used.')
            source=source.replace('No account, uploads, advertising scripts or analytics are used by this tool.', 'No account, uploads or advertising scripts are used by this tool. Optional usage analytics runs only after your consent.')
            source=source.replace('</body>', analytics_markup(analytics,path,tool['name'] if tool else cfg['brand']+' '+path,tool['slug'] if tool else '',source)+'</body>',1)
            page.write_text(source,encoding='utf-8')
    report={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'mode':'production' if production else 'preview',
            'site_url':site_url or None,'ads_enabled':ads_enabled,'tools_total':len(slugs),
            'analytics_enabled':analytics['enabled'],'analytics_configured':analytics['configured'],
            'adsense_verification_publisher':publisher or None,'ads_txt_enabled':bool(publisher),
            'adsense_review_crawlers_allowed':bool(publisher),
            'indexable_paths':sitemap, 'draft_paths':[f'/tools/{t["slug"]}/' for t in cfg['tools'] if not (production and t.get('approved_for_index',False) and t.get('evidence_reviewed',False) and t.get('qa_verified',False))],
            'site_map':site_url+'/sitemap.xml' if production else None}
    (DIST/'build-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--production',action='store_true')
    p.add_argument('--site-url',default=os.getenv('SITE_URL',''))
    p.add_argument('--adsense-publisher',default=os.getenv('ADSENSE_PUBLISHER',''))
    p.add_argument('--adsense-verification-publisher',default=os.getenv('ADSENSE_VERIFICATION_PUBLISHER'),help='Ownership meta tag and ads.txt only; defaults to content/monetization.json. Does not enable ads.')
    p.add_argument('--ads-approved',action='store_true',default=os.getenv('ADS_APPROVED')=='1')
    p.add_argument('--privacy-ready',action='store_true',default=os.getenv('PRIVACY_READY')=='1')
    a=p.parse_args();build(a.production,a.site_url,a.adsense_publisher,a.ads_approved,a.privacy_ready,a.adsense_verification_publisher)
