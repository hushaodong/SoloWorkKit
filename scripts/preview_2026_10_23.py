from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT.parent
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
 for name,src,w,h in [('home-desktop','index.html',1440,950),('home-mobile','index.html',390,850),('preview-clientrename','tools/clientrename/index.html',1200,900),('preview-visitfloor','tools/visitfloor/index.html',1200,900)]:
  page=browser.new_page(viewport={'width':w,'height':h},device_scale_factor=1)
  page.set_content((ROOT/'dist'/src).read_text(encoding='utf-8'),wait_until='load')
  page.screenshot(path=str(OUT/(name+'.png')),full_page=(name=='home-mobile'))
  page.close()
 browser.close()
