import json, pathlib, subprocess, time, tempfile, io, zipfile, socket
from playwright.sync_api import sync_playwright
from PIL import Image
ROOT=pathlib.Path(__file__).resolve().parents[1]
DIST=ROOT/'dist'
port=8765
srv=subprocess.Popen(['python','-m','http.server',str(port),'--bind','127.0.0.1','--directory',str(DIST)],stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
results={}
try:
 time.sleep(1)
 with sync_playwright() as p:
  browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
  for slug in ['metersplit','clientrename','visitfloor','rushquote','warrantynest']:
   page=browser.new_page(viewport={'width':390,'height':844},accept_downloads=True)
   errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
   page.set_content((DIST/'tools'/slug/'index.html').read_text(encoding='utf-8'),wait_until='load',timeout=20000)
   assert page.locator('h1').count()==1
   assert 'noindex' in page.locator('meta[name=robots]').get_attribute('content')
   overflow=page.evaluate('document.documentElement.scrollWidth > window.innerWidth+2')
   assert not overflow,(slug,'mobile overflow')
   if slug=='metersplit':
    assert page.locator('#result tr').count()==3
    page.locator('#bill').fill('200');page.locator('#fixed').fill('40')
    assert '$200.00' in page.locator('#total').inner_text()
    with page.expect_download() as d:page.locator('#export').click()
    assert d.value.suggested_filename.endswith('.csv')
   if slug=='clientrename':
    im=Image.new('RGB',(10,10),(120,20,20));buf=io.BytesIO();im.save(buf,'JPEG')
    page.locator('#files').set_input_files([{'name':'DSC_1234.jpg','mimeType':'image/jpeg','buffer':buf.getvalue()}])
    page.locator('#prefix').fill('Test Client');page.locator('#preview').click()
    assert 'Test-Client_001.jpg' in page.locator('#names').inner_text()
    with page.expect_download() as d:page.locator('#zip').click()
    target=pathlib.Path(tempfile.gettempdir())/'worklane-clientrename-test.zip';d.value.save_as(str(target))
    with zipfile.ZipFile(target) as z:
     assert z.namelist()==['Test-Client_001.jpg']
     assert z.read('Test-Client_001.jpg')==buf.getvalue()
   if slug=='visitfloor':
    assert '$' in page.locator('#charge').inner_text()
    page.locator('#truck').fill('200')
    assert float(page.locator('#charge').inner_text().replace('$','').replace(',',''))>200
    with page.expect_download() as d:page.locator('#export').click()
    assert d.value.suggested_filename.endswith('.csv')
   if slug=='rushquote':
    assert '$' in page.locator('#suggested').inner_text()
    page.locator('#premium').fill('50')
    assert page.locator('#percent').inner_text()=='$1,800.00'
    with page.expect_download() as d:page.locator('#export').click()
    assert d.value.suggested_filename.endswith('.csv')
   if slug=='warrantynest':
    page.locator('#add').click();assert page.locator('#count').inner_text()=='1'
    with page.expect_download() as d:page.locator('#ics').click()
    ics=pathlib.Path(tempfile.gettempdir())/'worklane-warranty-test.ics';d.value.save_as(str(ics));assert 'BEGIN:VEVENT' in ics.read_text()
    with page.expect_download() as d:page.locator('#csv').click()
    assert d.value.suggested_filename.endswith('.csv')
   assert not errors,(slug,errors)
   results[slug]={'status':'pass','mobile_390px':'no_horizontal_overflow','page_js_errors':errors,'tested_origin':'set_content only; HTTP localhost blocked by sandbox'}
   page.close()
  browser.close()
finally:
 srv.terminate();srv.wait(timeout=5)
(ROOT/'QA_RESULTS_2026-10-23.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
