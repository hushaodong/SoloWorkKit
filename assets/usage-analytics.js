(function () {
  'use strict';
  const CHOICE_KEY = 'worklane.analytics-consent.v1';
  const MAX_AGE = 180 * 86400000;
  function choice(raw, now) {
    try {
      const c = JSON.parse(raw);
      return c && c.v === 1 && ['granted', 'denied'].includes(c.value) &&
        Number.isFinite(c.at) && c.at <= now && now - c.at < MAX_AGE ? c.value : null;
    } catch (_) { return null; }
  }
  function referral(value) {
    try { const u = new URL(value); return /^https?:$/.test(u.protocol) ? u.origin : ''; }
    catch (_) { return ''; }
  }
  function payload(c, name, referrer) {
    // Explicit fields only: never inherit the SDK's full URL, hash or document title.
    const p = { website: c.website_id, hostname: c.hostname, url: c.path,
      title: c.title, referrer: referral(referrer) };
    if (name) p.name = name;
    return p;
  }
  if (typeof module !== 'undefined') module.exports = {choice, referral, payload, CHOICE_KEY};
  if (typeof document === 'undefined') return;
  const node = document.getElementById('wl-analytics-config');
  if (!node) return;
  let c;
  try { c = JSON.parse(node.textContent); } catch (_) { return; }
  if (!c.enabled || location.hostname !== c.hostname) return;
  let granted = false, started = false, pageSent = false, sent = 0, sdk = null;
  const blocked = () => navigator.globalPrivacyControl === true || navigator.doNotTrack === '1';
  const read = () => { try { return choice(localStorage.getItem(CHOICE_KEY), Date.now()); } catch (_) { return null; } };
  const remember = value => { try { localStorage.setItem(CHOICE_KEY, JSON.stringify({v:1,value,at:Date.now()})); } catch (_) {} };
  function load() {
    if (sdk) return sdk;
    sdk = new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.src = c.script_url; script.async = true;
      script.setAttribute('data-website-id', c.website_id);
      script.setAttribute('data-auto-track', 'false');
      script.setAttribute('data-exclude-search', 'true');
      script.setAttribute('data-exclude-hash', 'true');
      script.setAttribute('data-do-not-track', 'true');
      script.setAttribute('data-domains', c.hostname);
      script.onload = () => window.umami && typeof window.umami.track === 'function' ? resolve(window.umami) : reject(Error('Unavailable'));
      script.onerror = () => reject(Error('Unavailable'));
      document.head.appendChild(script);
    });
    return sdk;
  }
  function track(name) {
    if (!granted || blocked() || sent >= 60) return;
    sent++;
    load().then(u => {
      if (granted && !blocked()) return u.track(payload(c, name, document.referrer));
    }).catch(() => {}); // Analytics failure must never interrupt a tool.
  }
  const style = document.createElement('style');
  style.textContent = '#wl-analytics-panel{position:fixed;bottom:16px;left:16px;right:16px;max-width:700px;margin:auto;padding:20px;border:1px solid #aacbc3;border-radius:12px;background:white;color:#173a40;box-shadow:0 8px 35px #173a4030;z-index:9999;font:14px/1.6 system-ui,sans-serif}#wl-analytics-panel h2{font:700 18px/1.3 system-ui,sans-serif;margin:0 0 8px}#wl-analytics-panel button,#wl-analytics-settings{font:inherit;padding:9px 12px;border:1px solid #7baba0;border-radius:7px;background:#f2f7f4;color:#075d53;cursor:pointer;margin:4px 8px 0 0}#wl-analytics-panel a{color:#075d53}#wl-analytics-panel[hidden]{display:none}#wl-analytics-settings{font-size:12px}@media print{#wl-analytics-panel,#wl-analytics-settings{display:none!important}}';
  document.head.appendChild(style);
  const panel = document.createElement('section');
  panel.id = 'wl-analytics-panel'; panel.hidden = true;
  panel.setAttribute('aria-labelledby', 'wl-analytics-title');
  panel.innerHTML = '<h2 id="wl-analytics-title">Optional usage analytics</h2><p>With your permission, Umami receives page paths, referral sites and tool event names. Its servers also process connection/device information. Your form values and files are never sent. You can withdraw at any time.</p><div><button type="button" id="wl-analytics-accept">Accept analytics</button><button type="button" id="wl-analytics-reject">Reject analytics</button><a href="/privacy/">Privacy details</a></div><p id="wl-analytics-status" role="status"></p>';
  document.body.appendChild(panel);
  const settings = document.createElement('button');
  settings.id = 'wl-analytics-settings'; settings.type = 'button'; settings.textContent = 'Analytics choices';
  (document.querySelector('.wl-footer .wl-container') || document.body).appendChild(settings);
  const accept = panel.querySelector('#wl-analytics-accept');
  const reject = panel.querySelector('#wl-analytics-reject');
  const status = panel.querySelector('#wl-analytics-status');
  function apply(value) {
    granted = value === 'granted' && !blocked();
    if (granted && !pageSent) { pageSent = true; track(); }
  }
  function open() {
    panel.hidden = false; accept.disabled = blocked();
    reject.textContent = granted ? 'Withdraw analytics' : 'Reject analytics';
    status.textContent = blocked() ? 'Your browser privacy setting keeps analytics off.' :
      granted ? 'Analytics is currently allowed. Withdraw to stop future events.' : 'Analytics is currently off.';
  }
  accept.onclick = () => { remember('granted'); apply('granted'); panel.hidden = true; settings.focus(); };
  reject.onclick = () => { remember('denied'); apply('denied'); panel.hidden = true; settings.focus(); };
  settings.onclick = open;
  const current = read(); apply(current);
  if (current === null && !blocked()) open();
  window.addEventListener('storage', e => { if (e.key === CHOICE_KEY) apply(choice(e.newValue, Date.now())); });
  const excluded = target => !target || !target.closest || target.closest('.wl-header,.wl-footer,.wl-guide,#wl-analytics-panel,#wl-analytics-settings');
  function start(target) {
    if (!c.tool || !granted || blocked() || excluded(target)) return;
    if (!started) { started = true; track('tool_start'); }
  }
  document.addEventListener('input', e => start(e.target), true);
  document.addEventListener('change', e => start(e.target), true);
  document.addEventListener('click', e => {
    if (excluded(e.target)) return;
    const button = e.target.closest('button');
    if (button && c.actions.includes(button.id) && !button.disabled) {
      start(button); track('action_' + button.id.toLowerCase());
    }
  }, true);
  window.addEventListener('worklane:analytics', e => {
    const d = e.detail || {};
    if (started && d.tool === c.tool && ['tool_complete','tool_error','export_generated'].includes(d.kind)) track(d.kind);
  });
})();
