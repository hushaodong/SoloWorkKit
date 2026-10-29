const fs=require('fs'),vm=require('vm'),assert=require('node:assert/strict');
const source=fs.readFileSync('assets/usage-analytics.js','utf8');
const moduleOnly={module:{exports:{}},URL};vm.runInNewContext(source,moduleOnly);const A=moduleOnly.module.exports;
const config={enabled:true,website_id:'12345678-1234-1234-1234-123456789abc',script_url:'https://cloud.umami.is/script.js',hostname:'soloworkkit-hushaodong.pages.dev',path:'/tools/lengthplan/',title:'Linear Cut Planner',tool:'lengthplan',actions:['calculate','csv']};
assert.equal(A.referral('https://www.google.com/search?q=private#secret'),'https://www.google.com');
assert.equal(A.referral('javascript:alert(1)'),'');
const p=A.payload(config,'tool_start','https://example.com/customer?email=private');
assert.equal(p.referrer,'https://example.com');assert.equal(p.url,'/tools/lengthplan/');assert.equal(p.data,undefined);assert.equal(p.name,'tool_start');
assert.equal(A.payload({...config,internal_test:true},'tool_start','').tag,'internal-test');assert.equal(p.tag,undefined);
assert.equal(A.choice('{bad',1000),null);assert.equal(A.choice(JSON.stringify({v:1,value:'granted',at:1001}),1000),null);assert.equal(A.choice(JSON.stringify({v:1,value:'granted',at:0}),180*86400000),null);
function harness({gpc=false,stored=null,hostname=config.hostname}={}){
 const nodes={},docEvents={},winEvents={},scripts=[],records=[];let saved=stored;
 class Element{
  constructor(tag='div',id=''){this.tagName=tag;this.id=id;this.hidden=false;this.disabled=false;this.attributes={};}
  set innerHTML(s){this.html=s;for(const id of ['wl-analytics-accept','wl-analytics-reject','wl-analytics-status'])nodes[id]=new Element('button',id);}
  querySelector(selector){return nodes[selector.slice(1)]||null;}
  setAttribute(k,v){this.attributes[k]=v;}
  appendChild(el){if(el.tagName==='script'){scripts.push(el);window.umami={track:payload=>records.push(payload)};el.onload();}if(el.id)nodes[el.id]=el;}
  closest(selector){return this.excluded ? this : null;}
  focus(){}
 }
 const node=new Element();node.textContent=JSON.stringify(config);nodes['wl-analytics-config']=node;
 const window={addEventListener:(n,f)=>winEvents[n]=f};
 const document={head:new Element('head'),body:new Element('body'),referrer:'https://www.google.com/search?q=private',getElementById:id=>nodes[id],createElement:tag=>new Element(tag),querySelector:()=>null,addEventListener:(n,f)=>docEvents[n]=f};
 const context={document,window,location:{hostname,search:''},navigator:{globalPrivacyControl:gpc},localStorage:{getItem:()=>saved,setItem:(k,v)=>saved=v},URL,URLSearchParams,Date,Promise,Error,JSON};
 vm.runInNewContext(source,context);
 const input=new Element('input');input.value='SECRET CUSTOMER DATA';
 const button=new Element('button','calculate');button.closest=()=>button;
 return {nodes,scripts,records,input,button,docEvents,winEvents,saved:()=>saved};
}
const flush=()=>new Promise(resolve=>setImmediate(resolve));
(async()=>{
 let h=harness();assert.equal(h.scripts.length,0);h.docEvents.input({target:h.input});h.winEvents['worklane:analytics']({detail:{tool:'lengthplan',kind:'tool_complete',email:'private'}});await flush();assert.equal(h.records.length,0);
 h.nodes['wl-analytics-reject'].onclick();h.docEvents.click({target:h.button});await flush();assert.equal(h.scripts.length,0);
 h.nodes['wl-analytics-accept'].onclick();await flush();assert.equal(h.scripts.length,1);assert.equal(h.scripts[0].attributes['data-auto-track'],'false');assert.equal(h.records.length,1);assert.equal(h.records[0].name,undefined);
 h.docEvents.input({target:h.input});h.winEvents['worklane:analytics']({detail:{tool:'lengthplan',kind:'tool_complete',email:'SECRET'}});await flush();assert.equal(h.records.filter(p=>p.name==='tool_start').length,1);assert.equal(h.records.filter(p=>p.name==='tool_complete').length,1);assert.ok(!JSON.stringify(h.records).includes('SECRET'));assert.ok(!JSON.stringify(h.records).includes('?'));
 h.docEvents.input({target:h.input});await flush();assert.equal(h.records.filter(p=>p.name==='tool_start').length,1);
 h.nodes['wl-analytics-reject'].onclick();const before=h.records.length;h.docEvents.input({target:h.input});h.winEvents['worklane:analytics']({detail:{tool:'lengthplan',kind:'export_generated'}});await flush();assert.equal(h.records.length,before);
 h=harness({gpc:true,stored:JSON.stringify({v:1,value:'granted',at:Date.now()})});await flush();assert.equal(h.scripts.length,0);h.nodes['wl-analytics-settings'].onclick();assert.equal(h.nodes['wl-analytics-accept'].disabled,true);
 h=harness({hostname:'unreviewed.example'});assert.equal(h.scripts.length,0);assert.equal(h.nodes['wl-analytics-panel'],undefined);
 console.log('PASS: no tracker before consent/after rejection, withdrawal, GPC, fixed host, sanitized payload, no form data and deduplicated tool starts.');
})().catch(error=>{console.error(error);process.exitCode=1;});
