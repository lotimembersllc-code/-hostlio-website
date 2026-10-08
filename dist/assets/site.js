(function(){
  var d=document,root=d.documentElement;root.classList.remove('nojs');root.classList.add('js');
  var hdr=d.querySelector('.site-header');
  function onScroll(){if(hdr)hdr.classList.toggle('scrolled',window.scrollY>8)}
  window.addEventListener('scroll',onScroll,{passive:true});onScroll();

  // mobile menu (Q2): açılınca odak ilk menü öğesine gider, odak başlık içinde döner, etiket Aç/Kapat olur,
  // dışarı dokununca ya da Escape ile kapanır, arka sayfa kaymaz, kapanınca odak düğmeye döner
  var t=d.querySelector('.menu-toggle'),n=d.getElementById('nav-links');
  function menuOpen(){return !!(n&&n.classList.contains('open'))}
  function setMenu(o,back){if(!t||!n)return;n.classList.toggle('open',o);t.setAttribute('aria-expanded',o);
    if(t.dataset.open)t.setAttribute('aria-label',o?t.dataset.close:t.dataset.open);root.classList.toggle('menu-open',o);
    if(o){var f=n.querySelector('a[href],button');if(f)f.focus()}else{closeMega();if(back)t.focus()}}
  function hdrFocusables(){return [].slice.call(hdr.querySelectorAll('a[href],button:not([disabled])')).filter(function(x){return x.offsetWidth||x.offsetHeight||x.getClientRects().length})}
  if(t&&n){
    t.addEventListener('click',function(){setMenu(!menuOpen(),false)});
    d.addEventListener('click',function(e){if(menuOpen()&&!hdr.contains(e.target))setMenu(false,false)});
    d.addEventListener('keydown',function(e){if(e.key!=='Tab'||!menuOpen())return;var f=hdrFocusables();if(!f.length)return;
      var i=f.indexOf(d.activeElement);
      if(e.shiftKey&&i<=0){e.preventDefault();f[f.length-1].focus()}else if(!e.shiftKey&&(i===-1||i===f.length-1)){e.preventDefault();f[0].focus()}});
    // masaüstü genişliğine geçilirse kilit kalmasın
    if(window.matchMedia){var mq=matchMedia('(min-width:1041px)');var mqf=function(){if(mq.matches&&menuOpen())setMenu(false,false)};if(mq.addEventListener)mq.addEventListener('change',mqf)}
  }
  // mega menu
  var mb=d.querySelector('.mega-btn'),mg=d.getElementById('mega');
  function closeMega(){if(mb&&mg){mg.hidden=true;mb.setAttribute('aria-expanded','false')}}
  if(mb&&mg){
    // Q3: mega açılırken dil menüsü kapanır (dil menüsü açılırken mega zaten kapanıyordu)
    mb.addEventListener('click',function(e){e.stopPropagation();var open=mg.hidden;mg.hidden=!open;mb.setAttribute('aria-expanded',open);if(open)closeLang()});
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
    // en içteki açık katman kapanır: dil menüsü → mega → mobil menü
    if(lm&&!lm.hidden){closeLang();lb.focus();return}
    if(mg&&!mg.hidden){closeMega();mb.focus();return}
    if(menuOpen())setMenu(false,true)});

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
  // GA4 olayları (consent.js; yalnız GA4_ID doluyken ve ziyaretçi izin verdiyse gönderilir — kişisel veri yok)
  function track(n,p){try{if(typeof window.hostlioTrack==='function')window.hostlioTrack(n,p)}catch(_e){}}
  d.querySelectorAll('[data-contact-form]').forEach(function(f){
    // Q8: süre sayfa yüklenince değil, formla ilk etkileşimde başlar. Çok hızlı gönderim artık sessizce
    // düşmez ve sahte "ulaştı" denmez: istek yine gider, yalnız suspect:'fast' ile işaretlenir.
    var t0=0;function mark(){if(!t0)t0=Date.now()}
    f.addEventListener('focusin',mark);f.addEventListener('input',mark);
    // Q14: tarayıcı balonu yerine çevrili alan mesajı (form novalidate); aria-invalid + aria-describedby
    function fieldErr(el,msg){var lab=el.closest('label')||el.parentNode,id='err-'+el.name,sp=d.getElementById(id);
      if(!msg){el.removeAttribute('aria-invalid');if(sp)sp.hidden=true;return}
      if(!sp){sp=d.createElement('span');sp.id=id;sp.className='field-err';lab.appendChild(sp);
        el.setAttribute('aria-describedby',((el.getAttribute('aria-describedby')||'')+' '+id).trim())}
      sp.textContent=msg;sp.hidden=false;el.setAttribute('aria-invalid','true')}
    function check(el){var v=(el.value||'').trim(),msg='';
      if(el.required&&!v)msg=f.dataset.vReq;else if(el.type==='email'&&v&&!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v))msg=f.dataset.vEmail;
      fieldErr(el,msg);return !msg}
    [].forEach.call(f.querySelectorAll('[required],input[type=email]'),function(el){
      el.addEventListener('blur',function(){if(el.getAttribute('aria-invalid'))check(el)});
      el.addEventListener('input',function(){if(el.getAttribute('aria-invalid'))check(el)})});
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var fd=new FormData(f),s=f.querySelector('.form-status'),b=f.querySelector('button[type=submit]');
      var bad=[].filter.call(f.querySelectorAll('[required],input[type=email]'),function(el){return !check(el)});
      if(bad.length){if(s)s.textContent='';bad[0].focus();return}
      // D9: bal küpü doluysa bot say — Make kotası harcanmaz; ama sahte başarı da gösterilmez
      if((fd.get('website')||'').toString().trim()){if(s)s.textContent=f.dataset.err;return}
      var fast=!t0||Date.now()-t0<1500;
      var g=function(k){return (fd.get(k)||'').toString().trim()};
      var lines=['Hotel: '+g('hotel'),'Rooms: '+g('rooms'),'Country/city: '+g('country'),'Language: '+(f.dataset.lang||''),'',g('message')];
      function mailto(){window.location.href='mailto:'+f.dataset.mail+'?subject='+encodeURIComponent(f.dataset.subject+' - '+g('hotel'))+'&body='+encodeURIComponent(lines.join('\n')+'\nEmail: '+g('email'))}
      if(!f.dataset.endpoint||!window.fetch){mailto();if(s)s.textContent=f.dataset.sent;return}
      if(b)b.disabled=true;if(s)s.textContent=f.dataset.sending||'';
      var payload={type:'contact',name:g('name'),email:g('email'),subject:'Request a Demo',message:lines.join('\n'),date:new Date().toISOString(),
        hotel:g('hotel'),rooms:g('rooms'),country:g('country'),lang:f.dataset.lang||'',page:location.pathname,acquisition:acq()};
      if(fast)payload.suspect='fast';
      fetch(f.dataset.endpoint,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)})
      .then(function(r){if(!r.ok)throw 0;f.reset();t0=0;if(s)s.textContent=f.dataset.ok;track('generate_lead',{form:'contact'})})
      .catch(function(){if(s)s.textContent=f.dataset.err})
      .then(function(){if(b)b.disabled=false});
    });
  });

  // Q13: 404 sayfası 6 dilin metnini taşır; adresin dil önekine (yoksa tarayıcı diline) göre gösterilir
  var nf=d.querySelectorAll('[data-nf]');
  if(nf.length){var m=location.pathname.match(/^\/(tr|en|es|it|pt|fr)(\/|$)/),nl=m?m[1]:((navigator.language||'en').slice(0,2).toLowerCase());
    var pick=d.querySelector('[data-nf="'+nl+'"]');
    if(pick){[].forEach.call(nf,function(x){x.hidden=x!==pick});root.lang=pick.getAttribute('lang');d.title=pick.dataset.title}}

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
      render();track('pricing_billing_toggle',{billing:annual?'annual':'monthly',context:'pricing'});[].forEach.call(box.querySelectorAll('a.btn'),function(a){try{var u=new URL(a.getAttribute('href'),location.origin);u.searchParams.set('billing',annual?'annual':'monthly');a.setAttribute('href',u.pathname+u.search)}catch(e){}})});
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

  // S1: mesaj şablonlarını kopyala (yalnız Clipboard API varken görünür)
  if(navigator.clipboard&&window.isSecureContext)d.querySelectorAll('[data-copy]').forEach(function(b){b.hidden=false;var lbl=b.textContent;
    b.addEventListener('click',function(){var q=b.parentNode.querySelector('.tpl-text');if(!q)return;
      navigator.clipboard.writeText(q.innerText.trim()).then(function(){b.textContent=b.dataset.done;setTimeout(function(){b.textContent=lbl},1800)},function(){})})});

  // "yazdır / PDF" düğmeleri (satır içi onclick yerine — O4 CSP)
  d.querySelectorAll('[data-print]').forEach(function(b){b.addEventListener('click',function(){window.print()})});

  // gentle reveal for below-the-fold blocks only (content is visible at rest)
  if('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches){
    var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){en.target.classList.remove('pre');io.unobserve(en.target)}})},{rootMargin:'0px 0px -8% 0px'});
    d.querySelectorAll('.rv').forEach(function(el){if(el.getBoundingClientRect().top>window.innerHeight){el.classList.add('pre');io.observe(el)}});
  }
})();
