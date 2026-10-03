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
  // O6: attribution.js'in sunduğu yüzey (süresi dolmuş kayıt dönmez)
  function acq(){try{return typeof window.hostlioAcq==='function'?window.hostlioAcq():null}catch(_e){return null}}
  var t0=Date.now();
  d.querySelectorAll('[data-contact-form]').forEach(function(f){
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var fd=new FormData(f),s=f.querySelector('.form-status'),b=f.querySelector('button[type=submit]');
      // D9: bal küpü doluysa ya da form 3 sn'den kısa sürede gönderildiyse bot say — Make kotası harcanmaz
      if((fd.get('website')||'').toString().trim()||Date.now()-t0<3000){f.reset();if(s)s.textContent=f.dataset.ok;return}
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

  // pricing: monthly/annual toggle + live prices (Y2: /assets/prices.js, tek kaynak pricing.py)
  d.querySelectorAll('.plans[data-plans]').forEach(function(box){
    var tg=box.previousElementSibling&&box.previousElementSibling.classList.contains('billing')?box.previousElementSibling:null;
    var HP=window.HostlioPrices,annual=false;
    function render(){
      if(HP)HP.apply(box,annual);
      [].forEach.call(box.querySelectorAll('[data-bm]'),function(x){x.hidden=annual});
      [].forEach.call(box.querySelectorAll('[data-ba]'),function(x){x.hidden=!annual});
      if(HP){var at=d.querySelector('.annual-table');if(at)HP.apply(at,false)}
    }
    if(tg)tg.addEventListener('click',function(ev){var t=ev.target.closest('[data-bill]');if(!t)return;annual=t.dataset.bill==='a';
      [].forEach.call(tg.querySelectorAll('[data-bill]'),function(x){var on=x===t;x.classList.toggle('on',on);x.setAttribute('aria-pressed',on)});
      render();[].forEach.call(box.querySelectorAll('a.btn'),function(a){try{var u=new URL(a.getAttribute('href'),location.origin);u.searchParams.set('billing',annual?'annual':'monthly');a.setAttribute('href',u.pathname+u.search)}catch(e){}})});
    if(HP)HP.onUpdate(render);
  });

  // ambient loop video in the final CTA: loads only when visible, never with reduced motion
  var fv=[].slice.call(d.querySelectorAll('video.final-video'));
  if(fv.length&&'IntersectionObserver' in window&&!matchMedia('(prefers-reduced-motion: reduce)').matches&&!(navigator.connection&&navigator.connection.saveData)){
    var vo=new IntersectionObserver(function(es){es.forEach(function(en){var v=en.target;
      if(en.isIntersecting){if(!v.src&&!v.firstChild){[['webm','video/webm'],['mp4','video/mp4']].forEach(function(x){var s=d.createElement('source');s.src=v.dataset[x[0]];s.type=x[1];v.appendChild(s)});v.load();v.addEventListener('playing',function(){v.classList.add('on');var bt=v._btn;if(bt)bt.hidden=false},{once:true})}
        if(!v._userPaused){var pr=v.play();if(pr&&pr.catch)pr.catch(function(){})}}else if(!v.paused)v.pause()})},{rootMargin:'200px 0px'});
    fv.forEach(function(v){
      // D6 (WCAG 2.2.2): kullanıcı döngüyü durdurabilir; durdurduysa görünür olunca kendiliğinden yeniden başlamaz
      var bt=v.parentNode.querySelector('.vid-toggle');v._btn=bt;
      if(bt)bt.addEventListener('click',function(){var stop=!v.paused;v._userPaused=stop;if(stop)v.pause();else{var pr=v.play();if(pr&&pr.catch)pr.catch(function(){})}
        bt.setAttribute('aria-pressed',stop);bt.setAttribute('aria-label',stop?bt.dataset.play:bt.dataset.pause)});
      vo.observe(v)});
  }

  // "yazdır / PDF" düğmeleri (satır içi onclick yerine — O4 CSP)
  d.querySelectorAll('[data-print]').forEach(function(b){b.addEventListener('click',function(){window.print()})});

  // gentle reveal for below-the-fold blocks only (content is visible at rest)
  if('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches){
    var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){en.target.classList.remove('pre');io.unobserve(en.target)}})},{rootMargin:'0px 0px -8% 0px'});
    d.querySelectorAll('.rv').forEach(function(el){if(el.getBoundingClientRect().top>window.innerHeight){el.classList.add('pre');io.observe(el)}});
  }
})();
