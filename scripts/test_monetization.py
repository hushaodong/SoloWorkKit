#!/usr/bin/env python3
"""Exercise verification-only builds and the transition to approved ad serving."""
import contextlib
import io
import json
import tempfile
import unittest
from itertools import product
from pathlib import Path
from unittest.mock import patch
from urllib.robotparser import RobotFileParser

from bs4 import BeautifulSoup
import build

PUBLISHER='ca-pub-1234567890123456'
ORIGIN='https://soloworkkit-hushaodong.pages.dev'


class MonetizationBuildTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.out=Path(self.tmp.name)/'dist'
        self.catalog=json.loads(build.CATALOG.read_text())
        # Test approval of one page without granting approval to all 35 tools.
        for tool in self.catalog['tools']:
            tool.update(approved_for_index=False,evidence_reviewed=False,qa_verified=False)
        self.catalog['tools'][0].update(approved_for_index=True,evidence_reviewed=True,qa_verified=True)
        catalog_path=Path(self.tmp.name)/'catalog.json'
        catalog_path.write_text(json.dumps(self.catalog))
        self.patches=[patch.object(build,'DIST',self.out),patch.object(build,'CATALOG',catalog_path)]
        for p in self.patches:p.start()

    def tearDown(self):
        for p in reversed(self.patches):p.stop()
        self.tmp.cleanup()

    def render(self,**kwargs):
        with contextlib.redirect_stdout(io.StringIO()):
            build.build(site_url=ORIGIN,**kwargs)
        return json.loads((self.out/'build-report.json').read_text())

    def test_verification_cannot_start_ads_or_search_indexing(self):
        report=self.render(verification_publisher=PUBLISHER)
        self.assertFalse(report['ads_enabled'])
        self.assertEqual(report['indexable_paths'],[])
        pages=list(self.out.rglob('index.html'))
        self.assertEqual(len(pages),39)
        for page in pages:
            soup=BeautifulSoup(page.read_text(),'html.parser')
            self.assertEqual(soup.find('meta',attrs={'name':'google-adsense-account'})['content'],PUBLISHER)
            self.assertIn('noindex',soup.find('meta',attrs={'name':'robots'})['content'])
            self.assertFalse(soup.select('script[src*="googlesyndication"]'))
        self.assertEqual((self.out/'ads.txt').read_text(),'google.com, pub-1234567890123456, DIRECT, f08c47fec0942fa0\n')
        robots=RobotFileParser()
        robots.parse((self.out/'robots.txt').read_text().splitlines())
        self.assertTrue(robots.can_fetch('Mediapartners-Google','/tools/punchlite/'))
        self.assertTrue(robots.can_fetch('Google-Display-Ads-Bot','/'))
        self.assertFalse(robots.can_fetch('Googlebot','/'))

    def test_explicit_empty_verification_removes_public_binding(self):
        self.render(verification_publisher='')
        self.assertFalse((self.out/'ads.txt').exists())
        self.assertNotIn('google-adsense-account',(self.out/'index.html').read_text())

    def test_ad_serving_requires_every_gate(self):
        for production,approved,privacy in product((False,True),repeat=3):
            if production and approved and privacy:continue
            with self.subTest(production=production,approved=approved,privacy=privacy):
                with self.assertRaises(ValueError):
                    self.render(production=production,adsense=PUBLISHER,ads_approved=approved,privacy_ready=privacy,verification_publisher=PUBLISHER)

    def test_approved_ads_do_not_leak_into_draft_or_legal_pages(self):
        report=self.render(production=True,adsense=PUBLISHER,ads_approved=True,privacy_ready=True,verification_publisher=PUBLISHER)
        self.assertTrue(report['ads_enabled'])
        ad_paths=[]
        for page in self.out.rglob('index.html'):
            soup=BeautifulSoup(page.read_text(),'html.parser')
            if soup.select('script[src*="googlesyndication"]'):
                parent=page.relative_to(self.out).parent
                ad_paths.append('/' if str(parent)=='.' else '/'+str(parent)+'/')
                self.assertNotIn('noindex',soup.find('meta',attrs={'name':'robots'})['content'])
        self.assertEqual(sorted(ad_paths),sorted(report['indexable_paths']))
        self.assertEqual(len(ad_paths),2)

    def test_invalid_or_inconsistent_publisher_is_rejected(self):
        for publisher in ('ca-pub-bad','<script>',1234):
            with self.subTest(publisher=publisher),self.assertRaises(ValueError):
                self.render(verification_publisher=publisher)
        with self.assertRaises(ValueError):
            self.render(production=True,adsense=PUBLISHER,ads_approved=True,privacy_ready=True,verification_publisher='ca-pub-9999999999999999')


if __name__=='__main__':
    unittest.main()
