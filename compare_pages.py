"""Karşılaştırma merkezi, "Hostlio Pro vs X" / "X alternatifi" sayfaları ve genel karşılaştırma sayfası (6 dil).

8 Ekim 2026 (v2, sahibin geri bildirimi): sayfalar Hostlio Pro'yu öne çıkarır. Sıra: neden Hostlio Pro (fayda kartları) →
yan yana tablo (Hostlio sütunu vurgulu, yalnız doğrulanmış rakip bilgisi) → kimin için → geçiş adımları → SSS → kaynak dipnotu.
"X hangi durumda daha uygun" bölümleri ve rakip öneren metinler KALDIRILDI.

DÜRÜSTLÜK KURALI (karşılaştırmalı reklam: 2006/114/EC, Ticari Reklam ve Haksız Ticari Uygulamalar Yönetmeliği):
- Rakip hakkındaki her bilgi rakibin RESMİ sayfasında CHECKED tarihinde doğrulandı; kaynaklar SRC'de ve sayfanın dipnotunda.
  Doğrulanamayan bilgi yazılmaz; "X'te yok" denmez, yalnız "incelediğimiz sayfada belirtilmiyor" gibi doğrulanabilir ifade.
- Tablo yalnız iki tarafı da doğrulanmış satırlardan oluşur. Hostlio'ya özgü özellikler fayda kartlarında anlatılır,
  rakip hakkında iddiaya dönüştürülmez.
- Hostlio tarafı yalnız canlı özellikler (WEB_SITE_DUZELTMELER.md §2–4; §3 reklamı yapılmaz); fiyatlar ⟦token⟧ (pricing.py).
Rakip fiyatı/özelliği değişince SRC tarihini ve ilgili hücreyi birlikte güncelleyin (3 ayda bir; sonraki kontrol Ocak 2027).
"""
import html
import pricing

CHECKED = "2026-10-08"
SRC = {
    "hr_en": ("HotelRunner: Pricing", "https://hotelrunner.com/en/pricing/"),
    "hr_tr": ("HotelRunner: Fiyatlandırma", "https://hotelrunner.com/tr/fiyatlandirma/"),
    "hr_cm": ("HotelRunner: Channel manager", "https://hotelrunner.com/en/products/channel-manager/"),
    "cb_pr": ("Cloudbeds: Pricing", "https://www.cloudbeds.com/pricing/"),
    "cb_home": ("Cloudbeds: Home", "https://www.cloudbeds.com/"),
    "cb_ge": ("Cloudbeds: Guest engagement", "https://www.cloudbeds.com/guest-engagement-software/"),
    "mews_pr": ("Mews: Pricing", "https://www.mews.com/en/pricing"),
    "am_en": ("Amenitiz: Pricing", "https://amenitiz.com/en/pricing"),
    "am_fr": ("Amenitiz : Nos tarifs", "https://amenitiz.com/fr/nos-tarifs"),
    "am_cm": ("Amenitiz: Channel manager", "https://amenitiz.com/en/product/channel-manager"),
    "hj_pr": ("HiJiffy: Plans and pricing", "https://www.hijiffy.com/plans-and-pricing"),
    "hj_home": ("HiJiffy: Home", "https://www.hijiffy.com/"),
    "ew_home": ("Elektraweb: Ana sayfa", "https://elektraweb.com/"),
    "ew_pr": ("Elektraweb: Fiyat listesi (teklif formu)", "https://elektraweb.com/elektraweb-fiyat-listesi/"),
    "ew_cm": ("Elektraweb: Kanal yönetimi", "https://elektraweb.com/kanal-yonetimi"),
    "ew_wa": ("Elektraweb: WhatsApp API", "https://elektraweb.com/whatsapp-api"),
    "ew_chat": ("Elektraweb: Akıllı Sohbet", "https://elektraweb.com/akilli-sohbet"),
    "sv_pr": ("Sirvoy: Pricing", "https://sirvoy.com/pricing"),
    "b24_pr": ("Beds24: Pricing", "https://beds24.com/pricing.html"),
    "ev_pr": ("eviivo: Pricing", "https://eviivo.com/pricing/"),
}

# HotelRunner Essential Sell: aylık gerçekleşen rezervasyon geliri × %1,25, asgari $29,95 (resmi SSS formülü)
def hr_sell_fee(revenue): return max(29.95, revenue * 0.0125)
BREAK_EVEN_PRO = round(pricing.monthly("pro") / 0.0125)          # Pro aylık ücreti = Sell ücreti olduğu gelir
BREAK_EVEN_STARTER = round(pricing.monthly("starter") / 0.0125)
HR_EXAMPLES = [2000, 5000, 10000, 20000]

LANGS6 = ("tr", "en", "es", "it", "pt", "fr")
DATE_TXT = {"tr": "8 Ekim 2026", "en": "October 8, 2026", "es": "8 de octubre de 2026", "it": "8 ottobre 2026",
            "pt": "8 de outubro de 2026", "fr": "8 octobre 2026"}

# ---------------------------------------------------------------- shared UI text (6 dil)
C = {
"tr": dict(asof="Ekim 2026 itibarıyla", src_h="Kaynaklar", src_lead="Rakip bilgileri, {d} tarihinde kontrol edilen resmî sayfalar",
  note="Hostlio Pro bu karşılaştırmada taraftır. Rakip bilgilerini yalnızca firmaların kendi resmî sayfalarından aldık; doğrulayamadığımız bilgiyi yazmadık. Fiyat ve paketler değişebilir. Hata görürseniz <a href=\"{contact}\">bize yazın</a>, düzeltelim.",
  trial="7 gün ücretsiz dene", pricing="Planları gör", more_h="Diğer karşılaştırmalar", hub_link="Tüm karşılaştırmalar", tools="Ücretsiz otel hesaplayıcıları",
  why_h="Oteller neden Hostlio Pro'ya geçiyor?", tbl_h="Hostlio Pro ve {x}: yan yana", fit_h="Hostlio Pro kimin için?", switch_h="{x}'dan Hostlio Pro'ya geçiş: 4 adım",
  switch_gen="Hostlio Pro'ya geçiş: 4 adım", switch_p="Kurulum dakikalar içinde başlar; kanallar çoğu zaman aynı gün bağlanır.",
  trust=["7 gün ücretsiz deneme", "Rezervasyon komisyonu yok", "Fiyatlar sitede açık", "Hızlı kurulum"], feature="Özellik"),
"en": dict(asof="As of October 2026", src_h="Sources", src_lead="Competitor information from official pages checked on {d}",
  note="Hostlio Pro is a party to this comparison. Competitor information comes only from each company's own official pages; anything we couldn't verify is left out. Prices and plans can change. Spotted a mistake? <a href=\"{contact}\">Tell us</a> and we'll fix it.",
  trial="Try it free for 7 days", pricing="See plans", more_h="More comparisons", hub_link="All comparisons", tools="Free hotel calculators",
  why_h="Why hotels switch to Hostlio Pro", tbl_h="Hostlio Pro vs {x} at a glance", fit_h="Who Hostlio Pro is built for", switch_h="Switching from {x} to Hostlio Pro in 4 steps",
  switch_gen="Switching to Hostlio Pro in 4 steps", switch_p="Your account is ready in minutes, and channels are usually connected the same day.",
  trust=["7-day free trial", "No booking commission", "Prices published", "Quick setup"], feature="Feature"),
"es": dict(asof="A octubre de 2026", src_h="Fuentes", src_lead="Información de la competencia de páginas oficiales comprobadas el {d}",
  note="Hostlio Pro es parte interesada en esta comparativa. La información de la competencia procede solo de las páginas oficiales de cada empresa; lo que no pudimos verificar, no lo incluimos. Los precios y planes pueden cambiar. ¿Ves un error? <a href=\"{contact}\">Escríbenos</a> y lo corregimos.",
  trial="Pruébalo gratis 7 días", pricing="Ver planes", more_h="Más comparativas", hub_link="Todas las comparativas", tools="Calculadoras hoteleras gratis",
  why_h="Por qué los hoteles se pasan a Hostlio Pro", tbl_h="Hostlio Pro vs {x}, de un vistazo", fit_h="Para quién está hecho Hostlio Pro", switch_h="Cambiar de {x} a Hostlio Pro en 4 pasos",
  switch_gen="Cambiar a Hostlio Pro en 4 pasos", switch_p="La cuenta está lista en minutos y los canales suelen conectarse el mismo día.",
  trust=["7 días de prueba gratis", "Sin comisión por reserva", "Precios publicados", "Configuración rápida"], feature="Función"),
"it": dict(asof="A ottobre 2026", src_h="Fonti", src_lead="Informazioni sui concorrenti da pagine ufficiali verificate l'{d}",
  note="Hostlio Pro è parte di questo confronto. Le informazioni sui concorrenti provengono solo dalle pagine ufficiali di ciascuna azienda; ciò che non abbiamo potuto verificare non è incluso. Prezzi e piani possono cambiare. Hai notato un errore? <a href=\"{contact}\">Scrivici</a> e lo correggiamo.",
  trial="Prova gratis per 7 giorni", pricing="Vedi i piani", more_h="Altri confronti", hub_link="Tutti i confronti", tools="Calcolatori gratuiti per hotel",
  why_h="Perché gli hotel passano a Hostlio Pro", tbl_h="Hostlio Pro e {x} a confronto", fit_h="Per chi è pensato Hostlio Pro", switch_h="Passare da {x} a Hostlio Pro in 4 passi",
  switch_gen="Passare a Hostlio Pro in 4 passi", switch_p="L'account è pronto in pochi minuti e i canali di solito si collegano in giornata.",
  trust=["Prova gratuita di 7 giorni", "Nessuna commissione sulle prenotazioni", "Prezzi pubblicati", "Configurazione rapida"], feature="Funzione"),
"pt": dict(asof="Em outubro de 2026", src_h="Fontes", src_lead="Informações sobre concorrentes de páginas oficiais verificadas em {d}",
  note="O Hostlio Pro é parte interessada nesta comparação. As informações sobre concorrentes vêm apenas das páginas oficiais de cada empresa; o que não conseguimos confirmar, deixamos de fora. Preços e planos podem mudar. Viu um erro? <a href=\"{contact}\">Fale com a gente</a> e corrigimos.",
  trial="Teste grátis por 7 dias", pricing="Ver planos", more_h="Mais comparativos", hub_link="Todos os comparativos", tools="Calculadoras gratuitas para hotéis",
  why_h="Por que os hotéis mudam para o Hostlio Pro", tbl_h="Hostlio Pro vs {x} lado a lado", fit_h="Para quem o Hostlio Pro foi feito", switch_h="Mudar da {x} para o Hostlio Pro em 4 passos",
  switch_gen="Mudar para o Hostlio Pro em 4 passos", switch_p="A conta fica pronta em minutos e os canais costumam ser conectados no mesmo dia.",
  trust=["Teste grátis de 7 dias", "Sem comissão por reserva", "Preços publicados", "Implantação rápida"], feature="Recurso"),
"fr": dict(asof="En octobre 2026", src_h="Sources", src_lead="Informations sur les concurrents issues de pages officielles vérifiées le {d}",
  note="Hostlio Pro est partie prenante de ce comparatif. Les informations sur les concurrents proviennent uniquement de leurs pages officielles ; ce que nous n’avons pas pu vérifier n’y figure pas. Prix et offres peuvent changer. Vous voyez une erreur ? <a href=\"{contact}\">Écrivez-nous</a>, nous la corrigerons.",
  trial="Essai gratuit de 7 jours", pricing="Voir les forfaits", more_h="Autres comparatifs", hub_link="Tous les comparatifs", tools="Calculateurs gratuits pour hôtels",
  why_h="Pourquoi les hôtels passent à Hostlio Pro", tbl_h="Hostlio Pro et {x} côte à côte", fit_h="Pour qui Hostlio Pro est conçu", switch_h="Passer d’{x} à Hostlio Pro en 4 étapes",
  switch_gen="Passer à Hostlio Pro en 4 étapes", switch_p="Le compte est prêt en quelques minutes et les canaux sont souvent connectés le jour même.",
  trust=["Essai gratuit de 7 jours", "Aucune commission sur les réservations", "Tarifs publics", "Mise en place rapide"], feature="Fonction"),
}

# Neden Hostlio Pro: fayda kartları (yalnız canlı özellikler; plan kısıtları metinde)
BEN = {
"tr": [("currency-circle-dollar", "Sabit aylık ücret, rezervasyon komisyonu yok", "Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ / ay. Hostlio rezervasyon başına ücret ya da gelir yüzdesi almaz; yüksek sezonda faturanız büyümez."),
       ("lock-simple", "Fiyatlar sitede, 7 gün ücretsiz deneme", "Ne ödeyeceğinizi satış görüşmesinden önce görürsünüz. 7 günlük denemede deneme bitene kadar ücret çekilmez; yıllık ödemede %20 indirim."),
       ("chats-circle", "Her planda WhatsApp'ta AI asistan Lio", "Lio misafir sorularını otelinizin bilgileriyle ve misafirin dilinde yanıtlar; indirim, şikâyet gibi kararları size bırakır. Pro ve Growth'ta Booking.com, Airbnb ve Expedia gelen kutuları da Lio'da."),
       ("sparkle", "Lio talep toplar, her sabah öneri getirir", "Pro ve Growth'ta Lio WhatsApp'ta rezervasyon ve ek hizmet talebi toplar; talep sizin onayınızla rezervasyona dönüşür. Lio Önerileri her planda her sabah gelir; onayınız olmadan hiçbir şey değişmez."),
       ("identification-card", "Kimlik taramalı online check-in", "Pro ve Growth'ta misafir gelmeden pasaport ya da kimliğini tarar ve dijital imza atar. Yalnızca okunan bilgiler kaydedilir; belgenin görüntüsü saklanmaz."),
       ("arrows-left-right", "Sertifikalı kanal yöneticisiyle 100+ OTA", "Booking.com, Airbnb, Expedia ve 100'den fazla kanalda müsaitlik ve fiyat tek takvimden güncellenir. Tüm planlarda."),
       ("users-three", "Analiz, ekip rolleri, 6 dilde panel", "Doluluk, ADR, RevPAR ve kanal bazında net gelir. Resepsiyon, kat hizmetleri ve muhasebe için ayrı roller. Panel 6 dilde, mobil uygulama tüm planlarda."),
       ("rocket-launch", "Hızlı kurulum, kolay geçiş", "Kurulum sihirbazı eksik bilgiyi gösterir; mevcut rezervasyonlarınızı CSV ya da Excel'den aktarırsınız. Yayına almadan önce \"Lio'yu dene\" ile kendi sorularınızı sorun.")],
"en": [("currency-circle-dollar", "A fixed monthly price, no booking commission", "Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ a month. Hostlio never takes a per-booking fee or a share of your revenue, so high season doesn't raise your bill."),
       ("lock-simple", "Prices on the website, 7-day free trial", "See what you'll pay before any sales call. No charge until the 7-day trial ends, and 20% off with annual billing."),
       ("chats-circle", "Lio, an AI assistant on WhatsApp in every plan", "Lio answers guests with your hotel's information, in the guest's language, and leaves decisions such as discounts or complaints to you. Pro and Growth bring Booking.com, Airbnb and Expedia inboxes into Lio too."),
       ("sparkle", "Lio takes requests and suggests what to do next", "On Pro and Growth, Lio collects booking and extra-service requests on WhatsApp; they become reservations once you approve. Every plan gets Lio Suggestions each morning, and nothing changes without your approval."),
       ("identification-card", "Online check-in with ID scan", "On Pro and Growth, guests scan their passport or ID and sign digitally before arrival. Only the extracted details are saved, never an image of the document."),
       ("arrows-left-right", "100+ OTAs through a certified channel manager", "Availability and rates for Booking.com, Airbnb, Expedia and 100+ other channels are updated from one calendar, on every plan."),
       ("users-three", "Analytics, staff roles, a panel in 6 languages", "Occupancy, ADR, RevPAR and net revenue per channel. Separate roles for reception, housekeeping and accounting. The panel speaks 6 languages, and the mobile app is on every plan."),
       ("rocket-launch", "Quick setup, easy move", "The setup wizard shows what's missing, and you import existing reservations from CSV or Excel. Ask \"Try Lio\" your own questions before going live.")],
"es": [("currency-circle-dollar", "Cuota mensual fija, sin comisión por reserva", "Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ al mes. Hostlio no cobra por reserva ni un porcentaje de tus ingresos, así que la temporada alta no encarece tu factura."),
       ("lock-simple", "Precios en la web, 7 días de prueba gratis", "Ves lo que pagarás antes de cualquier llamada comercial. Sin cargo hasta que termina la prueba de 7 días y un 20 % de descuento en pago anual."),
       ("chats-circle", "Lio, asistente de IA en WhatsApp en todos los planes", "Lio responde a los huéspedes con la información de tu hotel y en su idioma, y te deja a ti las decisiones como descuentos o quejas. En Pro y Growth también gestiona las bandejas de Booking.com, Airbnb y Expedia."),
       ("sparkle", "Lio recoge solicitudes y te sugiere qué hacer", "En Pro y Growth, Lio recoge solicitudes de reserva y de servicios extra por WhatsApp, que se convierten en reservas cuando las apruebas. Todos los planes reciben Sugerencias de Lio cada mañana; nada cambia sin tu aprobación."),
       ("identification-card", "Check-in online con escaneo del documento", "En Pro y Growth, el huésped escanea su pasaporte o DNI y firma digitalmente antes de llegar. Solo se guardan los datos leídos, nunca una imagen del documento."),
       ("arrows-left-right", "Más de 100 OTAs con un channel manager certificado", "La disponibilidad y las tarifas de Booking.com, Airbnb, Expedia y más de 100 canales se actualizan desde un solo calendario, en todos los planes."),
       ("users-three", "Análisis, roles de equipo y panel en 6 idiomas", "Ocupación, ADR, RevPAR e ingresos netos por canal. Roles separados para recepción, limpieza y contabilidad. El panel está en 6 idiomas (incluido el español) y la app móvil en todos los planes."),
       ("rocket-launch", "Configuración rápida, cambio sencillo", "El asistente de configuración te muestra lo que falta e importas tus reservas desde CSV o Excel. Antes de empezar, haz tus propias preguntas con \"Probar Lio\".")],
"it": [("currency-circle-dollar", "Canone mensile fisso, nessuna commissione sulle prenotazioni", "Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ al mese. Hostlio non applica costi per prenotazione né percentuali sul fatturato: in alta stagione la fattura non cresce."),
       ("lock-simple", "Prezzi sul sito, 7 giorni di prova gratuita", "Sai quanto pagherai prima di qualsiasi chiamata commerciale. Nessun addebito fino alla fine della prova di 7 giorni e 20% di sconto con il pagamento annuale."),
       ("chats-circle", "Lio, assistente AI su WhatsApp in tutti i piani", "Lio risponde agli ospiti con le informazioni del tuo hotel e nella loro lingua, e lascia a te le decisioni come sconti o reclami. Con Pro e Growth gestisce anche le caselle di Booking.com, Airbnb ed Expedia."),
       ("sparkle", "Lio raccoglie richieste e ti suggerisce cosa fare", "Con Pro e Growth, Lio raccoglie su WhatsApp richieste di prenotazione e di servizi extra, che diventano prenotazioni quando le approvi. In tutti i piani arrivano ogni mattina i Suggerimenti di Lio; nulla cambia senza la tua approvazione."),
       ("identification-card", "Check-in online con scansione del documento", "Con Pro e Growth, l'ospite scansiona passaporto o carta d'identità e firma digitalmente prima dell'arrivo. Vengono salvati solo i dati letti, mai un'immagine del documento."),
       ("arrows-left-right", "Oltre 100 OTA con un channel manager certificato", "Disponibilità e tariffe su Booking.com, Airbnb, Expedia e oltre 100 canali si aggiornano da un unico calendario, in tutti i piani."),
       ("users-three", "Analisi, ruoli per lo staff, pannello in 6 lingue", "Occupazione, ADR, RevPAR e ricavo netto per canale. Ruoli separati per reception, housekeeping e contabilità. Il pannello è in 6 lingue (italiano incluso) e l'app mobile è in tutti i piani."),
       ("rocket-launch", "Configurazione rapida, passaggio semplice", "La procedura guidata mostra cosa manca e importi le prenotazioni esistenti da CSV o Excel. Prima di partire, fai le tue domande a Lio con \"Prova Lio\".")],
"pt": [("currency-circle-dollar", "Mensalidade fixa, sem comissão por reserva", "Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ por mês. O Hostlio não cobra por reserva nem percentual da receita, então a alta temporada não aumenta sua fatura."),
       ("lock-simple", "Preços no site, 7 dias de teste grátis", "Você vê quanto vai pagar antes de qualquer ligação de vendas. Sem cobrança até o fim do teste de 7 dias e 20% de desconto no plano anual."),
       ("chats-circle", "Lio, assistente de IA no WhatsApp em todos os planos", "O Lio responde aos hóspedes com as informações do seu hotel, no idioma de cada um, e deixa com você decisões como descontos ou reclamações. No Pro e no Growth, as caixas de entrada do Booking.com, Airbnb e Expedia também ficam com o Lio."),
       ("sparkle", "O Lio recebe pedidos e sugere o próximo passo", "No Pro e no Growth, o Lio recebe pedidos de reserva e de serviços extras no WhatsApp, que viram reservas quando você aprova. Todos os planos recebem as Sugestões do Lio toda manhã; nada muda sem a sua aprovação."),
       ("identification-card", "Check-in online com leitura do documento", "No Pro e no Growth, o hóspede lê o passaporte ou documento de identidade e assina digitalmente antes de chegar. Só os dados lidos são salvos, nunca a imagem do documento."),
       ("arrows-left-right", "Mais de 100 OTAs com channel manager certificado", "Disponibilidade e tarifas no Booking.com, Airbnb, Expedia e em mais de 100 canais são atualizadas a partir de um único calendário, em todos os planos."),
       ("users-three", "Análises, perfis de equipe e painel em 6 idiomas", "Ocupação, ADR, RevPAR e receita líquida por canal. Perfis separados para recepção, governança e financeiro. O painel está em 6 idiomas (inclui português) e o app móvel em todos os planos."),
       ("rocket-launch", "Implantação rápida, migração simples", "O assistente de configuração mostra o que falta e você importa as reservas de um arquivo CSV ou Excel. Antes de começar, faça suas próprias perguntas em \"Testar o Lio\".")],
"fr": [("currency-circle-dollar", "Un abonnement mensuel fixe, sans commission", "Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ par mois. Hostlio ne prend ni frais par réservation ni pourcentage du chiffre d’affaires : la haute saison n’alourdit pas votre facture."),
       ("lock-simple", "Tarifs publics, essai gratuit de 7 jours", "Vous savez ce que vous paierez avant tout appel commercial. Aucun prélèvement avant la fin de l’essai de 7 jours, et −20 % en paiement annuel."),
       ("chats-circle", "Lio, assistant IA sur WhatsApp dans tous les forfaits", "Lio répond aux clients avec les informations de votre hôtel, dans leur langue, et vous laisse les décisions comme les remises ou les réclamations. En Pro et Growth, il gère aussi les messageries Booking.com, Airbnb et Expedia."),
       ("sparkle", "Lio recueille les demandes et vous fait des suggestions", "En Pro et Growth, Lio recueille sur WhatsApp les demandes de réservation et de services additionnels, qui deviennent des réservations une fois validées par vous. Tous les forfaits reçoivent chaque matin les Suggestions de Lio ; rien ne change sans votre accord."),
       ("identification-card", "Check-in en ligne avec lecture de la pièce d’identité", "En Pro et Growth, le client scanne son passeport ou sa carte d’identité et signe numériquement avant son arrivée. Seules les données lues sont enregistrées, jamais l’image du document."),
       ("arrows-left-right", "Plus de 100 OTA via un channel manager certifié", "Disponibilités et tarifs sur Booking.com, Airbnb, Expedia et plus de 100 canaux sont mis à jour depuis un seul calendrier, dans tous les forfaits."),
       ("users-three", "Analyses, rôles d’équipe, tableau de bord en 6 langues", "Taux d’occupation, ADR, RevPAR et revenu net par canal. Des rôles distincts pour la réception, les étages et la comptabilité. Le tableau de bord parle 6 langues (dont le français) et l’application mobile est incluse dans tous les forfaits."),
       ("rocket-launch", "Mise en place rapide, changement simple", "L’assistant de configuration signale ce qui manque et vous importez vos réservations depuis un fichier CSV ou Excel. Avant de démarrer, posez vos propres questions avec « Essayer Lio ».")],
}

# Kimin için (dürüst kapsam; rakip önermez)
FIT = {
"tr": "Hostlio Pro; bağımsız ve butik oteller, pansiyonlar, apart oteller ve hosteller için, 1–150 oda ve en fazla 2 tesis (Growth) düşünülerek yapıldı. Odak noktası günü yöneten üç şey: PMS, kanal yöneticisi ve AI misafir mesajlaşması. Rezervasyon motoru, web sitesi kurucu ve ödeme tahsilatı Hostlio Pro'nun parçası değildir. Panel 6 dilde, destek Türkçe ve İngilizce.",
"en": "Hostlio Pro is built for independent and boutique hotels, guesthouses, aparthotels and hostels with 1–150 rooms and up to 2 properties (Growth). It focuses on the three things that run the day: PMS, channel manager and AI guest messaging. A booking engine, website builder and payment collection are not part of Hostlio Pro. The panel is in 6 languages; support is in English and Turkish.",
"es": "Hostlio Pro está hecho para hoteles independientes y boutique, hostales, apartahoteles y hostels de 1 a 150 habitaciones y hasta 2 alojamientos (Growth). Se centra en lo que mueve el día a día: PMS, channel manager y mensajería con huéspedes con IA. El motor de reservas, el creador de webs y el cobro de pagos no forman parte de Hostlio Pro. El panel está en 6 idiomas; el soporte, en inglés y turco.",
"it": "Hostlio Pro è pensato per hotel indipendenti e boutique, B&B, residence e ostelli da 1 a 150 camere e fino a 2 strutture (Growth). Si concentra su ciò che fa girare la giornata: PMS, channel manager e messaggi agli ospiti con l'AI. Motore di prenotazione, creazione del sito e incasso dei pagamenti non fanno parte di Hostlio Pro. Il pannello è in 6 lingue; l'assistenza è in inglese e turco.",
"pt": "O Hostlio Pro foi feito para hotéis independentes e boutique, pousadas, apart-hotéis e hostels de 1 a 150 quartos e até 2 propriedades (Growth). O foco está no que move o dia a dia: PMS, channel manager e mensagens com hóspedes por IA. Motor de reservas, criador de sites e processamento de pagamentos não fazem parte do Hostlio Pro. O painel está em 6 idiomas; o suporte, em inglês e turco.",
"fr": "Hostlio Pro est conçu pour les hôtels indépendants et boutique, chambres d’hôtes, résidences hôtelières et auberges de 1 à 150 chambres, jusqu’à 2 établissements (Growth). Il se concentre sur ce qui fait tourner la journée : PMS, channel manager et messagerie client par IA. Moteur de réservation, création de site et encaissement des paiements ne font pas partie de Hostlio Pro. Le tableau de bord est en 6 langues ; le support est en anglais et en turc.",
}

# Geçiş adımları; {x} = rakip adı ya da "mevcut programınız"
SWITCH = {
"tr": [("Denemeyi başlatın", "Hesabınızı açın, oda tiplerinizi ve fiyatlarınızı girin; kurulum sihirbazı eksikleri gösterir."),
       ("Rezervasyonları aktarın", "{frm} rezervasyonlarınızı CSV ya da Excel olarak dışa aktarıp içeri alın: sütun eşleme, tarih biçimi seçimi ve mükerrer kontrolü dahil."),
       ("Kanalları bağlayın", "OTA'larınızı sertifikalı kanal yöneticisine bağlayın. Müsaitliğin tek sistemden gitmesi için geçiş saatini önceden belirleyin."),
       ("Lio'yu hazırlayın", "Otel bilgilerinizi doldurun ve \"Lio'yu dene\" ile birkaç misafir sorusu sorun.")],
"en": [("Start your trial", "Create your account and add room types and rates; the setup wizard shows what's missing."),
       ("Import your reservations", "Export your reservations {frm} as CSV or Excel and import them, with column mapping, date-format choice and duplicate checks."),
       ("Connect your channels", "Connect your OTAs through the certified channel manager. Pick a cut-over time so availability is sent from one system only."),
       ("Get Lio ready", "Fill in your hotel information and ask a few guest questions with \"Try Lio\".")],
"es": [("Empieza la prueba", "Crea tu cuenta y añade tipos de habitación y tarifas; el asistente de configuración te muestra lo que falta."),
       ("Importa tus reservas", "Exporta tus reservas {frm} en CSV o Excel e impórtalas, con asignación de columnas, formato de fecha y control de duplicados."),
       ("Conecta tus canales", "Conecta tus OTAs mediante el channel manager certificado. Elige el momento del cambio para que la disponibilidad salga de un solo sistema."),
       ("Prepara a Lio", "Completa la información de tu hotel y haz algunas preguntas de huésped con \"Probar Lio\".")],
"it": [("Avvia la prova", "Crea l'account e inserisci tipologie di camera e tariffe; la procedura guidata mostra cosa manca."),
       ("Importa le prenotazioni", "Esporta le prenotazioni {frm} in CSV o Excel e importale, con mappatura delle colonne, formato data e controllo dei duplicati."),
       ("Collega i canali", "Collega le OTA tramite il channel manager certificato. Scegli il momento del passaggio, così la disponibilità parte da un solo sistema."),
       ("Prepara Lio", "Compila le informazioni dell'hotel e fai qualche domanda da ospite con \"Prova Lio\".")],
"pt": [("Comece o teste", "Crie sua conta e cadastre tipos de quarto e tarifas; o assistente de configuração mostra o que falta."),
       ("Importe suas reservas", "Exporte suas reservas {frm} em CSV ou Excel e importe, com mapeamento de colunas, formato de data e controle de duplicados."),
       ("Conecte seus canais", "Conecte suas OTAs pelo channel manager certificado. Defina o horário da troca para que a disponibilidade saia de um só sistema."),
       ("Prepare o Lio", "Preencha as informações do hotel e faça algumas perguntas de hóspede em \"Testar o Lio\".")],
"fr": [("Lancez l’essai", "Créez votre compte et saisissez types de chambres et tarifs ; l’assistant de configuration signale ce qui manque."),
       ("Importez vos réservations", "Exportez vos réservations {frm} en CSV ou Excel et importez-les, avec correspondance des colonnes, format de date et contrôle des doublons."),
       ("Connectez vos canaux", "Connectez vos OTA via le channel manager certifié. Choisissez l’heure de bascule pour que les disponibilités partent d’un seul système."),
       ("Préparez Lio", "Renseignez les informations de l’hôtel et posez quelques questions de client avec « Essayer Lio ».")],
}
# step 2 "nereden" ifadesi (sayfa verisinde "frm" yoksa bu)
FRM = {"tr": "Mevcut programınızdaki", "en": "from your current software", "es": "de tu programa actual", "it": "dal tuo gestionale attuale",
       "pt": "do seu sistema atual", "fr": "depuis votre logiciel actuel"}

def _usd(n, lang):
    """HotelRunner örnekleri USD; 2 ondalık gerekiyorsa yaz."""
    s = f"{n:,.2f}" if not float(n).is_integer() else f"{int(n):,}"
    if lang == "en": return "$" + s
    if lang == "fr": return s.replace(",", " ").replace(".", ",") + " $"
    s = s.replace(",", "X").replace(".", ",").replace("X", ".")
    return ("$" + s) if lang in ("tr", "pt") else (s + " $")

# ---------------------------------------------------------------- page content
# rows: (satır, Hostlio Pro hücresi, rakip hücresi) — yalnız iki tarafı da doğrulanmış satırlar
P = {}

P["vs-hotelrunner"] = {
"tr": dict(
  card="Hostlio Pro ile HotelRunner: sabit aylık ücret mi, gelir yüzdesi mi?",
  title="Hostlio Pro vs HotelRunner (2026): Fiyat, AI | Hostlio Pro",
  desc="HotelRunner alternatifi mi arıyorsunuz? Hostlio Pro: sabit aylık ücret, rezervasyon komisyonu yok, her planda WhatsApp'ta AI asistan. Kaynaklı, tarihli.",
  crumb="Hostlio Pro vs HotelRunner", h1='Hostlio Pro vs <em class="hl">HotelRunner</em>',
  lead="Geliriniz arttıkça yazılım faturanız da artmasın. Hostlio Pro sabit aylık ücretle çalışır, rezervasyon gelirinizden pay almaz ve her planda misafirlerinize WhatsApp'tan cevap veren bir AI asistanla gelir.",
  name="HotelRunner", frm="HotelRunner'daki",
  rows=[("Fiyat modeli", "Sabit aylık ücret: Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ (USD, erken kayıt)", "Essential planlar: tüm kanallardan gerçekleşen aylık rezervasyon gelirinin %0,75–%1,25'i, asgari aylık $19,95–$39,95. Advanced ve Elite: satış ekibiyle görüşme"),
        ("Gelirden pay / rezervasyon başı ücret", "Yok", "Essential planlarda gelir yüzdesi (yukarıda)"),
        ("AI misafir mesajlaşması", "Tüm planlarda Lio; Pro ve Growth'ta Booking.com, Airbnb ve Expedia gelen kutuları da", "Konuşma yöneticisi, AI asistan ve AI çeviri, Advanced planlardaki Misafir İlişkileri Yönetimi'nde listeleniyor (fiyat satış ekibinden)"),
        ("WhatsApp ile misafir mesajlaşması", "Tüm planlarda (Lio)", "İncelediğimiz fiyat ve ürün sayfalarında belirtilmiyor"),
        ("Kanal yöneticisi", "Tüm planlarda, 100+ OTA'ya sertifikalı bağlantı", "Sell ve Complete planlarında; \"150+ kanal\""),
        ("Ücretsiz deneme", "7 gün; deneme bitene kadar ücret çekilmez", "\"Ücretsiz deneyin\" seçeneği var; süresi fiyat sayfasında belirtilmiyor")],
  srcs=["hr_tr", "hr_en", "hr_cm"],
  calc_h="Sabit ücret ile gelir yüzdesi: örnek hesap",
  calc_p="HotelRunner'ın SSS'sinde yayınlanan formüle göre Essential Sell planında aylık ücret, tüm kanallardan gerçekleşen rezervasyon gelirinin %1,25'idir; bu tutar $29,95'in altında kalırsa asgari ücret ödenir. Hostlio Pro planı ise geliriniz ne olursa olsun sabittir. Rakamlar bizim hesabımızdır; OTA komisyonları ve vergiler hariçtir, iki ürünün kapsamı da birebir aynı değildir.",
  calc_after=f"Bu formüle göre aylık rezervasyon geliri yaklaşık {_usd(BREAK_EVEN_PRO, 'tr')}'ı geçtiğinde Hostlio Pro planı, Essential Sell'den daha az tutar; gelir arttıkça fark büyür. Bu eşiğin altında Essential Sell daha düşüktür. Starter için eşik yaklaşık {_usd(BREAK_EVEN_STARTER, 'tr')}'dır.",
  faq=[("HotelRunner'dan Hostlio Pro'ya geçebilir miyim?", "Evet. Rezervasyonlarınızı HotelRunner'dan CSV ya da Excel olarak dışa aktarıp Hostlio Pro'ya içe aktarırsınız; sütun eşleme, tarih biçimi seçimi ve mükerrer kayıt kontrolü vardır. Kanallarınızı Hostlio Pro'nun sertifikalı kanal yöneticisine bağlarken müsaitliğin tek sistemden gitmesi için geçiş saatini önceden planlayın. Rezervasyon motoru ya da online ödeme tahsilatı kullanıyorsanız, bunların Hostlio Pro'da bulunmadığını hesaba katın."),
       ("Hostlio Pro komisyon alıyor mu?", "Hayır. Hostlio Pro sabit aylık ücretlidir; rezervasyon başına ücret ya da gelir yüzdesi almaz. OTA'ların kendi komisyonları her durumda ayrıca geçerlidir."),
       ("HotelRunner komisyonlu mu çalışıyor?", "HotelRunner'ın fiyatlandırma sayfasına göre Essential planlarda aylık ücret, tüm kanallardan gerçekleşen rezervasyon gelirinin bir yüzdesidir (%0,75–%1,25) ve her planın asgari aylık tutarı vardır ($19,95–$39,95). Advanced ve Elite planlarının fiyatı satış ekibinden alınır (8 Ekim 2026)."),
       ("Hangisi daha ekonomik?", f"Gelirinize bağlı. HotelRunner'ın yayınladığı formüle göre Essential Sell ücreti, aylık rezervasyon geliri yaklaşık {_usd(BREAK_EVEN_PRO, 'tr')} olduğunda Hostlio Pro planının aylık ücretine (⟦price:pro⟧) eşit olur. Bunun üzerinde Hostlio Pro daha az tutar, altında Essential Sell daha düşüktür. Hostlio Pro'da AI asistan Lio her planda dahildir.")]),
"en": dict(
  card="Hostlio Pro vs HotelRunner: flat monthly fee or a share of revenue?",
  title="Hostlio Pro vs HotelRunner (2026): Pricing, AI | Hostlio Pro",
  desc="Looking for a HotelRunner alternative? Hostlio Pro: a flat monthly fee, no booking commission and an AI assistant on WhatsApp in every plan. Sourced and dated.",
  crumb="Hostlio Pro vs HotelRunner", h1='Hostlio Pro vs <em class="hl">HotelRunner</em>',
  lead="Your software bill shouldn't grow with your revenue. Hostlio Pro is a flat monthly fee, takes no share of your bookings and comes with an AI assistant that answers guests on WhatsApp in every plan.",
  name="HotelRunner", frm="from HotelRunner",
  rows=[("Pricing model", "Flat monthly fee: Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ (USD, early bird)", "Essential plans: 0.75%–1.25% of monthly realized booking revenue from all channels, with a $19.95–$39.95 monthly minimum. Advanced and Elite: talk to sales"),
        ("Revenue share / per-booking fee", "None", "Revenue percentage on Essential plans (above)"),
        ("AI guest messaging", "Lio on every plan; Booking.com, Airbnb and Expedia inboxes too on Pro and Growth", "Conversation manager, AI assistant and AI translation are listed under Guest Relationship Management in the Advanced plans (priced by sales)"),
        ("WhatsApp guest messaging", "Every plan (Lio)", "Not stated on the pricing and product pages we checked"),
        ("Channel manager", "Every plan, certified connections to 100+ OTAs", "On Sell and Complete; \"150+ channels\""),
        ("Free trial", "7 days; no charge until the trial ends", "\"Start free trial\" offered; length not stated on the pricing page")],
  srcs=["hr_en", "hr_tr", "hr_cm"],
  calc_h="Flat fee vs revenue share: a worked example",
  calc_p="Under the formula in HotelRunner's pricing FAQ, the Essential Sell fee is 1.25% of monthly realized booking revenue from all channels, with $29.95 as the minimum. Hostlio Pro's plan price stays the same whatever your revenue. The numbers are our own calculation; they exclude OTA commissions and taxes, and the two products don't cover exactly the same features.",
  calc_after=f"By this formula, once monthly booking revenue passes roughly {_usd(BREAK_EVEN_PRO, 'en')}, Hostlio Pro costs less than Essential Sell, and the gap widens as revenue grows. Below that, Essential Sell is lower. For Starter the threshold is about {_usd(BREAK_EVEN_STARTER, 'en')}.",
  faq=[("Can I switch from HotelRunner to Hostlio Pro?", "Yes. Export your reservations from HotelRunner as a CSV or Excel file and import them into Hostlio Pro, with column mapping, date-format choice and duplicate checks. When you connect your channels to Hostlio Pro's certified channel manager, plan the cut-over so availability is sent from one system only. If you use a booking engine or online payment collection today, note that Hostlio Pro doesn't include them."),
       ("Does Hostlio Pro charge a commission?", "No. Hostlio Pro is a flat monthly fee with no per-booking fee or revenue percentage. OTAs charge their own commission either way."),
       ("Is HotelRunner commission-based?", "According to HotelRunner's pricing page, Essential plans charge a percentage (0.75%–1.25%) of monthly realized booking revenue from all channels, and each plan has a monthly minimum ($19.95–$39.95). Advanced and Elite plans are priced by the sales team (October 8, 2026)."),
       ("Which one costs less?", f"It depends on your revenue. By HotelRunner's published formula, the Essential Sell fee equals Hostlio Pro's monthly price (⟦price:pro⟧) at about {_usd(BREAK_EVEN_PRO, 'en')} of monthly booking revenue. Above that, Hostlio Pro costs less; below it, Essential Sell is lower. Hostlio Pro includes the Lio AI assistant on every plan.")]),
}

# Elektraweb: tüm bilgiler 8 Ekim 2026'da elektraweb.com resmî sayfalarından (ham HTML) doğrulandı; bkz. scratchpad/site_karsi2.md
P["vs-elektraweb"] = {
"tr": dict(
  card="Hostlio Pro ile Elektraweb: açık fiyat, her planda WhatsApp'ta AI",
  title="Hostlio Pro vs Elektraweb (2026): Fiyat, AI | Hostlio Pro",
  desc="Elektraweb alternatifi mi arıyorsunuz? Hostlio Pro: fiyatlar sitede açık, sabit aylık ücret, her planda WhatsApp'ta AI asistan ve 7 gün ücretsiz deneme.",
  crumb="Hostlio Pro vs Elektraweb", h1='Hostlio Pro vs <em class="hl">Elektraweb</em>',
  lead="Fiyatı teklif beklemeden görün, bugün deneyin. Hostlio Pro'nun planları sitede açık, ücreti sabit; WhatsApp'ta misafirlere cevap veren AI asistan Lio her planda dahil. 1–150 odalı bağımsız oteller ve pansiyonlar için.",
  name="Elektraweb", frm="Elektraweb'deki", switch_h="Elektraweb'den Hostlio Pro'ya geçiş: 4 adım",
  rows=[("Fiyat", "Sitede açık: Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ / ay (USD, erken kayıt); yıllıkta %20 indirim", "Fiyat listesi sayfası teklif formuna yönlendiriyor (\"Fiyat teklifi almak için tıklayınız\"); yayınlanmış rakam yok"),
        ("Deneme", "7 gün ücretsiz; deneme bitene kadar ücret çekilmez", "Ücretsiz demo talep formu; deneme süresi belirtilmiyor"),
        ("WhatsApp'ta AI misafir mesajlaşması", "Tüm planlarda dahil (Lio); Pro ve Growth'ta Booking.com, Airbnb ve Expedia gelen kutuları da", "WhatsApp API ve Akıllı Sohbet ürün sayfalarında AI destekli asistan anlatılıyor; ürün menüsünde ayrı başlıklar, fiyat teklifle"),
        ("Kanal yöneticisi", "Tüm planlarda, 100+ OTA'ya sertifikalı bağlantı", "Dahili kanal yöneticisi modülü; \"Booking, Expedia, Hotels.com gibi bilinen tüm kanallarla bağlantısı hazır\""),
        ("Çalışma şekli", "Bulutta; panel 6 dilde, mobil uygulama tüm planlarda", "Web tabanlı, bulutta çalışan; tablet ve telefonda kullanılabiliyor"),
        ("Odak", "PMS, kanal yöneticisi ve AI misafir asistanı tek pakette; 1–150 oda", "Ön büro, rezervasyon motoru, kanal yönetimi, POS, muhasebe, stok, bordro gibi modüller; \"her büyüklük ve konseptteki turizm tesisi için\"")],
  srcs=["ew_pr", "ew_home", "ew_cm", "ew_wa", "ew_chat"],
  faq=[("Elektraweb'den Hostlio'ya geçebilir miyim?", "Evet. Rezervasyonlarınızı Elektraweb'den CSV ya da Excel olarak dışa aktarıp Hostlio Pro'ya içe aktarırsınız; sütun eşleme, tarih biçimi seçimi ve mükerrer kayıt kontrolü vardır. Kanallarınızı Hostlio Pro'nun sertifikalı kanal yöneticisine bağlarken müsaitliğin tek sistemden gitmesi için geçiş saatini önceden planlayın. Hostlio Pro PMS, kanal yöneticisi ve AI misafir mesajlaşmasına odaklanır; POS, muhasebe, bordro, rezervasyon motoru ve ödeme tahsilatı içermez. Bu modülleri kullanıyorsanız geçişi buna göre planlayın."),
       ("Elektraweb'in fiyatı ne kadar?", "Elektraweb sitesinde fiyat yayınlamıyor; fiyat listesi sayfası teklif formuna yönlendiriyor (8 Ekim 2026). Hostlio Pro'nun planları fiyatlandırma sayfasında açık: Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ / ay."),
       ("Hostlio Pro'da WhatsApp AI asistanı hangi planda?", "Hepsinde. Lio, Starter dahil her planda misafirlere WhatsApp'tan otelinizin bilgileriyle ve misafirin dilinde cevap verir; indirim, şikâyet gibi kararları size bırakır. Pro ve Growth'ta OTA gelen kutuları ve sizin onayınızla rezervasyona dönüşen talepler de vardır."),
       ("Kurulum ne kadar sürer?", "Hesap dakikalar içinde hazır olur; kurulum sihirbazı eksik bilgileri gösterir ve kanallar çoğu zaman aynı gün bağlanır. 7 günlük denemeyle kendi odalarınız ve fiyatlarınızla başlayabilirsiniz.")]),
"en": dict(
  card="Hostlio Pro vs Elektraweb: published pricing, AI on WhatsApp in every plan",
  title="Hostlio Pro vs Elektraweb (2026): Pricing, AI | Hostlio Pro",
  desc="Looking for an Elektraweb alternative? Hostlio Pro: published flat monthly pricing, an AI assistant on WhatsApp in every plan and a 7-day free trial.",
  crumb="Hostlio Pro vs Elektraweb", h1='Hostlio Pro vs <em class="hl">Elektraweb</em>',
  lead="See the price without waiting for a quote, and try it today. Hostlio Pro lists its plans on its website at a fixed monthly fee, and Lio, an AI assistant that answers guests on WhatsApp, is included in every plan. Built for independent hotels and guesthouses of 1–150 rooms.",
  name="Elektraweb", frm="from Elektraweb",
  rows=[("Pricing", "Published: Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ a month (USD, early bird); 20% off annually", "The price-list page leads to a quote form (\"Fiyat teklifi almak için tıklayınız\", click to get a quote); no published figures"),
        ("Trial", "7 days free; no charge until the trial ends", "Free demo request form; no trial length stated"),
        ("AI guest messaging on WhatsApp", "Included in every plan (Lio); Booking.com, Airbnb and Expedia inboxes too on Pro and Growth", "The WhatsApp API and Smart Chat (Akıllı Sohbet) product pages describe an AI-assisted assistant; listed as separate items in the product menu, priced by quote"),
        ("Channel manager", "Every plan, certified connections to 100+ OTAs", "Built-in channel manager module; ready connections to \"all well-known channels such as Booking, Expedia, Hotels.com\""),
        ("Deployment", "Cloud; panel in 6 languages, mobile app on every plan", "Web-based, cloud-hosted; usable on tablets and phones"),
        ("Focus", "PMS, channel manager and AI guest assistant in one package; 1–150 rooms", "Modules including front office, booking engine, channel manager, POS, accounting, inventory and payroll; \"for tourism properties of every size and concept\"")],
  srcs=["ew_pr", "ew_home", "ew_cm", "ew_wa", "ew_chat"],
  faq=[("Can I switch from Elektraweb to Hostlio Pro?", "Yes. Export your reservations from Elektraweb as a CSV or Excel file and import them into Hostlio Pro, with column mapping, date-format choice and duplicate checks. When you connect your channels to Hostlio Pro's certified channel manager, plan the cut-over so availability is sent from one system only. Hostlio Pro focuses on PMS, channel manager and AI guest messaging; it doesn't include POS, accounting, payroll, a booking engine or payment collection, so plan the move around any of those modules you use."),
       ("How much does Elektraweb cost?", "Elektraweb doesn't publish prices on its website; its price-list page leads to a quote form (October 8, 2026). Hostlio Pro's plans are on its pricing page: Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ a month."),
       ("Which Hostlio Pro plan includes the WhatsApp AI assistant?", "All of them. From Starter up, Lio answers guests on WhatsApp with your hotel's information and in the guest's language, and leaves decisions such as discounts or complaints to you. Pro and Growth add OTA inboxes and booking requests that become reservations once you approve them."),
       ("How long does setup take?", "Your account is ready in minutes; the setup wizard shows what's missing and channels are usually connected the same day. Start with the 7-day trial using your own rooms and rates.")]),
}

P["vs-cloudbeds"] = {
"en": dict(
  card="Hostlio Pro vs Cloudbeds: published price vs quote, AI messaging",
  title="Hostlio Pro vs Cloudbeds (2026): Pricing, AI, Fit | Hostlio Pro",
  desc="Hostlio Pro vs Cloudbeds: published flat pricing instead of a quote, AI guest messaging on WhatsApp in every plan, 7-day trial. Sourced and dated.",
  crumb="Hostlio Pro vs Cloudbeds", h1='Hostlio Pro vs <em class="hl">Cloudbeds</em>',
  lead="See the price before the sales call. Hostlio Pro publishes its plans, includes an AI assistant on WhatsApp in every one of them and lets you start a 7-day trial today. It's built for independent properties of 1–150 rooms.",
  name="Cloudbeds", frm="from Cloudbeds",
  rows=[("Pricing", "Published: Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ a month (USD, early bird)", "Quote-based: Flex, One, Experience and Enterprise plans all show \"Request a quote\""),
        ("Booking commission", "None, flat monthly fee", "States no added commission on reservations made through its Booking Engine or Channel Manager; metasearch commissions apply after the stay"),
        ("AI guest messaging and WhatsApp", "Every plan (Lio on WhatsApp); OTA inboxes on Pro and Growth", "AI chatbot and a unified inbox covering WhatsApp, SMS, email and OTA messages; on the pricing page, Guest Experience is listed in the Experience plan"),
        ("Channel manager", "Every plan, certified connections to 100+ OTAs", "In the One plan and above"),
        ("Free trial", "7 days; no charge until the trial ends", "Not mentioned on the pricing page; demo offered")],
  srcs=["cb_pr", "cb_home", "cb_ge"],
  faq=[("Can I switch from Cloudbeds to Hostlio Pro?", "Yes. Export your reservations from Cloudbeds and import them into Hostlio Pro as a CSV or Excel file, with column mapping and duplicate checks. Connect your OTAs to Hostlio Pro's certified channel manager and plan the cut-over so availability is sent from one system only. Hostlio Pro covers the PMS, channel manager and guest messaging; it doesn't include a booking engine or payment processing."),
       ("How much does Cloudbeds cost?", "Cloudbeds doesn't publish prices. Its pricing page lists four plans (Flex, One, Experience, Enterprise), each with \"Request a quote\" (October 8, 2026). Hostlio Pro's plans are on its pricing page, from ⟦price:starter⟧ a month."),
       ("Does Hostlio Pro include WhatsApp in every plan?", "Yes. Lio answers guests on WhatsApp from the Starter plan up. Pro and Growth add Booking.com, Airbnb and Expedia inboxes, and booking requests that you approve."),
       ("How long does switching take?", "Your account is ready in minutes and channels are usually connected the same day. Reservations can be imported from a CSV or Excel file.")]),
"es": dict(
  card="Hostlio Pro vs Cloudbeds: precio publicado o presupuesto, IA incluida",
  title="Hostlio Pro vs Cloudbeds (2026): precios e IA | Hostlio Pro",
  desc="Hostlio Pro frente a Cloudbeds: precio fijo publicado en lugar de presupuesto, IA en WhatsApp en todos los planes y 7 días de prueba. Con fuentes y fecha.",
  crumb="Hostlio Pro vs Cloudbeds", h1='Hostlio Pro vs <em class="hl">Cloudbeds</em>',
  lead="Conoce el precio antes de la llamada comercial. Hostlio Pro publica sus planes, incluye un asistente de IA en WhatsApp en todos ellos y puedes empezar hoy una prueba de 7 días. Está pensado para alojamientos independientes de 1 a 150 habitaciones.",
  name="Cloudbeds", frm="de Cloudbeds",
  rows=[("Precio", "Publicado: Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ al mes (USD, precio de lanzamiento)", "Con presupuesto: los planes Flex, One, Experience y Enterprise muestran \"Request a quote\""),
        ("Comisión por reserva", "Ninguna, cuota mensual fija", "Indica que no cobra comisión añadida por las reservas de su Booking Engine o Channel Manager; en metabuscadores cobra comisión tras la estancia"),
        ("Mensajería con IA y WhatsApp", "Todos los planes (Lio en WhatsApp); bandejas de OTAs en Pro y Growth", "Chatbot con IA y bandeja unificada con WhatsApp, SMS, email y mensajes de OTAs; en la página de precios, Guest Experience figura en el plan Experience"),
        ("Channel manager", "Todos los planes, conexiones certificadas con más de 100 OTAs", "En el plan One y superiores"),
        ("Prueba gratis", "7 días; sin cargo hasta que termina la prueba", "No se menciona en la página de precios; ofrece demo")],
  srcs=["cb_pr", "cb_home", "cb_ge"],
  faq=[("¿Puedo pasarme de Cloudbeds a Hostlio Pro?", "Sí. Exporta tus reservas de Cloudbeds e impórtalas en Hostlio Pro en CSV o Excel, con asignación de columnas y control de duplicados. Conecta tus OTAs al channel manager certificado de Hostlio Pro y planifica el cambio para que la disponibilidad salga de un solo sistema. Hostlio Pro cubre PMS, channel manager y mensajería con huéspedes; no incluye motor de reservas ni cobro de pagos."),
       ("¿Cuánto cuesta Cloudbeds?", "Cloudbeds no publica precios. Su página de precios muestra cuatro planes (Flex, One, Experience, Enterprise), todos con \"Request a quote\" (8 de octubre de 2026). Los planes de Hostlio Pro están en su página de precios, desde ⟦price:starter⟧ al mes."),
       ("¿Hostlio Pro incluye WhatsApp en todos los planes?", "Sí. Lio responde a los huéspedes por WhatsApp desde el plan Starter. Pro y Growth añaden las bandejas de Booking.com, Airbnb y Expedia y solicitudes de reserva que tú apruebas."),
       ("¿Cuánto tarda el cambio?", "La cuenta está lista en minutos y los canales suelen conectarse el mismo día. Las reservas se pueden importar desde un archivo CSV o Excel.")]),
"pt": dict(
  card="Hostlio Pro vs Cloudbeds: preço publicado ou orçamento, IA incluída",
  title="Hostlio Pro vs Cloudbeds (2026): preços e IA | Hostlio Pro",
  desc="Hostlio Pro x Cloudbeds: preço fixo publicado em vez de orçamento, IA no WhatsApp em todos os planos e 7 dias de teste. Com fontes e data.",
  crumb="Hostlio Pro vs Cloudbeds", h1='Hostlio Pro vs <em class="hl">Cloudbeds</em>',
  lead="Saiba o preço antes da ligação de vendas. O Hostlio Pro publica seus planos, inclui um assistente de IA no WhatsApp em todos eles e você pode começar hoje um teste de 7 dias. Foi feito para hotéis independentes de 1 a 150 quartos.",
  name="Cloudbeds", frm="da Cloudbeds",
  rows=[("Preço", "Publicado: Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ por mês (USD, early bird)", "Sob orçamento: os planos Flex, One, Experience e Enterprise mostram \"Request a quote\""),
        ("Comissão por reserva", "Nenhuma, mensalidade fixa", "Informa que não cobra comissão adicional nas reservas do seu Booking Engine ou Channel Manager; em metabuscadores cobra comissão após a estadia"),
        ("Mensagens com IA e WhatsApp", "Todos os planos (Lio no WhatsApp); caixas de entrada das OTAs no Pro e no Growth", "Chatbot com IA e caixa de entrada unificada com WhatsApp, SMS, e-mail e mensagens de OTAs; na página de preços, Guest Experience aparece no plano Experience"),
        ("Channel manager", "Todos os planos, conexões certificadas com mais de 100 OTAs", "No plano One e acima"),
        ("Teste grátis", "7 dias; sem cobrança até o fim do teste", "Não mencionado na página de preços; oferece demonstração")],
  srcs=["cb_pr", "cb_home", "cb_ge"],
  faq=[("Posso migrar da Cloudbeds para o Hostlio Pro?", "Sim. Exporte suas reservas da Cloudbeds e importe no Hostlio Pro em CSV ou Excel, com mapeamento de colunas e controle de duplicados. Conecte suas OTAs ao channel manager certificado do Hostlio Pro e planeje a troca para que a disponibilidade saia de um só sistema. O Hostlio Pro cobre PMS, channel manager e mensagens com hóspedes; não inclui motor de reservas nem processamento de pagamentos."),
       ("Quanto custa a Cloudbeds?", "A Cloudbeds não publica preços. A página de preços mostra quatro planos (Flex, One, Experience, Enterprise), todos com \"Request a quote\" (8 de outubro de 2026). Os planos do Hostlio Pro estão na página de preços, a partir de ⟦price:starter⟧ por mês."),
       ("O Hostlio Pro inclui WhatsApp em todos os planos?", "Sim. O Lio responde aos hóspedes no WhatsApp desde o plano Starter. Pro e Growth acrescentam as caixas de entrada do Booking.com, Airbnb e Expedia e pedidos de reserva que você aprova."),
       ("Quanto tempo leva a migração?", "A conta fica pronta em minutos e os canais costumam ser conectados no mesmo dia. As reservas podem ser importadas de um arquivo CSV ou Excel.")]),
}

# Alternatifler tablosu: yalnız resmî fiyat sayfasında doğrulanan ürünler; "kime uygun" sütunu YOK (rakip önermez)
ALTS = {
"en": [("Hostlio Pro", "Flat monthly fee", "⟦price:starter⟧/month (Starter, early bird)", "7 days"),
       ("HotelRunner", "% of booking revenue with a monthly minimum (Essential)", "0.75% a month, min. $19.95 (Essential Manage)", "Offered; length not stated"),
       ("Sirvoy", "Flat monthly fee by room tier", "Up to 10 rooms: €22 (Starter) or €79 (Pro, with channel manager) a month, monthly billing", "14 days"),
       ("Beds24", "Pay as you go: base + per room + per channel link", "From €15.50/month", "Free trial available"),
       ("eviivo", "From-price plus a per-booking fee", "From $50/month (single property, excl. taxes) + $0.50 per confirmed booking", "14 days (single property)"),
       ("Amenitiz", "Quote based on number of rooms", "Not published", "Not offered; free demo")],
"es": [("Hostlio Pro", "Cuota mensual fija", "⟦price:starter⟧/mes (Starter, lanzamiento)", "7 días"),
       ("HotelRunner", "% de los ingresos por reservas con mínimo mensual (Essential)", "0,75 % al mes, mínimo 19,95 $ (Essential Manage)", "Disponible; duración no indicada"),
       ("Sirvoy", "Cuota mensual fija por tramo de habitaciones", "Hasta 10 habitaciones: 22 € (Starter) o 79 € (Pro, con channel manager) al mes, pago mensual", "14 días"),
       ("Beds24", "Pago por uso: base + por habitación + por conexión de canal", "Desde 15,50 €/mes", "Prueba gratuita disponible"),
       ("eviivo", "Precio desde + tarifa por reserva", "Desde 50 $/mes (un alojamiento, sin impuestos) + 0,50 $ por reserva confirmada", "14 días (un alojamiento)"),
       ("Amenitiz", "Presupuesto según número de habitaciones", "No publicado", "No ofrece; demo gratuita")],
"pt": [("Hostlio Pro", "Mensalidade fixa", "⟦price:starter⟧/mês (Starter, early bird)", "7 dias"),
       ("HotelRunner", "% da receita de reservas com mínimo mensal (Essential)", "0,75% ao mês, mínimo US$ 19,95 (Essential Manage)", "Disponível; duração não informada"),
       ("Sirvoy", "Mensalidade fixa por faixa de quartos", "Até 10 quartos: € 22 (Starter) ou € 79 (Pro, com channel manager) por mês, cobrança mensal", "14 dias"),
       ("Beds24", "Pague pelo uso: base + por quarto + por conexão de canal", "A partir de € 15,50/mês", "Teste grátis disponível"),
       ("eviivo", "Preço a partir de + taxa por reserva", "A partir de US$ 50/mês (uma propriedade, sem impostos) + US$ 0,50 por reserva confirmada", "14 dias (uma propriedade)"),
       ("Amenitiz", "Orçamento conforme o número de quartos", "Não publicado", "Não oferece; demonstração gratuita")],
}
ALT_COLS = {"en": ("Software", "Pricing model", "Published starting price", "Free trial (as stated)"),
            "es": ("Software", "Modelo de precio", "Precio de partida publicado", "Prueba gratis (según la web)"),
            "pt": ("Software", "Modelo de preço", "Preço inicial publicado", "Teste grátis (segundo o site)")}

P["alt-cloudbeds"] = {
"en": dict(
  card="Cloudbeds alternatives for small hotels, with published prices",
  title="Cloudbeds Alternatives for Small Hotels (2026) | Hostlio Pro",
  desc="Cloudbeds alternative for small hotels: Hostlio Pro publishes its prices, charges no booking commission and includes AI on WhatsApp. Checked Oct 2026.",
  crumb="Cloudbeds alternatives", h1='Cloudbeds <em class="hl">alternatives</em> for small hotels',
  lead="Cloudbeds prices by quote. Hostlio Pro shows its price up front, from ⟦price:starter⟧ a month, with the channel manager and an AI assistant on WhatsApp in every plan, and no booking commission.",
  name="Cloudbeds", frm="from Cloudbeds",
  alt_h="Alternatives with published prices", alt_p="Pricing models and starting prices as published on each company's own pricing page. Cloudbeds itself lists Flex, One, Experience and Enterprise plans, all by quote.",
  ask_h="Questions to ask any Cloudbeds alternative, answered for Hostlio Pro",
  ask=[("How will I pay, and will it grow with my revenue?", "A flat monthly fee: Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧. No booking commission, no revenue share; 20% off with annual billing."),
       ("Is the channel manager included?", "Yes, in every plan, with certified connections to Booking.com, Airbnb, Expedia and 100+ OTAs."),
       ("Are guest messages from WhatsApp and the OTAs handled, and in which plan?", "Lio answers on WhatsApp in every plan. Pro and Growth add Booking.com, Airbnb and Expedia inboxes, plus booking and extra-service requests that you approve."),
       ("Can I try it with my own rooms and rates?", "Yes. Start a 7-day trial on the plan you choose and set up your real rooms and rates; no charge until the trial ends.")],
  srcs=["cb_pr", "hr_en", "sv_pr", "b24_pr", "ev_pr", "am_en"],
  faq=[("Is there a cheaper alternative to Cloudbeds?", "Cloudbeds doesn't publish prices, so a direct comparison needs a quote. Hostlio Pro starts at ⟦price:starter⟧ a month with the channel manager and the Lio AI assistant included, and charges no booking commission. Other published starting prices are in the table above (October 8, 2026)."),
       ("Which Cloudbeds alternative includes AI guest messaging?", "Hostlio Pro includes its AI assistant Lio on WhatsApp in every plan, and adds Booking.com, Airbnb and Expedia inboxes on Pro and Growth."),
       ("Can I switch from Cloudbeds to Hostlio Pro?", "Yes. Export your reservations from Cloudbeds and import them into Hostlio Pro as CSV or Excel, with column mapping and duplicate checks; then connect your OTAs and plan the cut-over. Hostlio Pro doesn't include a booking engine or payment processing.")]),
"es": dict(
  card="Alternativas a Cloudbeds para hoteles pequeños, con precios publicados",
  title="Alternativas a Cloudbeds para hoteles pequeños | Hostlio Pro",
  desc="Alternativa a Cloudbeds para hoteles pequeños: Hostlio Pro publica precios, no cobra comisión e incluye IA en WhatsApp. Precios a oct. 2026.",
  crumb="Alternativas a Cloudbeds", h1='<em class="hl">Alternativas</em> a Cloudbeds para hoteles pequeños',
  lead="Cloudbeds trabaja con presupuesto. Hostlio Pro muestra su precio desde el principio, desde ⟦price:starter⟧ al mes, con channel manager y asistente de IA en WhatsApp en todos los planes, y sin comisión por reserva.",
  name="Cloudbeds", frm="de Cloudbeds",
  alt_h="Alternativas con precios publicados", alt_p="Modelos y precios de partida tal como los publica cada empresa en su propia página de precios. Cloudbeds muestra los planes Flex, One, Experience y Enterprise, todos con presupuesto.",
  ask_h="Preguntas para cualquier alternativa a Cloudbeds, respondidas para Hostlio Pro",
  ask=[("¿Cómo pagaré y crecerá con mis ingresos?", "Cuota mensual fija: Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧. Sin comisión por reserva ni porcentaje de ingresos; 20 % de descuento en pago anual."),
       ("¿El channel manager está incluido?", "Sí, en todos los planes, con conexiones certificadas con Booking.com, Airbnb, Expedia y más de 100 OTAs."),
       ("¿Se gestionan los mensajes de WhatsApp y de las OTAs? ¿En qué plan?", "Lio responde por WhatsApp en todos los planes. Pro y Growth añaden las bandejas de Booking.com, Airbnb y Expedia y solicitudes de reserva y de servicios extra que tú apruebas."),
       ("¿Puedo probarlo con mis habitaciones y tarifas?", "Sí. Empieza una prueba de 7 días en el plan que elijas y configura tus habitaciones y tarifas reales; sin cargo hasta que termina.")],
  srcs=["cb_pr", "hr_en", "sv_pr", "b24_pr", "ev_pr", "am_en"],
  faq=[("¿Hay una alternativa más barata a Cloudbeds?", "Cloudbeds no publica precios, así que una comparación directa requiere presupuesto. Hostlio Pro empieza en ⟦price:starter⟧ al mes con channel manager y el asistente Lio incluidos, sin comisión por reserva. Los demás precios de partida publicados están en la tabla (8 de octubre de 2026)."),
       ("¿Qué alternativa a Cloudbeds incluye mensajería con IA?", "Hostlio Pro incluye su asistente de IA Lio en WhatsApp en todos los planes y añade las bandejas de Booking.com, Airbnb y Expedia en Pro y Growth."),
       ("¿Puedo pasarme de Cloudbeds a Hostlio Pro?", "Sí. Exporta tus reservas de Cloudbeds e impórtalas en Hostlio Pro en CSV o Excel, con asignación de columnas y control de duplicados; después conecta tus OTAs y planifica el cambio. Hostlio Pro no incluye motor de reservas ni cobro de pagos.")]),
"pt": dict(
  card="Alternativas à Cloudbeds para hotéis pequenos, com preços publicados",
  title="Alternativas à Cloudbeds para hotéis pequenos | Hostlio Pro",
  desc="Alternativa à Cloudbeds para hotéis pequenos: o Hostlio Pro publica preços, não cobra comissão e inclui IA no WhatsApp. Preços de out. 2026.",
  crumb="Alternativas à Cloudbeds", h1='<em class="hl">Alternativas</em> à Cloudbeds para hotéis pequenos',
  lead="A Cloudbeds trabalha com orçamento. O Hostlio Pro mostra o preço logo de início, a partir de ⟦price:starter⟧ por mês, com channel manager e assistente de IA no WhatsApp em todos os planos, e sem comissão por reserva.",
  name="Cloudbeds", frm="da Cloudbeds",
  alt_h="Alternativas com preços publicados", alt_p="Modelos e preços iniciais como cada empresa publica na própria página de preços. A Cloudbeds mostra os planos Flex, One, Experience e Enterprise, todos sob orçamento.",
  ask_h="Perguntas para qualquer alternativa à Cloudbeds, respondidas para o Hostlio Pro",
  ask=[("Como vou pagar, e o valor cresce com a minha receita?", "Mensalidade fixa: Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧. Sem comissão por reserva nem percentual da receita; 20% de desconto no plano anual."),
       ("O channel manager está incluído?", "Sim, em todos os planos, com conexões certificadas com Booking.com, Airbnb, Expedia e mais de 100 OTAs."),
       ("As mensagens do WhatsApp e das OTAs são atendidas? Em qual plano?", "O Lio responde no WhatsApp em todos os planos. Pro e Growth acrescentam as caixas de entrada do Booking.com, Airbnb e Expedia e pedidos de reserva e de serviços extras que você aprova."),
       ("Posso testar com meus quartos e tarifas?", "Sim. Comece um teste de 7 dias no plano que escolher e cadastre seus quartos e tarifas reais; sem cobrança até o fim do teste.")],
  srcs=["cb_pr", "hr_en", "sv_pr", "b24_pr", "ev_pr", "am_en"],
  faq=[("Existe uma alternativa mais barata à Cloudbeds?", "A Cloudbeds não publica preços, então uma comparação direta exige orçamento. O Hostlio Pro começa em ⟦price:starter⟧ por mês com channel manager e o assistente Lio incluídos, sem comissão por reserva. Os outros preços iniciais publicados estão na tabela (8 de outubro de 2026)."),
       ("Qual alternativa à Cloudbeds inclui mensagens com IA?", "O Hostlio Pro inclui o assistente de IA Lio no WhatsApp em todos os planos e acrescenta as caixas de entrada do Booking.com, Airbnb e Expedia no Pro e no Growth."),
       ("Posso migrar da Cloudbeds para o Hostlio Pro?", "Sim. Exporte suas reservas da Cloudbeds e importe no Hostlio Pro em CSV ou Excel, com mapeamento de colunas e controle de duplicados; depois conecte suas OTAs e planeje a troca. O Hostlio Pro não inclui motor de reservas nem processamento de pagamentos.")]),
}

P["alt-amenitiz"] = {
"en": dict(
  card="Amenitiz alternative: published pricing and AI messaging on WhatsApp",
  title="Amenitiz Alternative: Hostlio Pro Compared (2026) | Hostlio Pro",
  desc="Looking for an Amenitiz alternative? Hostlio Pro publishes its prices, offers a 7-day trial and includes an AI assistant on WhatsApp in every plan.",
  crumb="Amenitiz alternative", h1='An <em class="hl">Amenitiz</em> alternative with published pricing',
  lead="Know the price before the demo. Hostlio Pro lists its plans on its website, includes an AI assistant on WhatsApp from the first plan and lets you try everything free for 7 days.",
  name="Amenitiz", frm="from Amenitiz",
  rows=[("Pricing", "Published: Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ a month (USD, early bird)", "Not published: personalised quote based on number of rooms; monthly or annual billing"),
        ("Booking fees", "None, flat monthly fee", "No commission on direct bookings and no per-reservation fees; AmenitizPay transactions 1.5% + €0.25"),
        ("Guest messaging on WhatsApp", "Every plan (Lio, AI assistant)", "\"Guest messaging + WhatsApp\" is in the Advanced plan, labelled \"live in June\" on the pricing page; Core has automated guest emails and a unified inbox"),
        ("Channel manager", "Every plan, certified connections to 100+ OTAs", "Core plan: unlimited OTA connections (\"150+ OTAs\")"),
        ("Free trial", "7 days; no charge until the trial ends", "Not offered; free demo, and \"Live in 30 days or your first month is on us\"")],
  srcs=["am_en", "am_fr", "am_cm"],
  faq=[("Can I switch from Amenitiz to Hostlio Pro?", "Yes. Export your reservations from Amenitiz and import them into Hostlio Pro as CSV or Excel, with column mapping and duplicate checks; then connect your OTAs and plan the cut-over so availability is sent from one system only. Hostlio Pro focuses on PMS, channel manager and AI guest messaging; it doesn't include a website builder, booking engine or payment processing."),
       ("How much does Amenitiz cost?", "Amenitiz doesn't publish prices. Its pricing page offers a personalised quote based on the number of rooms, with monthly or annual billing (October 8, 2026). Hostlio Pro starts at ⟦price:starter⟧ a month."),
       ("Which Hostlio Pro plan includes WhatsApp?", "All of them. Lio answers guests on WhatsApp from Starter up; Pro and Growth add Booking.com, Airbnb and Expedia inboxes."),
       ("Is Hostlio Pro available in French, Spanish, Italian and Portuguese?", "The dashboard, mobile app and guest check-in form are available in English, Turkish, Spanish, French, Italian and Portuguese. Support is in English and Turkish.")]),
"fr": dict(
  card="Alternative à Amenitiz : tarifs publics et IA sur WhatsApp",
  title="Alternative à Amenitiz : Hostlio Pro comparé (2026) | Hostlio Pro",
  desc="Une alternative à Amenitiz ? Hostlio Pro affiche ses tarifs, propose 7 jours d’essai et inclut un assistant IA sur WhatsApp dans tous les forfaits.",
  crumb="Alternative à Amenitiz", h1='Une alternative à <em class="hl">Amenitiz</em> avec des tarifs publics',
  lead="Connaître le prix avant la démo. Hostlio Pro affiche ses forfaits sur son site, inclut un assistant IA sur WhatsApp dès le premier forfait et vous laisse tout essayer gratuitement pendant 7 jours.",
  name="Amenitiz", frm="depuis Amenitiz",
  rows=[("Tarifs", "Publics : Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ par mois (USD, tarif early bird)", "Non publiés : devis personnalisé selon le nombre de chambres ; paiement mensuel ou annuel"),
        ("Commissions", "Aucune, abonnement mensuel fixe", "Aucune commission sur les réservations directes ni frais par réservation ; transactions AmenitizPay 1,5 % + 0,25 €"),
        ("Messagerie client sur WhatsApp", "Tous les forfaits (Lio, assistant IA)", "« Messagerie client + WhatsApp » dans l’offre Advanced, avec la mention « disponible en juin » sur la page tarifs ; Core : e-mails automatiques et messagerie unifiée"),
        ("Channel manager", "Tous les forfaits, connexions certifiées à plus de 100 OTA", "Offre Core : connexions OTA illimitées (« 150+ OTAs »)"),
        ("Essai gratuit", "7 jours ; aucun prélèvement avant la fin de l’essai", "Non proposé ; démo gratuite et « mise en ligne en 30 jours ou premier mois offert »")],
  srcs=["am_fr", "am_en", "am_cm"],
  faq=[("Puis-je passer d’Amenitiz à Hostlio Pro ?", "Oui. Exportez vos réservations depuis Amenitiz et importez-les dans Hostlio Pro en CSV ou Excel, avec correspondance des colonnes et contrôle des doublons ; connectez ensuite vos OTA et planifiez la bascule pour que les disponibilités partent d’un seul système. Hostlio Pro se concentre sur le PMS, le channel manager et la messagerie IA ; il n’inclut ni création de site, ni moteur de réservation, ni encaissement."),
       ("Combien coûte Amenitiz ?", "Amenitiz ne publie pas ses prix. Sa page tarifs propose un devis personnalisé selon le nombre de chambres, en paiement mensuel ou annuel (8 octobre 2026). Hostlio Pro démarre à ⟦price:starter⟧ par mois."),
       ("Quel forfait Hostlio Pro inclut WhatsApp ?", "Tous. Lio répond aux clients sur WhatsApp dès Starter ; Pro et Growth ajoutent les messageries Booking.com, Airbnb et Expedia."),
       ("Hostlio Pro est-il disponible en français ?", "Oui : le tableau de bord, l’application mobile et le formulaire de check-in client existent en français (ainsi qu’en anglais, turc, espagnol, italien et portugais). Le support est en anglais et en turc.")]),
}

P["alt-hijiffy"] = {
"en": dict(
  card="HiJiffy alternative: AI guest messaging with the PMS included",
  title="HiJiffy Alternative: AI Messaging with PMS Included | Hostlio Pro",
  desc="HiJiffy alternative for small hotels: Hostlio Pro puts the PMS, channel manager and an AI assistant on WhatsApp in one subscription, from the first plan.",
  crumb="HiJiffy alternative", h1='A <em class="hl">HiJiffy</em> alternative with the PMS included',
  lead="One subscription instead of two. Hostlio Pro is the PMS and channel manager with an AI guest assistant built in, so Lio answers on WhatsApp with your live availability and your own rates, from ⟦price:starter⟧ a month.",
  name="HiJiffy", frm="from your current PMS", gen_switch=True,
  rows=[("What it is", "PMS + channel manager + AI guest assistant (Lio)", "A guest-communication and AI layer that integrates with PMSs, booking engines and CRMs"),
        ("Pricing", "From ⟦price:starter⟧ a month, PMS and channel manager included", "Per property, \"starting at\" by room count: Basic €99, Pro €159, Premium €319 a month with yearly billing (€105 / €170 / €350 monthly), plus a setup fee of €99 / €399 / €599 for each 5 properties; Enterprise by quote"),
        ("WhatsApp", "Every plan (Lio)", "From the Premium plan; Pro covers website, Facebook, Instagram and Telegram"),
        ("OTA messaging", "Booking.com, Airbnb and Expedia inboxes on Pro and Growth", "Its site says it centralises OTA messaging including Booking.com, Expedia and Airbnb"),
        ("PMS and channel manager", "Included in every plan, 100+ OTAs", "Not a PMS or channel manager; PMS integration from Premium"),
        ("Free trial", "7 days; no charge until the trial ends", "Not mentioned; subscribe or book a demo")],
  srcs=["hj_pr", "hj_home"],
  faq=[("Can I switch from HiJiffy to Hostlio Pro?", "Yes, if you also want to move your PMS and channel manager: Hostlio Pro replaces both and includes the Lio AI assistant. Import your reservations from your current PMS as CSV or Excel, connect your OTAs, then fill in Lio's hotel information. Lio works on WhatsApp and OTA inboxes; it doesn't cover website chat or social media channels."),
       ("How much does HiJiffy cost?", "HiJiffy's pricing page lists per-property \"starting at\" prices that depend on room count: Basic €99, Pro €159 and Premium €319 a month with yearly billing, or €105, €170 and €350 billed monthly, plus a setup fee. Enterprise is by quote (October 8, 2026)."),
       ("Which HiJiffy plan includes WhatsApp?", "According to HiJiffy's pricing page, WhatsApp is part of the Premium plan; the Pro plan's channels are website, Facebook, Instagram and Telegram. In Hostlio Pro, WhatsApp is on every plan."),
       ("Is Hostlio Pro only a chatbot?", "No. Hostlio Pro is a PMS and channel manager with an AI assistant built in, so it also handles reservations, availability on 100+ OTAs, online check-in and analytics.")]),
"pt": dict(
  card="Alternativa à HiJiffy: mensagens com IA e PMS incluído",
  title="Alternativa à HiJiffy com PMS incluído | Hostlio Pro",
  desc="Alternativa à HiJiffy para hotéis pequenos: o Hostlio Pro reúne PMS, channel manager e assistente de IA no WhatsApp numa só assinatura, desde o primeiro plano.",
  crumb="Alternativa à HiJiffy", h1='Uma alternativa à <em class="hl">HiJiffy</em> com o PMS incluído',
  lead="Uma assinatura em vez de duas. O Hostlio Pro é o próprio PMS e channel manager, com um assistente de IA embutido: o Lio responde no WhatsApp com a disponibilidade real e as suas tarifas, a partir de ⟦price:starter⟧ por mês.",
  name="HiJiffy", frm="do seu PMS atual", gen_switch=True,
  rows=[("O que é", "PMS + channel manager + assistente de IA (Lio)", "Uma camada de comunicação com hóspedes e IA que se integra a PMSs, motores de reserva e CRMs"),
        ("Preço", "A partir de ⟦price:starter⟧ por mês, PMS e channel manager incluídos", "Por propriedade, \"a partir de\" conforme o número de quartos: Basic € 99, Pro € 159, Premium € 319 por mês no plano anual (€ 105 / € 170 / € 350 no mensal), mais taxa de implantação de € 99 / € 399 / € 599 a cada 5 propriedades; Enterprise sob orçamento"),
        ("WhatsApp", "Todos os planos (Lio)", "A partir do plano Premium; o Pro cobre site, Facebook, Instagram e Telegram"),
        ("Mensagens das OTAs", "Caixas de entrada do Booking.com, Airbnb e Expedia no Pro e no Growth", "O site informa que centraliza as mensagens das OTAs, incluindo Booking.com, Expedia e Airbnb"),
        ("PMS e channel manager", "Incluídos em todos os planos, mais de 100 OTAs", "Não é PMS nem channel manager; integração com PMS a partir do Premium"),
        ("Teste grátis", "7 dias; sem cobrança até o fim do teste", "Não mencionado; assinar ou agendar demonstração")],
  srcs=["hj_pr", "hj_home"],
  faq=[("Posso migrar da HiJiffy para o Hostlio Pro?", "Sim, se você também quiser trocar o PMS e o channel manager: o Hostlio Pro substitui os dois e inclui o assistente de IA Lio. Importe as reservas do seu PMS atual em CSV ou Excel, conecte suas OTAs e preencha as informações do hotel para o Lio. O Lio funciona no WhatsApp e nas caixas de entrada das OTAs; não cobre chat do site nem redes sociais."),
       ("Quanto custa a HiJiffy?", "A página de preços da HiJiffy mostra preços \"a partir de\" por propriedade, que dependem do número de quartos: Basic € 99, Pro € 159 e Premium € 319 por mês no plano anual, ou € 105, € 170 e € 350 no mensal, mais taxa de implantação. O Enterprise é sob orçamento (8 de outubro de 2026)."),
       ("Qual plano da HiJiffy inclui WhatsApp?", "Segundo a página de preços da HiJiffy, o WhatsApp faz parte do plano Premium; os canais do plano Pro são site, Facebook, Instagram e Telegram. No Hostlio Pro, o WhatsApp está em todos os planos."),
       ("O Hostlio Pro é só um chatbot?", "Não. O Hostlio Pro é um PMS e channel manager com assistente de IA embutido; também cuida das reservas, da disponibilidade em mais de 100 OTAs, do check-in online e das análises.")]),
}

# ---------------------------------------------------------------- general comparison page (key "compare", 6 dil)
# Little Hotelier 8 Ekim 2026'da doğrulanamadı (resmî fiyat sayfası 403) ⇒ tablodan çıkarıldı. Mews 8 Ekim'de resmî sayfadan doğrulandı.
GEN = {
"tr": dict(title="Otel Programı Karşılaştırması 2026: Fiyatlar | Hostlio Pro",
  desc="Otel programı karşılaştırması 2026: Hostlio Pro ile HotelRunner, Elektraweb, Cloudbeds, Mews ve Amenitiz; fiyat, komisyon, deneme ve WhatsApp'ta AI.",
  crumb="Otel programı karşılaştırması", h1='Otel programı karşılaştırması: <em class="hl">Hostlio Pro</em> ve diğerleri (2026)',
  lead="Sabit aylık ücret, rezervasyon komisyonu yok, fiyatlar sitede açık ve her planda WhatsApp'ta AI asistan. Hostlio Pro'yu bağımsız oteller için popüler yazılımlarla, firmaların kendi yayınladığı bilgilere göre yan yana koyduk.",
  tbl_h="Hostlio Pro ve diğer otel programları", tbl_p="Rakip bilgileri firmaların resmî fiyat ve ürün sayfalarından alındı ve 8 Ekim 2026'da kontrol edildi.",
  cols=["Yazılım", "Fiyatlar yayınlanıyor mu?", "Başlangıç", "Rezervasyon komisyonu", "Ücretsiz deneme", "WhatsApp'ta AI misafir mesajlaşması"],
  rows=[("Hostlio Pro", "Evet", "⟦price:starter⟧/ay (erken kayıt)", "Yok, sabit aylık ücret", "7 gün", "Tüm planlarda (Lio, 30+ dil)"),
        ("HotelRunner", "Evet (Essential planlar)", "Asgari 19,95 $/ay + rezervasyon gelirinin %0,75'i (Essential Manage)", "Essential planlarda aylık rezervasyon gelirinin %0,75–%1,25'i", "\"Ücretsiz deneyin\" var; süresi belirtilmiyor", "AI asistan Advanced planlarda listeleniyor (fiyat satış ekibinden); WhatsApp incelediğimiz sayfalarda belirtilmiyor"),
        ("Elektraweb", "Hayır; fiyat listesi sayfası teklif formuna yönlendiriyor", "Teklif", "Fiyat sayfasında belirtilmiyor", "Belirtilmiyor; ücretsiz demo var", "WhatsApp API ve Akıllı Sohbet ürün sayfalarında AI destekli asistan anlatılıyor (fiyat teklifle)"),
        ("Cloudbeds", "Hayır, teklif usulü", "Teklif", "Booking Engine ve Channel Manager rezervasyonlarından ek komisyon almadığını belirtiyor", "Fiyat sayfasında belirtilmiyor; demo var", "WhatsApp ve SMS üzerinden AI chatbot; Guest Experience, Experience planında listeleniyor"),
        ("Mews", "Hayır, teklif usulü (oda başına fiyat)", "Teklif", "Fiyat sayfasında belirtilmiyor", "Fiyat sayfasında belirtilmiyor", "\"WhatsApp ve SMS üzerinden AI mesajlaşma\" Mews Pro planında listeleniyor"),
        ("Amenitiz", "Hayır, oda sayısına göre teklif", "Teklif", "Doğrudan rezervasyonda komisyon yok; AmenitizPay işlem başına %1,5 + 0,25 €", "Yok; ücretsiz demo", "\"Guest messaging + WhatsApp\" Advanced planda (\"live in June\" etiketiyle)")],
  srcs=["ew_pr", "hr_tr", "cb_pr", "cb_ge", "mews_pr", "am_en"],
  links_h="Ayrıntılı karşılaştırmalar",
  faq=[("Otel programı nedir?", "Otel programı (otel yönetim yazılımı, PMS), bir konaklama tesisinin rezervasyonlarını, oda müsaitliğini, satış kanallarını ve misafir bilgilerini tek yerden yönetmesini sağlayan yazılımdır."),
       ("Otel programı fiyatları ne kadar?", "Bu tablodaki yazılımlardan fiyatını yayınlayanlar Hostlio Pro ve HotelRunner: Hostlio Pro sabit ücretle ayda ⟦price:starter⟧'dan başlar; HotelRunner Essential planları asgari 19,95 $ artı rezervasyon gelirinden yüzde alır. Elektraweb, Cloudbeds, Mews ve Amenitiz teklif verir (8 Ekim 2026). Daha fazla rakam için otel programı fiyatları 2026 rehberimize bakın."),
       ("Komisyonlu mu sabit fiyatlı mı daha avantajlı?", "Doluluk ve ortalama oda fiyatı arttıkça gelire bağlı modelin maliyeti büyür. Sabit aylık ücret bütçeyi öngörülebilir kılar: Hostlio Pro'da yüksek sezonda da fatura değişmez."),
       ("Mevcut programımdan Hostlio Pro'ya geçebilir miyim?", "Evet. Rezervasyonlarınızı CSV ya da Excel dosyasıyla içeri aktarırsınız (sütun eşleme ve mükerrer kontrolü dahil), kanallarınızı sertifikalı kanal yöneticisine bağlarsınız. Hesap dakikalar içinde hazır olur, kanallar çoğu zaman aynı gün bağlanır.")]),
"en": dict(title="Hotel Software Comparison 2026: Pricing and AI | Hostlio Pro",
  desc="Hotel software comparison 2026: Hostlio Pro vs HotelRunner, Elektraweb, Cloudbeds, Mews and Amenitiz on pricing, commission, trial and AI on WhatsApp.",
  crumb="Hotel software comparison", h1='Hotel software comparison: <em class="hl">Hostlio Pro</em> vs the rest (2026)',
  lead="A fixed monthly price, no booking commission, prices on the website and an AI assistant on WhatsApp in every plan. Here's Hostlio Pro side by side with popular software for independent hotels, using what each company publishes.",
  tbl_h="Hostlio Pro and other hotel software", tbl_p="Competitor information comes from each company's official pricing and product pages, checked on October 8, 2026.",
  cols=["Software", "Published prices?", "Starting at", "Booking commission", "Free trial", "AI guest messaging on WhatsApp"],
  rows=[("Hostlio Pro", "Yes", "⟦price:starter⟧/month (early bird)", "None, flat monthly fee", "7 days", "Every plan (Lio, 30+ languages)"),
        ("HotelRunner", "Yes (Essential plans)", "$19.95/month minimum + 0.75% of booking revenue (Essential Manage)", "0.75%–1.25% of monthly booking revenue on Essential plans", "\"Start free trial\" offered; length not stated", "AI assistant listed in the Advanced plans (priced by sales); WhatsApp not stated on the pages we checked"),
        ("Elektraweb", "No; the price-list page leads to a quote form", "Quote", "Not stated on the pricing page", "Not stated; free demo offered", "AI-assisted assistant described on its WhatsApp API and Smart Chat product pages (priced by quote)"),
        ("Cloudbeds", "No, quote-based", "Quote", "States no added commission on Booking Engine and Channel Manager reservations", "Not mentioned on the pricing page; demo offered", "AI chatbot via WhatsApp and SMS; Guest Experience listed in the Experience plan"),
        ("Mews", "No, quote-based (priced per room)", "Quote", "Not stated on the pricing page", "Not mentioned on the pricing page", "\"AI messaging via WhatsApp and SMS\" listed in Mews Pro"),
        ("Amenitiz", "No, quote by number of rooms", "Quote", "No commission on direct bookings; AmenitizPay 1.5% + €0.25 per transaction", "Not offered; free demo", "\"Guest messaging + WhatsApp\" in the Advanced plan (labelled \"live in June\")")],
  srcs=["ew_pr", "hr_en", "cb_pr", "cb_ge", "mews_pr", "am_en"],
  links_h="Detailed comparisons",
  faq=[("What is hotel management software?", "Hotel management software (a PMS) lets a property manage reservations, room availability, sales channels and guest information in one place."),
       ("How much does hotel software cost?", "Of the vendors in this table, Hostlio Pro and HotelRunner publish prices: Hostlio Pro starts at ⟦price:starter⟧ a month as a flat fee; HotelRunner's Essential plans have a $19.95 monthly minimum plus a share of booking revenue. Elektraweb, Cloudbeds, Mews and Amenitiz give quotes (October 8, 2026)."),
       ("Is a commission or a flat fee better?", "As occupancy and average rates rise, revenue-based costs grow. A flat monthly fee keeps the budget predictable: with Hostlio Pro your bill stays the same in high season."),
       ("Can I switch to Hostlio Pro from my current software?", "Yes. Import your reservations from a CSV or Excel file (with column mapping and duplicate checks) and connect your channels to the certified channel manager. Your account is ready in minutes, and channels are usually connected the same day.")]),
"es": dict(title="Comparativa de software hotelero 2026: precios | Hostlio Pro",
  desc="Comparativa de software hotelero 2026: Hostlio Pro frente a HotelRunner, Cloudbeds, Mews y Amenitiz en precio, comisión, prueba gratis e IA en WhatsApp.",
  crumb="Comparativa de software hotelero", h1='Comparativa de software hotelero: <em class="hl">Hostlio Pro</em> frente al resto (2026)',
  lead="Cuota mensual fija, sin comisión por reserva, precios publicados y un asistente de IA en WhatsApp en todos los planes. Aquí tienes Hostlio Pro junto a programas populares para hoteles independientes, con lo que publica cada empresa.",
  tbl_h="Hostlio Pro y otros programas para hoteles", tbl_p="La información de la competencia procede de las páginas oficiales de precios y producto de cada empresa, comprobadas el 8 de octubre de 2026.",
  cols=["Software", "¿Precios publicados?", "Desde", "Comisión por reserva", "Prueba gratis", "Mensajería IA con huéspedes en WhatsApp"],
  rows=[("Hostlio Pro", "Sí", "⟦price:starter⟧/mes (lanzamiento)", "Ninguna, cuota mensual fija", "7 días", "Todos los planes (Lio, más de 30 idiomas)"),
        ("HotelRunner", "Sí (planes Essential)", "Mínimo 19,95 $/mes + 0,75 % de los ingresos por reservas (Essential Manage)", "0,75–1,25 % de los ingresos mensuales por reservas en los planes Essential", "Ofrece \"Start free trial\"; duración no indicada", "Asistente de IA en los planes Advanced (precio con ventas); WhatsApp no figura en las páginas que revisamos"),
        ("Elektraweb", "No; la página de precios lleva a un formulario de presupuesto", "Presupuesto", "No se indica en la página de precios", "No se indica; ofrece demo gratuita", "Asistente con IA descrito en sus páginas de WhatsApp API y Smart Chat (precio con presupuesto)"),
        ("Cloudbeds", "No, con presupuesto", "Presupuesto", "Indica que no añade comisión a las reservas del Booking Engine y del Channel Manager", "No se menciona en la página de precios; ofrece demo", "Chatbot con IA por WhatsApp y SMS; Guest Experience figura en el plan Experience"),
        ("Mews", "No, con presupuesto (precio por habitación)", "Presupuesto", "No se indica en la página de precios", "No se menciona en la página de precios", "\"AI messaging via WhatsApp and SMS\" figura en Mews Pro"),
        ("Amenitiz", "No, presupuesto según habitaciones", "Presupuesto", "Sin comisión en reservas directas; AmenitizPay 1,5 % + 0,25 € por transacción", "No ofrece; demo gratuita", "\"Guest messaging + WhatsApp\" en el plan Advanced (con la etiqueta \"live in June\")")],
  srcs=["ew_pr", "hr_en", "cb_pr", "cb_ge", "mews_pr", "am_en"],
  links_h="Comparativas detalladas",
  faq=[("¿Qué es un software de gestión hotelera?", "Un software de gestión hotelera (un PMS hotelero) permite a un alojamiento gestionar reservas, disponibilidad de habitaciones, canales de venta e información de los huéspedes en un solo lugar."),
       ("¿Cuánto cuesta un programa para hoteles?", "De los proveedores de esta tabla, publican precios Hostlio Pro y HotelRunner: Hostlio Pro empieza en ⟦price:starter⟧ al mes con cuota fija; los planes Essential de HotelRunner tienen un mínimo de 19,95 $ al mes más un porcentaje de los ingresos por reservas. Elektraweb, Cloudbeds, Mews y Amenitiz dan presupuesto (8 de octubre de 2026)."),
       ("¿Qué es mejor, comisión o cuota fija?", "A medida que suben la ocupación y la tarifa media, el coste basado en ingresos crece. Una cuota mensual fija mantiene el presupuesto previsible: con Hostlio Pro tu factura no cambia en temporada alta."),
       ("¿Puedo pasarme a Hostlio Pro desde mi programa actual?", "Sí. Importa tus reservas desde un archivo CSV o Excel (con asignación de columnas y control de duplicados) y conecta tus canales al channel manager certificado. La cuenta está lista en minutos y los canales suelen conectarse el mismo día.")]),
"it": dict(title="Confronto gestionali hotel 2026: prezzi e AI | Hostlio Pro",
  desc="Confronto gestionali per hotel 2026: Hostlio Pro rispetto a HotelRunner, Cloudbeds, Mews e Amenitiz su prezzi, commissioni, prova gratuita e AI su WhatsApp.",
  crumb="Confronto gestionali hotel", h1='Confronto gestionali per hotel: <em class="hl">Hostlio Pro</em> e gli altri (2026)',
  lead="Canone mensile fisso, nessuna commissione sulle prenotazioni, prezzi pubblicati e un assistente AI su WhatsApp in tutti i piani. Ecco Hostlio Pro accanto a gestionali diffusi tra gli hotel indipendenti, con le informazioni pubblicate da ciascuna azienda.",
  tbl_h="Hostlio Pro e altri gestionali per hotel", tbl_p="Le informazioni sui concorrenti provengono dalle pagine ufficiali di prezzi e prodotto di ciascuna azienda, verificate l'8 ottobre 2026.",
  cols=["Software", "Prezzi pubblicati?", "Da", "Commissione sulle prenotazioni", "Prova gratuita", "Messaggi AI agli ospiti su WhatsApp"],
  rows=[("Hostlio Pro", "Sì", "⟦price:starter⟧/mese (early bird)", "Nessuna, canone mensile fisso", "7 giorni", "Tutti i piani (Lio, oltre 30 lingue)"),
        ("HotelRunner", "Sì (piani Essential)", "Minimo 19,95 $/mese + 0,75% del fatturato da prenotazioni (Essential Manage)", "0,75–1,25% del fatturato mensile da prenotazioni nei piani Essential", "Offre \"Start free trial\"; durata non indicata", "Assistente AI nei piani Advanced (prezzo dal team commerciale); WhatsApp non indicato nelle pagine verificate"),
        ("Elektraweb", "No; la pagina prezzi rimanda a un modulo di preventivo", "Preventivo", "Non indicata nella pagina prezzi", "Non indicata; demo gratuita", "Assistente con AI descritto nelle pagine WhatsApp API e Smart Chat (prezzo su preventivo)"),
        ("Cloudbeds", "No, su preventivo", "Preventivo", "Dichiara di non aggiungere commissioni sulle prenotazioni da Booking Engine e Channel Manager", "Non menzionata nella pagina prezzi; demo disponibile", "Chatbot AI via WhatsApp e SMS; Guest Experience è nel piano Experience"),
        ("Mews", "No, su preventivo (prezzo per camera)", "Preventivo", "Non indicata nella pagina prezzi", "Non menzionata nella pagina prezzi", "\"AI messaging via WhatsApp and SMS\" incluso in Mews Pro"),
        ("Amenitiz", "No, preventivo in base alle camere", "Preventivo", "Nessuna commissione sulle prenotazioni dirette; AmenitizPay 1,5% + 0,25 € per transazione", "Non offerta; demo gratuita", "\"Guest messaging + WhatsApp\" nel piano Advanced (etichetta \"live in June\")")],
  srcs=["ew_pr", "hr_en", "cb_pr", "cb_ge", "mews_pr", "am_en"],
  links_h="Confronti dettagliati",
  faq=[("Che cos'è un gestionale per hotel?", "Un gestionale per hotel (PMS) permette a una struttura di gestire prenotazioni, disponibilità delle camere, canali di vendita e dati degli ospiti in un unico posto."),
       ("Quanto costa un gestionale per hotel?", "Tra i fornitori in tabella, pubblicano i prezzi Hostlio Pro e HotelRunner: Hostlio Pro parte da ⟦price:starter⟧ al mese con canone fisso; i piani Essential di HotelRunner prevedono un minimo di 19,95 $ al mese più una percentuale del fatturato da prenotazioni. Elektraweb, Cloudbeds, Mews e Amenitiz lavorano su preventivo (8 ottobre 2026)."),
       ("Meglio una commissione o un canone fisso?", "Con l'aumento di occupazione e tariffa media, i costi legati al fatturato crescono. Un canone mensile fisso rende il budget prevedibile: con Hostlio Pro la fattura resta uguale anche in alta stagione."),
       ("Posso passare a Hostlio Pro dal mio gestionale attuale?", "Sì. Importa le prenotazioni da un file CSV o Excel (con mappatura delle colonne e controllo dei duplicati) e collega i canali al channel manager certificato. L'account è pronto in pochi minuti e i canali di solito si collegano in giornata.")]),
"pt": dict(title="Comparativo de sistemas para hotel 2026: preços | Hostlio Pro",
  desc="Comparativo de sistemas para hotel 2026: Hostlio Pro x HotelRunner, Cloudbeds, Mews e Amenitiz em preço, comissão por reserva, teste grátis e IA no WhatsApp.",
  crumb="Comparativo de sistemas para hotel", h1='Comparativo de sistemas para hotel: <em class="hl">Hostlio Pro</em> e os outros (2026)',
  lead="Mensalidade fixa, sem comissão por reserva, preços publicados e um assistente de IA no WhatsApp em todos os planos. Veja o Hostlio Pro ao lado de sistemas populares entre hotéis independentes, com o que cada empresa publica.",
  tbl_h="Hostlio Pro e outros sistemas para hotel", tbl_p="As informações sobre concorrentes vêm das páginas oficiais de preços e produto de cada empresa, verificadas em 8 de outubro de 2026.",
  cols=["Sistema", "Preços publicados?", "A partir de", "Comissão por reserva", "Teste grátis", "Mensagens com IA no WhatsApp"],
  rows=[("Hostlio Pro", "Sim", "⟦price:starter⟧/mês (early bird)", "Nenhuma, mensalidade fixa", "7 dias", "Todos os planos (Lio, mais de 30 idiomas)"),
        ("HotelRunner", "Sim (planos Essential)", "Mínimo US$ 19,95/mês + 0,75% da receita de reservas (Essential Manage)", "0,75%–1,25% da receita mensal de reservas nos planos Essential", "Oferece \"Start free trial\"; duração não informada", "Assistente de IA nos planos Advanced (preço com vendas); WhatsApp não aparece nas páginas que verificamos"),
        ("Elektraweb", "Não; a página de preços leva a um formulário de orçamento", "Orçamento", "Não informada na página de preços", "Não informado; demonstração gratuita", "Assistente com IA descrito nas páginas de WhatsApp API e Smart Chat (preço sob orçamento)"),
        ("Cloudbeds", "Não, sob orçamento", "Orçamento", "Informa que não cobra comissão adicional nas reservas do Booking Engine e do Channel Manager", "Não mencionado na página de preços; oferece demonstração", "Chatbot com IA via WhatsApp e SMS; Guest Experience aparece no plano Experience"),
        ("Mews", "Não, sob orçamento (preço por quarto)", "Orçamento", "Não informada na página de preços", "Não mencionado na página de preços", "\"AI messaging via WhatsApp and SMS\" listado no Mews Pro"),
        ("Amenitiz", "Não, orçamento conforme os quartos", "Orçamento", "Sem comissão em reservas diretas; AmenitizPay 1,5% + € 0,25 por transação", "Não oferece; demonstração gratuita", "\"Guest messaging + WhatsApp\" no plano Advanced (com a etiqueta \"live in June\")")],
  srcs=["ew_pr", "hr_en", "cb_pr", "cb_ge", "mews_pr", "am_en"],
  links_h="Comparativos detalhados",
  faq=[("O que é um sistema de gestão hoteleira?", "Um sistema de gestão hoteleira (PMS) permite que uma hospedagem gerencie reservas, disponibilidade de quartos, canais de venda e dados dos hóspedes num só lugar."),
       ("Quanto custa um sistema para hotel?", "Dos fornecedores desta tabela, publicam preços o Hostlio Pro e a HotelRunner: o Hostlio Pro começa em ⟦price:starter⟧ por mês com mensalidade fixa; os planos Essential da HotelRunner têm mínimo de US$ 19,95 por mês mais um percentual da receita de reservas. Elektraweb, Cloudbeds, Mews e Amenitiz trabalham com orçamento (8 de outubro de 2026)."),
       ("O que é melhor, comissão ou mensalidade fixa?", "Quando a ocupação e a diária média sobem, o custo baseado na receita cresce. Uma mensalidade fixa deixa o orçamento previsível: com o Hostlio Pro a fatura não muda na alta temporada."),
       ("Posso migrar do meu sistema atual para o Hostlio Pro?", "Sim. Importe suas reservas de um arquivo CSV ou Excel (com mapeamento de colunas e controle de duplicados) e conecte seus canais ao channel manager certificado. A conta fica pronta em minutos e os canais costumam ser conectados no mesmo dia.")]),
"fr": dict(title="Comparatif logiciels hôteliers 2026 : prix, IA | Hostlio Pro",
  desc="Comparatif logiciels hôteliers 2026 : Hostlio Pro face à HotelRunner, Cloudbeds, Mews et Amenitiz sur les prix, commissions, essai gratuit et IA sur WhatsApp.",
  crumb="Comparatif logiciels hôteliers", h1='Comparatif des logiciels hôteliers : <em class="hl">Hostlio Pro</em> et les autres (2026)',
  lead="Un abonnement mensuel fixe, aucune commission sur les réservations, des tarifs publics et un assistant IA sur WhatsApp dans tous les forfaits. Voici Hostlio Pro face à des logiciels répandus chez les hôtels indépendants, d’après ce que publie chaque entreprise.",
  tbl_h="Hostlio Pro et les autres logiciels hôteliers", tbl_p="Les informations sur les concurrents proviennent des pages officielles de tarifs et de produits de chaque entreprise, vérifiées le 8 octobre 2026.",
  cols=["Logiciel", "Tarifs publics ?", "À partir de", "Commission sur les réservations", "Essai gratuit", "Messagerie client IA sur WhatsApp"],
  rows=[("Hostlio Pro", "Oui", "⟦price:starter⟧/mois (early bird)", "Aucune, abonnement mensuel fixe", "7 jours", "Tous les forfaits (Lio, plus de 30 langues)"),
        ("HotelRunner", "Oui (offres Essential)", "Minimum 19,95 $/mois + 0,75 % du chiffre d’affaires des réservations (Essential Manage)", "0,75 à 1,25 % du chiffre d’affaires mensuel des réservations (offres Essential)", "« Start free trial » proposé ; durée non indiquée", "Assistant IA dans les offres Advanced (prix sur demande) ; WhatsApp non mentionné sur les pages consultées"),
        ("Elektraweb", "Non ; la page tarifs renvoie vers un formulaire de devis", "Devis", "Non indiqué sur la page tarifs", "Non indiqué ; démo gratuite", "Assistant IA décrit sur ses pages WhatsApp API et Smart Chat (prix sur devis)"),
        ("Cloudbeds", "Non, sur devis", "Devis", "Indique ne pas ajouter de commission sur les réservations du Booking Engine et du Channel Manager", "Non mentionné sur la page tarifs ; démo proposée", "Chatbot IA via WhatsApp et SMS ; Guest Experience figure dans l’offre Experience"),
        ("Mews", "Non, sur devis (prix par chambre)", "Devis", "Non indiqué sur la page tarifs", "Non mentionné sur la page tarifs", "« AI messaging via WhatsApp and SMS » dans Mews Pro"),
        ("Amenitiz", "Non, devis selon le nombre de chambres", "Devis", "Aucune commission sur les réservations directes ; AmenitizPay 1,5 % + 0,25 € par transaction", "Non proposé ; démo gratuite", "« Messagerie client + WhatsApp » dans l’offre Advanced (mention « disponible en juin »)")],
  srcs=["ew_pr", "am_fr", "hr_en", "cb_pr", "cb_ge", "mews_pr"],
  links_h="Comparatifs détaillés",
  faq=[("Qu’est-ce qu’un logiciel de gestion hôtelière ?", "Un logiciel de gestion hôtelière (PMS) permet à un établissement de gérer réservations, disponibilités, canaux de vente et données clients au même endroit."),
       ("Combien coûte un logiciel hôtelier ?", "Parmi les éditeurs du tableau, Hostlio Pro et HotelRunner publient leurs prix : Hostlio Pro démarre à ⟦price:starter⟧ par mois en abonnement fixe ; les offres Essential de HotelRunner ont un minimum de 19,95 $ par mois plus un pourcentage du chiffre d’affaires des réservations. Elektraweb, Cloudbeds, Mews et Amenitiz fonctionnent sur devis (8 octobre 2026)."),
       ("Commission ou abonnement fixe : que choisir ?", "Quand le taux d’occupation et le prix moyen augmentent, un coût lié au chiffre d’affaires augmente aussi. Un abonnement fixe rend le budget prévisible : avec Hostlio Pro, la facture ne change pas en haute saison."),
       ("Puis-je passer à Hostlio Pro depuis mon logiciel actuel ?", "Oui. Importez vos réservations depuis un fichier CSV ou Excel (avec correspondance des colonnes et contrôle des doublons) et connectez vos canaux au channel manager certifié. Le compte est prêt en quelques minutes et les canaux sont souvent connectés le jour même.")]),
}

HUB = {
"tr": dict(title="Otel Programı Karşılaştırmaları | Hostlio Pro",
  desc="Hostlio Pro'yu HotelRunner ve diğer otel programlarıyla karşılaştırın: sabit aylık ücret, rezervasyon komisyonu yok, her planda WhatsApp'ta AI.",
  crumb="Karşılaştırmalar", h1='Neden <em class="hl">Hostlio Pro</em>? Otel programı karşılaştırmaları',
  lead="Sabit aylık ücret, rezervasyon komisyonu yok, fiyatlar sitede açık ve her planda WhatsApp'ta AI asistan. Karşılaştırmalarımız rakip bilgisini yalnızca firmaların kendi resmî sayfalarından alır ve tarihlidir.",
  list_h="Karşılaştırmalar", general="Genel karşılaştırma: Hostlio Pro, HotelRunner, Elektraweb, Cloudbeds, Mews ve Amenitiz", prices="Otel programı fiyatları 2026"),
"en": dict(title="Hotel Software Comparisons & Alternatives | Hostlio Pro",
  desc="Compare Hostlio Pro with HotelRunner, Cloudbeds, Amenitiz and HiJiffy: a flat monthly fee, no booking commission and AI on WhatsApp in every plan.",
  crumb="Comparisons", h1='Why <em class="hl">Hostlio Pro</em>? Hotel software comparisons',
  lead="A fixed monthly price, no booking commission, prices on the website and an AI assistant on WhatsApp in every plan. Our comparisons take competitor information only from each company's official pages, and they're dated.",
  list_h="Comparisons", general="Overview: Hostlio Pro, HotelRunner, Elektraweb, Cloudbeds, Mews and Amenitiz"),
"es": dict(title="Comparativas de software hotelero | Hostlio Pro",
  desc="Compara Hostlio Pro con Cloudbeds y otras alternativas: cuota mensual fija, sin comisión por reserva e IA en WhatsApp en todos los planes.",
  crumb="Comparativas", h1='¿Por qué <em class="hl">Hostlio Pro</em>? Comparativas de software hotelero',
  lead="Cuota mensual fija, sin comisión por reserva, precios publicados y un asistente de IA en WhatsApp en todos los planes. Nuestras comparativas toman la información de la competencia solo de sus páginas oficiales y llevan fecha.",
  list_h="Comparativas", general="Visión general: Hostlio Pro, HotelRunner, Cloudbeds, Mews y Amenitiz"),
"pt": dict(title="Comparativos de sistemas para hotel | Hostlio Pro",
  desc="Compare o Hostlio Pro com Cloudbeds, HiJiffy e outras alternativas: mensalidade fixa, sem comissão por reserva e IA no WhatsApp em todos os planos.",
  crumb="Comparativos", h1='Por que o <em class="hl">Hostlio Pro</em>? Comparativos de sistemas para hotel',
  lead="Mensalidade fixa, sem comissão por reserva, preços publicados e um assistente de IA no WhatsApp em todos os planos. Nossos comparativos usam informações de concorrentes só das páginas oficiais de cada empresa e têm data.",
  list_h="Comparativos", general="Visão geral: Hostlio Pro, HotelRunner, Cloudbeds, Mews e Amenitiz"),
"fr": dict(title="Comparatifs de logiciels hôteliers | Hostlio Pro",
  desc="Comparez Hostlio Pro à Amenitiz et à d’autres logiciels hôteliers : abonnement fixe, aucune commission, IA sur WhatsApp partout.",
  crumb="Comparatifs", h1='Pourquoi <em class="hl">Hostlio Pro</em> ? Comparatifs de logiciels hôteliers',
  lead="Un abonnement mensuel fixe, aucune commission sur les réservations, des tarifs publics et un assistant IA sur WhatsApp dans tous les forfaits. Nos comparatifs ne reprennent que les informations publiées par chaque concurrent sur ses pages officielles, et ils sont datés.",
  list_h="Comparatifs", general="Vue d’ensemble : Hostlio Pro, HotelRunner, Cloudbeds, Mews et Amenitiz"),
}
HUB_KEYS = ["vs-hotelrunner", "vs-elektraweb", "vs-cloudbeds", "alt-cloudbeds", "alt-amenitiz", "alt-hijiffy"]

# ---------------------------------------------------------------- rendering (mevcut bileşenler: page-hero, support, steps, table-wrap, related-list)
def _plain(s): return s.replace('<em class="hl">', "").replace("</em>", "")

def _yes(B): return f'<span class="yes">{B.icon("check", "")}</span>'

def _cta(lang, B, extra=""):
    c = C[lang]
    return f'<div class="cta-row"{extra}>{B.btn(c["trial"], B.SIGNUP_URL)}{B.btn(c["pricing"], B.url("pricing", lang), "ghost")}</div>'

def _hero(d, lang, B):
    trust = "".join(f'<li>{_yes(B)}{t}</li>' for t in C[lang]["trust"])
    return (f'<section class="page-hero"><div class="wrap"><h1>{d["h1"]}</h1><p class="lead">{d["lead"]}</p>{_cta(lang, B)}'
            f'<ul class="cmp-trust">{trust}</ul></div></section>')

def _why(lang, B, h=None):
    cards = "".join(f'<article><span class="ai">{B.icon(ic)}</span><h3>{t}</h3><p>{p}</p></article>' for ic, t, p in BEN[lang])
    return (f'<section style="padding-top:0"><div class="wrap"><h2 style="margin-bottom:28px">{h or C[lang]["why_h"]}</h2>'
            f'<div class="support cmp-why">{cards}</div></div></section>')

def _sources(lang, keys, B):
    c = C[lang]
    links = " · ".join(f'<a href="{SRC[k][1]}" rel="nofollow noopener">{html.escape(SRC[k][0])}</a>' for k in keys)
    return (f'<div class="cmp-src small muted"><p><strong>{c["src_h"]}.</strong> {c["src_lead"].format(d=DATE_TXT[lang])}: {links}</p>'
            f'<p>{c["note"].format(contact=B.url("contact", lang))}</p></div>')

def _vs_table(d, lang, B):
    c = C[lang]
    rows = "".join(f'<tr><th scope="row">{lbl}</th><td class="hl">{_yes(B)}{hv}</td><td>{cv}</td></tr>' for lbl, hv, cv in d["rows"])
    return (f'<div class="table-wrap" style="margin-top:24px"><table class="cmp cmp-3"><caption class="sr-only">{html.escape(c["tbl_h"].format(x=d["name"]))}, {c["asof"]}</caption>'
            f'<thead><tr><th scope="col">{c["asof"]}</th><th scope="col" class="hl">Hostlio Pro</th><th scope="col">{d["name"]}</th></tr></thead><tbody>{rows}</tbody></table></div>')

def _multi_table(cols, rows, caption):
    head = "".join(f'<th scope="col">{x}</th>' for x in cols)
    body = ""
    for r in rows:
        cls = ' class="hl"' if r[0] == "Hostlio Pro" else ""
        body += f'<tr{cls}><th scope="row">{r[0]}</th>' + "".join(f"<td>{x}</td>" for x in r[1:]) + "</tr>"
    return (f'<div class="table-wrap" style="margin-top:24px"><table class="cmp cmp-rows"><caption class="sr-only">{html.escape(caption)}</caption>'
            f'<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>')

def hr_table(lang):
    hd = {"tr": ("Aylık rezervasyon geliri", "HotelRunner Essential Sell (%1,25, asgari $29,95)", "Hostlio Pro"),
          "en": ("Monthly booking revenue", "HotelRunner Essential Sell (1.25%, min. $29.95)", "Hostlio Pro")}[lang]
    rows = "".join(f'<tr><th scope="row" class="num">{_usd(r, lang)}</th><td class="num">{_usd(round(hr_sell_fee(r), 2), lang)}</td><td class="num hl">⟦price:pro⟧</td></tr>' for r in HR_EXAMPLES)
    return (f'<div class="table-wrap" style="margin-top:16px"><table class="cmp cmp-3"><thead><tr><th scope="col">{hd[0]}</th><th scope="col">{hd[1]}</th><th scope="col" class="hl">{hd[2]}</th></tr></thead><tbody>{rows}</tbody></table></div>')

def _fit(lang):
    return f'<h2 style="margin-top:64px">{C[lang]["fit_h"]}</h2><div class="answer"><p>{FIT[lang]}</p></div>'

CTA_GAP = ' style="margin-top:32px"'
def _switch(lang, B, name=None, frm=None, override=None):
    c = C[lang]
    h = (override or c["switch_h"].format(x=name)) if name else c["switch_gen"]
    steps = "".join(f'<li><h3>{t}</h3><p>{p.format(frm=frm or FRM[lang])}</p></li>' for t, p in SWITCH[lang])
    return (f'<section class="dark"><div class="wrap"><div class="section-head"><h2>{h}</h2><p>{c["switch_p"]}</p></div>'
            f'<ol class="steps four">{steps}</ol>{_cta(lang, B, CTA_GAP)}</div></section>')

def _more(key, lang, B):
    c = C[lang]
    ks = [k for k in HUB_KEYS if k != key and lang in B.ROUTES[k]]
    items = [(B.url(k, lang), P[k][lang]["card"]) for k in ks]
    if key != "compare": items.append((B.url("compare", lang), HUB[lang]["general"] if lang in HUB else GEN[lang]["tbl_h"]))
    lis = "".join(f'<li><a href="{u}">{html.escape(t)}</a></li>' for u, t in items)
    hub = f'<a href="{B.url("cmp-hub", lang)}">{c["hub_link"]}</a> · ' if lang in B.ROUTES["cmp-hub"] else ""
    if not lis: return ""
    return (f'<section style="padding-top:clamp(48px,6vw,80px);padding-bottom:0"><div class="wrap"><h2 style="font-size:var(--t-2);margin-bottom:20px">{c["more_h"]}</h2>'
            f'<ul class="related-list">{lis}</ul><p class="small" style="margin-top:16px">{hub}<a href="{B.url("tools", lang)}">{c["tools"]}</a></p></div></section>')

def vs_page(key, lang, B):
    d = P[key][lang]; c = C[lang]
    calc = ""
    if key == "vs-hotelrunner":
        calc = f'<h2 style="margin-top:64px">{d["calc_h"]}</h2><p style="max-width:75ch">{d["calc_p"]}</p>{hr_table(lang)}<p style="max-width:75ch;margin-top:14px">{d["calc_after"]}</p>'
    table = f'''<section class="white"><div class="wrap">
<h2>{c["tbl_h"].format(x=d["name"])}</h2>{_vs_table(d, lang, B)}{_sources(lang, d["srcs"], B)}
{calc}{_fit(lang)}
</div></section>'''
    return (_hero(d, lang, B) + _why(lang, B) + table
            + _switch(lang, B, None if d.get("gen_switch") else d["name"], d.get("frm"), d.get("switch_h")) + _more(key, lang, B))

def alt_page(key, lang, B):
    d = P[key][lang]; c = C[lang]
    alts = _multi_table(ALT_COLS[lang], ALTS[lang], f'{d["alt_h"]}, {c["asof"]}')
    ask = "".join(f'<div class="row"><h3>{q}</h3><div><p>{_yes(B)}{a}</p></div></div>' for q, a in d["ask"])
    body = f'''<section class="white"><div class="wrap">
<h2>{d["alt_h"]}</h2><p style="max-width:75ch">{d["alt_p"]}</p>{alts}{_sources(lang, d["srcs"], B)}
<h2 style="margin-top:64px">{d["ask_h"]}</h2><div class="rows cmp-ask">{ask}</div>
{_fit(lang)}
</div></section>'''
    return _hero(d, lang, B) + _why(lang, B) + body + _switch(lang, B, d["name"], d.get("frm")) + _more(key, lang, B)

def general_page(lang, B):
    """Genel karşılaştırma sayfası (rota "compare", 6 dil): Hostlio Pro önce, diğerleri tabloda özet."""
    d = GEN[lang]; c = C[lang]
    links = [(B.url(k, lang), P[k][lang]["card"]) for k in HUB_KEYS if lang in B.ROUTES[k]]
    lis = "".join(f'<li><a href="{u}">{html.escape(t)}</a></li>' for u, t in links)
    linkblock = (f'<h2 style="margin-top:64px;font-size:var(--t-2)">{d["links_h"]}</h2><ul class="related-list" style="margin-top:20px">{lis}</ul>' if lis else "")
    body = (_hero(d, lang, B) + _why(lang, B) +
            f'''<section class="white"><div class="wrap">
<h2>{d["tbl_h"]}</h2><p style="max-width:75ch">{d["tbl_p"]}</p>{_multi_table(d["cols"], d["rows"], _plain(d["h1"]))}{_sources(lang, d["srcs"], B)}
{_fit(lang)}{linkblock}
</div></section>''' + _switch(lang, B))
    return {"key": "compare", "title": d["title"], "desc": d["desc"], "trail": [(d["crumb"], B.url("compare", lang))], "body": body, "faq": d["faq"]}

def hub_page(lang, B):
    d = HUB[lang]
    ks = [k for k in HUB_KEYS if lang in B.ROUTES[k]]
    cards = [(B.url(k, lang), P[k][lang]["card"], P[k][lang]["desc"]) for k in ks]
    cards.append((B.url("compare", lang), d["general"], GEN[lang]["desc"]))
    if lang == "tr" and "post-prices" in B.ROUTES: cards.append((B.url("post-prices", "tr"), d["prices"], ""))
    items = "".join(f'<li><a href="{u}">{html.escape(t)}</a>' + (f'<p>{html.escape(pricing.fill(ds, lang))}</p>' if ds else "") + '</li>' for u, t, ds in cards)
    body = (_hero(d, lang, B)
            + f'<section style="padding-top:0" class="related"><div class="wrap"><h2 style="margin-bottom:20px">{d["list_h"]}</h2><ul class="related-list">{items}</ul>'
              f'<p class="small muted" style="margin-top:16px"><a href="{B.url("tools", lang)}">{C[lang]["tools"]}</a></p></div></section>'
            + _why(lang, B) + f'<section class="white"><div class="wrap">{_fit(lang).replace("margin-top:64px", "margin-top:0")}</div></section>' + _switch(lang, B))
    return {"key": "cmp-hub", "title": d["title"], "desc": d["desc"], "trail": [(d["crumb"], B.url("cmp-hub", lang))], "body": body, "page_type": "CollectionPage"}

def pages(lang, B):
    out = []
    if lang in B.ROUTES["cmp-hub"]: out.append(hub_page(lang, B))
    for key in HUB_KEYS:
        if lang not in B.ROUTES[key]: continue
        d = P[key][lang]
        body = vs_page(key, lang, B) if "rows" in d else alt_page(key, lang, B)
        out.append({"key": key, "title": d["title"], "desc": d["desc"], "body": body, "faq": d["faq"],
                    "trail": [(HUB[lang]["crumb"], B.url("cmp-hub", lang)), (d["crumb"], B.url(key, lang))]})
    return out
