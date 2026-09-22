// tasarim-v2 — ödeme sayfası arayüzü: dil, plan özeti, aylık/yıllık düğmeleri.
// ⛔ Ödeme mantığı burada DEĞİL (bkz. signup betiği: submitForm, toggleBilling).
(function(){
  var d=document,CO=window.CO; if(!CO) return;
  var FOOT={en:['Terms of Service','Privacy Policy'],tr:['Kullanım Şartları','Gizlilik Politikası'],es:['Términos del servicio','Política de privacidad'],it:['Termini di servizio','Informativa sulla privacy'],pt:['Termos de serviço','Política de privacidade'],fr:["Conditions d’utilisation",'Politique de confidentialité']};
  var LOCALE={en:'en_US',tr:'tr_TR',es:'es_ES',it:'it_IT',pt:'pt_BR',fr:'fr_FR'};
  function planId(){var c=d.querySelector('input[name="plan"]:checked');return c?c.id.replace('plan-',''):'starter'}
  function annual(){return typeof isAnnual!=='undefined'&&isAnnual}
  function summary(){
    var id=planId(),L=CO.lang,pt=(CO.PLAN_TXT[L]||CO.PLAN_TXT.en)[id];
    var names={starter:'Starter',pro:'Pro',growth:'Growth'};
    d.getElementById('sum-name').textContent=names[id];
    d.getElementById('sum-price').textContent='$'+(annual()?CO.ANNUAL[id]:CO.MONTHLY[id]);
    d.getElementById('sum-suffix').textContent=annual()?tr('mo_ann'):tr('mo');
    var ul=d.getElementById('sum-feats'),chk='<svg viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="M4 10.5l4 4 8-9" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
    ul.innerHTML='';(pt?pt[1]:[]).forEach(function(f){var li=d.createElement('li');li.innerHTML=chk;var s=d.createElement('span');s.textContent=f;li.appendChild(s);ul.appendChild(li)});
  }
  function apply(){
    var L=CO.lang; d.documentElement.lang=L==='pt'?'pt-BR':L;
    d.querySelectorAll('[data-t]').forEach(function(el){el.textContent=tr(el.getAttribute('data-t'))});
    d.querySelectorAll('[data-tph]').forEach(function(el){el.placeholder=tr(el.getAttribute('data-tph'))});
    var t=d.getElementById('co-terms'); if(t) t.innerHTML=tr('terms').replace('{t}',CO.TERMS[L]).replace('{p}',CO.PRIVACY[L]);
    var ft=d.getElementById('co-f-terms'),fp=d.getElementById('co-f-privacy'),f=FOOT[L]||FOOT.en;
    if(ft){ft.textContent=f[0];ft.href=CO.TERMS[L]} if(fp){fp.textContent=f[1];fp.href=CO.PRIVACY[L]}
    d.querySelectorAll('[data-home]').forEach(function(a){a.href=CO.HOME[L]});
    var b=d.getElementById('submit-btn'); if(b&&!b.disabled) b.textContent=tr('submit');
    var o=d.querySelector('#country option[value="__OTHER__"]'); if(o) o.textContent=tr('other');
    if(typeof toggleBilling==='function'){ // fiyat satırlarını yeni dilde yeniden yaz
      d.querySelectorAll('.plan-option label').forEach(function(lb){var id=lb.getAttribute('for').replace('plan-','');
        lb.querySelector('.plan-price').innerHTML='$'+(annual()?CO.ANNUAL[id]:CO.MONTHLY[id])+'<small>'+(annual()?tr('mo_ann'):tr('mo'))+'</small>';
        var reg={starter:59,pro:109,growth:189}[id]; lb.querySelector('.plan-old').innerHTML=tr('regular')+' <s>$'+reg+'</s>'});
    }
    var sel=d.getElementById('co-lang'); if(sel) sel.value=L;
    summary();
  }
  function setBill(a){
    if(a!==annual()&&typeof toggleBilling==='function') toggleBilling();
    d.querySelectorAll('.co-billing [data-bill]').forEach(function(x){var on=(x.dataset.bill==='a')===a;x.classList.toggle('on',on);x.setAttribute('aria-pressed',on)});
    summary();
  }
  d.addEventListener('DOMContentLoaded',function(){
    var q=new URLSearchParams(location.search),p=q.get('plan');
    if(p&&d.getElementById('plan-'+p)) d.getElementById('plan-'+p).checked=true;
    apply();
    if(q.get('billing')==='annual') setBill(true);
    d.querySelectorAll('input[name="plan"]').forEach(function(r){r.addEventListener('change',summary)});
    d.querySelectorAll('.co-billing [data-bill]').forEach(function(x){x.addEventListener('click',function(){setBill(x.dataset.bill==='a')})});
    var sel=d.getElementById('co-lang');
    if(sel) sel.addEventListener('change',function(){CO.lang=sel.value;try{localStorage.setItem('hostlio_lang',sel.value)}catch(e){}
      var u=new URL(location.href);u.searchParams.set('lang',sel.value);history.replaceState(null,'',u);apply()});
    // success_url dönüşünde (?checkout=success) formu gizle: ödeme alınmış.
    if(q.get('checkout')==='success'){var fw=d.getElementById('form-wrap');if(fw)fw.style.display='none'}
    d.documentElement.classList.remove('nojs');d.documentElement.classList.add('js');
  });
})();
