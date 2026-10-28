const fs=require('fs'),vm=require('vm'),assert=require('node:assert/strict');
const source=fs.readFileSync('apps/lengthplan/index.html','utf8').match(/<script id="lengthplan-code">([\s\S]*?)<\/script>/)[1];
const context={module:{exports:{}},console};vm.runInNewContext(source,context);const P=context.module.exports;
const mm=x=>Math.round(x*1000);
const pack=(lengths,stock=100,kerf=0,trim=0,keep=10)=>P.plan(lengths.map((x,i)=>({length:mm(x),label:'Part '+i,id:i})),mm(stock),mm(kerf),mm(trim),mm(keep));
assert.equal(P.number('30 1/2'),30.5);assert.equal(P.measure('1','in'),25400);assert.equal(P.measure('25.4','mm'),25400);
for(const bad of ['-1','NaN','1/0','3in','1e4',''])assert.throws(()=>P.number(bad));
assert.equal(P.parse('length,quantity,label\n30 1/2,2,"Leg, left"','in').length,2);
assert.equal(P.parse('30,1,"Leg, left"','in')[0].label,'Leg, left');
for(const bad of ['1,0','1,1.5','1,501','0,2','5,500\n2,1','1,2,"unclosed','length,quantity,label'])assert.throws(()=>P.parse(bad,'in'));
let r=pack([30,30,30,30,24,24],96,.125);assert.equal(r.bins.length,2);assert.equal(r.finished,mm(168));assert.equal(r.reservedKerf,mm(.75));assert.equal(r.offcut,mm(23.25));assert.equal(r.reusable,mm(17.625));
assert.throws(()=>pack([96],96,.125));assert.equal(pack([96],96,0).bins.length,1);
assert.equal(pack([48,48],100,1,1).bins.length,1);assert.throws(()=>pack([1],100,0,50));
// First/best-fit descending needs 3 bins on this instance; the exact search must find 2.
r=pack([6,5,3,2,2,2],10);assert.equal(r.bins.length,2);assert.equal(r.proved,true);
// Independent exact oracle tries every existing bin, with no best-fit logic.
function brute(a,capacity){let best=a.length,bins=[];function visit(i){if(i===a.length){best=Math.min(best,bins.length);return;}for(let j=0;j<bins.length;j++){if(bins[j]+a[i]<=capacity){bins[j]+=a[i];visit(i+1);bins[j]-=a[i];}}if(bins.length<best){bins.push(a[i]);visit(i+1);bins.pop();}}visit(0);return best;}
let seed=27;const random=n=>{seed=(seed*1664525+1013904223)>>>0;return seed%n;};
for(let t=0;t<150;t++){const kerf=random(3),trim=random(2),capacity=30-2*trim,n=2+random(8),lengths=Array.from({length:n},()=>1+random(capacity-kerf));r=pack(lengths,30,kerf,trim);assert.equal(r.bins.length,brute(lengths.map(x=>x+kerf),capacity));assert.equal(r.finished+r.reservedKerf+r.trimLoss+r.offcut,r.stock*r.bins.length);assert.equal(new Set(r.bins.flatMap(b=>b.parts.map(p=>p.id))).size,n);assert.ok(r.bins.every(b=>b.rem>=0));assert.equal(r.proved,true);}
r=pack(Array.from({length:500},(_,i)=>1+i%13),100,1,2);assert.equal(r.count,500);assert.ok(r.bins.every(b=>b.rem>=0));assert.equal(r.finished+r.reservedKerf+r.trimLoss+r.offcut,r.stock*r.bins.length);
assert.equal(P.csvCell('=1+1'),'"\'=1+1"');assert.equal(P.csvCell('hello, "saw"'),'"hello, ""saw"""');
// Report settings must remain understandable after the input form is hidden in print.
r=pack([762,762,762,762,609.6,609.6],2438.4,3.175,6.35,304.8);r.price=24.5;r.currency='GBP';
let settings=Object.fromEntries(P.settingsRows(r,'in'));
assert.equal(settings['Stock length (each)'],'96 in');assert.equal(settings['Reserved kerf (per piece)'],'0.125 in');assert.equal(settings['End trim (each end)'],'0.25 in');assert.equal(settings['Keep offcuts at least'],'12 in');assert.equal(settings['Quoted stock cost'],'49.00 GBP');
settings=Object.fromEntries(P.settingsRows(r,'mm'));assert.equal(settings['Stock length (each)'],'2438.4 mm');assert.equal(settings['End trim (each end)'],'6.35 mm');
const report=P.csvRows(r,'in'),totals=Object.fromEntries(report.filter(row=>row.length===2));assert.equal(totals['End trim'],'1 in');assert.equal(totals['Offcuts'],'22.25 in');assert.equal(totals['User-entered price per stock'],'24.5');assert.equal(report.filter(row=>row.length===6&&typeof row[0]==='number').length,6);
r.price=0;assert.equal(Object.fromEntries(P.settingsRows(r,'in'))['Quoted stock cost'],'Not entered');
console.log('PASS: fractions, input/kerf/trim boundaries, 150 independent oracle comparisons, 500-piece conservation, CSV safety and complete report settings/costs in both units.');
