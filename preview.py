import re,glob,os,base64,json
D='dist'
css=open('src/assets/style.css').read()
for fn in os.listdir('src/assets/fonts'):
    b=base64.b64encode(open('src/assets/fonts/'+fn,'rb').read()).decode()
    css=css.replace(f'url(/assets/fonts/{fn})',f'url(data:font/woff2;base64,{b})')
css+='\n.site-header{top:env(safe-area-inset-top,0px)}\n.preview-bar{background:#121B36;color:#fff;font:600 13px/1.4 var(--font);padding:8px 16px;text-align:center}.preview-bar a{color:#ECE8FB}\n'
favicon=base64.b64encode(open('src/assets/favicon.svg','rb').read()).decode()
pages={}
for f in sorted(glob.glob(D+'/**/index.html',recursive=True)):
    path='/'+os.path.relpath(f,D).replace('index.html','')
    s=open(f).read()
    body=re.search(r'<body>(.*?)<script src="/assets/site.js"',s,re.S).group(1)
    import html as H; title=H.unescape(re.search(r'<title>(.*?)</title>',s).group(1))
    lang=re.search(r'<html class="nojs" lang="([\w-]+)"',s).group(1)
    # internal links -> hash routes
    body=re.sub(r'href="(/(?!assets)[^"#]*)"',lambda m:f'href="#{m.group(1)}"' if not m.group(1).endswith('.txt') else 'href="#/"',body)
    body=body.replace('href="#main"','href="#main" data-skip')
    body=re.sub(r' data-endpoint="[^"]*"','',body)
    for fn in os.listdir('src/assets/img'):
        body=body.replace('/assets/img/'+fn, 'IMG_'+fn)
    pages[path]={'b':body,'t':title,'l':lang}
js=open('src/assets/site.js').read()
imgs={fn:'data:image/webp;base64,'+base64.b64encode(open('src/assets/img/'+fn,'rb').read()).decode() for fn in os.listdir('src/assets/img')}
data=json.dumps(pages,ensure_ascii=False).replace('</','<\\/')
imgjson=json.dumps(imgs)
out=f'''<title>Hostlio Site Preview</title>
<link rel="icon" href="data:image/svg+xml;base64,{favicon}">
<style>{css}</style>
<div id="app"></div>
<script>
const P={data};const IM={imgjson};
function render(){{
  let p=(location.hash.replace(/^#/,'')||'/').split('?')[0];
  if(!P[p])p='/';
  const pg=P[p];document.title=pg.t;document.documentElement.lang=pg.l;
  const note=pg.l==='tr'?'Önizleme: yeni Hostlio Pro sitesi, tüm sayfalar gezilebilir. Kayıt formu ve panel girişi canlı sitede çalışır.':'Preview: new Hostlio Pro site, every page is browsable. Sign-up and dashboard login work on the live site.';
  document.getElementById('app').innerHTML='<div class="preview-bar">'+note+'</div>'+pg.b.replace(/IMG_([\\w.-]+\\.webp)/g,(m,f)=>IM[f]||'');
  document.querySelectorAll('[data-skip]').forEach(a=>a.addEventListener('click',e=>{{e.preventDefault();document.getElementById('main').focus();document.getElementById('main').scrollIntoView()}}));
  document.getElementById('main').tabIndex=-1;
  window.scrollTo(0,0);
  (function(){{ {js} }})();
}}
addEventListener('hashchange',render);render();
</script>'''
open('/mnt/user-data/outputs/hostlio-onizleme.html','w').write(out)
print(len(pages),'pages',round(len(out)/1024),'KB')
