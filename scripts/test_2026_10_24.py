from playwright.sync_api import sync_playwright
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
slugs=['fencebid','mulchcompare','weddingflow','turnoverbudget','feenet']
res=[]
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
    for slug in slugs:
        page=browser.new_page(viewport={'width':390,'height':844},accept_downloads=True)
        errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
        html=(ROOT/'dist/tools'/slug/'index.html').read_text(encoding='utf-8')
        page.set_content(html,wait_until='load')
        page.wait_for_timeout(200)
        title=page.title()
        assert page.locator('h1').count()>0
        assert page.locator('meta[name=robots]').get_attribute('content')=='noindex,follow'
        assert page.locator('.wl-guide').count()==1
        if slug=='fencebid':
            assert page.locator('#total').inner_text()=='$5,163.40'
            page.locator('#add').click();assert page.locator('#runs .row').count()==3
            page.locator('#span').fill('6');assert '$' in page.locator('#total').inner_text()
        elif slug=='mulchcompare':
            assert page.locator('#bagTotal').inner_text()=='$115.50'
            page.locator('#add').click();assert page.locator('#beds .row').count()==3
            page.locator('#bagPrice').fill('100');assert 'Bulk is cheaper' in page.locator('#winner').inner_text()
        elif slug=='weddingflow':
            assert page.locator('#timeline li').count()>=5
            page.locator('#coverage').fill('2');assert 'Coverage conflict' in page.locator('#coverageStatus').inner_text()
            with page.expect_download() as d:page.locator('#ics').click()
            assert d.value.suggested_filename.endswith('.ics')
        elif slug=='turnoverbudget':
            assert page.locator('#planned').inner_text()=='$1,850.00'
            page.locator('#add').click();assert page.locator('#items .row').count()==4
            page.locator('#rent').fill('3000');assert '$' in page.locator('#actual').inner_text()
        elif slug=='feenet':
            assert 'Processing fees' in page.locator('#comparison').inner_text()
            assert '$9,640' in page.locator('#comparison').inner_text()
            page.locator('#rateA').fill('5');assert 'costs' in page.locator('#winner').inner_text()
        if slug!='weddingflow':
            with page.expect_download() as d:page.locator('#export').click()
            assert d.value.suggested_filename.endswith('.csv')
        page.wait_for_timeout(100)
        overflow=page.evaluate('document.documentElement.scrollWidth > window.innerWidth+1')
        assert not overflow,(slug,page.evaluate('document.documentElement.scrollWidth'))
        assert not errors,(slug,errors)
        res.append({'slug':slug,'title':title,'mobile_width':390,'javascript_errors':errors,'horizontal_overflow':overflow,'download':'PASS'})
        page.close()
    browser.close()
(ROOT/'QA_RESULTS_2026-10-24.json').write_text(json.dumps({'checks':res,'note':'Chromium page.set_content() smoke tests, not live HTTPS/Safari'},indent=2))
print('PASS',len(res),'tools: core interactions, file export, mobile layout, no JS exceptions')
