#!/usr/bin/env python3
"""Browser smoke test against localhost; screenshots are build artifacts."""
import contextlib, http.server, socketserver, threading, time
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*args): pass
with socketserver.TCPServer(('127.0.0.1',0),lambda *a,**k:Quiet(*a,directory=str(ROOT/'dist'),**k)) as srv:
    threading.Thread(target=srv.serve_forever,daemon=True).start()
    host=f'http://127.0.0.1:{srv.server_address[1]}'
    with sync_playwright() as p:
        b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
        try:
            for width in (390,1280):
                page=b.new_page(viewport={'width':width,'height':844 if width==390 else 900},device_scale_factor=1)
                errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
                page.set_content((ROOT/'dist'/'index.html').read_text(encoding='utf-8'),wait_until='load')
                assert page.title().startswith('Worklane Tools')
                assert page.locator('a.toolcard').count()==5
                page.locator('#toolSearch').fill('photo')
                assert page.locator('a.toolcard:visible').count()>=1
                page.locator('#toolSearch').fill('')
                page.locator('[data-cat=landlords]').click()
                assert page.locator('a.toolcard:visible').count()==1
                page.locator('[data-cat=all]').click()
                assert page.locator('a.toolcard:visible').count()==5
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth+1'), 'home horizontal overflow '+str(width)
                assert not errors,errors
                page.screenshot(path=str(ROOT/('preview-home-mobile.png' if width==390 else 'preview-home-desktop.png')),full_page=True)
                page.close()
            for slug in ('punchlite','moveoutpdf','shotgrid','gentlenudge','notarymiles'):
                page=b.new_page(viewport={'width':390,'height':844})
                errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
                page.set_content((ROOT/'dist'/'tools'/slug/'index.html').read_text(encoding='utf-8'),wait_until='load')
                assert page.locator('.wl-guide h2').count()==1
                assert page.locator('.wl-header a').count()>1
                assert page.locator('meta[name=robots]').get_attribute('content').startswith('noindex')
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth+1'),f'{slug} horizontal overflow'
                assert not errors,(slug,errors)
                page.close()
            print('BROWSER PASS: 5 tools loaded, home search/categories interactive, 390px responsive, no JS errors')
        finally:b.close();srv.shutdown()
