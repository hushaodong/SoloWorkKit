import unittest
import contextlib, io, json, tempfile
from pathlib import Path
import build as builder
from build import analytics_config, analytics_markup

class AnalyticsConfigTest(unittest.TestCase):
    def valid(self):
        return dict(enabled=True, provider='umami', consent_required=True, privacy_ready=True,
            website_id='12345678-1234-1234-1234-123456789abc',script_url='https://cloud.umami.is/script.js',
            site_hostname='soloworkkit-hushaodong.pages.dev',
            data_region='EU',operator_name='Test fixture',privacy_contact='fixture@example.test')
    def test_disabled_is_inert(self):
        self.assertFalse(analytics_config('https://soloworkkit-hushaodong.pages.dev',{'enabled':False})['enabled'])
    def test_missing_gate_rejected(self):
        for key,value in [('website_id',''),('privacy_ready',False),('privacy_ready','false'),('consent_required',False),('privacy_contact',''),('data_region',''),('script_url','https://unreviewed.test/script.js')]:
            with self.subTest(key=key):
                cfg=self.valid();cfg[key]=value
                with self.assertRaises(ValueError):analytics_config('https://soloworkkit-hushaodong.pages.dev',cfg)
    def test_no_origin_stays_off(self):
        self.assertFalse(analytics_config('',self.valid())['enabled'])
        self.assertFalse(analytics_config('https://different.example.test',self.valid())['enabled'])
    def test_markup_has_only_reviewed_actions(self):
        cfg=analytics_config('https://soloworkkit-hushaodong.pages.dev',self.valid())
        markup=analytics_markup(cfg,'/tools/lengthplan/','Planner','lengthplan','<button id="calculate">Go</button><input value="PRIVATE"><button>Unknown</button>')
        self.assertIn('"actions": ["calculate"]',markup)
        self.assertNotIn('PRIVATE',markup)
        self.assertIn('src="/assets/usage-analytics.js"',markup)
        self.assertNotIn('src="https://cloud.umami.is',markup)
    def test_enabled_build_covers_routes_without_enabling_ads(self):
        old_dist,old_config=builder.DIST,builder.ANALYTICS
        try:
            with tempfile.TemporaryDirectory() as tmp:
                builder.DIST=Path(tmp)/'dist';builder.ANALYTICS=Path(tmp)/'analytics.json'
                builder.ANALYTICS.write_text(json.dumps(self.valid()))
                with contextlib.redirect_stdout(io.StringIO()):
                    builder.build(site_url='https://soloworkkit-hushaodong.pages.dev')
                pages=list(builder.DIST.rglob('index.html'))
                total=len(json.loads(builder.CATALOG.read_text())['tools'])+4
                self.assertEqual(len(pages),total)
                for page in pages:
                    source=page.read_text()
                    self.assertIn('id="wl-analytics-config"',source)
                    self.assertIn('src="/assets/usage-analytics.js"',source)
                    self.assertNotIn('No analytics, advertising pixels',source)
                    self.assertNotIn('advertising scripts or analytics are used',source)
                    self.assertNotIn('pagead2.googlesyndication.com',source)
                self.assertNotIn('wl-analytics-config',(builder.DIST/'404.html').read_text())
                report=json.loads((builder.DIST/'build-report.json').read_text())
                self.assertTrue(report['analytics_enabled']);self.assertFalse(report['ads_enabled'])
                self.assertEqual(report['indexable_paths'],[])
        finally:builder.DIST, builder.ANALYTICS=old_dist, old_config

if __name__=='__main__':unittest.main()
