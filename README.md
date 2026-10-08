# Hostlio Pro — web sitesi (hostliopro.com)

Python statik üretici, 6 dil (EN, TR, ES, IT, PT-BR, FR). Canlı alan adı **hostliopro.com** (www → apex).
Aşağıdaki "v5 … v14" bölümleri sürüm geçmişidir; geçerli mimari bu bölümdedir (3 Ekim 2026).

## Mimari (güncel)
| Dosya | Görev |
|---|---|
| `build.py` | Giriş noktası: rotalar (`ROUTES`), ortak düzen (`layout`, `finish`), JSON-LD, sitemap, llms*.txt, `vercel.json` üretimi, CSP, yönlendirmeler. `python3 build.py` → `dist/` |
| `pricing.py` | **Tek fiyat kaynağı**: aylık/yıllık/Early Bird fiyatları, AI mesaj kotası, oda limiti, deneme günü, dile göre para biçimi. Metinlerde rakam yerine `⟦price:starter⟧`, `⟦annual:pro⟧`, `⟦annual_mo:growth⟧`, `⟦regular:…⟧`, `⟦quota:…⟧`, `⟦rooms:…⟧` yazılır |
| `content_<dil>.py` | Sayfa içerikleri (6 dil); `home_v3.py` ana sayfa, `pages_v4.py` tesis tipi/karşılaştırma sayfaları, `lang_<es/it/pt/fr>.py` dil sözlükleri |
| `booking_templates.py` | Booking.com otomatik cevap yazısının (6 dil) başlık/açıklaması ve 12 kopyalanabilir mesaj şablonu; `pages_v4.guides()` yazıya ekler, blog listesi başlığı `post_meta()` ile aynı kaynaktan |
| `legal_v6.py`, `legal_v6_intl.py`, `legal_v5.py` | Gizlilik, şartlar, hesap silme (alt işleyici listesi `SUBPROCESSORS`) |
| `security_page.py`, `roi_page.py`, `signup_page.py` | Güvenlik + DPA, ROI hesaplayıcı, kayıt/ödeme sayfaları |
| `src/` | Olduğu gibi kopyalanan dosyalar: `assets/` (CSS, JS, görsel, font, video), `attribution.js`, Google doğrulama dosyası, `robots.txt`, `vercel.json` tabanı |
| `page_dates.json` | Sayfa başına içerik özeti + tarih (dateModified / sitemap lastmod). Build günceller; commit edin |
| `scripts/check.py` | Kapı: kırık link/asset, JSON-LD, hreflang, title/description tekrarı ve uzunluğu, satır içi betik (CSP), fiyat yer tutucusu, yönlendirme hedefleri. `--live-prices` canlı `plans` ucuyla karşılaştırır |
| `scripts/attribution-check.mjs` | `src/attribution.js` ilk temas + 90 gün testi (kök `attribution.js` birebir kopya olmalı) |
| `preview.py`, `shots/*.py` | Yerel önizleme ve ekran görüntüsü/erişilebilirlik betikleri (build'e bağlı değil) |

İç link (S4, 8 Ekim 2026): yazılarda "İlgili yazılar", ürün/segment sayfalarında "İlgili rehberler" bloğu `build.py`
`RELATED_POSTS` / `PAGE_GUIDES` eşlemesinden üretilir; yeni yazı eklerken bu iki tabloya da ekleyin.
404: Vercel tek `/404.html` verir; sayfa 6 dilin metnini taşır, `site.js` dil önekine göre gösterir.

Tarayıcı betikleri (`src/assets/`): `site.js` (menüler, fiyat düğmesi, iletişim formu, video), `prices.js`
(sayfadaki `hostlio-pricing` JSON'u + canlı `plans` ucu, `early_bird=false` ⇒ Early Bird metinleri gizlenir),
`signup.js` (kayıt formu → `signup-checkout`, sunucu hata kodlarının 6 dile çevirisi), `roi.js`, `consent.js` (GA4 + çerez izni).
Satır içi `<script>` ve `onclick=` **yasak** (CSP `script-src 'self'`; `check.py` yakalar). Veri gerekiyorsa
`<script type="application/json">` bloğu kullanın.

### Analitik (GA4 + çerez izni, 8 Ekim 2026)
- Kimlik `build.py` → `GA4_ID` (şu an `G-W74GFJQYJ4`). `""` yapılırsa hiçbir analitik yüklenmez: `consent.js` yok, bant yok,
  altbilgi düğmesi yok, CSP'de Google kökeni yok, gizlilik politikası eski metninde kalır.
- `src/assets/consent.js` (`<head>`'de, senkron): Consent Mode v2 varsayılanı dördü de `denied`; bant 6 dilde; **gtag.js yalnız
  "Kabul et"ten sonra** yüklenir (izinden önce Google'a istek yok). `ad_*` sinyalleri hep `denied`, Google sinyalleri kapalı.
  Seçim `localStorage.hostlio_consent` (6 ay). Altbilgide ve gizlilik politikasında "Çerez tercihleri" düğmesi bandı açar.
  "Reddet" `_ga*` çerezlerini siler. CSP eklemeleri `csp()`'de (Google'ın GA4 listesi).
- Gizlilik politikası çerez paragrafı: `analytics_consent.py` (`GA4_TEXT`, 6 dil; build çerez h2'sini bulup ekler, `id="cookies"`).
- Olaylar (parametrelerde kişisel veri yok; `window.hostlioTrack`):

| Olay | Nerede | Parametreler |
|---|---|---|
| `page_view` | her sayfa (otomatik) | — |
| `signup_cta_click` | `/xx/signup/` bağlantısı tıklanınca; **kayıt sayfası açılınca gönderilir** | `cta_location` (header/footer/hero/pricing_plans/final_cta/content), `cta_page`, `plan`, `billing` |
| `signup_form_start` | kayıt formuna ilk odak | `plan`, `billing` |
| `signup_plan_select` | kayıt sayfasında plan değişimi | `plan` |
| `signup_submit` | geçerli form gönderimi (başarılıysa Stripe dönüşünde gönderilir) | `plan`, `billing` |
| `begin_checkout` | Stripe'a yönlendirme (Stripe dönüşünde gönderilir) | `plan`, `billing` |
| `signup_error` | sunucu/ağ hatası | `plan`, `error_field` |
| `sign_up` | `?checkout=success` dönüşü | `method=stripe_checkout` |
| `checkout_cancelled` | `?checkout=cancelled` dönüşü | — |
| `generate_lead` | iletişim formu başarılı | `form=contact` |
| `pricing_billing_toggle` | aylık/yıllık düğmesi | `billing`, `context` (pricing/signup) |

  Ayrılmadan hemen önceki olaylar (`signup_cta_click`, `signup_submit`+`begin_checkout`) sekmenin sessionStorage'ına yazılıp
  sonraki sayfada gönderilir: gtag olayları ~5 sn toplu gönderir, hemen gezinince kayboluyordu (test edildi).
  GA4'te anahtar olay (key event) önerisi: `sign_up`, `generate_lead`, `begin_checkout`.

### Adresler
- Kayıt: `/xx/signup/` (her dilde; CTA'lar `finish()` ile doğrudan buraya gider). `/signup/` dil algılayan giriş
  noktası (Stripe dönüşü `?checkout=success|cancelled`, eski bağlantılar).
- `trailingSlash: true`, `cleanUrls` KAPALI ⇒ `/google3ccd63ec6d0747db.html`, `/llms.txt` gibi dosyalar
  yönlendirmesiz 200 döner. Eski `.html` adresleri `lang_redirects()` + `src/vercel.json` ile açıkça yönlenir.

### Fiyat değişince / Early Bird bitince
1. Stripe'ta fiyatı değiştirin, backend `planConfig.ts` `EARLY_BIRD` bayrağını çevirin.
2. `pricing.py`'yi aynı değerlere getirin (`EARLY_BIRD=False` için `regular_annual` doldurulmalı, yoksa build durur).
   Early Bird metinleri (SSS, plan kartı notları) "ilk 50 müşteri" der — kapanınca metinleri de güncelleyin.
3. `python3 build.py && python3 scripts/check.py --live-prices` → `RESULT: OK`.
Fiyat ve ödeme sayfaları canlı ucu zaten okuduğu için bu adımlar yapılana kadar da doğru tutarı gösterir.

### Yayın
- `vercel.json` build tarafından üretilir; `buildCommand` `build.py` içindeki `BUILD_COMMAND`'dır. Python varsa
  build + check.py hatası deploy'u düşürür; yalnız python3 hiç yoksa commit'li `dist/` kullanılır.
- CI: `.github/workflows/kapilar.yml` (build, check.py, attribution testi, `git diff --exit-code dist`).
  Push için `workflow` yetkili token gerekir.

## Sürüm geçmişi

## v5 değişiklikleri
- Marka adı her yerde "Hostlio Pro" (logo: Hostlio + turuncu Pro). Schema'da alternateName "Hostlio".
- Gizlilik Politikası ve Kullanım Şartları mevcut siteden (20 Nisan 2026 metni) alındı: EN `/privacy/`, `/terms/` (eski URL'ler korunur), TR çevirileri `/gizlilik-politikasi/`, `/kullanim-sartlari/` (İngilizce metin esastır notuyla). Footer'da linkler + `/delete-account`.
- Mevcut sitedeki `signup.html`, `delete-account.html`, `attribution.js` (UTM ilk temas takibi, tüm sayfalarda yüklenir) ve Google Search Console doğrulama dosyası korunur.
- Kayıt butonları `/signup`, giriş `https://dashboard.hostliopro.com`.
- Eski blogdaki 4 İngilizce yazı yeni tasarıma taşındı (`/en/blog/...`); eski URL'ler ve /about, /contact, /faq, /channels için 301 yönlendirmeleri `src/vercel.json`'da. Eski overbooking yazısı yeni overbooking rehberine yönlenir.
- Mobilde ana görsel kolajı (avlu fotoğrafı, otel sahibi, Lio mesaj balonu, bildirim çipleri) masaüstündeki düzenle aynı gösterilir.
- "Kredi kartı gerekmez" ve yıllık planlarda %20 indirim bilgisi (Kullanım Şartları'na göre) SSS ve CTA'lara eklendi.
- Not: Gizlilik Politikası "takip çerezi kullanmıyoruz" diyor. GA4 eklenirse politikanın güncellenmesi gerekir; çerezsiz Plausible bu metinle uyumludur.

### v4: SEO/GEO değişiklikleri (claude-seo skill'i ile denetlendi)
- Türkçe arama dili: "otel programı", "pansiyon programı" vb. başlık, açıklama, H1 ve SSS'lerde.
- 7 yeni sayfa x 2 dil: pansiyon / butik otel / apart otel / hostel programı, otel programı karşılaştırması (kaynaklı, tarihli), 2 rehber (overbooking, Booking.com otomatik cevap). Toplam 38 sayfa.
- Her sayfada görünür "Son güncelleme" tarihi; blog yazılarında yazar satırı ve dateModified.
- `llms-full.txt` (tüm sitenin düz metni), responsive görseller (480w srcset), ana görsel preload + fetchpriority.
- Güvenlik başlıkları (HSTS, X-Frame-Options, Permissions-Policy) `src/vercel.json`'da.
- Ölçüm ve varlık ayarları `build.py` başında: GA4_ID, PLAUSIBLE_DOMAIN, GSC_VERIFY, BING_VERIFY, SAME_AS, APP_STORE_URL. Boş bırakılanlar sayfaya yazılmaz.
- IndexNow anahtar dosyası otomatik üretilir (`/<INDEXNOW_KEY>.txt`).

### Yayından sonra yapılacaklar (sırayla)
1. Google Search Console ve Bing Webmaster Tools'ta siteyi doğrula (token'ları build.py'ye yaz), `sitemap.xml` gönder.
2. Analytics'i aç (GA4 veya Plausible). AI trafiği için referrer'ları izle: chatgpt.com, perplexity.ai, claude.ai, gemini.google.com, copilot.microsoft.com.
3. IndexNow ile tüm URL'leri bildir (Bing, Yandex; ChatGPT aramasının Bing sonuçlarını kullandığı biliniyor).
4. SAME_AS'e resmi profilleri ekle: LinkedIn şirket sayfası, Instagram, YouTube, Hotel Tech Report, G2, Capterra. APP_STORE_URL'i doldur.
5. Blog yazılarına gerçek yazar adları ekle (ör. kurucu/ürün sorumlusu), Hakkımızda'ya ekip bölümü.
6. Site dışı: Hotel Tech Report / G2 / Capterra profilleri ve ilk müşteri yorumları, Channex partner dizini, Reddit ve otelci toplulukları, Google Business Profile, YouTube'da ürün videoları (reklam videoları hazır).
7. Karşılaştırma sayfasını 3 ayda bir güncelle (rakip fiyatları değişir; güncel içerik AI'da daha çok alıntılanır).
8. Gizlilik Politikası ve Kullanım Şartları sayfalarını ekle.

### v3 değişiklikleri
- Marka renkleri (hostlio-dashboard-main/src/index.css): turuncu #FF6B35, lacivert #1B2B4B, koyu #0F1E36; zemin reklam görsellerindeki krem #FBF6F0. Turuncu butonlarda erişilebilirlik için lacivert yazı kullanıldı (kontrast 5.9:1).
- Logo: uygulama ikonundaki işaret (lacivert kare, beyaz H, turuncu çizgi ve nokta).
- Görseller: Hostlio'nun kendi reklam videoları ve afişinden kareler (brand-*.webp) + Unsplash fotoğrafları (hostlio-*.webp).
- Yeni bölümler: hero kolajı, "Gece 02:14" hikâye kartları, 8 kartlı özellik bentosu, tesis tipi kartları, AI bölümünde fotoğraf kartı, kapak görselli blog yazıları, görselli Özellikler ve Hakkımızda sayfaları.

### Tasarım (v2)
- Referans: guesty.com'un yapısı (sıcak kırık beyaz zemin, ince ağırlıklı büyük başlıklar, italik vurgu kelimesi, hap butonlar, ilgi alanı seçici, sekmeli ürün turu, fotoğraf kartları üzerinde yüzen arayüz çipleri, "tek çatı altında" akordeon, koyu AI bölümü, iki kolonlu SSS). Guesty'nin logosu, rengi ve metni kullanılmadı.
- Kullanılan skill'ler: Anthropic `frontend-design`, `ui-ux-pro-max`, `taste-skill` (soft-skill: double-bezel kartlar, buton içinde ikon, özel easing), Vercel web interface guidelines.
- Font: Instrument Sans (self-host, normal + italik). İkonlar: Phosphor Light. OTA logoları: Simple Icons.
- Fotoğraflar (Unsplash lisansı, ücretsiz): lobi Josh Hild, oda Andrew Neel, işletmeci ve oda masası Vitaly Gariev. `src/assets/img/`

Framework yok. `python3 build.py` → `dist/` klasörü (24 sayfa + sitemap, robots, llms.txt, 404).

### Yayına alma (Vercel)
1. Bu klasörü bir GitHub reposuna koy.
2. Vercel → New Project → Framework: **Other**, Build command: `python3 build.py`, Output: `dist`.
   (Ya da doğrudan `dist/` klasörünü sürükle-bırak ile yükle.)
3. Domain: `www.hostliopro.com`. Eski URL'ler için `src/vercel.json` içine `redirects` ekle.
4. Google Search Console + Bing Webmaster Tools'a `https://www.hostliopro.com/sitemap.xml` gönder.

### Düzenleme
| Ne | Nerede |
|---|---|
| Kayıt/giriş linki, form endpoint, e-posta | `build.py` üstündeki sabitler (`APP_URL`, `FORM_ENDPOINT`, `EMAIL`) |
| Fiyatlar | `build.py` → `PLANS` + `content_*.py` → `PLAN_TXT`, FAQ metinleri, `llms.txt` bloğu |
| Türkçe metinler | `content_tr.py` |
| İngilizce metinler | `content_en.py` |
| Tasarım (renk/tipografi) | `src/assets/style.css` (üstteki `:root` token'ları) |
| Yeni blog yazısı | `ROUTES`'a anahtar ekle, `content_*.py` içinde `POSTS` + `post_xxx()` fonksiyonu, `pages()` listesine ekle |

Formu gerçek bir servise bağlamak için `FORM_ENDPOINT`'e Formspree/Basin/kendi Supabase edge function URL'ini yaz; boşsa mailto ile çalışır.

### SEO katmanı
- Her sayfada benzersiz title/description, canonical, `hreflang` (tr, en, x-default), Open Graph + Twitter kartı (`og-tr.png`, `og-en.png`)
- JSON-LD `@graph`: Organization, WebSite, WebPage (About/Contact/FAQ/Collection tipleri), BreadcrumbList, SoftwareApplication (+ fiyat teklifleri), FAQPage, BlogPosting
- `sitemap.xml` hreflang alternatifleriyle; semantik HTML, tek H1, sıralı başlıklar
- Self-host variable font (preload), framework JS yok, görseller HTML/CSS ile → hızlı LCP, CLS≈0
- axe-core WCAG 2 AA taraması: 0 ihlal

### GEO (AI arama motorları: ChatGPT, Perplexity, Claude, Google AI Overviews)
- `robots.txt` GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended vb. için açık
- `/llms.txt`: ürünün tek dosyalık, gerçeklere dayalı özeti + tüm sayfa linkleri
- Her ana sayfada "Kısaca…" / "…nedir?" cevap bloğu (AI'ın alıntılayacağı net tanım cümlesi)
- Karşılaştırma tabloları (plan/özellik, kanal listesi), SSS'ler hem görünür hem schema'da
- Tarihli içerik (`dateModified`, "Son güncelleme"), rakamlar tutarlı (30+ dil, 100+ OTA, 20+ ülke, 7 gün deneme)

### Yayından önce doğrulanması gerekenler
Eski sitede olmayan, benim varsaydığım bilgiler — yanlışsa `content_*.py` içinde düzelt:
- Kayıt/giriş adresi `app.hostliopro.com/signup` ve `/login`
- Online check-in'in Pro ve Growth planlarında olması
- "Komisyon yok, kurulum ücreti yok" ifadesi
- Lio'nun **onay modu** (cevapları göndermeden önce onaylama) ve devir kuralları
- Kota dolunca otomatik yanıtın durması; plan değişikliğinin sonraki dönemde yansıması
- Fiyatlara KDV/vergi dahil olmaması; Türkçe destek
- Gizlilik Politikası ve Kullanım Şartları sayfaları eklenmedi (hukuki metin gerektirir) — eski sayfaların URL'lerini footer'a ekle
- Müşteri yorumu/logo yok: gerçek, izinli yorumlar gelince eklenmeli (sosyal kanıt dönüşüm için önemli)

### v6 — 6 dil (TR, EN, ES, IT, PT, FR)
- Yeni diller: `content_es/it/pt/fr.py` (sayfalar) + `lang_es/it/pt/fr.py` (arayüz, ana sayfa, tesis tipi sayfaları, karşılaştırma, rehberler, yasal metin çevirileri).
- URL'ler: /es/, /it/, /pt/, /fr/ altında yerelleştirilmiş slug'lar (build.py → ROUTES).
- Her sayfada 6 dilli hreflang + x-default (en), og:locale + alternate, dile özel OG görseli (og/make.py), sitemap alternates, llms.txt'de dil bölümleri.
- Başlıkta dil seçici menüsü. Eski İngilizce blog yazıları yalnızca EN.
- Yasal metin çevirilerinde "İngilizce metin esastır" notu var.
- Kontrol: 130 sayfa, kırık link yok, JSON-LD geçerli, axe temiz, 360/390/768 px'te yatay kaydırma yok.

### v7 — mevcut siteden entegrasyonlar (~/Developer/-hostlio-website-main)
- Plan bilgileri depodaki güncel haliyle hizalandı: Starter 3.000 / Pro 20.000 / Growth 50.000 AI mesajı; Growth çoklu tesis, 150 odaya kadar (6 dil, llms.txt dahil).
- Fiyatlar: Aylık/Yıllık geçişi (%20) + Supabase `plans` fonksiyonundan canlı fiyat (mevcut sitedeki anon anahtarla; yanıt gelmezse sayfadaki fiyatlar kalır). Early Bird kapanırsa "early-bird" satırı otomatik gizlenir.
- İletişim formu: Make.com webhook'una eski formla aynı JSON (type, name, email, subject, message, date) + hotel, rooms, country, lang, page, acquisition (attribution.js ilk temas kaydı). Hata olursa kullanıcıya e-posta/WhatsApp önerilir.
- WhatsApp +1 341 341 4479: iletişim sayfası, footer ve Organization şeması (telephone).
- Kanonik alan adı: https://hostliopro.com (mevcut sitedeki gibi, www değil).
- signup.html, attribution.js, delete-account.html, Google doğrulama dosyası: mevcut siteyle birebir aynı (kontrol edildi).
- Vercel: kök vercel.json (buildCommand `python3 build.py`, outputDirectory `dist`) build sırasında src/vercel.json'dan üretilir. Pillow yoksa görsel varyantları üretilmez, depodaki hazır dosyalar kullanılır.
- CI: .github/workflows/kapilar.yml → build + scripts/check.py (kırık link, JSON-LD, hreflang karşılıklılığı, tekrar eden title).

### v8 — güncel depo (21 Eylül) ile hizalama
- Kotalar tekrar 1.000 / 5.000 / 12.000 AI mesajı; Growth 2 tesise kadar, 150 oda (patron kararı, commit d35b596).
- E-posta / web chat / Telegram misafir mesajlaşması vaatleri 6 dilde kaldırıldı. Lio: WhatsApp (tüm planlar) + OTA gelen kutuları Booking.com, Airbnb, Expedia (Pro ve Growth). (commit 1f05feb)
- "Kredi kartı gerekmez" ifadesi kaldırıldı: kart kayıtta alınır, deneme bitene kadar ücret çekilmez (CTA, SSS, kullanım şartları; commit 75db455).
- src/signup.html depodaki son sürümle değiştirildi.

### v9 — yıllık fiyatlar
- Her plan kartında yıllık fiyat satırı (Starter $39/ay – $470/yıl, Pro $71/ay – $854/yıl, Growth $119/ay – $1.430/yıl), fiyat sayfasında 6 dilde aylık/yıllık fiyat tablosu, yapılandırılmış veride yıllık teklifler, llms.txt. Canlı fiyat gelirse satırlar da güncellenir.

### v10 — yeni görseller (Higgsfield, GPT Image 2.5, 2K)
- 12 yeni görsel `src/assets/img/gen-*.webp` (1080×1350, 480w varyantlarıyla):
  hostel, apart, pansiyon, butik oda → tesis tipi sayfaları + ana sayfa kartları;
  blog kapakları: owner-laptop (PMS), reception (overbooking), night-desk (otomatik cevap), checkin-phone (AI),
  eski EN yazılar: arrival, room-dusk, facade, terrace-phone.
- 6 dilde alt metinler: build.py → GEN_ALT.
- Kullanılmayan hostlio-lobby/phone/room görselleri unused_img/ klasörüne taşındı.
- Görseller yapay zekâ ile üretildi: gerçek müşteri, gerçek otel ya da referans olarak sunulmamalı.

### v11 — ek görseller ve döngü video
- Özellikler sayfası: gen-team-desk (resepsiyonda tablete bakan ekip). Hakkımızda: gen-shutters (gün doğarken panjur açan işletmeci). Alt metinler 6 dilde (GEN_ALT).
- Sayfa sonu CTA'sı (neredeyse her sayfada): gece resepsiyon sahnesinin 10 sn'lik ileri-geri döngü videosu (Grok Video 1.5, sessiz). src/assets/video/night-desk.webm (≈195 KB) + .mp4 (≈395 KB).
  Görünür olunca yüklenir; "hareketi azalt" ve veri tasarrufu modunda yüklenmez, poster görseli gösterilir. Masaüstünde sağda, metnin arkasında değil.

### v12 — "Yanınızda bir ekip var" bölümü
- Stok fotoğraf yerine gen-support-call (görüntülü kurulum görüşmesindeki otelci) + üstünde kodla çizilmiş destek sohbeti kartı ve "Kanal bağlandı" etiketi (6 dil, home_v3.SUPCARD).
- Gerçek ekip fotoğrafı gelirse sadece sup_img değiştirilir. hostlio-owner unused_img/ klasörüne taşındı.

### v13 — ödeme (kayıt) ve hesap silme sayfaları yeni tasarıma alındı
- `/signup` artık üretiliyor: `signup_page.py` + `src_legacy/signup_script.js` (eski betik, mantık birebir) + `src/assets/checkout.js` (dil, plan özeti, aylık/yıllık).
  - 6 dil: ?lang= → localStorage → yönlendiren sayfanın dili → tarayıcı dili. Site içindeki "Ücretsiz dene" bağlantılarına dil parametresi site.js ekliyor.
  - ?plan= ve ?billing= ön seçimi; sol tarafta seçili planın özeti ve "kart kayıtta alınır, deneme bitene kadar çekim yok" notu.
  - Ödeme mantığı (signup-checkout edge function, ülke/para birimi/saat dilimi tablosu, oda limiti, attribution) DEĞİŞMEDİ. noindex.
- `/delete-account` (ve 6 dildeki karşılıkları) artık normal site şablonunda; eski `delete-account.html` kaldırıldı, /delete-account.html → /delete-account/ 301.
- Eski dosyalar `src_legacy/` klasöründe duruyor (yayına kopyalanmaz).
- Uzun dillerde başlık menüsü taşması düzeltildi.

### v14 — web sitesi analiz raporu (22 Eylül 2026) düzeltmeleri
Kritik
- K1 WhatsApp numarası her yerde +1 279-268-2488 / wa.me/12792682488 (footer, iletişim, JSON-LD, llms.txt) — `build.py` → `WHATSAPP`.
- K2 Fiyat kartı: Aylık'ta yalnız "billed monthly", Yıllık'ta yalnız "$470 billed yearly" (6 dil). Kök neden: `.plan .billed{display:block}` `hidden` özniteliğini eziyordu; style.css başına `[hidden]{display:none!important}` eklendi.
- K3 Kayıt sayfası zaten v13'te yeni tasarımdaydı; `/en/signup/`, `/tr/signup/` … → `/signup?lang=..` yönlendirmesi eklendi, sol panel fiyat kartlarıyla aynı listeyi kullanıyor.
- K4 Türkçe `/tr/` altına taşındı. `/` tarayıcı diline göre /tr/, /es/, /it/, /pt/, /fr/ ya da /en/'e (geçici) yönlenir; eski Türkçe adresler 301 ile /tr/… adresine gider. Yönlendirmeler build sırasında `lang_redirects()` ile üretilip vercel.json'a eklenir. 404 sayfası İngilizce.
- K5 Gizlilik ve Şartlar yeniden yazıldı (`legal_v6.py`, `legal_v6_intl.py`; tarih 23 Eylül 2026): kart peşin + otomatik ücretlendirme ve yenileme, AI kotası ve %110'da durma, Early Bird kilidi, UTM/ilk temas kaydı, online check-in kimlik görseli ve imza, alt işleyici listesi (Twilio/SendGrid "planlanan"), saklama süreleri, CCPA ve KVKK, AI sorumluluk notu. Yeni `/en/dpa/` (DPA, İngilizce) + indirilebilir PDF `src/assets/legal/hostlio-pro-dpa.pdf`.
  ⚠️ Yayından önce avukat okuması. `legal_v6.RETENTION` sürelerini sunucu tarafıyla teyit edin (mesaj 60 gün varsayılan — Setup1.jsx; misafir iletişim 90 gün — rapor).
Yüksek
- Y1 Kayıtta para birimi uyarısı ("Booking.com'daki para birimiyle aynı olmalı, sonradan değiştirilemez") 6 dilde; ülkeye göre varsayılan zaten vardı.
- Y2 Kurulum sözü her yerde: "Hesap dakikalar içinde hazır, kanallar aynı gün bağlı" (30 dk / 5 dk ifadeleri kaldırıldı).
- Y3 "rezervasyona ekler", "her cevap rezervasyon bilgisini kullanır", "anahtarsız giriş" ifadeleri 6 dilde yumuşatıldı.
- Y4 "10–150 oda" → "1–150 oda" (llms.txt, meta, SSS dahil).
- Y5 `build.py` → `DEMO_URL`: Cal.com/Calendly linki yazılınca tüm "Demo iste" düğmeleri takvime gider; boşken iletişim sayfası.
- Y6 Pazarlama metinlerinde "Channex" yerine "sertifikalı kanal bağlantıları"; ad yalnız SSS ve hukuki metinlerde.
Orta
- O1 es/fr/it/pt'de fiyat ve SSS zaten çevriliydi (adresler yerel: /es/precios/). /es/pricing/ gibi tahminler için 301 eklendi.
- O2 Gizlilik/Şartlar/Hesap silme İngilizcede /en/privacy/, /en/terms/, /en/delete-account/ (eski adreslerden 301).
- O3 Hakkımızda: `build.py` → `FOUNDER_NOTE`, `TEAM` doldurulunca 6 dilde kurucu notu ve ekip bölümü çıkar.
- O4 İçerik görsellerinin hepsinde alt metin (GEN_ALT). Yalnız dekoratif sayfa sonu görseli boş alt ile bırakıldı.
- O5 Kayıt formunda örnek otel adı "Seaside Boutique Hotel".
- O7 Karşılaştırma tablosunda her satıra kaynak linki ve "Eylül 2026'da kontrol edildi".
Güçlendirme
- Güvenlik ve veri sayfası (6 dil, footer → Şirket), ROI hesaplayıcı (6 dil, footer → Kaynaklar).
- Kanal listesi sayfası YAPILMADI: katalog sunucuda dinamik (`channex_adapters`), statik liste yok; Channex de statik liste yayınlanmasını istemiyor (Evan, 16 Eylül).
