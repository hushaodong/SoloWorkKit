from pathlib import Path
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parents[1]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for name,path,width,height in [('home-desktop',R/'dist/index.html',1440,1000),('home-mobile',R/'dist/index.html',390,900),('marginwatch-mobile',R/'dist/tools/marginwatch/index.html',390,900)]:
  page=b.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
  page.set_content(path.read_text(encoding='utf-8'),wait_until='domcontentloaded')
  page.screenshot(path=str(R.parent/(name+'.png')),full_page=True)
  page.close()
 b.close()
print('Screenshots generated')
