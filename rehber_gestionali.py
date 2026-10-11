"""Takvim yazısı (22 Ekim 2026 planı): "I gestionali per hotel più usati nel 2026" — yalnız IT.
Resmî siteler 12 Ekim 2026. İtalya için açık pazar payı verisi yok ⇒ sıralama yok; müşteri sayıları firma beyanı.
Hotel in Cloud → TeamSystem Hospitality; Ericsoft/Bedzzle/5stelle* Zucchetti grubu. Kross Booking (site 2019'da kalmış),
Scrigno (GP Dati, zincir odaklı), protel, Leonardo, Sirvoy (İtalyanca site yok) bilerek dışarıda.
Hostlio'nun Alloggiati'ye GÖNDERMEDİĞİ ve RT/SDI sunmadığı açıkça yazılır."""
import html

SRC = [
 ("TeamSystem Hospitality: prezzi", "https://www.teamsystem.com/horeca/ts-hospitality/prezzi/prezzi-hotel-bb-agriturismo/"),
 ("Zak by WuBook", "https://wubook.net/page/gestionale-hotel-bb-case-vacanze-9.html"),
 ("Slope", "https://www.slope.it/"),
 ("Octorate: prezzi", "https://www.octorate.com/it/prezzi/"),
 ("Bedzzle", "https://www.bedzzle.com/it/"),
 ("5stelle*", "https://www.hotelcinquestelle.cloud/"),
 ("Ericsoft", "https://www.ericsoft.com/it/"),
 ("Passepartout: gestionale hotel", "https://www.passepartout.net/software/gestionale-hotel"),
 ("RoomRaccoon: prezzi", "https://roomraccoon.it/prezzi/"),
 ("Mews: pricing", "https://www.mews.com/en/pricing"),
 ("Cloudbeds: Italy compliance", "https://www.cloudbeds.com/government-compliance/italy/"),
 ("Beds24: pricing", "https://beds24.com/en/pricing/pricing"),
]

def _tbl(head, rows):
    h = "".join(f'<th scope="col">{x}</th>' for x in head)
    b = "".join(("<tr class=\"hl\">" if r[0] == "Hostlio Pro" else "<tr>") + f'<th scope="row">{r[0]}</th>'
                + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table class="cmp"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

META = {"it": dict(key="post-gestionali", date="2026-10-12", title="I gestionali per hotel più usati nel 2026: confronto onesto",
                   desc="Gestionali per hotel e B&B in Italia nel 2026: TeamSystem, Zak, Slope, Octorate, Zucchetti, Passepartout e altri. Prezzi, Alloggiati Web, SDI.")}

def it(U):
    from build import btn, SIGNUP_URL
    cta = btn("Prova gratis per ⟦trial⟧ giorni", SIGNUP_URL) + btn("Vedi i piani", U("pricing"), "ghost")
    rows = [
      ("Hostlio Pro", "PMS in cloud + channel manager + assistente AI", "Canone fisso pubblicato: ⟦price:starter⟧ / ⟦price:pro⟧ / ⟦price:growth⟧ al mese", "Non invia (dati raccolti con il check-in online)", "No"),
      ("TeamSystem Hospitality (ex Hotel in Cloud)", "PMS in cloud, channel manager e booking engine inclusi", "Pubblicato: da 360&nbsp;€ + IVA l'anno (1–3 camere); oltre 30 camere su richiesta", "Comunicazioni ISTAT/Alloggiati dichiarate", "Fatturazione elettronica inclusa; corrispettivi telematici"),
      ("Zak (WuBook)", "Suite in cloud: PMS, channel manager, booking engine", "Su misura", "Invio automatico ad Alloggiati e ISTAT dichiarato", "Fatture elettroniche allo SDI"),
      ("Slope", "PMS in cloud per hotel medi e grandi", "Su preventivo, canone annuale", "Invio schedine PS, ISTAT, tassa di soggiorno dichiarato", "Fatture XML e integrazione con registratori telematici"),
      ("Octorate", "Suite in cloud; il piano Basic è solo channel manager e booking engine", "Basic da 8&nbsp;€ a camera al mese; Pro e Ultimate su richiesta", "ISTAT e Alloggiati Web tra le funzioni del PMS", "Non dichiarato"),
      ("Bedzzle (Zucchetti)", "PMS in cloud con channel manager e booking engine", "Su misura", "Invio del tracciato al portale dichiarato", "Invio allo SDI e stampanti RT"),
      ("5stelle* (Zucchetti)", "PMS in cloud per hotel e gruppi", "Avviamento + canone annuo per camere, su richiesta", "Genera il file per Alloggiati Web", "Ciclo SDI completo e stampante RT"),
      ("Ericsoft (Zucchetti)", "Suite per hotel e catene", "Non pubblicato", "Non indicato in pagina", "Fatturazione elettronica"),
      ("Passepartout Welcome", "Gestionale con versione cloud (Smart Cloud fino a 15 camere)", "Su preventivo", "Invio automatizzato a Questura e ISTAT dichiarato", "XML per SDI (invio a pagamento), registratori telematici"),
      ("RoomRaccoon", "PMS all-in-one con channel manager", "Da 164&nbsp;€ al mese (Entry) secondo il calcolatore", "Modulo Alloggiati Web dichiarato", "SDI e stampanti fiscali Epson"),
      ("Cloudbeds", "Piattaforma in cloud", "Su preventivo", "Servizio Alloggiati o esportazione manuale", "Ricevute fiscali Epson"),
      ("Mews", "Piattaforma in cloud", "Su preventivo, per camera", "Non verificato", "Non verificato"),
      ("Beds24", "PMS e channel manager a consumo", "12,90&nbsp;€ + 2,60&nbsp;€ a camera + 0,55&nbsp;€ per collegamento", "Non verificato", "Non verificato"),
    ]
    ex = [
      ("Hostlio Pro", "⟦price:starter⟧ (Starter)", "⟦price:pro⟧ (Pro)", "Channel manager e AI inclusi"),
      ("TeamSystem Hospitality", "72&nbsp;€ + IVA", "167,83&nbsp;€ + IVA", "Canone annuale (864&nbsp;€ e 2.014&nbsp;€) diviso per 12"),
      ("Beds24", "42,20&nbsp;€", "84,50&nbsp;€", "Con 3 e 4 tipologie su 2 e 3 OTA"),
      ("RoomRaccoon Entry", "164&nbsp;€", "228&nbsp;€", "Secondo il calcolatore; IVA non indicata"),
    ]
    c = f'''<div class="answer"><p><strong>In breve:</strong> in Italia i gestionali per hotel più diffusi tra le strutture indipendenti sono soprattutto prodotti italiani: TeamSystem Hospitality (l'ex Hotel in Cloud), Zak di WuBook, Slope, Octorate, le soluzioni del gruppo Zucchetti (Ericsoft, Bedzzle, 5stelle*) e Passepartout Welcome; tra gli esteri RoomRaccoon, Cloudbeds, Mews e Beds24. Non esistono dati pubblici affidabili sulle quote di mercato, quindi questa non è una classifica. Per un piccolo hotel contano soprattutto tre cose: channel manager incluso, gestione di Alloggiati Web e fatturazione, e un prezzo chiaro.</p></div>
<p class="small muted">Hostlio Pro è uno dei prodotti confrontati, quindi non siamo neutrali. Abbiamo usato solo informazioni pubblicate sui siti ufficiali dei fornitori, consultati il 12 ottobre 2026; i numeri di clienti sono dichiarazioni dei fornitori. Prezzi e funzioni cambiano: verifica sempre sul sito del fornitore prima di decidere.</p>
<h2>Cosa deve fare un gestionale per hotel in Italia</h2>
<p>Oltre al planning delle camere e alle prenotazioni, in Italia un gestionale viene giudicato su obblighi molto concreti: la comunicazione degli ospiti ad <a href="{U("post-alloggiati")}">Alloggiati Web</a> entro 24 ore, le statistiche ISTAT tramite il sistema regionale, l'imposta di soggiorno del comune e, per chi emette documenti fiscali, fatturazione elettronica (SDI) e registratore telematico. A questo si aggiungono il <a href="{U("channel")}">channel manager</a> per Booking.com, Airbnb ed Expedia e, sempre più spesso, la gestione dei messaggi degli ospiti.</p>
<h2>Tabella di confronto</h2>
{_tbl(["Gestionale", "Cos'è", "Prezzo", "Alloggiati Web", "Fiscale (SDI / RT)"], rows)}
<p class="small muted">"Dichiarato" significa che il fornitore lo indica sul proprio sito; non abbiamo verificato come avviene l'invio (web service o file).</p>
<h2>Quanto costa per 10 e 25 camere</h2>
<p>Canone mensile calcolato dai prezzi pubblicati e dai calcolatori ufficiali. I fornitori che lavorano su preventivo non sono inclusi. I prodotti non includono le stesse funzioni: non decidere solo sul prezzo.</p>
{_tbl(["Gestionale", "10 camere", "25 camere", "Nota"], ex)}
<h2>I gestionali italiani</h2>
<h3>TeamSystem Hospitality (ex Hotel in Cloud)</h3>
<p>Il vecchio Hotel in Cloud oggi è TeamSystem Hospitality. È pensato per ogni tipo di struttura, dall'hotel all'agriturismo fino a B&amp;B e case vacanza. Un unico piano include PMS, channel manager, booking engine e fatturazione elettronica; il prezzo è pubblicato e parte da 360&nbsp;€ + IVA l'anno per 1–3 camere, con 14 giorni di prova gratuita.</p>
<h3>Zak di WuBook</h3>
<p>Suite in cloud di Fano per hotel, B&amp;B, ostelli e case vacanza, con PMS, channel manager e booking engine integrati. Dichiara l'invio automatico ad Alloggiati Web e ISTAT, la tassa di soggiorno e le fatture elettroniche allo SDI. Prezzi su misura; WuBook dichiara oltre 22.000 strutture nel mondo.</p>
<h3>Slope</h3>
<p>PMS in cloud di Perugia, rivolto soprattutto a hotel medi e grandi, gruppi e hotel con ristorante. Dichiara l'invio di schedine alloggiati, ISTAT e tassa di soggiorno e l'integrazione con i registratori telematici. Prezzo su preventivo con canone annuale; dichiara oltre 1.400 strutture italiane.</p>
<h3>Octorate</h3>
<p>Suite in cloud di Roma per hotel, B&amp;B, ostelli e campeggi. Attenzione al piano Basic (da 8&nbsp;€ a camera al mese): comprende channel manager e booking engine ma non il PMS, che è nei piani Pro e Ultimate su richiesta. Ha un agente AI che risponde agli ospiti su WhatsApp, email e canali OTA. 14 giorni di prova.</p>
<h3>Il gruppo Zucchetti: Ericsoft, Bedzzle e 5stelle*</h3>
<p>Tre prodotti diversi dello stesso gruppo. <strong>Ericsoft</strong> si rivolge a hotel e catene e dichiara oltre 4.000 strutture. <strong>Bedzzle</strong> è un PMS in cloud per hotel, residence, agriturismi e B&amp;B, con invio allo SDI e stampanti RT. <strong>5stelle*</strong> è un PMS in cloud per hotel e gruppi con ciclo SDI completo e collegamento alla stampante RT. Nessuno pubblica i prezzi.</p>
<h3>Passepartout Welcome</h3>
<p>Gestionale del gruppo sammarinese Passepartout, con una versione Smart Cloud per strutture fino a 15 camere. Channel manager e booking engine integrati, invio automatizzato dei dati a Questura e ISTAT dichiarato. Prezzo su preventivo.</p>
<h2>I gestionali esteri</h2>
<p><strong>RoomRaccoon</strong> pubblica un calcolatore (da 164&nbsp;€ al mese) e un modulo per Alloggiati Web, SDI e stampanti fiscali. <strong>Cloudbeds</strong> e <strong>Mews</strong> lavorano su preventivo; Cloudbeds offre un servizio per Alloggiati e un'integrazione con ROSS1000. <strong>Beds24</strong> è economico e flessibile, ma non ha un sito in italiano e non abbiamo trovato informazioni sugli adempimenti italiani.</p>
<h2>Hostlio Pro: dove si colloca</h2>
<p>Hostlio Pro è un PMS in cloud per hotel indipendenti, B&amp;B e affittacamere da 1 a 150 camere. Ogni piano include channel manager certificato (oltre 100 OTA), planning delle camere, app mobile e Lio, l'assistente AI che risponde agli ospiti su WhatsApp nella loro lingua con le informazioni del tuo hotel. Il prezzo è pubblicato e fisso, senza commissioni sulle prenotazioni. Per essere chiari su cosa <strong>non</strong> fa: non invia i dati ad Alloggiati Web (li raccoglie con il <a href="{U("checkin")}">check-in online</a>, l'invio resta a te), non gestisce fatturazione elettronica SDI né registratore telematico. Se questi invii automatici sono indispensabili, valuta un gestionale italiano oppure abbina Hostlio Pro al tuo software fiscale.</p>
<div class="cta-row" style="margin-top:12px">{cta}</div>
<h2>Come scegliere</h2>
<ul><li><strong>B&amp;B e piccole strutture:</strong> canone fisso, channel manager incluso e app mobile. Controlla come viene gestito Alloggiati Web.</li>
<li><strong>Hotel indipendenti fino a 150 camere:</strong> sincronizzazione affidabile con le OTA, messaggi degli ospiti in un'unica casella, ruoli per lo staff e costo annuo completo, moduli compresi.</li>
<li><strong>Hotel con ristorante, SPA o più strutture:</strong> le suite più ampie, con POS e ciclo fiscale completo, valgono il preventivo.</li></ul>
<p>Per i criteri nel dettaglio leggi <a href="{U("post-pms")}">come scegliere un gestionale per piccoli hotel</a>.</p>
'''
    lis = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(n)}</a></li>' for n, u in SRC)
    c += f'<h2>Fonti</h2><p class="small muted">Tutte le fonti sono state consultate il 12 ottobre 2026. I prezzi per numero di camere di TeamSystem Hospitality, RoomRaccoon e Beds24 provengono dal calcolatore o dal listino sulla pagina ufficiale.</p><ul>{lis}</ul>'
    faq = [("Qual è il gestionale per hotel più usato in Italia?", "Non esistono dati pubblici affidabili sulle quote di mercato. Tra le strutture indipendenti sono molto diffusi prodotti italiani come TeamSystem Hospitality (ex Hotel in Cloud), Zak di WuBook, Slope, Octorate, le soluzioni Zucchetti (Ericsoft, Bedzzle, 5stelle*) e Passepartout Welcome."),
           ("Quanto costa un gestionale per un hotel di 10 camere?", "Tra i fornitori che pubblicano i prezzi, circa 40–165&nbsp;€ al mese (12 ottobre 2026), a seconda di cosa è incluso. Molti gestionali italiani lavorano su preventivo."),
           ("Il gestionale invia i dati ad Alloggiati Web?", "Dipende dal prodotto: alcuni dichiarano l'invio automatico, altri generano un file da caricare sul portale. Chiedilo sempre prima di scegliere. Hostlio Pro non invia i dati: li raccoglie con il check-in online."),
           ("Posso provare Hostlio Pro gratis?", "Sì, per ⟦trial⟧ giorni. La carta viene registrata all'iscrizione ma non viene addebitato nulla fino alla fine della prova. I piani costano ⟦price:starter⟧, ⟦price:pro⟧ e ⟦price:growth⟧ al mese.")]
    return c, faq

FN = {"it": it}
