"""Takvim yazısı (öne alındı, 12 Ekim 2026): "Channel manager per piccole strutture" — yalnız IT.
GSC: "channel manager per piccole strutture" 10,4. sıra (yazı yokken). Resmî siteler 12 Ekim 2026: SiteMinder (İtalya fiyat akışı,
IVA belirtilmemiş: 10 cam. 95 €, 21–30 cam. 139 €), Smoobu, Octorate, Beds24, RoomRaccoon, TeamSystem, WuBook, Zucchetti grubu.
Booking.com Premier (%10–15) ve Airbnb Preferred+ resmî sayfalardan; Channex'in statüsü Channex'in, Hostlio'nun değil."""
import html

SRC = [
 ("SiteMinder: prezzi", "https://www.siteminder.com/it/prezzi/"),
 ("Smoobu: prezzi", "https://www.smoobu.com/it/prezzi/"),
 ("Octorate: prezzi", "https://www.octorate.com/it/prezzi/"),
 ("Beds24: pricing", "https://beds24.com/pricing.html"),
 ("RoomRaccoon: prezzi", "https://roomraccoon.it/prezzi/"),
 ("TeamSystem Hospitality: prezzi", "https://www.teamsystem.com/horeca/ts-hospitality/prezzi/prezzi-hotel-bb-agriturismo/"),
 ("WuBook: channel manager", "https://wubook.net/page/channel-manager-11.html"),
 ("Kross Booking", "https://www.krossbooking.com/it/"),
 ("Vertical Booking: channel manager", "https://www.verticalbooking.com/en/our-solutions/channel-manager/"),
 ("Bedzzle: prezzi", "https://www.bedzzle.com/it/prezzi"),
 ("Booking.com: soluzioni tecnologiche (Premier provider)", "https://partner.booking.com/it/soluzioni-tecnologiche-case"),
 ("Booking.com: scegliere il connectivity provider giusto", "https://partner.booking.com/en-us/solutions/advice/choosing-right-connectivity-provider"),
 ("Airbnb: Preferred Software Partners 2025", "https://news.airbnb.com/announcing-our-2025-preferred-software-partners/"),
]

def _tbl(head, rows):
    h = "".join(f'<th scope="col">{x}</th>' for x in head)
    b = "".join(("<tr class=\"hl\">" if r[0] == "Hostlio Pro" else "<tr>") + f'<th scope="row">{r[0]}</th>'
                + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table class="cmp"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

META = {"it": dict(key="post-cmit", date="2026-10-12", title="Channel manager per piccole strutture: come scegliere (2026)",
                   desc="Channel manager per B&B, affittacamere e piccoli hotel: cosa conta davvero, prezzi pubblicati per 10 e 25 camere, Premier e Preferred+. Fonti ufficiali.")}

def it(U):
    from build import btn, SIGNUP_URL
    cta = btn("Prova gratis per ⟦trial⟧ giorni", SIGNUP_URL) + btn("Vedi il channel manager", U("channel"), "ghost")
    rows = [
      ("Hostlio Pro", "PMS + channel manager + assistente AI", "Oltre 100 OTA", "Canone fisso: ⟦price:starter⟧ / ⟦price:pro⟧ / ⟦price:growth⟧ al mese", "⟦trial⟧ giorni"),
      ("SiteMinder", "Channel manager (anche offerta Plus)", "Oltre 450 canali", "10 camere 95&nbsp;€, 21–30 camere 139&nbsp;€ al mese (IVA non specificata)", "14 giorni"),
      ("TeamSystem Hospitality (ex Hotel in Cloud)", "PMS con channel manager incluso", "Non indicato", "Da 360&nbsp;€ + IVA l'anno (1–3 camere)", "14 giorni"),
      ("Octorate", "Suite; Basic = channel manager + booking engine", "Oltre 160 canali", "Basic da 8&nbsp;€ a camera al mese", "14 giorni"),
      ("Zak / WuBook", "Suite con channel manager", "Oltre 100 OTA", "Su misura", "Su richiesta"),
      ("Kross Booking", "PMS + channel manager", "Non indicato", "Su richiesta", "Demo 30 giorni"),
      ("Smoobu", "PMS + channel manager, soprattutto affitti brevi", "Oltre 100 portali", "Da 29&nbsp;€ al mese + 0,9% a prenotazione, o 35&nbsp;€ prepagato (prima unità)", "14 giorni"),
      ("RoomRaccoon", "Suite", "3 canali in Entry, 5 in Essential", "Entry 164&nbsp;€ al mese fino a 18 camere", "Dopo una demo"),
      ("Beds24", "PMS + channel manager a consumo", "Oltre 60 canali", "12,90&nbsp;€ + 2,60&nbsp;€ a camera + 0,55&nbsp;€ per collegamento", "Gratuita"),
      ("Gruppo Zucchetti (Vertical Booking, Ericsoft, Bedzzle)", "CRS o moduli del PMS", "Vertical Booking: oltre 450 canali", "Su preventivo", "Demo"),
    ]
    ex = [
      ("Hostlio Pro", "⟦price:starter⟧ (Starter)", "⟦price:pro⟧ (Pro)", "PMS e AI inclusi"),
      ("SiteMinder", "95&nbsp;€", "139&nbsp;€", "Solo channel manager; IVA non specificata"),
      ("TeamSystem Hospitality", "72&nbsp;€ + IVA", "167,83&nbsp;€ + IVA", "Canone annuale diviso per 12; PMS incluso"),
      ("Beds24", "42,20&nbsp;€", "84,50&nbsp;€", "3 e 4 tipologie su 2 e 3 OTA"),
      ("RoomRaccoon Entry", "164&nbsp;€", "228&nbsp;€", "Solo 3 canali"),
    ]
    c = f'''<div class="answer"><p><strong>In breve:</strong> per un B&amp;B, un affittacamere o un piccolo hotel il channel manager giusto è quello che si collega direttamente a Booking.com, Airbnb ed Expedia con una connessione di qualità, include tutti i canali che usi senza costi a canale, fa parte del gestionale (così non inserisci tutto due volte) e ha un prezzo chiaro. Tra i fornitori che pubblicano i prezzi, per 10 camere si va da circa 42 a 164&nbsp;€ al mese.</p></div>
<p class="small muted">Hostlio Pro è uno dei prodotti confrontati, quindi non siamo neutrali. Abbiamo usato solo informazioni pubblicate sui siti ufficiali dei fornitori, di Booking.com e di Airbnb, consultati il 12 ottobre 2026. I prezzi cambiano: verifica sempre sul sito del fornitore.</p>
<h2>A cosa serve un channel manager</h2>
<p>Il <a href="{U("channel")}">channel manager</a> invia disponibilità, prezzi e restrizioni a tutti i portali da un unico pannello e chiude la camera ovunque appena arriva una prenotazione. È quello che evita l'<a href="{U("post-overbooking")}">overbooking</a> e ti risparmia di aggiornare a mano ogni extranet. Per la differenza con il gestionale leggi <a href="{U("post-pms-vs-cm")}">channel manager e PMS: che differenza c'è</a>.</p>
<h2>5 cose da controllare in una piccola struttura</h2>
<ol><li><strong>Qualità della connessione.</strong> Booking.com riconosce come "Premier" solo i fornitori con le connessioni migliori: secondo Booking.com è un livello che ogni anno raggiunge solo il 10–15% dei partner. Airbnb distingue i partner "Preferred" da quelli "Preferred+", che superano i suoi requisiti dopo una verifica di sicurezza e qualità dell'API.</li>
<li><strong>Canali inclusi.</strong> Alcune offerte d'ingresso limitano a 3 o 5 canali, altre fanno pagare ogni collegamento. Conta i portali che usi oggi e quelli che vuoi aggiungere.</li>
<li><strong>Gestionale integrato.</strong> Un channel manager separato significa due programmi, due abbonamenti e il rischio di disallineamenti tra planning e portali.</li>
<li><strong>Costo annuo completo.</strong> Canone, IVA, attivazione, moduli e commissioni a prenotazione. Una commissione dello 0,9% sembra poca, ma in alta stagione pesa.</li>
<li><strong>Prova gratuita.</strong> Collega almeno un portale durante la prova e cambia il prezzo di un giorno: verifica che arrivi nell'extranet.</li></ol>
<h2>Tabella di confronto</h2>
{_tbl(["Soluzione", "Tipo", "Canali dichiarati", "Prezzo", "Prova"], rows)}
<h2>Quanto costa per 10 e 25 camere</h2>
<p>Canone mensile dai prezzi pubblicati e dai calcolatori ufficiali; i fornitori su preventivo non sono inclusi. Non tutti includono il gestionale: confronta anche cosa ottieni.</p>
{_tbl(["Soluzione", "10 camere", "25 camere", "Nota"], ex)}
<h2>Le soluzioni una per una</h2>
<p><strong>SiteMinder</strong> è il channel manager con più canali (oltre 450) e pubblica un listino per l'Italia: 95&nbsp;€ al mese per 10 camere. È un prodotto a sé: il gestionale va scelto a parte o con l'offerta Little Hotelier dello stesso gruppo. <strong>TeamSystem Hospitality</strong> (l'ex Hotel in Cloud) include channel manager, PMS e fatturazione elettronica in un unico piano con prezzo pubblicato. <strong>Octorate</strong> parte da 8&nbsp;€ a camera con il piano Basic, che però comprende channel manager e booking engine ma non il PMS. <strong>Zak di WuBook</strong> e <strong>Kross Booking</strong> sono soluzioni italiane complete, con prezzi su richiesta. <strong>Smoobu</strong> è pensato soprattutto per affitti brevi e case vacanza; il piano Flex aggiunge lo 0,9% a prenotazione. <strong>RoomRaccoon</strong> limita il piano d'ingresso a 3 canali. <strong>Beds24</strong> è il più economico all'inizio, ma si paga a camera e a collegamento e la configurazione è più tecnica. Le soluzioni del <strong>gruppo Zucchetti</strong> (Vertical Booking, Ericsoft, Bedzzle) sono su preventivo e guardano soprattutto a hotel medi, grandi e catene.</p>
<h2>Hostlio Pro: dove si colloca</h2>
<p>In Hostlio Pro il channel manager è incluso in ogni piano, insieme a PMS, planning delle camere, app mobile e Lio, l'assistente AI che risponde agli ospiti su WhatsApp nella loro lingua. Le connessioni verso oltre 100 OTA passano dall'infrastruttura di Channex, che Booking.com indica tra i suoi Premier provider consigliati e che Airbnb ha inserito tra i partner Preferred+ del 2025: è lo status di Channex, non di Hostlio Pro. Il prezzo è pubblicato e fisso, senza commissioni sulle prenotazioni e senza costi a canale. Cosa non fa: non invia i dati ad <a href="{U("post-alloggiati")}">Alloggiati Web</a> e non gestisce fatturazione elettronica SDI né registratore telematico.</p>
<div class="cta-row" style="margin-top:12px">{cta}</div>
<p>Per un confronto più ampio leggi anche <a href="{U("post-gestionali")}">i gestionali per hotel più usati nel 2026</a>.</p>
'''
    lis = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(n)}</a></li>' for n, u in SRC)
    c += f'<h2>Fonti</h2><p class="small muted">Tutte le fonti sono state consultate il 12 ottobre 2026. I prezzi per l\'Italia di SiteMinder provengono dal listino ufficiale caricato dalla sua pagina prezzi; quelli di Beds24 e RoomRaccoon dai calcolatori ufficiali.</p><ul>{lis}</ul>'
    faq = [("Quale channel manager scegliere per un B&B?", "Uno con connessione diretta a Booking.com, Airbnb ed Expedia, canali inclusi senza costi aggiuntivi, integrato nel gestionale e con un prezzo chiaro. Provalo gratuitamente collegando almeno un portale."),
           ("Quanto costa un channel manager per 10 camere?", "Tra i fornitori che pubblicano i prezzi, circa 42–164&nbsp;€ al mese (12 ottobre 2026). Alcuni includono anche il gestionale, altri no."),
           ("Cosa significa Booking.com Premier provider?", "È il livello più alto del programma di connettività di Booking.com: secondo Booking.com lo raggiunge ogni anno solo il 10–15% dei fornitori, per qualità e affidabilità della connessione."),
           ("Il channel manager è incluso in Hostlio Pro?", "Sì, in tutti i piani, con connessioni verso oltre 100 OTA e senza commissioni sulle prenotazioni.")]
    return c, faq

FN = {"it": it}
