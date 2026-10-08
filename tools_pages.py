"""Ücretsiz otel araçları (SEO S9 / B4): RevPAR–ADR–doluluk hesaplayıcı, OTA komisyonu → net gelir
hesaplayıcı ve Araçlar dizini. 6 dil. Hesap /assets/kpi.js'te (satır içi betik yok, CSP); formüller
scripts/kpi.test.js ile test edilir. Sayfadaki örnek rakamlar testtekiyle AYNI olmalı.
Hostlio iddiaları yalnız canlı özellikler: panelde Analiz (doluluk, ADR, RevPAR, kanal bazında brüt/komisyon/net)."""
import html

CUR = {"tr": "TRY", "en": "USD", "es": "EUR", "it": "EUR", "pt": "BRL", "fr": "EUR"}
CURS = ["USD", "EUR", "GBP", "TRY", "BRL"]

T = {
"tr": dict(
  hub_crumb="Araçlar", hub_title="Ücretsiz Otel Hesaplayıcıları: RevPAR, Komisyon | Hostlio Pro",
  hub_desc="Otelciler için ücretsiz hesaplayıcılar: RevPAR, ADR ve doluluk oranı, OTA komisyonu sonrası net gelir ve AI mesajlaşma tasarrufu. Kayıt gerekmez.",
  hub_h1='Otelciler için <em class="hl">ücretsiz</em> hesaplayıcılar',
  hub_lead="Kayıt olmadan, tarayıcınızda çalışan basit araçlar. Girdiğiniz rakamlar hiçbir yere gönderilmez.",
  hub_note="Hesaplamalar yalnızca tarayıcınızda yapılır; girdiğiniz rakamlar kaydedilmez ve sunucuya gönderilmez.",
  cards=[("kpi", "RevPAR, ADR ve doluluk oranı hesaplama", "Oda sayısı, satılan oda gecesi ve oda gelirinden üç temel göstergeyi formülleriyle birlikte hesaplayın."),
         ("commission", "OTA komisyonu → net gelir", "Booking.com, Expedia gibi kanallardan gelen rezervasyonda komisyon ve ek kesintilerden sonra elinize ne kalıyor?"),
         ("roi", "AI mesajlaşma tasarruf hesaplayıcı", "Misafir mesajlarını cevaplamanın kaç saat ve ne kadar personel maliyeti tuttuğunu tahmin edin.")],
  currency="Para birimi",
  kpi_crumb="RevPAR, ADR ve doluluk hesaplama",
  kpi_title="RevPAR, ADR ve Doluluk Oranı Hesaplama (Ücretsiz) | Hostlio Pro",
  kpi_desc="RevPAR, ADR ve doluluk oranını saniyeler içinde hesaplayın. Formüller, adım adım örnek ve sık yapılan hatalar. Ücretsiz otel hesaplayıcısı, kayıt gerekmez.",
  kpi_h1='RevPAR, ADR ve <em class="hl">doluluk oranı</em> hesaplama',
  kpi_lead="Dönemdeki oda sayınızı, satılan oda gecelerini ve oda gelirinizi girin; doluluk oranı, ortalama oda fiyatı (ADR) ve müsait oda başına gelir (RevPAR) anında hesaplansın.",
  f_rooms="Satılabilir oda sayısı", f_days="Dönemdeki gün sayısı", f_sold="Satılan oda gecesi", f_revenue="Dönemin oda geliri",
  h_sold="Her dolu oda, her gece için 1 sayılır. 3 gece kalan bir misafir = 3 oda gecesi.",
  h_revenue="Yalnızca oda geliri; kahvaltı dışı ekstralar, transfer ve vergiler hariç (raporlamanızda nasıl tutuyorsanız tutarlı olun).",
  r_avail="Satılabilir oda gecesi", r_occ="Doluluk oranı", r_adr="ADR (ortalama oda fiyatı)", r_revpar="RevPAR (müsait oda başına gelir)",
  warn="Satılan oda gecesi, satılabilir oda gecesinden fazla olamaz. Oda veya gün sayısını kontrol edin.",
  privacy="Hesap tarayıcınızda yapılır; rakamlarınız hiçbir yere gönderilmez.",
  f_h="Formüller",
  f_items=[("Doluluk oranı", "Satılan oda gecesi ÷ satılabilir oda gecesi × 100", "Odalarınızın yüzde kaçının dolu olduğunu gösterir. Satılabilir oda gecesi = oda sayısı × gün sayısı."),
           ("ADR (Average Daily Rate)", "Oda geliri ÷ satılan oda gecesi", "Satılan bir oda gecesinin ortalama fiyatı. Boş odaları hesaba katmaz."),
           ("RevPAR (Revenue per Available Room)", "Oda geliri ÷ satılabilir oda gecesi = ADR × doluluk oranı", "Fiyat ve doluluğu tek rakamda birleştirir; boş kalan odaların maliyetini de gösterir.")],
  ex_h="Adım adım örnek",
  ex_p="12 odalı bir butik otel, 31 günlük bir ayda 285 oda gecesi satmış ve 39.900 ₺ oda geliri elde etmiş olsun:",
  ex_list=["Satılabilir oda gecesi: 12 × 31 = 372", "Doluluk oranı: 285 ÷ 372 = %76,6", "ADR: 39.900 ₺ ÷ 285 = 140 ₺", "RevPAR: 39.900 ₺ ÷ 372 = 107,26 ₺ (ya da 140 ₺ × %76,6)"],
  ex_after="Hesaplayıcıdaki varsayılan rakamlar bu örnektir; kendi rakamlarınızla değiştirin.",
  why_h="Hangi gösterge neyi anlatır?",
  why=[("Doluluk yüksek, RevPAR düşükse", "Odalarınızı fazla ucuza satıyor olabilirsiniz. Yoğun günlerde fiyatı biraz artırmak doluluğu çok düşürmeden RevPAR'ı yükseltebilir."),
       ("ADR yüksek, doluluk düşükse", "Fiyat talebin üzerinde olabilir ya da kanal dağıtımınız zayıf olabilir. Daha fazla kanalda görünmek ve minimum konaklama kurallarını gözden geçirmek işe yarayabilir."),
       ("RevPAR'ı karşılaştırırken", "Aynı dönemi geçen yılla, ya da benzer büyüklükteki rakip tesislerle karşılaştırın. Farklı oda sayısındaki oteller için RevPAR, toplam gelirden daha adil bir ölçüdür.")],
  mist_h="Sık yapılan hatalar",
  mist=["Kahvaltı, transfer ve tur gelirini oda gelirine katmak (ADR ve RevPAR şişer).",
        "Satılabilir oda sayısından arızalı odaları bir ay düşüp bir ay düşmemek. Hangi yöntemi seçerseniz her dönem aynısını kullanın.",
        "Ücretsiz (kompliman) odaları satılan oda gecesine katıp gelir yazmamak; ADR'yi düşük gösterir.",
        "Komisyonlu kanal gelirini brüt mü net mi yazdığınızı karıştırmak. Kanal karlılığı için <a href=\"{commission}\">OTA komisyon hesaplayıcısını</a> kullanın."],
  hl_h="Hostlio Pro'da bu rakamlar kendiliğinden gelir",
  hl_p="Hostlio Pro panelindeki Analiz ekranı doluluk, ADR ve RevPAR'ı rezervasyonlarınızdan otomatik hesaplar; önceki dönemle ve geçen yılla karşılaştırır, kanal bazında brüt gelir, komisyon ve net geliri gösterir. Raporları Excel'e aktarabilirsiniz. <a href=\"{features}\">Tüm özellikleri görün</a> ya da <a href=\"{pricing}\">planları karşılaştırın</a> (aylık ⟦price:starter⟧'dan başlar).",
  faq=[("RevPAR nasıl hesaplanır?", "RevPAR, dönemin oda gelirinin satılabilir oda gecesi sayısına bölünmesiyle bulunur. Aynı sonucu ADR'yi doluluk oranıyla çarparak da alırsınız: 140 ₺ ADR ve %76,6 doluluk yaklaşık 107 ₺ RevPAR eder."),
       ("ADR ile RevPAR arasındaki fark nedir?", "ADR yalnızca satılan odaların ortalama fiyatıdır; RevPAR ise boş odaları da hesaba katar. Bu yüzden RevPAR hem fiyat hem doluluk performansını tek rakamda gösterir."),
       ("Doluluk oranı nasıl hesaplanır?", "Satılan oda gecesini, satılabilir oda gecesine (oda sayısı × gün) bölüp 100 ile çarparsınız. 20 odalı bir otel 30 günde 450 oda gecesi sattıysa doluluk 450 ÷ 600 = %75'tir."),
       ("Oda gelirine kahvaltı dahil mi?", "Konaklamaya dahil (paket) kahvaltıyı ayırmak çoğu zaman pratik değildir; önemli olan her dönem aynı yöntemi kullanmaktır. Ayrıca satılan ekstralar (transfer, tur, ayrı ücretli kahvaltı) oda gelirine katılmaz."),
       ("Girdiğim rakamlar kaydediliyor mu?", "Hayır. Hesaplama tamamen tarayıcınızda yapılır; rakamlar sunucuya gönderilmez.")],
  com_crumb="OTA komisyon hesaplama",
  com_title="OTA Komisyon Hesaplama: Net Gelir Hesaplayıcı | Hostlio Pro",
  com_desc="Booking.com, Expedia gibi OTA rezervasyonlarında komisyon ve ödeme kesintisinden sonra elinize kalan net geliri ve gece başı net fiyatı ücretsiz hesaplayın.",
  com_h1='OTA komisyonu sonrası <em class="hl">net gelir</em> hesaplama',
  com_lead="Rezervasyon tutarını, sözleşmenizdeki komisyon oranını ve varsa ödeme/ek kesinti oranını girin. Komisyon tutarı, elinize kalan net gelir ve gece başı net fiyat anında hesaplanır.",
  f_gross="Rezervasyon tutarı (brüt)", f_rate="Komisyon oranı", f_fee="Ödeme ve diğer kesintiler", f_nights="Gece sayısı (isteğe bağlı)",
  h_rate="Oranı kanal sözleşmenizden ya da extranet'teki faturadan kontrol edin. Varsayılan rakamlar yalnızca örnektir.",
  r_commission="Komisyon tutarı", r_fees="Diğer kesintiler", r_net="Net gelir", r_kept="Elinize kalan oran", r_night="Gece başı net",
  c_how_h="Nasıl hesaplanır?",
  c_how=["Komisyon = brüt tutar × komisyon oranı", "Diğer kesintiler = brüt tutar × kesinti oranı (ör. sanal kart veya ödeme işlem ücreti)", "Net gelir = brüt tutar − komisyon − diğer kesintiler", "Gece başı net = net gelir ÷ gece sayısı"],
  c_ex_h="Örnek",
  c_ex_p="3 gecelik, 1.200 ₺'lik bir rezervasyonda komisyon %18, ödeme kesintisi %1,5 olsun: komisyon 216 ₺, diğer kesinti 18 ₺, net gelir 966 ₺, gece başı net 322 ₺. Yani misafirin ödediği 400 ₺'lik gecenin 322 ₺'si size kalır.",
  c_note="Bazı kanallar komisyonu vergiler dahil tutar üzerinden, bazıları vergiler hariç tutar üzerinden hesaplar. Brüt tutarı sözleşmenizdeki esasa göre girin. Bu sayfa vergi danışmanlığı değildir.",
  c_direct_h="Doğrudan rezervasyonla karşılaştırın",
  c_direct_p="Aynı oda doğrudan (telefon, WhatsApp, web siteniz) satıldığında komisyon ödenmez. Örnekteki gibi elinize kalan oran %80,5 ise, doğrudan rezervasyonda %19,5'e kadar indirim verseniz bile net geliriniz OTA satışından düşük olmaz. Doğrudan satışın kendi maliyetlerini (ödeme altyapısı, reklam) da hesaba katın.",
  c_hl_p="Hostlio Pro'nun Analiz ekranı her kanalın brüt gelirini, komisyonunu ve net gelirini yan yana gösterir; hangi kanalın komisyondan sonra gerçekten kazandırdığını görürsünüz. <a href=\"{channel}\">Kanal yöneticisi</a> 100+ OTA'yı tek takvimde toplar; <a href=\"{ai}\">Lio</a> WhatsApp'tan gelen soruları yanıtlayarak doğrudan rezervasyon talebi almanıza yardım eder. <a href=\"{pricing}\">Planlar</a> aylık ⟦price:starter⟧'dan başlar.",
  c_faq=[("OTA komisyonu nasıl hesaplanır?", "Komisyon, rezervasyon tutarının sözleşmenizdeki oranla çarpılmasıyla bulunur: 1.200 ₺ × %18 = 216 ₺. Net gelir için bu tutarı ve varsa ödeme kesintilerini brüt tutardan çıkarın."),
         ("Komisyon vergiler dahil mi hesaplanır?", "Kanala ve ülkeye göre değişir. Sözleşmenizde ve kanalın aylık faturasında hangi tutarın esas alındığı yazar; hesaplayıcıya o tutarı girin."),
         ("Net ADR nedir?", "Komisyon ve kesintiler düşüldükten sonra satılan bir oda gecesine kalan ortalama gelirdir. Kanalları karşılaştırırken brüt ADR yerine net ADR'ye bakmak daha doğru sonuç verir."),
         ("Rakamlarım kaydediliyor mu?", "Hayır. Hesaplama tarayıcınızda yapılır ve hiçbir yere gönderilmez.")],
),
"en": dict(
  hub_crumb="Tools", hub_title="Free Hotel Calculators: RevPAR, ADR, Commission | Hostlio Pro",
  hub_desc="Free calculators for hoteliers: RevPAR, ADR and occupancy rate, net revenue after OTA commission, and AI messaging savings. No signup needed.",
  hub_h1='<em class="hl">Free</em> calculators for hoteliers',
  hub_lead="Simple tools that run in your browser, no signup needed. The numbers you enter are never sent anywhere.",
  hub_note="Calculations run only in your browser; the numbers you enter are not stored or sent to a server.",
  cards=[("kpi", "RevPAR, ADR and occupancy calculator", "Work out the three core hotel KPIs from rooms, room nights sold and room revenue, with the formulas shown."),
         ("commission", "OTA commission → net revenue", "What do you actually keep from a Booking.com or Expedia booking after commission and other fees?"),
         ("roi", "AI messaging ROI calculator", "Estimate the staff hours and cost that answering guest messages takes today.")],
  currency="Currency",
  kpi_crumb="RevPAR, ADR and occupancy calculator",
  kpi_title="RevPAR, ADR & Occupancy Rate Calculator (Free) | Hostlio Pro",
  kpi_desc="Calculate RevPAR, ADR and occupancy rate in seconds. Formulas, a worked example and common mistakes. Free hotel KPI calculator, no signup needed.",
  kpi_h1='RevPAR, ADR and <em class="hl">occupancy</em> calculator',
  kpi_lead="Enter your rooms, the room nights you sold and your room revenue for the period. Occupancy rate, average daily rate (ADR) and revenue per available room (RevPAR) update instantly.",
  f_rooms="Rooms available to sell", f_days="Days in the period", f_sold="Room nights sold", f_revenue="Room revenue for the period",
  h_sold="Each occupied room counts once per night. A guest staying 3 nights = 3 room nights.",
  h_revenue="Room revenue only; leave out extras such as transfers, tours and taxes (whatever you choose, be consistent).",
  r_avail="Available room nights", r_occ="Occupancy rate", r_adr="ADR (average daily rate)", r_revpar="RevPAR (revenue per available room)",
  warn="Room nights sold can't exceed available room nights. Check the number of rooms or days.",
  privacy="Calculated in your browser; your numbers are never sent anywhere.",
  f_h="The formulas",
  f_items=[("Occupancy rate", "Room nights sold ÷ available room nights × 100", "The share of your rooms that were occupied. Available room nights = rooms × days."),
           ("ADR (average daily rate)", "Room revenue ÷ room nights sold", "The average price of one room night sold. It ignores empty rooms."),
           ("RevPAR (revenue per available room)", "Room revenue ÷ available room nights = ADR × occupancy rate", "Combines price and occupancy in one number, so it also shows the cost of empty rooms.")],
  ex_h="A worked example",
  ex_p="A 12-room boutique hotel sold 285 room nights in a 31-day month and earned $39,900 in room revenue:",
  ex_list=["Available room nights: 12 × 31 = 372", "Occupancy rate: 285 ÷ 372 = 76.6%", "ADR: $39,900 ÷ 285 = $140", "RevPAR: $39,900 ÷ 372 = $107.26 (or $140 × 76.6%)"],
  ex_after="The calculator's default values are this example; replace them with your own numbers.",
  why_h="What each number tells you",
  why=[("High occupancy, low RevPAR", "You may be selling rooms too cheaply. Raising rates a little on busy dates can lift RevPAR without losing much occupancy."),
       ("High ADR, low occupancy", "Your rate may be above demand, or your distribution may be thin. Appearing on more channels and reviewing minimum-stay rules can help."),
       ("Comparing RevPAR", "Compare the same period last year, or properties of a similar size. For hotels with different room counts RevPAR is fairer than total revenue.")],
  mist_h="Common mistakes",
  mist=["Adding breakfast, transfer and tour income to room revenue (it inflates ADR and RevPAR).",
        "Removing out-of-order rooms from available rooms one month but not the next. Pick one method and keep it.",
        "Counting complimentary rooms as sold with no revenue, which drags ADR down.",
        "Mixing gross and net revenue for commission-based channels. For channel profitability use the <a href=\"{commission}\">OTA commission calculator</a>."],
  hl_h="In Hostlio Pro these numbers come in by themselves",
  hl_p="The Analytics screen in the Hostlio Pro dashboard calculates occupancy, ADR and RevPAR from your reservations, compares them with the previous period and last year, and shows gross revenue, commission and net revenue per channel. You can export reports to Excel. <a href=\"{features}\">See all features</a> or <a href=\"{pricing}\">compare plans</a> (from ⟦price:starter⟧ a month).",
  faq=[("How do you calculate RevPAR?", "Divide room revenue for the period by available room nights. You get the same result by multiplying ADR by the occupancy rate: a $140 ADR at 76.6% occupancy is about $107 RevPAR."),
       ("What is the difference between ADR and RevPAR?", "ADR is the average price of the rooms you sold; RevPAR also counts the rooms you didn't sell. That's why RevPAR shows price and occupancy performance in one number."),
       ("How do you calculate hotel occupancy rate?", "Divide room nights sold by available room nights (rooms × days) and multiply by 100. A 20-room hotel that sold 450 room nights in 30 days has 450 ÷ 600 = 75% occupancy."),
       ("Should breakfast be included in room revenue?", "Separating breakfast included in a package rate is often impractical; what matters is using the same method every period. Extras sold separately (transfers, tours, paid breakfast) are not room revenue."),
       ("Are the numbers I enter saved?", "No. The calculation runs entirely in your browser; nothing is sent to a server.")],
  com_crumb="OTA commission calculator",
  com_title="OTA Commission Calculator: Net Revenue per Booking | Hostlio Pro",
  com_desc="Work out what you keep from a Booking.com or Expedia booking after commission and payment fees, plus net revenue per night. Free calculator, no signup.",
  com_h1='OTA commission → <em class="hl">net revenue</em> calculator',
  com_lead="Enter the booking amount, the commission rate in your contract and any payment or other fees. Commission, the net revenue you keep and net revenue per night update instantly.",
  f_gross="Booking amount (gross)", f_rate="Commission rate", f_fee="Payment and other fees", f_nights="Nights (optional)",
  h_rate="Check the rate in your channel contract or on the invoice in the extranet. The default values are only an example.",
  r_commission="Commission", r_fees="Other fees", r_net="Net revenue", r_kept="Share you keep", r_night="Net per night",
  c_how_h="How it's calculated",
  c_how=["Commission = gross amount × commission rate", "Other fees = gross amount × fee rate (e.g. virtual card or payment processing fees)", "Net revenue = gross amount − commission − other fees", "Net per night = net revenue ÷ nights"],
  c_ex_h="Example",
  c_ex_p="A 3-night booking worth $1,200 with 18% commission and a 1.5% payment fee: commission $216, other fees $18, net revenue $966, net per night $322. Of the $400 the guest pays per night, you keep $322.",
  c_note="Some channels charge commission on the amount including taxes, others on the amount excluding taxes. Enter the gross amount on the basis your contract uses. This page is not tax advice.",
  c_direct_h="Compare with a direct booking",
  c_direct_p="When the same room is sold direct (phone, WhatsApp, your website) there is no commission. If you keep 80.5%, as in the example, you could offer up to 19.5% off on a direct booking and still not earn less than from the OTA sale. Remember direct sales have their own costs (payment processing, advertising).",
  c_hl_p="The Analytics screen in Hostlio Pro shows gross revenue, commission and net revenue side by side for every channel, so you can see which one really pays after commission. The <a href=\"{channel}\">channel manager</a> keeps 100+ OTAs on one calendar, and <a href=\"{ai}\">Lio</a> answers WhatsApp questions so you can take direct booking requests. <a href=\"{pricing}\">Plans</a> start at ⟦price:starter⟧ a month.",
  c_faq=[("How do you calculate OTA commission?", "Multiply the booking amount by the rate in your contract: $1,200 × 18% = $216. For net revenue, subtract that and any payment fees from the gross amount."),
         ("Is commission charged on the amount including taxes?", "It depends on the channel and country. Your contract and the channel's monthly invoice state which amount is used; enter that amount in the calculator."),
         ("What is net ADR?", "The average revenue left per room night sold after commission and fees. When comparing channels, net ADR gives a truer picture than gross ADR."),
         ("Are my numbers saved?", "No. The calculation runs in your browser and nothing is sent anywhere.")],
),
"es": dict(
  hub_crumb="Herramientas", hub_title="Calculadoras gratis para hoteles: RevPAR y comisión | Hostlio Pro",
  hub_desc="Calculadoras gratuitas para hoteleros: RevPAR, ADR y ocupación, ingreso neto tras la comisión de la OTA y ahorro con mensajería IA. Sin registro.",
  hub_h1='Calculadoras <em class="hl">gratuitas</em> para hoteleros',
  hub_lead="Herramientas sencillas que funcionan en tu navegador, sin registro. Los números que introduces no se envían a ningún sitio.",
  hub_note="Los cálculos se hacen solo en tu navegador; los datos no se guardan ni se envían a ningún servidor.",
  cards=[("kpi", "Calculadora de RevPAR, ADR y ocupación", "Calcula los tres indicadores clave del hotel a partir de habitaciones, noches vendidas e ingresos por habitaciones, con las fórmulas."),
         ("commission", "Comisión OTA → ingreso neto", "¿Cuánto te queda realmente de una reserva de Booking.com o Expedia después de la comisión y otros cargos?"),
         ("roi", "Calculadora de ROI de mensajería IA", "Estima las horas y el coste de personal que hoy te lleva responder a los huéspedes.")],
  currency="Moneda",
  kpi_crumb="Calculadora de RevPAR, ADR y ocupación",
  kpi_title="Calculadora de RevPAR, ADR y ocupación hotelera | Hostlio Pro",
  kpi_desc="Calcula RevPAR, ADR y porcentaje de ocupación en segundos. Fórmulas, ejemplo paso a paso y errores frecuentes. Calculadora hotelera gratuita, sin registro.",
  kpi_h1='Calculadora de RevPAR, ADR y <em class="hl">ocupación</em>',
  kpi_lead="Introduce tus habitaciones, las noches de habitación vendidas y los ingresos por habitaciones del periodo. La ocupación, la tarifa media diaria (ADR) y el ingreso por habitación disponible (RevPAR) se calculan al instante.",
  f_rooms="Habitaciones a la venta", f_days="Días del periodo", f_sold="Noches de habitación vendidas", f_revenue="Ingresos por habitaciones del periodo",
  h_sold="Cada habitación ocupada cuenta una vez por noche. Un huésped que se queda 3 noches = 3 noches de habitación.",
  h_revenue="Solo ingresos por habitaciones; sin extras como traslados, excursiones e impuestos (elijas lo que elijas, sé coherente).",
  r_avail="Noches de habitación disponibles", r_occ="Porcentaje de ocupación", r_adr="ADR (tarifa media diaria)", r_revpar="RevPAR (ingreso por habitación disponible)",
  warn="Las noches vendidas no pueden superar las noches disponibles. Revisa el número de habitaciones o de días.",
  privacy="Se calcula en tu navegador; tus datos no se envían a ningún sitio.",
  f_h="Las fórmulas",
  f_items=[("Porcentaje de ocupación", "Noches vendidas ÷ noches disponibles × 100", "Qué parte de tus habitaciones estuvo ocupada. Noches disponibles = habitaciones × días."),
           ("ADR (Average Daily Rate)", "Ingresos por habitaciones ÷ noches vendidas", "El precio medio de una noche de habitación vendida. No tiene en cuenta las habitaciones vacías."),
           ("RevPAR (Revenue per Available Room)", "Ingresos por habitaciones ÷ noches disponibles = ADR × ocupación", "Une precio y ocupación en un solo número, así que también muestra el coste de las habitaciones vacías.")],
  ex_h="Ejemplo paso a paso",
  ex_p="Un hotel boutique de 12 habitaciones vendió 285 noches de habitación en un mes de 31 días e ingresó 39.900 € por habitaciones:",
  ex_list=["Noches disponibles: 12 × 31 = 372", "Ocupación: 285 ÷ 372 = 76,6 %", "ADR: 39.900 € ÷ 285 = 140 €", "RevPAR: 39.900 € ÷ 372 = 107,26 € (o 140 € × 76,6 %)"],
  ex_after="Los valores por defecto de la calculadora son este ejemplo; sustitúyelos por los tuyos.",
  why_h="Qué te dice cada indicador",
  why=[("Ocupación alta, RevPAR bajo", "Puede que vendas demasiado barato. Subir un poco la tarifa en fechas de alta demanda puede mejorar el RevPAR sin perder mucha ocupación."),
       ("ADR alto, ocupación baja", "La tarifa puede estar por encima de la demanda o tu distribución puede ser escasa. Estar en más canales y revisar las estancias mínimas puede ayudar."),
       ("Al comparar el RevPAR", "Compáralo con el mismo periodo del año anterior o con alojamientos de tamaño parecido. Entre hoteles con distinto número de habitaciones, el RevPAR es más justo que los ingresos totales.")],
  mist_h="Errores frecuentes",
  mist=["Sumar desayunos, traslados y excursiones a los ingresos por habitaciones (infla ADR y RevPAR).",
        "Restar las habitaciones fuera de servicio un mes sí y otro no. Elige un método y mantenlo.",
        "Contar habitaciones de cortesía como vendidas sin ingresos, lo que hunde el ADR.",
        "Mezclar ingresos brutos y netos de los canales con comisión. Para ver la rentabilidad por canal usa la <a href=\"{commission}\">calculadora de comisión OTA</a>."],
  hl_h="En Hostlio Pro estos números se calculan solos",
  hl_p="La pantalla de Análisis del panel de Hostlio Pro calcula la ocupación, el ADR y el RevPAR a partir de tus reservas, los compara con el periodo anterior y con el año pasado, y muestra ingresos brutos, comisión e ingresos netos por canal. Puedes exportar los informes a Excel. <a href=\"{features}\">Ver todas las funcionalidades</a> o <a href=\"{pricing}\">comparar planes</a> (desde ⟦price:starter⟧ al mes).",
  faq=[("¿Cómo se calcula el RevPAR?", "Divide los ingresos por habitaciones del periodo entre las noches de habitación disponibles. El resultado es el mismo que multiplicar el ADR por la ocupación: 140 € de ADR con un 76,6 % de ocupación son unos 107 € de RevPAR."),
       ("¿Qué diferencia hay entre ADR y RevPAR?", "El ADR es el precio medio de las habitaciones vendidas; el RevPAR también cuenta las que no se vendieron. Por eso el RevPAR resume precio y ocupación en un solo número."),
       ("¿Cómo se calcula el porcentaje de ocupación hotelera?", "Divide las noches vendidas entre las noches disponibles (habitaciones × días) y multiplica por 100. Un hotel de 20 habitaciones que vendió 450 noches en 30 días tiene una ocupación de 450 ÷ 600 = 75 %."),
       ("¿El desayuno cuenta como ingreso por habitación?", "Separar el desayuno incluido en una tarifa paquete suele ser poco práctico; lo importante es usar el mismo criterio en cada periodo. Los extras vendidos aparte (traslados, excursiones, desayuno de pago) no son ingresos por habitación."),
       ("¿Se guardan los datos que introduzco?", "No. El cálculo se hace por completo en tu navegador; no se envía nada a ningún servidor.")],
  com_crumb="Calculadora de comisión OTA",
  com_title="Calculadora de comisión OTA: ingreso neto | Hostlio Pro",
  com_desc="Calcula cuánto te queda de una reserva de Booking.com o Expedia tras la comisión y los gastos de pago, y el ingreso neto por noche. Gratis y sin registro.",
  com_h1='Comisión OTA → <em class="hl">ingreso neto</em>',
  com_lead="Introduce el importe de la reserva, la comisión de tu contrato y otros cargos si los hay. La comisión, el ingreso neto y el neto por noche se calculan al instante.",
  f_gross="Importe de la reserva (bruto)", f_rate="Porcentaje de comisión", f_fee="Gastos de pago y otros", f_nights="Noches (opcional)",
  h_rate="Comprueba el porcentaje en tu contrato con el canal o en la factura de la extranet. Los valores por defecto son solo un ejemplo.",
  r_commission="Comisión", r_fees="Otros gastos", r_net="Ingreso neto", r_kept="Parte que te queda", r_night="Neto por noche",
  c_how_h="Cómo se calcula",
  c_how=["Comisión = importe bruto × porcentaje de comisión", "Otros gastos = importe bruto × porcentaje de gastos (p. ej. tarjeta virtual o pasarela de pago)", "Ingreso neto = importe bruto − comisión − otros gastos", "Neto por noche = ingreso neto ÷ noches"],
  c_ex_h="Ejemplo",
  c_ex_p="Una reserva de 3 noches de 1.200 € con un 18 % de comisión y un 1,5 % de gastos de pago: comisión 216 €, otros gastos 18 €, ingreso neto 966 €, neto por noche 322 €. De los 400 € que paga el huésped por noche, te quedan 322 €.",
  c_note="Algunos canales calculan la comisión sobre el importe con impuestos y otros sin impuestos. Introduce el importe bruto según la base de tu contrato. Esta página no es asesoramiento fiscal.",
  c_direct_h="Compárala con una reserva directa",
  c_direct_p="Si la misma habitación se vende de forma directa (teléfono, WhatsApp, tu web) no hay comisión. Si te queda el 80,5 %, como en el ejemplo, podrías ofrecer hasta un 19,5 % de descuento en directo sin ganar menos que con la OTA. Ten en cuenta los costes propios de la venta directa (pasarela de pago, publicidad).",
  c_hl_p="La pantalla de Análisis de Hostlio Pro muestra ingresos brutos, comisión e ingresos netos de cada canal, para que veas cuál es rentable de verdad tras la comisión. El <a href=\"{channel}\">channel manager</a> reúne más de 100 OTAs en un calendario y <a href=\"{ai}\">Lio</a> responde por WhatsApp para que recibas solicitudes de reserva directa. Los <a href=\"{pricing}\">planes</a> empiezan en ⟦price:starter⟧ al mes.",
  c_faq=[("¿Cómo se calcula la comisión de una OTA?", "Multiplica el importe de la reserva por el porcentaje de tu contrato: 1.200 € × 18 % = 216 €. Para el ingreso neto, resta ese importe y los gastos de pago del importe bruto."),
         ("¿La comisión se calcula con impuestos incluidos?", "Depende del canal y del país. Tu contrato y la factura mensual del canal indican qué importe se usa; introduce ese importe en la calculadora."),
         ("¿Qué es el ADR neto?", "El ingreso medio que queda por noche vendida después de comisiones y gastos. Para comparar canales, el ADR neto es más fiel que el bruto."),
         ("¿Se guardan mis datos?", "No. El cálculo se hace en tu navegador y no se envía nada.")],
),
"it": dict(
  hub_crumb="Strumenti", hub_title="Calcolatori gratis per hotel: RevPAR e commissioni | Hostlio Pro",
  hub_desc="Calcolatori gratuiti per albergatori: RevPAR, ADR e occupazione, ricavo netto dopo la commissione OTA e risparmio con i messaggi AI. Senza registrazione.",
  hub_h1='Calcolatori <em class="hl">gratuiti</em> per albergatori',
  hub_lead="Strumenti semplici che funzionano nel browser, senza registrazione. I numeri che inserisci non vengono inviati da nessuna parte.",
  hub_note="I calcoli avvengono solo nel tuo browser; i dati non vengono salvati né inviati a un server.",
  cards=[("kpi", "Calcolatore di RevPAR, ADR e occupazione", "Calcola i tre indicatori chiave dell’hotel da camere, notti vendute e ricavi camere, con le formule."),
         ("commission", "Commissione OTA → ricavo netto", "Quanto ti resta davvero di una prenotazione Booking.com o Expedia dopo commissione e altri costi?"),
         ("roi", "Calcolatore ROI dei messaggi AI", "Stima le ore e il costo del personale che oggi richiede rispondere agli ospiti.")],
  currency="Valuta",
  kpi_crumb="Calcolatore di RevPAR, ADR e occupazione",
  kpi_title="Calcolo RevPAR, ADR e tasso di occupazione (gratis) | Hostlio Pro",
  kpi_desc="Calcola RevPAR, ADR e tasso di occupazione in pochi secondi. Formule, esempio passo passo ed errori comuni. Calcolatore gratuito per hotel, senza registrazione.",
  kpi_h1='Calcolo di RevPAR, ADR e <em class="hl">tasso di occupazione</em>',
  kpi_lead="Inserisci le camere, le notti camera vendute e i ricavi camere del periodo. Tasso di occupazione, prezzo medio giornaliero (ADR) e ricavo per camera disponibile (RevPAR) si aggiornano subito.",
  f_rooms="Camere in vendita", f_days="Giorni del periodo", f_sold="Notti camera vendute", f_revenue="Ricavi camere del periodo",
  h_sold="Ogni camera occupata conta una volta per notte. Un ospite che resta 3 notti = 3 notti camera.",
  h_revenue="Solo ricavi camere; escludi extra come transfer, escursioni e imposte (qualunque scelta, sii coerente).",
  r_avail="Notti camera disponibili", r_occ="Tasso di occupazione", r_adr="ADR (prezzo medio giornaliero)", r_revpar="RevPAR (ricavo per camera disponibile)",
  warn="Le notti vendute non possono superare le notti disponibili. Controlla il numero di camere o di giorni.",
  privacy="Il calcolo avviene nel browser; i tuoi numeri non vengono inviati.",
  f_h="Le formule",
  f_items=[("Tasso di occupazione", "Notti vendute ÷ notti disponibili × 100", "La quota di camere occupate. Notti disponibili = camere × giorni."),
           ("ADR (Average Daily Rate)", "Ricavi camere ÷ notti vendute", "Il prezzo medio di una notte camera venduta. Non considera le camere vuote."),
           ("RevPAR (Revenue per Available Room)", "Ricavi camere ÷ notti disponibili = ADR × tasso di occupazione", "Unisce prezzo e occupazione in un solo numero, quindi mostra anche il costo delle camere vuote.")],
  ex_h="Esempio passo passo",
  ex_p="Un boutique hotel di 12 camere ha venduto 285 notti camera in un mese di 31 giorni con 39.900 € di ricavi camere:",
  ex_list=["Notti disponibili: 12 × 31 = 372", "Occupazione: 285 ÷ 372 = 76,6%", "ADR: 39.900 € ÷ 285 = 140 €", "RevPAR: 39.900 € ÷ 372 = 107,26 € (oppure 140 € × 76,6%)"],
  ex_after="I valori predefiniti del calcolatore sono questo esempio; sostituiscili con i tuoi.",
  why_h="Cosa ti dice ogni indicatore",
  why=[("Occupazione alta, RevPAR basso", "Forse vendi a prezzi troppo bassi. Alzare un po’ la tariffa nelle date di punta può aumentare il RevPAR senza perdere molta occupazione."),
       ("ADR alto, occupazione bassa", "La tariffa può essere sopra la domanda o la distribuzione può essere limitata. Essere su più canali e rivedere i soggiorni minimi può aiutare."),
       ("Quando confronti il RevPAR", "Confrontalo con lo stesso periodo dell’anno precedente o con strutture di dimensioni simili. Tra hotel con un numero di camere diverso, il RevPAR è più equo dei ricavi totali.")],
  mist_h="Errori comuni",
  mist=["Sommare colazioni, transfer ed escursioni ai ricavi camere (gonfia ADR e RevPAR).",
        "Togliere le camere fuori servizio un mese sì e uno no. Scegli un metodo e mantienilo.",
        "Contare le camere gratuite come vendute senza ricavi, abbassando l’ADR.",
        "Confondere ricavi lordi e netti dei canali a commissione. Per la redditività per canale usa il <a href=\"{commission}\">calcolatore di commissioni OTA</a>."],
  hl_h="In Hostlio Pro questi numeri arrivano da soli",
  hl_p="La schermata Analisi del pannello Hostlio Pro calcola occupazione, ADR e RevPAR dalle tue prenotazioni, li confronta con il periodo precedente e con l’anno scorso e mostra ricavi lordi, commissioni e ricavi netti per canale. Puoi esportare i report in Excel. <a href=\"{features}\">Vedi tutte le funzionalità</a> o <a href=\"{pricing}\">confronta i piani</a> (da ⟦price:starter⟧ al mese).",
  faq=[("Come si calcola il RevPAR?", "Dividi i ricavi camere del periodo per le notti camera disponibili. Ottieni lo stesso risultato moltiplicando l’ADR per il tasso di occupazione: 140 € di ADR al 76,6% di occupazione fanno circa 107 € di RevPAR."),
       ("Che differenza c’è tra ADR e RevPAR?", "L’ADR è il prezzo medio delle camere vendute; il RevPAR conta anche quelle non vendute. Per questo il RevPAR riassume prezzo e occupazione in un solo numero."),
       ("Come si calcola il tasso di occupazione di un hotel?", "Dividi le notti vendute per le notti disponibili (camere × giorni) e moltiplica per 100. Un hotel di 20 camere che ha venduto 450 notti in 30 giorni ha un’occupazione di 450 ÷ 600 = 75%."),
       ("La colazione rientra nei ricavi camere?", "Separare la colazione inclusa in una tariffa pacchetto spesso non è pratico; conta usare lo stesso criterio in ogni periodo. Gli extra venduti a parte (transfer, escursioni, colazione a pagamento) non sono ricavi camere."),
       ("I numeri che inserisco vengono salvati?", "No. Il calcolo avviene interamente nel browser; nulla viene inviato a un server.")],
  com_crumb="Calcolatore commissioni OTA",
  com_title="Calcolatore commissioni OTA: ricavo netto | Hostlio Pro",
  com_desc="Calcola quanto ti resta di una prenotazione Booking.com o Expedia dopo commissione e costi di pagamento, e il netto per notte. Gratis, senza registrazione.",
  com_h1='Commissione OTA → <em class="hl">ricavo netto</em>',
  com_lead="Inserisci l’importo della prenotazione, la commissione del contratto ed eventuali altri costi. Commissione, ricavo netto e netto per notte si aggiornano subito.",
  f_gross="Importo prenotazione (lordo)", f_rate="Percentuale di commissione", f_fee="Costi di pagamento e altri", f_nights="Notti (facoltativo)",
  h_rate="Verifica la percentuale nel contratto con il canale o nella fattura dell’extranet. I valori predefiniti sono solo un esempio.",
  r_commission="Commissione", r_fees="Altri costi", r_net="Ricavo netto", r_kept="Quota che ti resta", r_night="Netto per notte",
  c_how_h="Come si calcola",
  c_how=["Commissione = importo lordo × percentuale di commissione", "Altri costi = importo lordo × percentuale costi (es. carta virtuale o commissioni di pagamento)", "Ricavo netto = importo lordo − commissione − altri costi", "Netto per notte = ricavo netto ÷ notti"],
  c_ex_h="Esempio",
  c_ex_p="Una prenotazione di 3 notti da 1.200 € con commissione del 18% e costi di pagamento dell’1,5%: commissione 216 €, altri costi 18 €, ricavo netto 966 €, netto per notte 322 €. Dei 400 € a notte pagati dall’ospite, a te restano 322 €.",
  c_note="Alcuni canali calcolano la commissione sull’importo con imposte, altri senza. Inserisci l’importo lordo secondo la base del tuo contratto. Questa pagina non è consulenza fiscale.",
  c_direct_h="Confronta con una prenotazione diretta",
  c_direct_p="Se la stessa camera è venduta direttamente (telefono, WhatsApp, il tuo sito) non c’è commissione. Se ti resta l’80,5%, come nell’esempio, potresti offrire fino al 19,5% di sconto in diretta senza guadagnare meno che con l’OTA. Considera i costi propri della vendita diretta (pagamenti, pubblicità).",
  c_hl_p="La schermata Analisi di Hostlio Pro mostra ricavi lordi, commissioni e ricavi netti di ogni canale, così vedi quale rende davvero dopo la commissione. Il <a href=\"{channel}\">channel manager</a> riunisce oltre 100 OTA in un calendario e <a href=\"{ai}\">Lio</a> risponde su WhatsApp per aiutarti a ricevere richieste di prenotazione diretta. I <a href=\"{pricing}\">piani</a> partono da ⟦price:starter⟧ al mese.",
  c_faq=[("Come si calcola la commissione OTA?", "Moltiplica l’importo della prenotazione per la percentuale del contratto: 1.200 € × 18% = 216 €. Per il ricavo netto sottrai questo importo e gli eventuali costi di pagamento dal lordo."),
         ("La commissione si calcola con le imposte incluse?", "Dipende dal canale e dal paese. Il contratto e la fattura mensile del canale indicano l’importo di riferimento; inserisci quello."),
         ("Cos’è l’ADR netto?", "Il ricavo medio che resta per notte venduta dopo commissioni e costi. Per confrontare i canali è più fedele dell’ADR lordo."),
         ("I miei numeri vengono salvati?", "No. Il calcolo avviene nel browser e non viene inviato nulla.")],
),
"pt": dict(
  hub_crumb="Ferramentas", hub_title="Calculadoras grátis para hotéis: RevPAR e comissão | Hostlio Pro",
  hub_desc="Calculadoras gratuitas para hoteleiros: RevPAR, ADR e taxa de ocupação, receita líquida após a comissão da OTA e economia com mensagens de IA. Sem cadastro.",
  hub_h1='Calculadoras <em class="hl">gratuitas</em> para hoteleiros',
  hub_lead="Ferramentas simples que funcionam no seu navegador, sem cadastro. Os números que você digita não são enviados a lugar nenhum.",
  hub_note="Os cálculos são feitos só no seu navegador; os dados não são salvos nem enviados a um servidor.",
  cards=[("kpi", "Calculadora de RevPAR, ADR e ocupação", "Calcule os três indicadores principais do hotel a partir de quartos, diárias vendidas e receita de hospedagem, com as fórmulas."),
         ("commission", "Comissão de OTA → receita líquida", "Quanto realmente sobra de uma reserva do Booking.com ou da Expedia depois da comissão e de outras taxas?"),
         ("roi", "Calculadora de ROI de mensagens com IA", "Estime as horas e o custo de equipe que responder hóspedes exige hoje.")],
  currency="Moeda",
  kpi_crumb="Calculadora de RevPAR, ADR e ocupação",
  kpi_title="Calculadora de RevPAR, ADR e taxa de ocupação | Hostlio Pro",
  kpi_desc="Calcule RevPAR, ADR e taxa de ocupação em segundos. Fórmulas, exemplo passo a passo e erros comuns. Calculadora hoteleira gratuita, sem cadastro.",
  kpi_h1='Calculadora de RevPAR, ADR e <em class="hl">taxa de ocupação</em>',
  kpi_lead="Informe seus quartos, as diárias vendidas e a receita de hospedagem do período. Taxa de ocupação, diária média (ADR) e receita por quarto disponível (RevPAR) são calculadas na hora.",
  f_rooms="Quartos disponíveis para venda", f_days="Dias do período", f_sold="Diárias vendidas (quartos-noite)", f_revenue="Receita de hospedagem do período",
  h_sold="Cada quarto ocupado conta uma vez por noite. Um hóspede que fica 3 noites = 3 diárias.",
  h_revenue="Só receita de hospedagem; sem extras como transfer, passeios e impostos (seja qual for a escolha, mantenha a coerência).",
  r_avail="Quartos-noite disponíveis", r_occ="Taxa de ocupação", r_adr="ADR (diária média)", r_revpar="RevPAR (receita por quarto disponível)",
  warn="As diárias vendidas não podem passar dos quartos-noite disponíveis. Confira o número de quartos ou de dias.",
  privacy="Calculado no seu navegador; seus números não são enviados.",
  f_h="As fórmulas",
  f_items=[("Taxa de ocupação", "Diárias vendidas ÷ quartos-noite disponíveis × 100", "Quanto dos seus quartos ficou ocupado. Quartos-noite disponíveis = quartos × dias."),
           ("ADR (Average Daily Rate)", "Receita de hospedagem ÷ diárias vendidas", "O preço médio de uma diária vendida. Não considera os quartos vazios."),
           ("RevPAR (Revenue per Available Room)", "Receita de hospedagem ÷ quartos-noite disponíveis = ADR × taxa de ocupação", "Junta preço e ocupação num só número, mostrando também o custo dos quartos vazios.")],
  ex_h="Exemplo passo a passo",
  ex_p="Um hotel boutique de 12 quartos vendeu 285 diárias num mês de 31 dias e faturou R$ 39.900 em hospedagem:",
  ex_list=["Quartos-noite disponíveis: 12 × 31 = 372", "Ocupação: 285 ÷ 372 = 76,6%", "ADR: R$ 39.900 ÷ 285 = R$ 140", "RevPAR: R$ 39.900 ÷ 372 = R$ 107,26 (ou R$ 140 × 76,6%)"],
  ex_after="Os valores padrão da calculadora são este exemplo; troque pelos seus.",
  why_h="O que cada indicador mostra",
  why=[("Ocupação alta, RevPAR baixo", "Talvez você esteja vendendo barato demais. Subir um pouco a tarifa nas datas de maior procura pode aumentar o RevPAR sem perder muita ocupação."),
       ("ADR alto, ocupação baixa", "A tarifa pode estar acima da demanda ou a distribuição pode estar fraca. Estar em mais canais e rever estadias mínimas pode ajudar."),
       ("Ao comparar o RevPAR", "Compare com o mesmo período do ano anterior ou com hotéis de porte parecido. Entre hotéis com número de quartos diferente, o RevPAR é mais justo que a receita total.")],
  mist_h="Erros comuns",
  mist=["Somar café da manhã, transfer e passeios à receita de hospedagem (infla ADR e RevPAR).",
        "Tirar os quartos interditados num mês e no outro não. Escolha um método e mantenha.",
        "Contar cortesias como vendidas sem receita, o que derruba o ADR.",
        "Misturar receita bruta e líquida dos canais com comissão. Para ver a rentabilidade por canal use a <a href=\"{commission}\">calculadora de comissão de OTA</a>."],
  hl_h="No Hostlio Pro esses números aparecem sozinhos",
  hl_p="A tela de Análise do painel do Hostlio Pro calcula ocupação, ADR e RevPAR a partir das suas reservas, compara com o período anterior e com o ano passado e mostra receita bruta, comissão e receita líquida por canal. Você pode exportar os relatórios para Excel. <a href=\"{features}\">Veja todos os recursos</a> ou <a href=\"{pricing}\">compare os planos</a> (a partir de ⟦price:starter⟧ por mês).",
  faq=[("Como calcular o RevPAR?", "Divida a receita de hospedagem do período pelos quartos-noite disponíveis. O resultado é o mesmo que multiplicar o ADR pela taxa de ocupação: ADR de R$ 140 com 76,6% de ocupação dá cerca de R$ 107 de RevPAR."),
       ("Qual a diferença entre ADR e RevPAR?", "O ADR é o preço médio dos quartos vendidos; o RevPAR também conta os que não foram vendidos. Por isso o RevPAR resume preço e ocupação num só número."),
       ("Como calcular a taxa de ocupação de um hotel?", "Divida as diárias vendidas pelos quartos-noite disponíveis (quartos × dias) e multiplique por 100. Um hotel de 20 quartos que vendeu 450 diárias em 30 dias tem ocupação de 450 ÷ 600 = 75%."),
       ("O café da manhã entra na receita de hospedagem?", "Separar o café incluído numa tarifa pacote costuma ser pouco prático; o importante é usar o mesmo critério em todo período. Extras vendidos à parte (transfer, passeios, café pago) não são receita de hospedagem."),
       ("Os números que eu digito ficam salvos?", "Não. O cálculo é feito inteiramente no seu navegador; nada é enviado a um servidor.")],
  com_crumb="Calculadora de comissão de OTA",
  com_title="Calculadora de comissão de OTA: receita líquida | Hostlio Pro",
  com_desc="Calcule quanto sobra de uma reserva do Booking.com ou da Expedia após comissão e taxas de pagamento, e a receita líquida por noite. Grátis e sem cadastro.",
  com_h1='Comissão de OTA → <em class="hl">receita líquida</em>',
  com_lead="Informe o valor da reserva, a comissão do seu contrato e outras taxas, se houver. Comissão, receita líquida e líquido por noite são calculados na hora.",
  f_gross="Valor da reserva (bruto)", f_rate="Percentual de comissão", f_fee="Taxas de pagamento e outras", f_nights="Noites (opcional)",
  h_rate="Confira o percentual no contrato com o canal ou na fatura da extranet. Os valores padrão são só um exemplo.",
  r_commission="Comissão", r_fees="Outras taxas", r_net="Receita líquida", r_kept="Parte que fica com você", r_night="Líquido por noite",
  c_how_h="Como é calculado",
  c_how=["Comissão = valor bruto × percentual de comissão", "Outras taxas = valor bruto × percentual de taxas (ex.: cartão virtual ou processamento de pagamento)", "Receita líquida = valor bruto − comissão − outras taxas", "Líquido por noite = receita líquida ÷ noites"],
  c_ex_h="Exemplo",
  c_ex_p="Uma reserva de 3 noites de R$ 1.200 com 18% de comissão e 1,5% de taxa de pagamento: comissão R$ 216, outras taxas R$ 18, receita líquida R$ 966, líquido por noite R$ 322. Dos R$ 400 por noite que o hóspede paga, ficam R$ 322 com você.",
  c_note="Alguns canais cobram comissão sobre o valor com impostos, outros sem impostos. Informe o valor bruto conforme a base do seu contrato. Esta página não é consultoria tributária.",
  c_direct_h="Compare com uma reserva direta",
  c_direct_p="Quando o mesmo quarto é vendido direto (telefone, WhatsApp, seu site) não há comissão. Se fica com você 80,5%, como no exemplo, você poderia dar até 19,5% de desconto na reserva direta sem ganhar menos que pela OTA. Considere os custos da venda direta (pagamentos, anúncios).",
  c_hl_p="A tela de Análise do Hostlio Pro mostra receita bruta, comissão e receita líquida de cada canal, para você ver qual realmente compensa depois da comissão. O <a href=\"{channel}\">channel manager</a> reúne mais de 100 OTAs num calendário e a <a href=\"{ai}\">Lio</a> responde no WhatsApp para você receber pedidos de reserva direta. Os <a href=\"{pricing}\">planos</a> começam em ⟦price:starter⟧ por mês.",
  c_faq=[("Como calcular a comissão da OTA?", "Multiplique o valor da reserva pelo percentual do contrato: R$ 1.200 × 18% = R$ 216. Para a receita líquida, subtraia esse valor e as taxas de pagamento do valor bruto."),
         ("A comissão é calculada com impostos?", "Depende do canal e do país. O contrato e a fatura mensal do canal indicam o valor de base; informe esse valor na calculadora."),
         ("O que é ADR líquido?", "A receita média que sobra por diária vendida depois de comissões e taxas. Para comparar canais, o ADR líquido é mais fiel que o bruto."),
         ("Meus números ficam salvos?", "Não. O cálculo é feito no navegador e nada é enviado.")],
),
"fr": dict(
  hub_crumb="Outils", hub_title="Calculateurs hôteliers gratuits : RevPAR, ADR | Hostlio Pro",
  hub_desc="Calculateurs gratuits pour hôteliers : RevPAR, ADR et taux d’occupation, revenu net après commission OTA et économies de la messagerie IA. Sans inscription.",
  hub_h1='Calculateurs <em class="hl">gratuits</em> pour hôteliers',
  hub_lead="Des outils simples qui fonctionnent dans votre navigateur, sans inscription. Les chiffres saisis ne sont envoyés nulle part.",
  hub_note="Les calculs se font uniquement dans votre navigateur ; les données ne sont ni enregistrées ni envoyées à un serveur.",
  cards=[("kpi", "Calculateur de RevPAR, ADR et taux d’occupation", "Calculez les trois indicateurs clés de l’hôtel à partir des chambres, des nuitées vendues et du chiffre d’affaires hébergement, formules à l’appui."),
         ("commission", "Commission OTA → revenu net", "Que vous reste-t-il vraiment d’une réservation Booking.com ou Expedia après la commission et les autres frais ?"),
         ("roi", "Calculateur de ROI de la messagerie IA", "Estimez les heures et le coût de personnel que demandent aujourd’hui les réponses aux clients.")],
  currency="Devise",
  kpi_crumb="Calculateur de RevPAR, ADR et taux d’occupation",
  kpi_title="Calcul du RevPAR, de l’ADR et du taux d’occupation | Hostlio Pro",
  kpi_desc="Calculez RevPAR, ADR (prix moyen) et taux d’occupation en quelques secondes. Formules, exemple détaillé et erreurs fréquentes. Outil gratuit, sans inscription.",
  kpi_h1='Calcul du RevPAR, de l’ADR et du <em class="hl">taux d’occupation</em>',
  kpi_lead="Saisissez vos chambres, les nuitées vendues et le chiffre d’affaires hébergement de la période. Taux d’occupation, prix moyen par chambre (ADR) et revenu par chambre disponible (RevPAR) se calculent aussitôt.",
  f_rooms="Chambres disponibles à la vente", f_days="Jours de la période", f_sold="Nuitées vendues (chambres-nuits)", f_revenue="CA hébergement de la période",
  h_sold="Chaque chambre occupée compte une fois par nuit. Un client qui reste 3 nuits = 3 nuitées.",
  h_revenue="Uniquement le chiffre d’affaires hébergement ; sans extras comme transferts, excursions et taxes (quel que soit votre choix, restez cohérent).",
  r_avail="Chambres-nuits disponibles", r_occ="Taux d’occupation", r_adr="ADR (prix moyen par chambre)", r_revpar="RevPAR (revenu par chambre disponible)",
  warn="Les nuitées vendues ne peuvent pas dépasser les chambres-nuits disponibles. Vérifiez le nombre de chambres ou de jours.",
  privacy="Calcul effectué dans votre navigateur ; vos chiffres ne sont envoyés nulle part.",
  f_h="Les formules",
  f_items=[("Taux d’occupation", "Nuitées vendues ÷ chambres-nuits disponibles × 100", "La part de vos chambres occupées. Chambres-nuits disponibles = chambres × jours."),
           ("ADR (Average Daily Rate, prix moyen)", "CA hébergement ÷ nuitées vendues", "Le prix moyen d’une nuitée vendue. Il ne tient pas compte des chambres vides."),
           ("RevPAR (Revenue per Available Room)", "CA hébergement ÷ chambres-nuits disponibles = ADR × taux d’occupation", "Réunit prix et occupation en un seul chiffre, et montre donc aussi le coût des chambres vides.")],
  ex_h="Exemple détaillé",
  ex_p="Un hôtel boutique de 12 chambres a vendu 285 nuitées sur un mois de 31 jours pour 39 900 € de chiffre d’affaires hébergement :",
  ex_list=["Chambres-nuits disponibles : 12 × 31 = 372", "Taux d’occupation : 285 ÷ 372 = 76,6 %", "ADR : 39 900 € ÷ 285 = 140 €", "RevPAR : 39 900 € ÷ 372 = 107,26 € (ou 140 € × 76,6 %)"],
  ex_after="Les valeurs par défaut du calculateur reprennent cet exemple ; remplacez-les par les vôtres.",
  why_h="Ce que dit chaque indicateur",
  why=[("Occupation élevée, RevPAR faible", "Vous vendez peut-être trop bon marché. Relever un peu le prix les jours de forte demande peut augmenter le RevPAR sans perdre beaucoup d’occupation."),
       ("ADR élevé, occupation faible", "Le prix est peut-être au-dessus de la demande, ou votre distribution est trop limitée. Être présent sur plus de canaux et revoir les durées minimales de séjour peut aider."),
       ("Pour comparer le RevPAR", "Comparez avec la même période de l’année précédente ou avec des établissements de taille proche. Entre hôtels de tailles différentes, le RevPAR est plus juste que le chiffre d’affaires total.")],
  mist_h="Erreurs fréquentes",
  mist=["Ajouter petits-déjeuners, transferts et excursions au CA hébergement (cela gonfle ADR et RevPAR).",
        "Retirer les chambres hors service un mois sur deux. Choisissez une méthode et gardez-la.",
        "Compter les chambres offertes comme vendues sans revenu, ce qui fait baisser l’ADR.",
        "Mélanger revenu brut et net des canaux à commission. Pour la rentabilité par canal, utilisez le <a href=\"{commission}\">calculateur de commission OTA</a>."],
  hl_h="Dans Hostlio Pro, ces chiffres arrivent tout seuls",
  hl_p="L’écran Analyse du tableau de bord Hostlio Pro calcule le taux d’occupation, l’ADR et le RevPAR à partir de vos réservations, les compare à la période précédente et à l’année dernière, et affiche revenu brut, commission et revenu net par canal. Vous pouvez exporter les rapports vers Excel. <a href=\"{features}\">Voir toutes les fonctionnalités</a> ou <a href=\"{pricing}\">comparer les forfaits</a> (dès ⟦price:starter⟧ par mois).",
  faq=[("Comment calculer le RevPAR ?", "Divisez le chiffre d’affaires hébergement de la période par les chambres-nuits disponibles. On obtient le même résultat en multipliant l’ADR par le taux d’occupation : 140 € d’ADR à 76,6 % d’occupation donnent environ 107 € de RevPAR."),
       ("Quelle différence entre ADR et RevPAR ?", "L’ADR est le prix moyen des chambres vendues ; le RevPAR tient aussi compte des chambres invendues. C’est pourquoi le RevPAR résume prix et occupation en un seul chiffre."),
       ("Comment calculer le taux d’occupation d’un hôtel ?", "Divisez les nuitées vendues par les chambres-nuits disponibles (chambres × jours) et multipliez par 100. Un hôtel de 20 chambres qui a vendu 450 nuitées en 30 jours a un taux d’occupation de 450 ÷ 600 = 75 %."),
       ("Le petit-déjeuner fait-il partie du CA hébergement ?", "Séparer le petit-déjeuner inclus dans un tarif forfaitaire est souvent peu pratique ; l’essentiel est de garder la même méthode à chaque période. Les extras vendus à part (transferts, excursions, petit-déjeuner payant) ne sont pas du CA hébergement."),
       ("Les chiffres saisis sont-ils enregistrés ?", "Non. Le calcul se fait entièrement dans votre navigateur ; rien n’est envoyé à un serveur.")],
  com_crumb="Calculateur de commission OTA",
  com_title="Calculateur de commission OTA : revenu net | Hostlio Pro",
  com_desc="Calculez ce qu’il vous reste d’une réservation Booking.com ou Expedia après commission et frais de paiement, et le net par nuit. Gratuit, sans inscription.",
  com_h1='Commission OTA → <em class="hl">revenu net</em>',
  com_lead="Saisissez le montant de la réservation, le taux de commission de votre contrat et les autres frais éventuels. Commission, revenu net et net par nuit se calculent aussitôt.",
  f_gross="Montant de la réservation (brut)", f_rate="Taux de commission", f_fee="Frais de paiement et autres", f_nights="Nuits (facultatif)",
  h_rate="Vérifiez le taux dans votre contrat avec le canal ou sur la facture de l’extranet. Les valeurs par défaut ne sont qu’un exemple.",
  r_commission="Commission", r_fees="Autres frais", r_net="Revenu net", r_kept="Part qui vous reste", r_night="Net par nuit",
  c_how_h="Comment c’est calculé",
  c_how=["Commission = montant brut × taux de commission", "Autres frais = montant brut × taux de frais (p. ex. carte virtuelle ou frais de paiement)", "Revenu net = montant brut − commission − autres frais", "Net par nuit = revenu net ÷ nuits"],
  c_ex_h="Exemple",
  c_ex_p="Une réservation de 3 nuits à 1 200 € avec 18 % de commission et 1,5 % de frais de paiement : commission 216 €, autres frais 18 €, revenu net 966 €, net par nuit 322 €. Sur les 400 € par nuit payés par le client, il vous reste 322 €.",
  c_note="Certains canaux calculent la commission sur le montant TTC, d’autres sur le montant HT. Saisissez le montant brut selon la base de votre contrat. Cette page n’est pas un conseil fiscal.",
  c_direct_h="Comparez avec une réservation directe",
  c_direct_p="Quand la même chambre est vendue en direct (téléphone, WhatsApp, votre site), il n’y a pas de commission. Si la part qui vous reste est de 80,5 %, comme dans l’exemple, vous pourriez accorder jusqu’à 19,5 % de remise en direct sans gagner moins qu’avec l’OTA. Tenez compte des coûts propres à la vente directe (paiement, publicité).",
  c_hl_p="L’écran Analyse de Hostlio Pro affiche revenu brut, commission et revenu net de chaque canal : vous voyez lequel rapporte vraiment après commission. Le <a href=\"{channel}\">channel manager</a> réunit plus de 100 OTA dans un seul calendrier et <a href=\"{ai}\">Lio</a> répond sur WhatsApp pour vous aider à recevoir des demandes de réservation directe. Les <a href=\"{pricing}\">forfaits</a> commencent à ⟦price:starter⟧ par mois.",
  c_faq=[("Comment calculer la commission d’une OTA ?", "Multipliez le montant de la réservation par le taux de votre contrat : 1 200 € × 18 % = 216 €. Pour le revenu net, soustrayez ce montant et les frais de paiement du montant brut."),
         ("La commission est-elle calculée TTC ?", "Cela dépend du canal et du pays. Votre contrat et la facture mensuelle du canal indiquent le montant de référence ; saisissez celui-là."),
         ("Qu’est-ce que l’ADR net ?", "Le revenu moyen qui reste par nuitée vendue après commissions et frais. Pour comparer les canaux, l’ADR net est plus fidèle que l’ADR brut."),
         ("Mes chiffres sont-ils enregistrés ?", "Non. Le calcul se fait dans votre navigateur et rien n’est envoyé.")],
),
}

APP_NAME = {"kpi": "RevPAR, ADR & occupancy calculator", "commission": "OTA commission calculator"}


def _links(L, B):
    return {k: B.url(k, L) for k in ("features", "pricing", "channel", "ai", "commission", "kpi", "roi")}


def _field(name, label, val, mn, step, suffix="", hint="", hid=""):
    d = f' aria-describedby="{hid}"' if hint else ""
    h = f'<small id="{hid}">{hint}</small>' if hint else ""
    return (f'<label class="co-field roi-f"><span>{label}</span><span class="roi-in"><input type="number" name="{name}" value="{val}" min="{mn}" step="{step}" inputmode="decimal"{d}>'
            + (f'<span class="roi-suf">{suffix}</span>' if suffix else "") + f'</span>{h}</label>')


def _currency(L, t):
    opts = "".join(f'<option value="{c}"{" selected" if c == CUR[L] else ""}>{c}</option>' for c in CURS)
    return f'<label class="co-field roi-f"><span>{t["currency"]}</span><select name="currency">{opts}</select></label>'


def _res(rows):
    return "".join(f'<div class="roi-r" style="flex-wrap:wrap"><span>{lbl}</span><b id="{i}">–</b>'
                   + (f'<span id="{i}-f" class="small" style="flex-basis:100%;color:#B9C6D8;font-variant-numeric:tabular-nums"></span>' if f else "") + '</div>'
                   for lbl, i, f in rows)


def _ul(items): return "<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


def _app_schema(L, B, key, t, name_key):
    return {"@type": "WebApplication", "name": t[name_key].replace('<em class="hl">', "").replace("</em>", ""),
            "url": B.abs_url(key, L), "applicationCategory": "BusinessApplication", "operatingSystem": "Any (web browser)",
            "isAccessibleForFree": True, "inLanguage": B.IN_LANG[L],
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "publisher": {"@id": B.SITE + "/#org"}}


def kpi_page(L, B):
    t = T[L]; lk = _links(L, B)
    form = (_currency(L, t) + _field("rooms", t["f_rooms"], 12, 0, 1) + _field("days", t["f_days"], 31, 0, 1)
            + _field("sold", t["f_sold"], 285, 0, 1, hint=t["h_sold"], hid="h-sold")
            + _field("revenue", t["f_revenue"], 39900, 0, "any", hint=t["h_revenue"], hid="h-rev"))
    res = _res([(t["r_avail"], "kpi-avail", 1), (t["r_occ"], "kpi-occ", 1), (t["r_adr"], "kpi-adr", 1), (t["r_revpar"], "kpi-revpar", 1)])
    fi = "".join(f'<div class="row"><h3>{h}</h3><div><p><strong>{f}</strong></p><p>{p}</p></div></div>' for h, f, p in t["f_items"])
    why = "".join(f'<div class="row"><h3>{h}</h3><div><p>{p}</p></div></div>' for h, p in t["why"])
    mist = _ul([m.format(**lk) for m in t["mist"]])
    body = f'''<section class="page-hero"><div class="wrap"><h1>{t["kpi_h1"]}</h1><p class="lead">{t["kpi_lead"]}</p></div></section>
<section style="padding-top:0"><div class="wrap roi">
<form class="roi-form" id="kpi-form" data-lang="{L}" data-warn="{html.escape(t["warn"])}" novalidate>{form}</form>
<div class="roi-out on-dark" aria-live="polite">{res}<p class="small" id="kpi-warn" role="alert" hidden></p><p class="small" style="margin:14px 0 0;color:#D9E1EC">{t["privacy"]}</p></div>
</div></section>
<section class="white rule"><div class="wrap">
<h2>{t["f_h"]}</h2><div class="rows">{fi}</div>
<h2 style="margin-top:64px">{t["ex_h"]}</h2><div class="prose"><p>{t["ex_p"]}</p><ol>{"".join(f"<li>{x}</li>" for x in t["ex_list"])}</ol><p class="small muted">{t["ex_after"]}</p></div>
<h2 style="margin-top:64px">{t["why_h"]}</h2><div class="rows">{why}</div>
<h2 style="margin-top:64px">{t["mist_h"]}</h2><div class="prose">{mist}</div>
<div class="answer" style="margin-top:56px"><h2 style="font-size:var(--t-1);margin-bottom:.4em">{t["hl_h"]}</h2><p>{t["hl_p"].format(**lk)}</p></div>
</div></section>'''
    return {"key": "kpi", "title": t["kpi_title"], "desc": t["kpi_desc"], "trail": [(t["hub_crumb"], B.url("tools", L)), (t["kpi_crumb"], B.url("kpi", L))],
            "body": body, "faq": t["faq"], "scripts": ["/assets/kpi.js"], "schema": [_app_schema(L, B, "kpi", t, "kpi_crumb")]}


def commission_page(L, B):
    t = T[L]; lk = _links(L, B)
    form = (_currency(L, t) + _field("gross", t["f_gross"], 1200, 0, "any") + _field("rate", t["f_rate"], 18, 0, "any", "%", hint=t["h_rate"], hid="h-rate")
            + _field("fee", t["f_fee"], 1.5, 0, "any", "%") + _field("nights", t["f_nights"], 3, 0, 1))
    res = _res([(t["r_commission"], "com-commission", 0), (t["r_fees"], "com-fees", 0), (t["r_net"], "com-net", 0), (t["r_kept"], "com-kept", 0), (t["r_night"], "com-night", 0)])
    body = f'''<section class="page-hero"><div class="wrap"><h1>{t["com_h1"]}</h1><p class="lead">{t["com_lead"]}</p></div></section>
<section style="padding-top:0"><div class="wrap roi">
<form class="roi-form" id="com-form" data-lang="{L}" novalidate>{form}</form>
<div class="roi-out on-dark" aria-live="polite">{res}<p class="small" style="margin:14px 0 0;color:#D9E1EC">{t["privacy"]}</p></div>
</div></section>
<section class="white rule"><div class="wrap prose">
<h2>{t["c_how_h"]}</h2>{_ul(t["c_how"])}
<h2>{t["c_ex_h"]}</h2><p>{t["c_ex_p"]}</p><p class="small muted">{t["c_note"]}</p>
<h2>{t["c_direct_h"]}</h2><p>{t["c_direct_p"]}</p>
<div class="answer" style="margin-top:40px"><p>{t["c_hl_p"].format(**lk)}</p></div>
<p style="margin-top:24px"><a href="{lk["kpi"]}">{t["kpi_crumb"]}</a> · <a href="{lk["roi"]}">{t["cards"][2][1]}</a></p>
</div></section>'''
    return {"key": "commission", "title": t["com_title"], "desc": t["com_desc"], "trail": [(t["hub_crumb"], B.url("tools", L)), (t["com_crumb"], B.url("commission", L))],
            "body": body, "faq": t["c_faq"], "scripts": ["/assets/kpi.js"], "schema": [_app_schema(L, B, "commission", t, "com_crumb")]}


def hub_page(L, B):
    t = T[L]
    items = "".join(f'<li><a href="{B.url(k, L)}">{html.escape(h)}</a><p>{html.escape(p)}</p></li>' for k, h, p in t["cards"])
    body = f'''<section class="page-hero"><div class="wrap"><h1>{t["hub_h1"]}</h1><p class="lead">{t["hub_lead"]}</p></div></section>
<section style="padding-top:0" class="related"><div class="wrap"><ul class="related-list">{items}</ul><p class="small muted" style="margin-top:16px">{t["hub_note"]}</p></div></section>'''
    return {"key": "tools", "title": t["hub_title"], "desc": t["hub_desc"], "trail": [(t["hub_crumb"], B.url("tools", L))], "body": body, "page_type": "CollectionPage"}


def pages(L, B):
    return [hub_page(L, B), kpi_page(L, B), commission_page(L, B)]
