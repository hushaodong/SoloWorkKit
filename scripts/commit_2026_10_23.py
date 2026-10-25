import json, pathlib
root=pathlib.Path(__file__).resolve().parents[1]
catp=root/'content/catalog.json';cat=json.loads(catp.read_text());needs=json.loads((root/'intake/2026-10-23.json').read_text())['needs']
existing={x['slug'] for x in cat['tools']}
for n in needs:
 assert n['slug'] not in existing,n['slug']
 tool={k:n[k] for k in ('slug','name','audience','category','emoji','headline','description')}
 tool.update(keywords=[n['primary']]+n['longtail'],best_for=n['jtbd'],howto={
 'metersplit':['Enter the total bill and the inclusive billing period.','Add each rental unit, occupants and days in the period.','Compare two hypothetical allocations and export CSV after checking lease and law.'],
 'clientrename':['Select JPG, PNG or WebP files and enter a project prefix.','Preview sequential filenames and confirm there are no naming collisions.','Download one ZIP of renamed copies and verify its contents.'],
 'visitfloor':['Enter round-trip travel, on-site time and your hourly labor cost.','Include truck, materials, overhead and a target margin.','Compare your current minimum with the sustainable price and export a quote.'],
 'rushquote':['Enter standard project fee, deadline and requested rush turnaround.','Compare percentage premium with extra overtime cost at a chosen margin.','Copy a proposed quote and obtain client approval before committing.'],
 'warrantynest':['Record property, appliance, model and installation date.','Enter the warranty term and preferred reminder lead time.','Export CSV for backup and an ICS calendar reminder file.']
 }[n['slug']],limitations={
 'metersplit':'No meter readings or legal verification. Utility allocation may be restricted by local rules and leases; no billing is performed.',
 'clientrename':'JPG/PNG/WebP only, 100 files and 120 MiB per ZIP. Original files stay on your device; large batches may exceed memory.',
 'visitfloor':'Cost and margin are assumptions, not market rates; taxes and unforeseen scope must be confirmed separately.',
 'rushquote':'No automatic client approval, payment, email or scheduling; rush fee and deadline must be agreed in writing.',
 'warrantynest':'No server backups or automatic notifications. Warranty eligibility and registration must be checked with the manufacturer.'
 }[n['slug']],faq_question={
 'metersplit':'Can I legally charge tenants based on occupant-days?',
 'clientrename':'Does the photo renamer upload or edit original images?',
 'visitfloor':'Does the calculator tell me what handymen in my city charge?',
 'rushquote':'Is a 30% rush fee standard?',
 'warrantynest':'Will the app email me before a warranty expires?'
 }[n['slug']],faq_answer={
 'metersplit':'Not necessarily. This is a comparison of assumptions; check your state/local rules and lease terms before billing.',
 'clientrename':'No. It creates a local ZIP of renamed copies, without uploading or modifying originals.',
 'visitfloor':'No. It computes a cost-based minimum using your own assumptions and existing minimum.',
 'rushquote':'No. Premiums vary; this tool compares pricing approaches rather than prescribing a market standard.',
 'warrantynest':'No. Import the downloaded ICS file into a calendar and verify its event reminders.'
 }[n['slug']],approved_for_index=False,evidence_reviewed=False,qa_verified=False,seed_from='2026-10-23')
 cat['tools'].append(tool)
catp.write_text(json.dumps(cat,indent=2,ensure_ascii=False)+'\n')
print('Catalog:',len(cat['tools']))
