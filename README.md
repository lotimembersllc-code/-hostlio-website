# Hostlio Pro — web sitesi v5 (TR + EN, statik)

## v5 değişiklikleri
- Marka adı her yerde "Hostlio Pro" (logo: Hostlio + turuncu Pro). Schema'da alternateName "Hostlio".
- Gizlilik Politikası ve Kullanım Şartları mevcut siteden (20 Nisan 2026 metni) alındı: EN `/privacy/`, `/terms/` (eski URL'ler korunur), TR çevirileri `/gizlilik-politikasi/`, `/kullanim-sartlari/` (İngilizce metin esastır notuyla). Footer'da linkler + `/delete-account`.
- Mevcut sitedeki `signup.html`, `delete-account.html`, `attribution.js` (UTM ilk temas takibi, tüm sayfalarda yüklenir) ve Google Search Console doğrulama dosyası korunur.
- Kayıt butonları `/signup`, giriş `https://dashboard.hostliopro.com`.
- Eski blogdaki 4 İngilizce yazı yeni tasarıma taşındı (`/en/blog/...`); eski URL'ler ve /about, /contact, /faq, /channels için 301 yönlendirmeleri `src/vercel.json`'da. Eski overbooking yazısı yeni overbooking rehberine yönlenir.
- Mobilde ana görsel kolajı (avlu fotoğrafı, otel sahibi, Lio mesaj balonu, bildirim çipleri) masaüstündeki düzenle aynı gösterilir.
- "Kredi kartı gerekmez" ve yıllık planlarda %20 indirim bilgisi (Kullanım Şartları'na göre) SSS ve CTA'lara eklendi.
- Not: Gizlilik Politikası "takip çerezi kullanmıyoruz" diyor. GA4 eklenirse politikanın güncellenmesi gerekir; çerezsiz Plausible bu metinle uyumludur.

## v4: SEO/GEO değişiklikleri (claude-seo skill'i ile denetlendi)
- Türkçe arama dili: "otel programı", "pansiyon programı" vb. başlık, açıklama, H1 ve SSS'lerde.
- 7 yeni sayfa x 2 dil: pansiyon / butik otel / apart otel / hostel programı, otel programı karşılaştırması (kaynaklı, tarihli), 2 rehber (overbooking, Booking.com otomatik cevap). Toplam 38 sayfa.
- Her sayfada görünür "Son güncelleme" tarihi; blog yazılarında yazar satırı ve dateModified.
- `llms-full.txt` (tüm sitenin düz metni), responsive görseller (480w srcset), ana görsel preload + fetchpriority.
- Güvenlik başlıkları (HSTS, X-Frame-Options, Permissions-Policy) `src/vercel.json`'da.
- Ölçüm ve varlık ayarları `build.py` başında: GA4_ID, PLAUSIBLE_DOMAIN, GSC_VERIFY, BING_VERIFY, SAME_AS, APP_STORE_URL. Boş bırakılanlar sayfaya yazılmaz.
- IndexNow anahtar dosyası otomatik üretilir (`/<INDEXNOW_KEY>.txt`).

## Yayından sonra yapılacaklar (sırayla)
1. Google Search Console ve Bing Webmaster Tools'ta siteyi doğrula (token'ları build.py'ye yaz), `sitemap.xml` gönder.
2. Analytics'i aç (GA4 veya Plausible). AI trafiği için referrer'ları izle: chatgpt.com, perplexity.ai, claude.ai, gemini.google.com, copilot.microsoft.com.
3. IndexNow ile tüm URL'leri bildir (Bing, Yandex; ChatGPT aramasının Bing sonuçlarını kullandığı biliniyor).
4. SAME_AS'e resmi profilleri ekle: LinkedIn şirket sayfası, Instagram, YouTube, Hotel Tech Report, G2, Capterra. APP_STORE_URL'i doldur.
5. Blog yazılarına gerçek yazar adları ekle (ör. kurucu/ürün sorumlusu), Hakkımızda'ya ekip bölümü.
6. Site dışı: Hotel Tech Report / G2 / Capterra profilleri ve ilk müşteri yorumları, Channex partner dizini, Reddit ve otelci toplulukları, Google Business Profile, YouTube'da ürün videoları (reklam videoları hazır).
7. Karşılaştırma sayfasını 3 ayda bir güncelle (rakip fiyatları değişir; güncel içerik AI'da daha çok alıntılanır).
8. Gizlilik Politikası ve Kullanım Şartları sayfalarını ekle.

## v3 değişiklikleri
- Marka renkleri (hostlio-dashboard-main/src/index.css): turuncu #FF6B35, lacivert #1B2B4B, koyu #0F1E36; zemin reklam görsellerindeki krem #FBF6F0. Turuncu butonlarda erişilebilirlik için lacivert yazı kullanıldı (kontrast 5.9:1).
- Logo: uygulama ikonundaki işaret (lacivert kare, beyaz H, turuncu çizgi ve nokta).
- Görseller: Hostlio'nun kendi reklam videoları ve afişinden kareler (brand-*.webp) + Unsplash fotoğrafları (hostlio-*.webp).
- Yeni bölümler: hero kolajı, "Gece 02:14" hikâye kartları, 8 kartlı özellik bentosu, tesis tipi kartları, AI bölümünde fotoğraf kartı, kapak görselli blog yazıları, görselli Özellikler ve Hakkımızda sayfaları.

## Tasarım (v2)
- Referans: guesty.com'un yapısı (sıcak kırık beyaz zemin, ince ağırlıklı büyük başlıklar, italik vurgu kelimesi, hap butonlar, ilgi alanı seçici, sekmeli ürün turu, fotoğraf kartları üzerinde yüzen arayüz çipleri, "tek çatı altında" akordeon, koyu AI bölümü, iki kolonlu SSS). Guesty'nin logosu, rengi ve metni kullanılmadı.
- Kullanılan skill'ler: Anthropic `frontend-design`, `ui-ux-pro-max`, `taste-skill` (soft-skill: double-bezel kartlar, buton içinde ikon, özel easing), Vercel web interface guidelines.
- Font: Instrument Sans (self-host, normal + italik). İkonlar: Phosphor Light. OTA logoları: Simple Icons.
- Fotoğraflar (Unsplash lisansı, ücretsiz): lobi Josh Hild, oda Andrew Neel, işletmeci ve oda masası Vitaly Gariev. `src/assets/img/`

Framework yok. `python3 build.py` → `dist/` klasörü (24 sayfa + sitemap, robots, llms.txt, 404).

## Yayına alma (Vercel)
1. Bu klasörü bir GitHub reposuna koy.
2. Vercel → New Project → Framework: **Other**, Build command: `python3 build.py`, Output: `dist`.
   (Ya da doğrudan `dist/` klasörünü sürükle-bırak ile yükle.)
3. Domain: `www.hostliopro.com`. Eski URL'ler için `src/vercel.json` içine `redirects` ekle.
4. Google Search Console + Bing Webmaster Tools'a `https://www.hostliopro.com/sitemap.xml` gönder.

## Düzenleme
| Ne | Nerede |
|---|---|
| Kayıt/giriş linki, form endpoint, e-posta | `build.py` üstündeki sabitler (`APP_URL`, `FORM_ENDPOINT`, `EMAIL`) |
| Fiyatlar | `build.py` → `PLANS` + `content_*.py` → `PLAN_TXT`, FAQ metinleri, `llms.txt` bloğu |
| Türkçe metinler | `content_tr.py` |
| İngilizce metinler | `content_en.py` |
| Tasarım (renk/tipografi) | `src/assets/style.css` (üstteki `:root` token'ları) |
| Yeni blog yazısı | `ROUTES`'a anahtar ekle, `content_*.py` içinde `POSTS` + `post_xxx()` fonksiyonu, `pages()` listesine ekle |

Formu gerçek bir servise bağlamak için `FORM_ENDPOINT`'e Formspree/Basin/kendi Supabase edge function URL'ini yaz; boşsa mailto ile çalışır.

## SEO katmanı
- Her sayfada benzersiz title/description, canonical, `hreflang` (tr, en, x-default), Open Graph + Twitter kartı (`og-tr.png`, `og-en.png`)
- JSON-LD `@graph`: Organization, WebSite, WebPage (About/Contact/FAQ/Collection tipleri), BreadcrumbList, SoftwareApplication (+ fiyat teklifleri), FAQPage, BlogPosting
- `sitemap.xml` hreflang alternatifleriyle; semantik HTML, tek H1, sıralı başlıklar
- Self-host variable font (preload), framework JS yok, görseller HTML/CSS ile → hızlı LCP, CLS≈0
- axe-core WCAG 2 AA taraması: 0 ihlal

## GEO (AI arama motorları: ChatGPT, Perplexity, Claude, Google AI Overviews)
- `robots.txt` GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended vb. için açık
- `/llms.txt`: ürünün tek dosyalık, gerçeklere dayalı özeti + tüm sayfa linkleri
- Her ana sayfada "Kısaca…" / "…nedir?" cevap bloğu (AI'ın alıntılayacağı net tanım cümlesi)
- Karşılaştırma tabloları (plan/özellik, kanal listesi), SSS'ler hem görünür hem schema'da
- Tarihli içerik (`dateModified`, "Son güncelleme"), rakamlar tutarlı (30+ dil, 100+ OTA, 20+ ülke, 7 gün deneme)

## Yayından önce doğrulanması gerekenler
Eski sitede olmayan, benim varsaydığım bilgiler — yanlışsa `content_*.py` içinde düzelt:
- Kayıt/giriş adresi `app.hostliopro.com/signup` ve `/login`
- Online check-in'in Pro ve Growth planlarında olması
- "Komisyon yok, kurulum ücreti yok" ifadesi
- Lio'nun **onay modu** (cevapları göndermeden önce onaylama) ve devir kuralları
- Kota dolunca otomatik yanıtın durması; plan değişikliğinin sonraki dönemde yansıması
- Fiyatlara KDV/vergi dahil olmaması; Türkçe destek
- Gizlilik Politikası ve Kullanım Şartları sayfaları eklenmedi (hukuki metin gerektirir) — eski sayfaların URL'lerini footer'a ekle
- Müşteri yorumu/logo yok: gerçek, izinli yorumlar gelince eklenmeli (sosyal kanıt dönüşüm için önemli)

## v6 — 6 dil (TR, EN, ES, IT, PT, FR)
- Yeni diller: `content_es/it/pt/fr.py` (sayfalar) + `lang_es/it/pt/fr.py` (arayüz, ana sayfa, tesis tipi sayfaları, karşılaştırma, rehberler, yasal metin çevirileri).
- URL'ler: /es/, /it/, /pt/, /fr/ altında yerelleştirilmiş slug'lar (build.py → ROUTES).
- Her sayfada 6 dilli hreflang + x-default (en), og:locale + alternate, dile özel OG görseli (og/make.py), sitemap alternates, llms.txt'de dil bölümleri.
- Başlıkta dil seçici menüsü. Eski İngilizce blog yazıları yalnızca EN.
- Yasal metin çevirilerinde "İngilizce metin esastır" notu var.
- Kontrol: 130 sayfa, kırık link yok, JSON-LD geçerli, axe temiz, 360/390/768 px'te yatay kaydırma yok.

## v7 — mevcut siteden entegrasyonlar (~/Developer/-hostlio-website-main)
- Plan bilgileri depodaki güncel haliyle hizalandı: Starter 3.000 / Pro 20.000 / Growth 50.000 AI mesajı; Growth çoklu tesis, 150 odaya kadar (6 dil, llms.txt dahil).
- Fiyatlar: Aylık/Yıllık geçişi (%20) + Supabase `plans` fonksiyonundan canlı fiyat (mevcut sitedeki anon anahtarla; yanıt gelmezse sayfadaki fiyatlar kalır). Early Bird kapanırsa "early-bird" satırı otomatik gizlenir.
- İletişim formu: Make.com webhook'una eski formla aynı JSON (type, name, email, subject, message, date) + hotel, rooms, country, lang, page, acquisition (attribution.js ilk temas kaydı). Hata olursa kullanıcıya e-posta/WhatsApp önerilir.
- WhatsApp +1 341 341 4479: iletişim sayfası, footer ve Organization şeması (telephone).
- Kanonik alan adı: https://hostliopro.com (mevcut sitedeki gibi, www değil).
- signup.html, attribution.js, delete-account.html, Google doğrulama dosyası: mevcut siteyle birebir aynı (kontrol edildi).
- Vercel: kök vercel.json (buildCommand `python3 build.py`, outputDirectory `dist`) build sırasında src/vercel.json'dan üretilir. Pillow yoksa görsel varyantları üretilmez, depodaki hazır dosyalar kullanılır.
- CI: .github/workflows/kapilar.yml → build + scripts/check.py (kırık link, JSON-LD, hreflang karşılıklılığı, tekrar eden title).

## v8 — güncel depo (21 Eylül) ile hizalama
- Kotalar tekrar 1.000 / 5.000 / 12.000 AI mesajı; Growth 2 tesise kadar, 150 oda (patron kararı, commit d35b596).
- E-posta / web chat / Telegram misafir mesajlaşması vaatleri 6 dilde kaldırıldı. Lio: WhatsApp (tüm planlar) + OTA gelen kutuları Booking.com, Airbnb, Expedia (Pro ve Growth). (commit 1f05feb)
- "Kredi kartı gerekmez" ifadesi kaldırıldı: kart kayıtta alınır, deneme bitene kadar ücret çekilmez (CTA, SSS, kullanım şartları; commit 75db455).
- src/signup.html depodaki son sürümle değiştirildi.

## v9 — yıllık fiyatlar
- Her plan kartında yıllık fiyat satırı (Starter $39/ay – $470/yıl, Pro $71/ay – $854/yıl, Growth $119/ay – $1.430/yıl), fiyat sayfasında 6 dilde aylık/yıllık fiyat tablosu, yapılandırılmış veride yıllık teklifler, llms.txt. Canlı fiyat gelirse satırlar da güncellenir.

## v10 — yeni görseller (Higgsfield, GPT Image 2.5, 2K)
- 12 yeni görsel `src/assets/img/gen-*.webp` (1080×1350, 480w varyantlarıyla):
  hostel, apart, pansiyon, butik oda → tesis tipi sayfaları + ana sayfa kartları;
  blog kapakları: owner-laptop (PMS), reception (overbooking), night-desk (otomatik cevap), checkin-phone (AI),
  eski EN yazılar: arrival, room-dusk, facade, terrace-phone.
- 6 dilde alt metinler: build.py → GEN_ALT.
- Kullanılmayan hostlio-lobby/phone/room görselleri unused_img/ klasörüne taşındı.
- Görseller yapay zekâ ile üretildi: gerçek müşteri, gerçek otel ya da referans olarak sunulmamalı.

## v11 — ek görseller ve döngü video
- Özellikler sayfası: gen-team-desk (resepsiyonda tablete bakan ekip). Hakkımızda: gen-shutters (gün doğarken panjur açan işletmeci). Alt metinler 6 dilde (GEN_ALT).
- Sayfa sonu CTA'sı (neredeyse her sayfada): gece resepsiyon sahnesinin 10 sn'lik ileri-geri döngü videosu (Grok Video 1.5, sessiz). src/assets/video/night-desk.webm (≈195 KB) + .mp4 (≈395 KB).
  Görünür olunca yüklenir; "hareketi azalt" ve veri tasarrufu modunda yüklenmez, poster görseli gösterilir. Masaüstünde sağda, metnin arkasında değil.

## v12 — "Yanınızda bir ekip var" bölümü
- Stok fotoğraf yerine gen-support-call (görüntülü kurulum görüşmesindeki otelci) + üstünde kodla çizilmiş destek sohbeti kartı ve "Kanal bağlandı" etiketi (6 dil, home_v3.SUPCARD).
- Gerçek ekip fotoğrafı gelirse sadece sup_img değiştirilir. hostlio-owner unused_img/ klasörüne taşındı.

## v13 — ödeme (kayıt) ve hesap silme sayfaları yeni tasarıma alındı
- `/signup` artık üretiliyor: `signup_page.py` + `src_legacy/signup_script.js` (eski betik, mantık birebir) + `src/assets/checkout.js` (dil, plan özeti, aylık/yıllık).
  - 6 dil: ?lang= → localStorage → yönlendiren sayfanın dili → tarayıcı dili. Site içindeki "Ücretsiz dene" bağlantılarına dil parametresi site.js ekliyor.
  - ?plan= ve ?billing= ön seçimi; sol tarafta seçili planın özeti ve "kart kayıtta alınır, deneme bitene kadar çekim yok" notu.
  - Ödeme mantığı (signup-checkout edge function, ülke/para birimi/saat dilimi tablosu, oda limiti, attribution) DEĞİŞMEDİ. noindex.
- `/delete-account` (ve 6 dildeki karşılıkları) artık normal site şablonunda; eski `delete-account.html` kaldırıldı, /delete-account.html → /delete-account/ 301.
- Eski dosyalar `src_legacy/` klasöründe duruyor (yayına kopyalanmaz).
- Uzun dillerde başlık menüsü taşması düzeltildi.
