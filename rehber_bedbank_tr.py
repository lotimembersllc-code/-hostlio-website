"""Takvim yazısı: "Bedbank nedir? Oteller için rehber (2026)" — yalnız TR. GSC: "bedbank nedir" 24–27. sıra.
Kaynaklar 16 Ekim 2026: HBX Group FY2025 sonuçları, WebBeds FY26, Emerging Travel Group, W2M, Hotelbeds fiyat bütünlüğü (2019),
Channex Hotelbeds eşleme kılavuzu. Ödeme vadesi ve komisyon oranı doğrulanamadı → yazılmaz. Hostlio: Hotelbeds'e Channex üzerinden."""
import html

SRC = [
 ("HBX Group: 2025 mali yıl sonuçları", "https://s205.q4cdn.com/629386486/files/doc_financials/2025/q4/2025-FY-Results-Press-Release.pdf"),
 ("HBX Group", "https://www.hbxgroup.com/"),
 ("WebBeds: FY26 sonuçları", "https://www.webbeds.com/news/fy26-results/"),
 ("WebBeds: ne yapıyoruz", "https://www.webbeds.com/about/what-we-do/"),
 ("Emerging Travel Group (RateHawk)", "https://www.emergingtravel.com/"),
 ("RateHawk: 100.000'i aşan doğrudan sözleşme (Mayıs 2024)", "https://blog.ratehawk.com/over-100000-direct-contracts-on-ratehawk/"),
 ("W2M: bedbank", "https://www.w2m.travel/en-en/our-brands/w2mbb"),
 ("Hotelbeds: fiyat bütünlüğü (4 Kasım 2019)", "https://hbxgroup.com/news-room/press-release/hotelbeds-tackles-rate-integrity-challenge-behalf-hotel-partners"),
 ("Hotelbeds: fiyat ihlalleri %90 azaldı (18 Aralık 2019)", "https://discover.hotelbeds.com/resources/check/rate-violation-incidents-down-just-001-room-nights-hotelbeds"),
 ("Channex: Hotelbeds eşleme kılavuzu", "https://docs.channex.io/channel-mapping-guides/hotelbeds"),
]

def _tbl(head, rows):
    h = "".join(f'<th scope="col">{x}</th>' for x in head)
    b = "".join("<tr>" + f'<th scope="row">{r[0]}</th>' + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table class="cmp"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

META = {"tr": dict(key="post-bedbank", date="2026-10-16", title="Bedbank nedir? Oteller için rehber (2026)",
                   desc="Bedbank nedir, OTA ve tur operatöründen farkı ne? Hotelbeds, WebBeds, RateHawk ve W2M; net fiyat, kontrat türleri, fiyat bütünlüğü ve kanal yöneticisi.")}

def tr(U):
    from build import btn, SIGNUP_URL
    cta = btn("7 gün ücretsiz dene", SIGNUP_URL) + btn("Kanal yöneticisi", U("channel"), "ghost")
    fark = _tbl(["", "Bedbank", "OTA", "Tur operatörü"], [
        ("Kime satar", "Acentelere, tur operatörlerine, OTA'lara (B2B)", "Doğrudan misafire (B2C)", "Misafire, paket olarak"),
        ("Fiyat", "Otelden net fiyat alır, üstüne kendi kârını koyar", "Genelde otelin fiyatından komisyon alır", "Odayı uçak ve transferle birlikte paketler"),
        ("Misafir görür mü", "Hayır, misafir bedbank'ı görmez", "Evet", "Evet"),
        ("Örnek", "Hotelbeds, WebBeds, RateHawk, W2M", "Booking.com, Expedia", "Bedbank'ların müşterisi olabilir")])
    oyuncu = _tbl(["Bedbank", "Kendi açıkladığı büyüklük", "Not"], [
        ("Hotelbeds (HBX Group)", "2025 mali yılında 8,2 milyar € işlem hacmi; 170'ten fazla ülke, yaklaşık 60.000 seyahat dağıtıcısı", "Şubat 2025'te İspanya borsasında işlem görmeye başladı"),
        ("WebBeds (Web Travel Group)", "2026 mali yılında 5,8 milyar AUD işlem hacmi; 50.000'den fazla seyahat alıcısı", "Avustralya borsasında"),
        ("RateHawk (Emerging Travel Group)", "110.000'den fazla seyahat acentesi; 250.000'den fazla doğrudan tesis", "2024'te doğrudan sözleşmede Türkiye ilk sırada"),
        ("W2M (World2Meet)", "Dünyada 500.000'den fazla otel", "İspanyol grubu")])
    c = f'''<div class="answer"><p><strong>Kısa cevap:</strong> Bedbank, otel odalarını otelden net fiyatla alıp seyahat acentelerine, tur operatörlerine ve OTA'lara toptan satan B2B aracıdır. Misafir bedbank'ı hiç görmez; odayı bir acentenin ya da bir paketin içinde satın alır. En büyükleri Hotelbeds, WebBeds, RateHawk ve W2M. Küçük bir otel için bedbank, tek başına ulaşamayacağı uzak pazarlardan ek rezervasyon demektir; karşılığında net fiyat, daha geç ödeme ve fiyatların yanlış kanala sızması riski vardır.</p></div>
<p class="small muted">Firma büyüklükleri firmaların kendi açıklamalarıdır; bilgiler 16 Ekim 2026'da resmî ve kurumsal kaynaklardan derlendi. Komisyon ve ödeme vadeleri sözleşmeye göre değişir; kendi sözleşmenize bakın.</p>
<h2>Bedbank, OTA ve tur operatörü farkı</h2>
{fark}
<p>Hotelbeds'in ana şirketi HBX Group kendini "bağımsız, küresel bir B2B seyahat teknolojisi pazaryeri" olarak tanımlıyor; WebBeds de kendini oteller ile seyahat alıcıları arasında bağlantı kuran bir B2B pazaryeri olarak anlatıyor.</p>
<h2>Büyük bedbank'lar</h2>
{oyuncu}
<p>Türkiye bedbank'lar için önemli bir pazar: RateHawk'ın Mayıs 2024 açıklamasına göre doğrudan sözleşme sayısında Türkiye ilk sırada.</p>
<h2>Oteller bedbank'larla nasıl çalışır?</h2>
<ul><li><strong>Sözleşme:</strong> Otel bedbank'la bir kontrat imzalar ve net fiyat verir. Hotelbeds'te kontratlar MaxiRoom ekstranetinden yönetilir.</li>
<li><strong>Sabit kontrat:</strong> Fiyat ve kontenjan sözleşmede sabitlenir. Bu durumda kanal yöneticisinden fiyat gönderilmez; minimum kontenjanlı kontratlarda bazı tarihleri kapatamayabilirsiniz.</li>
<li><strong>Dinamik kontrat:</strong> Fiyat, müsaitlik ve kısıtlamalar kanal yöneticisinden gönderilir; böylece bedbank satışı da tek takvimden yönetilir ve overbooking riski azalır.</li>
<li><strong>Ödeme:</strong> Ödemeyi misafir değil bedbank yapar, genelde konaklamadan sonra. Vade sözleşmeye bağlıdır.</li></ul>
<h2>Fiyat bütünlüğü: net fiyat neden sızar?</h2>
<p>Bedbank'a verilen net fiyatlar bazen kamuya açık sitelerde, sizin kendi fiyatınızın altında görünebilir. Hotelbeds 2019'da bu soruna karşı, acentelere yönelik fiyatları OTA'larda satan iş ortaklarını üç uyarıdan sonra bağlantısını kesen bir politika açıkladı ve ihlallerin %90 azaldığını duyurdu. Bu açıklamalar 2019 tarihli; sözleşme yaparken fiyatlarınızın hangi kanallarda satılabileceğini yazılı olarak sorun.</p>
<h2>Küçük bir otel için artıları ve eksileri</h2>
<ul><li><strong>Artı:</strong> Tek başına ulaşamayacağınız binlerce acente ve uzak pazar.</li>
<li><strong>Artı:</strong> Kanal yöneticisiyle bağlıysa tek müsaitlik havuzu, az iş yükü.</li>
<li><strong>Eksi:</strong> Net fiyat kamuya açık fiyattan düşüktür, kâr marjı daralır.</li>
<li><strong>Eksi:</strong> Ödeme rezervasyonda değil sonradan gelir.</li>
<li><strong>Eksi:</strong> Sabit ve kontenjanlı kontratlar esnekliği azaltır; birden fazla bedbank idari yük getirir.</li></ul>
<p>Komisyon ve net gelir hesabı için <a href="{U("commission")}">OTA komisyon hesaplayıcısını</a>, Booking.com tarafı için <a href="{U("post-bookingkom")}">Booking.com komisyonu</a> yazısını okuyabilirsiniz.</p>
<h2>Hostlio Pro ile bedbank bağlantısı</h2>
<p>Hostlio Pro'nun <a href="{U("channel")}">kanal yöneticisi</a> Channex altyapısıyla 100'den fazla kanala bağlanır; Hotelbeds bunlardan biridir. Hotelbeds'in verdiği XML bilgileriyle kontratınızı seçer, odalarınızı eşlersiniz; dinamik kontratlarda fiyat, müsaitlik ve kısıtlamaları ayrı ayrı açıp kapatabilirsiniz. Sabit fiyatlı kontratlarda fiyat gönderilmez. Diğer bedbank'larla bağlantıyı kurmadan önce bize sorun.</p>
<div class="cta-row" style="margin-top:12px">{cta}</div>
'''
    lis = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(n)}</a></li>' for n, u in SRC)
    c += f'<h2>Kaynaklar</h2><p class="small muted">Tüm kaynaklara 16 Ekim 2026 tarihinde erişildi.</p><ul>{lis}</ul>'
    faq = [("Bedbank nedir?", "Otel odalarını otelden net fiyatla alıp seyahat acentelerine, tur operatörlerine ve OTA'lara satan B2B aracıdır. Misafir bedbank'ı görmez."),
           ("Bedbank ile OTA arasındaki fark nedir?", "OTA (Booking.com, Expedia) odayı doğrudan misafire satar ve genelde komisyon alır; bedbank ise acentelere toptan satar ve otelden net fiyat alır."),
           ("En büyük bedbank'lar hangileri?", "Hotelbeds (HBX Group), WebBeds, RateHawk (Emerging Travel Group) ve W2M en büyükleri arasında."),
           ("Hostlio Pro Hotelbeds'e bağlanır mı?", "Evet. Hostlio Pro'nun kanal yöneticisi Channex altyapısıyla Hotelbeds dahil 100'den fazla kanala bağlanır.")]
    return c, faq

FN = {"tr": tr}
