(function(){
  var d=document,root=d.documentElement;root.classList.remove('nojs');root.classList.add('js');
  var hdr=d.querySelector('.site-header');
  function onScroll(){if(hdr)hdr.classList.toggle('scrolled',window.scrollY>8)}
  window.addEventListener('scroll',onScroll,{passive:true});onScroll();

  // mobile menu
  var t=d.querySelector('.menu-toggle'),n=d.getElementById('nav-links');
  if(t&&n){t.addEventListener('click',function(){var o=n.classList.toggle('open');t.setAttribute('aria-expanded',o)})}
  // mega menu
  var mb=d.querySelector('.mega-btn'),mg=d.getElementById('mega');
  function closeMega(){if(mb&&mg){mg.hidden=true;mb.setAttribute('aria-expanded','false')}}
  if(mb&&mg){
    mb.addEventListener('click',function(e){e.stopPropagation();var open=mg.hidden;mg.hidden=!open;mb.setAttribute('aria-expanded',open)});
    d.addEventListener('click',function(e){if(!mg.hidden&&!mg.contains(e.target))closeMega()});
  }
  // language menu
  var lb=d.querySelector('button.lang'),lm=d.getElementById('lang-menu');
  function closeLang(){if(lb&&lm){lm.hidden=true;lb.setAttribute('aria-expanded','false')}}
  if(lb&&lm){
    lb.addEventListener('click',function(e){e.stopPropagation();var open=lm.hidden;lm.hidden=!open;lb.setAttribute('aria-expanded',open);if(open)closeMega()});
    d.addEventListener('click',function(e){if(!lm.hidden&&!lm.contains(e.target))closeLang()});
  }
  d.addEventListener('keydown',function(e){if(e.key!=='Escape')return;
    if(lm&&!lm.hidden){closeLang();lb.focus()}
    if(mg&&!mg.hidden){closeMega();mb.focus()}
    if(n&&n.classList.contains('open')){n.classList.remove('open');t.setAttribute('aria-expanded','false');t.focus()}});

  // showcase tabs
  d.querySelectorAll('[role="tablist"]').forEach(function(list){
    var tabs=[].slice.call(list.querySelectorAll('[role="tab"]'));
    function sel(tab){tabs.forEach(function(x){var on=x===tab;x.setAttribute('aria-selected',on);x.tabIndex=on?0:-1;var p=d.getElementById(x.getAttribute('aria-controls'));if(p)p.hidden=!on})}
    tabs.forEach(function(tab,i){
      tab.addEventListener('click',function(){sel(tab)});
      tab.addEventListener('keydown',function(e){var k=e.key,j=-1;if(k==='ArrowRight')j=(i+1)%tabs.length;if(k==='ArrowLeft')j=(i-1+tabs.length)%tabs.length;if(j>-1){e.preventDefault();sel(tabs[j]);tabs[j].focus()}});
    });
  });

  // interest picker -> signup with selected interests
  d.querySelectorAll('[data-picker]').forEach(function(f){
    var out=f.querySelector('[data-count]');
    function upd(){var c=f.querySelectorAll('input:checked').length;if(out)out.textContent=out.dataset[c?'some':'none'].replace('{n}',c)}
    f.addEventListener('change',upd);upd();
  });

  // contact form -> Make.com webhook (same JSON shape as the previous site), mailto fallback
  function acq(){try{return JSON.parse(localStorage.getItem('hostlio_acq')||'null')}catch(_e){return null}}
  d.querySelectorAll('[data-contact-form]').forEach(function(f){
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var fd=new FormData(f),s=f.querySelector('.form-status'),b=f.querySelector('button[type=submit]');
      var g=function(k){return (fd.get(k)||'').toString().trim()};
      var lines=['Hotel: '+g('hotel'),'Rooms: '+g('rooms'),'Country/city: '+g('country'),'Language: '+(f.dataset.lang||''),'',g('message')];
      function mailto(){window.location.href='mailto:'+f.dataset.mail+'?subject='+encodeURIComponent(f.dataset.subject+' - '+g('hotel'))+'&body='+encodeURIComponent(lines.join('\n')+'\nEmail: '+g('email'))}
      if(!f.dataset.endpoint||!window.fetch){mailto();if(s)s.textContent=f.dataset.sent;return}
      if(b)b.disabled=true;if(s)s.textContent=f.dataset.sending||'';
      fetch(f.dataset.endpoint,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({
        type:'contact',name:g('name'),email:g('email'),subject:'Request a Demo',message:lines.join('\n'),date:new Date().toISOString(),
        hotel:g('hotel'),rooms:g('rooms'),country:g('country'),lang:f.dataset.lang||'',page:location.pathname,acquisition:acq()})})
      .then(function(r){if(!r.ok)throw 0;f.reset();if(s)s.textContent=f.dataset.ok})
      .catch(function(){if(s)s.textContent=f.dataset.err})
      .then(function(){if(b)b.disabled=false});
    });
  });

  // pricing: monthly/annual toggle + live prices from the Supabase `plans` endpoint (fallback = rendered prices)
  d.querySelectorAll('.plans[data-plans-endpoint]').forEach(function(box){
    var tg=box.previousElementSibling&&box.previousElementSibling.classList.contains('billing')?box.previousElementSibling:null;
    var data={starter:{m:49,a:470},pro:{m:89,a:854},growth:{m:149,a:1430}},eb=true,annual=false;
    var cards=[].slice.call(box.querySelectorAll('.plan'));
    cards.forEach(function(c){var h=c.querySelector('h3');c._id=h?h.id.replace('plan-',''):''});
    function render(){cards.forEach(function(c){var v=data[c._id];if(!v)return;var b=c.querySelector('.price b');if(b)b.textContent=b.textContent.replace(/\d[\d.,\s  ]*/,String(annual?Math.round(v.a/12):v.m)+(/\d\s*[$€]/.test(b.textContent)?' ':''));
      var bm=c.querySelector('[data-bm]'),ba=c.querySelector('[data-ba]');if(bm)bm.hidden=annual;if(ba)ba.hidden=!annual;
      var e=c.querySelector('p.small.muted.num');if(e)e.hidden=!eb;
      var at=c.querySelector('[data-at]');if(at)at.textContent='$'+v.a.toLocaleString('en-US')})}
    if(tg)tg.addEventListener('click',function(ev){var t=ev.target.closest('[data-bill]');if(!t)return;annual=t.dataset.bill==='a';
      [].forEach.call(tg.querySelectorAll('[data-bill]'),function(x){var on=x===t;x.classList.toggle('on',on);x.setAttribute('aria-pressed',on)});
      render();[].forEach.call(box.querySelectorAll('a.btn'),function(a){a.href=a.href.replace(/([?&])billing=\w+&?/,'$1').replace(/[?&]$/,'')+(a.href.indexOf('?')>-1?'&':'?')+'billing='+(annual?'annual':'monthly')})});
    if(window.fetch)fetch(box.dataset.plansEndpoint,{headers:{Authorization:'Bearer '+box.dataset.anon}}).then(function(r){return r.ok?r.json():null}).then(function(j){
      if(!j||!Array.isArray(j.plans))return;
      j.plans.forEach(function(p){if(!data[p.id])return;if(p.monthly&&p.monthly.amount!=null)data[p.id].m=p.monthly.amount;if(p.annual&&p.annual.amount!=null)data[p.id].a=p.annual.amount});
      if(typeof j.early_bird==='boolean')eb=j.early_bird;render()}).catch(function(){});
  });

  // ambient loop video in the final CTA: loads only when visible, never with reduced motion
  var fv=[].slice.call(d.querySelectorAll('video.final-video'));
  if(fv.length&&'IntersectionObserver' in window&&!matchMedia('(prefers-reduced-motion: reduce)').matches&&!(navigator.connection&&navigator.connection.saveData)){
    var vo=new IntersectionObserver(function(es){es.forEach(function(en){var v=en.target;
      if(en.isIntersecting){if(!v.src&&!v.firstChild){[['webm','video/webm'],['mp4','video/mp4']].forEach(function(x){var s=d.createElement('source');s.src=v.dataset[x[0]];s.type=x[1];v.appendChild(s)});v.load();v.addEventListener('playing',function(){v.classList.add('on')},{once:true})}
        var pr=v.play();if(pr&&pr.catch)pr.catch(function(){})}else if(!v.paused)v.pause()})},{rootMargin:'200px 0px'});
    fv.forEach(function(v){vo.observe(v)});
  }

  // kayıt/ödeme bağlantılarına sayfa dilini ekle (ödeme sayfası aynı dilde açılsın)
  var hl=(root.getAttribute('lang')||'en').slice(0,2);
  d.querySelectorAll('a[href^="/signup"]').forEach(function(a){try{var u=new URL(a.getAttribute('href'),location.origin);if(!u.searchParams.get('lang'))u.searchParams.set('lang',hl);a.setAttribute('href',u.pathname+u.search)}catch(e){}});

  // gentle reveal for below-the-fold blocks only (content is visible at rest)
  if('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches){
    var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){en.target.classList.remove('pre');io.unobserve(en.target)}})},{rootMargin:'0px 0px -8% 0px'});
    d.querySelectorAll('.rv').forEach(function(el){if(el.getBoundingClientRect().top>window.innerHeight){el.classList.add('pre');io.observe(el)}});
  }
})();
