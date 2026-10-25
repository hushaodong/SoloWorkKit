import json,pathlib
from playwright.sync_api import sync_playwright
root=pathlib.Path(__file__).resolve().parents[1]
slugs=['drywallwise','vendorboard','scopelock','proofsheet','leasetick']
results=[]
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
    for slug in slugs:
        ctx=browser.new_context(viewport={'width':390,'height':844},accept_downloads=True)
        page=ctx.new_page();errs=[];page.on('pageerror',lambda e:errs.append(str(e)))
        page.set_content((root/'dist/tools'/slug/'index.html').read_text(encoding='utf-8'),wait_until='load')
        page.wait_for_timeout(180)
        before=page.evaluate('document.documentElement.scrollWidth<=window.innerWidth')
        assert before,(slug,'horizontal overflow')
        if slug=='drywallwise':
            page.locator('#add').click();assert page.locator('#sheets').inner_text()!='0'
            assert 'Bedroom' in page.locator('#rooms').inner_text()
        if slug=='vendorboard':
            page.locator('#property').fill('Maple Unit 2');page.locator('#vendor').fill('ABC Plumbing');page.locator('#summary').fill('Fix faucet');page.locator('#add').click();assert page.locator('#open').inner_text()=='1'
            page.locator('[data-status]').select_option('Completed');assert page.locator('#open').inner_text()=='0'
        if slug=='scopelock':
            page.locator('#project').fill('Landing page');page.locator('#deliverables').fill('Three pages');page.locator('#save').click();page.locator('#change').fill('Extra login screen');page.locator('#add').click();assert page.locator('#count').inner_text()=='1';page.locator('[data-decision]').select_option('Approved');assert page.locator('#approved').inner_text()=='3.00'
        if slug=='proofsheet':
            # generate test image with Pillow
            from PIL import Image
            tmp=root/'test_photo.jpg';Image.new('RGB',(120,80),(100,170,160)).save(tmp)
            page.locator('#files').set_input_files(str(tmp));page.wait_for_timeout(250);assert page.locator('#count').inner_text()=='1'
            page.locator('#generate').click();assert 'px' in page.locator('#size').inner_text()
            with page.expect_download(timeout=6000) as d:page.locator('#download').click()
            assert d.value.suggested_filename.endswith('.png')
            tmp.unlink()
        if slug=='leasetick':
            page.locator('#property').fill('Unit 2');page.locator('#end').fill('2027-01-31');page.locator('#add').click();assert '2026-12-02' in page.locator('#leases').inner_text()
            with page.expect_download(timeout=6000) as d:page.locator('#ics').click()
            assert d.value.suggested_filename.endswith('.ics')
        assert not errs,(slug,errs)
        page.screenshot(path=str(root.parent/('preview-'+slug+'.png')),full_page=True)
        results.append({'slug':slug,'mobile_390px':True,'interactive_flow':'pass','page_errors':errs})
        ctx.close()
    browser.close()
(root/'QA_RESULTS_2026-10-21.json').write_text(json.dumps({'tested_tools':results,'total':len(results)},indent=2))
print(json.dumps(results,indent=2))
