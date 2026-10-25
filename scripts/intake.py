#!/usr/bin/env python3
"""Intake 5 researched candidate needs. Hard-exclude duplicates; never autopublish them."""
import argparse, datetime, difflib, json, re, sys
from pathlib import Path
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parents[1]
HISTORY=ROOT/'content/history.json'

def normalize(s):
    s=re.sub(r'[^a-z0-9]+',' ',s.lower()).strip()
    stop={'a','an','the','for','and','to','with','of','in','on','app','tool','simple','free','best'}
    return ' '.join(w for w in s.split() if w not in stop)

def duplicate(a,b):
    if a['slug'].lower()==b['slug'].lower(): return 'slug already used'
    x,y=normalize(a['problem']),normalize(b['problem'])
    score=difflib.SequenceMatcher(None,x,y).ratio()
    jac=len(set(x.split())&set(y.split()))/max(len(set(x.split())|set(y.split())),1)
    if score >= .76 or (jac >= .60 and a['audience'].lower()==b['audience'].lower()):
        return f'semantically similar ({score:.2f} string, {jac:.2f} token overlap)'
    return None

def main():
    p=argparse.ArgumentParser();p.add_argument('file',help='JSON file containing date and 5 candidate needs');p.add_argument('--commit',action='store_true',help='accept non-duplicate candidates into persistent history');args=p.parse_args()
    incoming=json.loads(Path(args.file).read_text(encoding='utf-8'))
    dt=incoming.get('date')
    try:datetime.date.fromisoformat(dt)
    except:raise SystemExit('Date required: YYYY-MM-DD')
    candidates=incoming.get('needs',[])
    if len(candidates)!=5:raise SystemExit('Exactly five research candidates required')
    history=json.loads(HISTORY.read_text(encoding='utf-8'))
    existing=history['entries'][:]
    failures=[]
    required=('slug','problem','audience','evidence_url','evidence_date','jtbd','competitor','seo_primary','monetization_hypothesis')
    for n in candidates:
        missing=[k for k in required if not n.get(k)]
        if missing:failures.append(f"{n.get('slug','?')}: missing {','.join(missing)}");continue
        if not re.fullmatch('[a-z][a-z0-9-]+',n['slug']):failures.append(f"{n['slug']}: invalid slug");continue
        try:datetime.date.fromisoformat(n['evidence_date'])
        except:failures.append(f"{n['slug']}: evidence_date invalid")
        if urlparse(n['evidence_url']).scheme not in ('http','https'):
            failures.append(f"{n['slug']}: evidence_url invalid")
        for e in existing:
            reason=duplicate(n,e)
            if reason:failures.append(f"{n['slug']}: possible duplicate of {e['slug']} ({reason})")
        existing.append({'slug':n['slug'],'problem':n['problem'],'audience':n['audience'],'date':dt})
    if failures:
        print('REJECTED: '+str(len(failures))+' issue(s)\n'+'\n'.join(failures),file=sys.stderr);raise SystemExit(1)
    if args.commit:
        history['entries']=existing;HISTORY.write_text(json.dumps(history,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        print('ACCEPTED: 5 unique candidates persisted. These are NOT yet approved for public indexing or ads.')
    else:print('PASS: 5 candidates unique against history; rerun with --commit to persist')
if __name__=='__main__':main()
