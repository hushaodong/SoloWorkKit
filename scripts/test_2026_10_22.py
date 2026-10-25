#!/usr/bin/env python3
"""Browser smoke tests for the five new H5 tools."""
from pathlib import Path
from playwright.sync_api import sync_playwright
import subprocess,time,json
R=Path(__file__).resolve().parents[1]
server=subprocess.Popen(['python','-m','http.server','8767','--bind','127.0.0.1','--directory',str(R/'dist')],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
results={}
try:
 time.sleep(.8)
 with sync_playwright() as p:
  browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
  for slug in ['concreteyield','photovaultplan','reserveready','marginwatch','travelbuffer']:
   context=browser.new_context(viewport={'width':390,'height':844},accept_downloads=True)
   page=context.new_page();errors=[]
   page.on('pageerror',lambda e:errors.append(str(e)))
   page.set_content((R/'dist'/'tools'/slug/'index.html').read_text(encoding='utf-8'),wait_until='domcontentloaded')
   assert page.locator('h1').count()==1
   assert page.locator('meta[name="robots"]').get_attribute('content')=='noindex,follow'
   assert page.locator('script[src*="adsbygoogle"]').count()==0
   if slug=='concreteyield':
    page.locator('#add').click();assert int(page.locator('#bags').inner_text())==49
    page.locator('#shape').select_option('hole');page.locator('#width').fill('12');page.locator('#depth').fill('24');page.locator('#quantity').fill('2');page.locator('#add').click();assert int(page.locator('#bags').inner_text())>49
    with page.expect_download() as d:page.locator('#export').click()
    assert d.value.suggested_filename.endswith('.csv')
   if slug=='photovaultplan':
    assert 'TB' in page.locator('#unique').inner_text()
    page.locator('#sample').set_input_files({'name':'raw-image.jpg','mimeType':'image/jpeg','buffer':b'X'*100000})
    page.locator('#useSample').click();assert abs(float(page.locator('#mb').input_value())-0.1)<0.001
    with page.expect_download() as d:page.locator('#export').click()
    assert d.value.suggested_filename.endswith('.csv')
   if slug=='reserveready':
    page.locator('#add').click();assert page.locator('#contrib').inner_text()=='$240.00'
    assert page.locator('#balance').inner_text()=='$1,680.00'
    assert page.locator('#minimum').inner_text().startswith('-')
   if slug=='marginwatch':
    page.locator('#add').click();assert page.locator('#worked').inner_text()=='4.00 h'
    assert page.locator('#forecast').inner_text()=='$4,745.00'
    with page.expect_download() as d:page.locator('#export').click()
    assert d.value.suggested_filename.endswith('.csv')
   if slug=='travelbuffer':
    page.locator('#date').fill('2026-11-05');page.locator('#add').click()
    page.locator('#time').fill('10:30');page.locator('#add').click()
    assert page.locator('#conflicts').inner_text()=='1'
    with page.expect_download() as d:page.locator('#ics').click()
    assert d.value.suggested_filename.endswith('.ics')
   # Mobile overflow and privacy gate.
   overflow=page.evaluate('document.documentElement.scrollWidth > window.innerWidth + 2')
   assert not overflow, f'{slug} horizontal overflow'
   assert not errors, f'{slug} JS errors {errors}'
   results[slug]={'mobile_390px':'pass','core_interaction':'pass','js_runtime':'pass','draft_noindex':'pass','ads_disabled':'pass'}
   context.close()
  browser.close()
finally:server.terminate();server.wait(timeout=10)
(R/'QA_RESULTS_2026-10-22.json').write_text(json.dumps({'date':'2026-10-22','results':results,'total_existing':25,'public_deploy_test':'not run: no public host'},indent=2)+'\n')
print('BROWSER PASS',len(results),'tools: core actions, mobile layout, JS errors, noindex, ads gate')
