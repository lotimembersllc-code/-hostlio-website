from build import btn, icon, logo, url, room_rack, channel_strip, faq_block, SIGNUP_URL, EMAIL, UPDATED, CHECK, software_schema, SITE, PLANS
L = "it"
def U(k): return url(k, L)

_MESI = ["gennaio","febbraio","marzo","aprile","maggio","giugno","luglio","agosto","settembre","ottobre","novembre","dicembre"]
def D(iso):
    y, m, d = iso[:10].split("-")
    return f"{int(d)} {_MESI[int(m)-1]} {y}"

PLAN_TXT = {
 "starter": ("Per piccoli B&B e boutique hotel", ["1 struttura, fino a 10 camere","1.000 messaggi AI / mese","Sincronizzazione con oltre 100 OTA","Messaggi AI su WhatsApp","Planning camere con calendario prenotazioni","Moduli per il visto in PDF automatici"]),
 "pro":     ("Per hotel in crescita con una sola struttura", ["1 struttura, fino a 50 camere","5.000 messaggi AI / mese","Tutto ciò che include Starter","WhatsApp + caselle OTA (Booking.com, Airbnb, Expedia)","Check-in online con firma digitale","Vendita di transfer e tour","App mobile iOS"]),
 "growth":  ("Per team che gestiscono due strutture", ["Fino a 2 strutture, 150 camere","12.000 messaggi AI / mese","Tutto ciò che include Pro","Sincronizzazione dei canali prioritaria","Supporto prioritario (entro il giorno lavorativo successivo)","Chiamata di onboarding personalizzata","Opzioni white-label"]),
}

def plans_html():
    out = []
    for p in PLANS:
        for_, feats = PLAN_TXT[p["id"]]
        pop = p["id"] == "pro"
        lis = "".join(f"<li>{CHECK}<span>{f}</span></li>" for f in feats)
        out.append(f'''<article class="plan{" pop" if pop else ""}" aria-labelledby="plan-{p["id"]}">
{'<span class="tag">Il più scelto</span>' if pop else ""}
<h3 id="plan-{p["id"]}">{p["name"]}</h3><p class="for">{for_}</p>
<div class="price num"><b>${p["price"]}</b><span class="muted">/ mese</span></div>
<p class="small muted num" style="margin:0">Prezzo di lancio (normalmente <s>${p["regular"]}</s>)</p>
<ul>{lis}</ul>
{btn("Inizia con "+p["name"], SIGNUP_URL+"?plan="+p["id"], "primary" if pop else "ghost")}
</article>''')
    return '<div class="plans">' + "".join(out) + "</div>"

FAQ_CORE = [
 ("Che cos'è Hostlio Pro?", "Hostlio Pro è un gestionale per hotel (PMS) basato sull'intelligenza artificiale, pensato per hotel indipendenti, boutique hotel e B&B. Riunisce in un'unica piattaforma Lio, un assistente AI che risponde ai messaggi degli ospiti 24 ore su 24 in oltre 30 lingue, un channel manager collegato a oltre 100 OTA, un calendario delle prenotazioni drag-and-drop e il check-in online."),
 ("Quanto costa Hostlio Pro?", "Ci sono tre piani: Starter a $49/mese, Pro a $89/mese e Growth a $149/mese. Questi prezzi includono uno sconto di lancio del 20% riservato ai primi 50 clienti, bloccato per tutta la durata dell'abbonamento. I prezzi normali sono $59, $109 e $189."),
 ("C'è una prova gratuita?", "Sì. Ogni piano include 7 giorni di prova gratuita. Inserisci un metodo di pagamento all'iscrizione, ma non viene addebitato nulla fino alla fine della prova e puoi disdire in qualsiasi momento prima. Nessun contratto a lungo termine."),
 ("A quali OTA si collega Hostlio Pro?", "Tramite Channex, Hostlio Pro si collega a oltre 100 canali, tra cui Booking.com, Airbnb, Expedia, Agoda, Trip.com, Hotels.com, Hotelbeds, Hostelworld e Google Hotels. Disponibilità, tariffe e prenotazioni restano sincronizzate su tutti."),
 ("In quali lingue risponde Lio?", "Lio risponde in oltre 30 lingue, tra cui inglese, turco, arabo, russo, tedesco, giapponese e cinese. Risponde nella lingua dell'ospite e tu vedi la traduzione nella tua dashboard."),
]

def home():
    import home_v3
    return home_v3.home(L, plans_html, FAQ_CORE)

def ai():
    body = f'''
<section class="page-hero"><div class="wrap split">
<div><h1>Lio, l'assistente AI per i messaggi degli ospiti</h1>
<p class="lead">Lio è un assistente AI addestrato sulle informazioni del tuo hotel. Risponde ai messaggi degli ospiti su WhatsApp e nelle caselle delle OTA (Booking.com, Airbnb, Expedia) in oltre 30 lingue, a qualsiasi ora.</p>
<div class="cta-row">{btn("Prova Lio gratis per 7 giorni", SIGNUP_URL)}</div></div>
<div class="panel typing"><p class="panel-title">WhatsApp, 02:47</p>
<div class="msg in" style="background:var(--bg)" lang="de">Hallo! Unser Flug landet um 1 Uhr. Können Sie uns abholen, und ist ein später Check-in möglich?</div>
<div class="msg out" lang="de">Natürlich! Unser Flughafentransfer kostet 35 € für bis zu 3 Gäste. Soll ich ihn für Ihre Ankunft um 1 Uhr buchen? Später Check-in ist kein Problem.<small lang="it">Lio, tedesco</small></div>
<p class="small muted" style="margin:10px 0 0">Transfer prenotato, link di pagamento inviato.</p></div>
</div></section>

<section class="white rule"><div class="wrap">
<div class="answer"><p><strong>Che cos'è un assistente AI per i messaggi degli ospiti di un hotel?</strong> Un software che risponde automaticamente alle domande che gli ospiti fanno prima e dopo la prenotazione, usando le informazioni dell'hotel stesso. Lio passa al tuo staff i messaggi a cui non sa rispondere o che richiedono una decisione umana (richieste di sconto, reclami, richieste speciali).</p></div>
<h2 style="margin-top:64px">Cosa fa Lio</h2><div class="rows">
<div class="row"><h3>Un'unica casella di posta</h3><div><p>I messaggi di WhatsApp e delle OTA (Booking.com, Airbnb, Expedia) arrivano in un'unica schermata. Lio abbina automaticamente ogni ospite alla sua prenotazione.</p></div></div>
<div class="row"><h3>Oltre 30 lingue, con traduzione automatica</h3><div><p>L'ospite scrive in giapponese, Lio risponde in giapponese e tu leggi la conversazione nella tua lingua. Anche le risposte manuali vengono tradotte nella lingua dell'ospite.</p></div></div>
<div class="row"><h3>Conosce il tuo hotel</h3><div><p>Orari di check-in e check-out, parcheggio, animali, orari della colazione, trasporti e caratteristiche delle camere. Li inserisci una volta e Lio li usa in modo coerente in ogni risposta.</p></div></div>
<div class="row"><h3>Un assistente che vende</h3><div><p>Lio non si limita a rispondere: propone transfer dall'aeroporto, tour della città ed extra al momento giusto e crea la prenotazione.</p></div></div>
<div class="row"><h3>Il controllo resta a te</h3><div><p>Nei primi giorni puoi approvare le risposte di Lio prima che vengano inviate. Decidi tu quali argomenti Lio chiude da solo e quali passa a te.</p></div></div>
</div></div></section>

<section><div class="wrap">
<div class="section-head"><h2>Messaggi AI inclusi per piano</h2><p>Un messaggio corrisponde a una singola risposta che Lio invia a un ospite.</p></div>
<div class="table-wrap"><table><thead><tr><th>Piano</th><th class="c">Messaggi AI / mese</th><th>Canali di messaggistica</th></tr></thead><tbody>
<tr><th>Starter</th><td class="c num">1.000</td><td>WhatsApp</td></tr>
<tr><th>Pro</th><td class="c num">5.000</td><td>WhatsApp + caselle OTA (Booking.com, Airbnb, Expedia)</td></tr>
<tr><th>Growth</th><td class="c num">12.000</td><td>WhatsApp + caselle OTA (Booking.com, Airbnb, Expedia)</td></tr>
</tbody></table></div>
</div></section>
'''
    faq = [
     ("E se Lio fornisce informazioni sbagliate?", "Lio usa solo le informazioni sull'hotel e i dati delle prenotazioni che fornisci tu. Quando non è sicuro, invece di tirare a indovinare ti passa il messaggio. Puoi anche approvare ogni risposta prima che venga inviata."),
     ("Risponde anche ai messaggi di Booking.com e Airbnb?", "Sì, anche a quelli di Expedia. Con i piani Pro e Growth i messaggi delle OTA arrivano nella casella di Lio e ricevono risposta allo stesso modo."),
     ("Cosa succede quando i messaggi inclusi finiscono?", "I messaggi continuano ad arrivare e compaiono nella tua dashboard; si sospendono solo le risposte automatiche. Puoi passare a un piano superiore per aumentare i messaggi disponibili."),
     FAQ_CORE[4],
    ]
    return {"key":"ai","title":"Assistente AI per hotel in oltre 30 lingue | Hostlio Pro",
            "desc":"Lio, l'assistente AI di Hostlio Pro, risponde agli ospiti dell'hotel su WhatsApp e nelle caselle delle OTA 24/7 in oltre 30 lingue e vende transfer e tour. Scopri come funziona.",
            "trail":[("Assistente AI Lio", U("ai"))],"body":body,"faq":faq}

def channel():
    body = f'''
<section class="page-hero"><div class="wrap split">
<div><h1>Un channel manager per oltre 100 OTA</h1>
<p class="lead">Gestisci disponibilità, tariffe e prenotazioni su Booking.com, Airbnb, Expedia, Agoda e oltre 100 altri canali da un unico calendario. Hostlio Pro sincronizza in tempo reale, in entrambe le direzioni, tramite Channex.</p>
<div class="cta-row">{btn("Inizia la prova gratuita di 7 giorni", SIGNUP_URL)}</div></div>
<div class="panel"><p class="panel-title">Canali collegati</p><div class="chan-list">
<div><span>Booking.com</span><span class="pill">Sincronizzato</span></div>
<div><span>Airbnb</span><span class="pill">Sincronizzato</span></div>
<div><span>Expedia</span><span class="pill">Sincronizzato</span></div>
<div><span>Agoda</span><span class="pill">Sincronizzato</span></div>
<div><span>Google Hotels</span><span class="pill">Sincronizzato</span></div>
</div></div>
</div></section>
<section class="white rule"><div class="wrap">
<div class="answer"><p><strong>Che cos'è un channel manager?</strong> Un software che mantiene sincronizzate disponibilità e tariffe di un hotel mentre vende le camere su più canali online contemporaneamente. Quando una camera viene venduta su un canale, si chiude subito su tutti gli altri, evitando le doppie prenotazioni (overbooking).</p></div>
<h2 style="margin-top:64px">Cosa fa il channel manager</h2><div class="rows">
<div class="row"><h3>Sincronizzazione bidirezionale</h3><div><p>Nuove prenotazioni, modifiche e cancellazioni arrivano automaticamente sul planning camere, e le modifiche che fai nel calendario vengono inviate a tutti i canali.</p></div></div>
<div class="row"><h3>Tariffe e restrizioni</h3><div><p>Invia tariffe, soggiorni minimi e stop sales per tipologia di camera a tutti i canali da un'unica schermata.</p></div></div>
<div class="row"><h3>Planning camere a colori</h3><div><p>Vedi a colpo d'occhio da quale canale arriva ogni prenotazione. Riassegna le camere con il drag-and-drop.</p></div></div>
<div class="row"><h3>Collegato alla messaggistica</h3><div><p>I messaggi degli ospiti delle prenotazioni OTA arrivano nella casella di Lio, con ospite, camera e date accanto a ogni conversazione.</p></div></div>
</div></div></section>
<section><div class="wrap"><div class="section-head"><h2>Principali canali supportati</h2><p>L'elenco segue la rete di connessioni di Channex. Manca un canale? Contattaci.</p></div>
<div class="table-wrap"><table><thead><tr><th>Canale</th><th>Tipo</th></tr></thead><tbody>
<tr><th>Booking.com</th><td>OTA</td></tr><tr><th>Airbnb</th><td>Affitti brevi</td></tr><tr><th>Expedia, Hotels.com</th><td>OTA</td></tr>
<tr><th>Agoda, Trip.com</th><td>OTA (focus sull'Asia)</td></tr><tr><th>Hotelbeds</th><td>Wholesaler (bedbank)</td></tr><tr><th>Hostelworld</th><td>Marketplace per ostelli</td></tr><tr><th>Google Hotels</th><td>Metamotore</td></tr>
</tbody></table></div></div></section>
'''
    faq = [FAQ_CORE[3],
     ("Il channel manager è incluso in tutti i piani?", "Sì. Starter, Pro e Growth includono tutti la sincronizzazione con oltre 100 OTA. Growth aggiunge la sincronizzazione prioritaria."),
     ("È difficile passare dal mio attuale channel manager?", "No. Crea le tipologie di camera in Hostlio Pro e collega i tuoi account OTA tramite Channex. Il nostro team di onboarding ti aiuta durante il passaggio."),
    ]
    return {"key":"channel","title":"Channel manager per hotel con oltre 100 OTA | Hostlio Pro",
            "desc":"Il channel manager di Hostlio Pro sincronizza in tempo reale disponibilità e tariffe su oltre 100 OTA, tra cui Booking.com, Airbnb, Expedia e Agoda, ed evita l'overbooking.",
            "trail":[("Channel manager", U("channel"))],"body":body,"faq":faq}

def checkin():
    body = f'''
<section class="page-hero"><div class="wrap split">
<div><h1>Check&#8209;in online con firma digitale</h1>
<p class="lead">Prima dell'arrivo, gli ospiti inviano dal telefono i dati del documento, gli accompagnatori e la firma. La consegna delle chiavi richiede pochi minuti.</p>
<div class="cta-row">{btn("Prova Pro gratis per 7 giorni", SIGNUP_URL+"?plan=pro")}</div></div>
<div class="panel"><p class="panel-title">Check-in online, camera 202</p>
<div class="field"><span>Nome e cognome</span><div>Keiko Sato</div></div>
<div class="field"><span>Nazionalità</span><div>Giappone</div></div>
<div class="field"><span>Accompagnatori</span><div>1 ospite aggiunto</div></div>
<div class="field"><span>Firma</span><div class="sig">Firma digitale ricevuta</div></div>
</div>
</div></section>
<section class="white rule"><div class="wrap">
<div class="answer"><p><strong>Come funziona il check-in online?</strong> Hostlio Pro invia a chi ha prenotato un link personale, sicuro e con scadenza. Da quel link l'ospite inserisce i dati del documento, aggiunge una foto del documento e gli eventuali accompagnatori e firma il modulo digitalmente. Tutto viene salvato direttamente nella prenotazione.</p></div>
<h2 style="margin-top:64px">Funzionalità del check-in online</h2><div class="rows">
<div class="row"><h3>Link sicuro</h3><div><p>Un link basato su token, unico per ogni prenotazione. Apre solo il modulo di quella prenotazione.</p></div></div>
<div class="row"><h3>Accompagnatori</h3><div><p>Tutte le persone che soggiornano in camera vengono aggiunte in un unico modulo, così nessuno deve inserire dati al banco.</p></div></div>
<div class="row"><h3>Firma digitale e consenso</h3><div><p>Gli ospiti accettano il regolamento della struttura e il consenso al trattamento dei dati firmando sullo schermo. Il documento firmato viene conservato con la prenotazione.</p></div></div>
<div class="row"><h3>Privacy by design</h3><div><p>I dati degli ospiti possono essere cancellati su richiesta e il testo del consenso fa parte del modulo.</p></div></div>
<div class="row"><h3>Esportazione per le comunicazioni ufficiali</h3><div><p>I dati raccolti possono essere esportati in un formato utilizzabile per gli obblighi locali di registrazione degli ospiti.</p></div></div>
</div></div></section>
<section class="dark on-dark"><div class="wrap"><div class="section-head"><h2>Tre passaggi per l'ospite</h2></div>
<ol class="steps"><li><h3>Apre il link</h3><p>Apre il link personale ricevuto dopo la conferma della prenotazione (inviato automaticamente via email o condiviso dall'hotel).</p></li>
<li><h3>Compila i dati</h3><p>Aggiunge i dati e la foto del documento e indica gli accompagnatori.</p></li>
<li><h3>Firma</h3><p>Accetta il regolamento della struttura e firma sullo schermo. Alla reception deve solo ritirare la chiave.</p></li></ol>
</div></section>
'''
    faq = [("Quali piani includono il check-in online?", "Il check-in online con firma digitale è incluso nei piani Pro e Growth."),
           ("L'ospite deve scaricare un'app?", "No. Il modulo di check-in si apre nel browser; non serve scaricare nessuna app."),
           ("E se un ospite non completa il check-in dal link?", "Fai il check-in nel modo consueto. Lo staff può anche inserire i dati al banco con l'app mobile di Hostlio Pro.")]
    return {"key":"checkin","title":"Check-in online per hotel con firma digitale | Hostlio Pro",
            "desc":"Con il check-in online di Hostlio Pro gli ospiti inviano dal telefono documento, accompagnatori e firma digitale prima dell'arrivo. Niente code alla reception.",
            "trail":[("Check-in online", U("checkin"))],"body":body,"faq":faq}

def features():
    body = f'''
<section class="page-hero"><div class="wrap split"><div><h1>Tutto quello che offre Hostlio Pro</h1>
<p class="lead">I moduli di cui un hotel indipendente ha bisogno ogni giorno: comunicazione con gli ospiti, distribuzione, prenotazioni, check-in e ricavi extra.</p></div><div class="hero-img"><img src="/assets/img/brand-hotelier.webp" alt="Titolare di un hotel che attraversa la hall con il caffè del mattino" width="720" height="900"></div></div></section>
<section class="white rule"><div class="wrap"><h2 class="sr-only">Moduli</h2><div class="rows">
<div class="row"><h3>Assistente AI Lio</h3><div><p>Risposte agli ospiti 24/7 in oltre 30 lingue. Messaggi di WhatsApp e delle OTA (Booking.com, Airbnb, Expedia) in un'unica casella.</p><a href="{U("ai")}">Scopri di più su Lio</a></div></div>
<div class="row"><h3>Channel manager</h3><div><p>Sincronizzazione di disponibilità, tariffe e prenotazioni con oltre 100 OTA tramite Channex.</p><a href="{U("channel")}">Channel manager</a></div></div>
<div class="row"><h3>Planning camere</h3><div><p>Calendario delle prenotazioni drag-and-drop. Cambi camera, prolungamenti e blocchi con un solo gesto.</p></div></div>
<div class="row"><h3>Check-in online</h3><div><p>Link sicuro, accompagnatori, foto del documento e firma digitale.</p><a href="{U("checkin")}">Check-in online</a></div></div>
<div class="row"><h3>Moduli per il visto in PDF automatici</h3><div><p>Genera con un clic, dai dati della prenotazione, lettere di invito e di conferma dell'alloggio per le richieste di visto.</p></div></div>
<div class="row"><h3>Vendita di transfer e tour</h3><div><p>Proponi transfer dall'aeroporto e tour durante la conversazione; Lio collega la richiesta alla prenotazione.</p></div></div>
<div class="row"><h3>App mobile</h3><div><p>Gestisci prenotazioni, messaggi e check-in anche lontano dall'hotel con l'app iOS. Funziona anche offline e sincronizza i dati quando torni online.</p></div></div>
</div></div></section>
<section><div class="wrap"><div class="section-head"><h2>Funzionalità per piano</h2></div>
<div class="table-wrap"><table><thead><tr><th>Funzionalità</th><th class="c">Starter</th><th class="c">Pro</th><th class="c">Growth</th></tr></thead><tbody>
<tr><th>Strutture</th><td class="c">1</td><td class="c">1</td><td class="c">2</td></tr>
<tr><th>Limite camere</th><td class="c num">10</td><td class="c num">50</td><td class="c num">150</td></tr>
<tr><th>Messaggi AI / mese</th><td class="c num">1.000</td><td class="c num">5.000</td><td class="c num">12.000</td></tr>
<tr><th>Sincronizzazione con oltre 100 OTA</th><td class="c">Sì</td><td class="c">Sì</td><td class="c">Prioritaria</td></tr>
<tr><th>Messaggi AI su WhatsApp</th><td class="c">Sì</td><td class="c">Sì</td><td class="c">Sì</td></tr>
<tr><th>Caselle OTA (Booking.com, Airbnb, Expedia)</th><td class="c">No</td><td class="c">Sì</td><td class="c">Sì</td></tr>
<tr><th>Calendario planning camere</th><td class="c">Sì</td><td class="c">Sì</td><td class="c">Sì</td></tr>
<tr><th>Moduli per il visto in PDF</th><td class="c">Sì</td><td class="c">Sì</td><td class="c">Sì</td></tr>
<tr><th>Check-in online e firma digitale</th><td class="c">No</td><td class="c">Sì</td><td class="c">Sì</td></tr>
<tr><th>Vendita di transfer e tour</th><td class="c">No</td><td class="c">Sì</td><td class="c">Sì</td></tr>
<tr><th>App mobile iOS</th><td class="c">No</td><td class="c">Sì</td><td class="c">Sì</td></tr>
<tr><th>Supporto prioritario e chiamata di onboarding</th><td class="c">No</td><td class="c">No</td><td class="c">Sì</td></tr>
<tr><th>White-label</th><td class="c">No</td><td class="c">No</td><td class="c">Sì</td></tr>
</tbody></table></div></div></section>
'''
    return {"key":"features","title":"Funzionalità del gestionale per hotel | Hostlio Pro",
            "desc":"Funzionalità di Hostlio Pro: assistente AI per gli ospiti, channel manager per oltre 100 OTA, planning camere drag-and-drop, check-in online, moduli visto PDF, transfer e app.",
            "trail":[("Funzionalità", U("features"))],"body":body,"faq":[FAQ_CORE[0], FAQ_CORE[3]]}

def pricing():
    body = f'''
<section class="page-hero"><div class="wrap"><h1>Prezzi di Hostlio Pro</h1>
<p class="lead">Un canone mensile fisso. Nessuna commissione sulle prenotazioni, nessun costo di attivazione. Prova qualsiasi piano gratis per 7 giorni.</p></div></section>
<section style="padding-top:0"><div class="wrap"><h2 class="sr-only">Piani</h2>
<span class="billing-note">20% di sconto per i primi 50 clienti, bloccato per sempre</span>
{plans_html()}
<p class="small muted" style="margin-top:18px">Prezzi in dollari USA, tasse escluse. Ultimo aggiornamento: <time datetime="{UPDATED}">{D(UPDATED)}</time>.</p>
</div></section>
<section class="white rule"><div class="wrap">
<div class="section-head"><h2>Quale piano fa per te?</h2></div>
<div class="rows">
<div class="row"><h3>Starter</h3><div><p>B&B e boutique hotel fino a 10 camere, con meno di 1.000 risposte al mese, che vogliono iniziare con la sincronizzazione dei canali e le risposte AI.</p></div></div>
<div class="row"><h3>Pro</h3><div><p>Hotel da 11 a 50 camere che vogliono affidare a Lio anche i messaggi delle OTA, usare il check-in online e vendere transfer e tour.</p></div></div>
<div class="row"><h3>Growth</h3><div><p>Due strutture o fino a 150 camere, quando servono supporto prioritario, un onboarding personalizzato e l'uso in white-label.</p></div></div>
</div></div></section>
'''
    faq = [FAQ_CORE[1], FAQ_CORE[2],
      ("Applicate commissioni sulle prenotazioni?", "No. Hostlio Pro è un abbonamento mensile fisso; non trattiene alcuna percentuale sul valore delle prenotazioni."),
      ("È prevista la fatturazione annuale?", "Sì. Gli abbonamenti vengono fatturati in anticipo su base mensile o annuale, e i piani annuali hanno uno sconto del 20% (Termini di servizio, sezione 3)."),
      ("Posso cambiare piano?", "Sì. Puoi passare a un piano superiore o inferiore in qualsiasi momento; la modifica si applica dal periodo di fatturazione successivo."),
      ("Quanto dura lo sconto di lancio?", "Si applica ai primi 50 clienti e il tuo prezzo resta bloccato per tutta la durata dell'abbonamento.")]
    return {"key":"pricing","title":"Prezzi del gestionale per hotel: da $49/mese | Hostlio Pro",
            "desc":"Prezzi di Hostlio Pro: Starter $49, Pro $89, Growth $149 al mese. Nessuna commissione, nessun costo di attivazione, 7 giorni di prova gratuita. Confronta i piani.",
            "trail":[("Prezzi", U("pricing"))],"body":body,"faq":faq,"schema":[software_schema(L, detailed=True)]}

FAQ_ALL = FAQ_CORE + [
 ("Per quali tipi di struttura è pensato Hostlio Pro?", "Per strutture indipendenti da 10 a 150 camere, come boutique hotel, hotel di città, B&B e affittacamere, residence e aparthotel e ostelli."),
 ("Esiste un'app mobile?", "Sì. I piani Pro e Growth includono un'app iOS. Funziona senza connessione a internet e sincronizza i dati quando torni online."),
 ("Come funziona il check-in online?", "Gli ospiti ricevono un link personale e sicuro e, prima dell'arrivo, inviano dal telefono i dati del documento, gli accompagnatori e una firma digitale. Disponibile nei piani Pro e Growth."),
 ("A cosa serve la funzione dei moduli per il visto in PDF?", "Trasforma automaticamente i dati della prenotazione in lettere di conferma dell'alloggio e di invito in PDF per gli ospiti che hanno bisogno di un visto."),
 ("I miei dati sono al sicuro?", "I dati vengono trasmessi tramite connessioni crittografate e i dati di ogni hotel sono isolati da quelli delle altre strutture con regole di accesso a livello di riga. I dati degli ospiti possono essere cancellati su richiesta."),
 ("Quanto tempo richiede la configurazione?", "La maggior parte degli hotel inizia il giorno stesso, aggiungendo le tipologie di camera e collegando i canali. Il piano Growth include una chiamata di onboarding personalizzata."),
 ("In quali lingue è disponibile il supporto?", "La dashboard e il supporto sono disponibili in inglese e in turco. Scrivici a " + EMAIL + "."),
]

def faq_page():
    body = f'''<section class="page-hero"><div class="wrap"><h1>Domande frequenti</h1>
<p class="lead">Le domande più comuni su funzionalità, prezzi e configurazione di Hostlio Pro. Non trovi la risposta? <a href="{U("contact")}">Scrivici</a>.</p></div></section>
<section style="padding-top:0"><div class="wrap">{faq_block(FAQ_ALL, L, heading=False, wrap=False)}</div></section>'''
    return {"key":"faq","title":"Domande frequenti sul gestionale per hotel | Hostlio Pro",
            "desc":"Domande frequenti su Hostlio Pro, il gestionale per hotel: prezzi, prova gratuita, integrazioni OTA, assistente AI Lio, check-in online e sicurezza dei dati.",
            "trail":[("Domande frequenti", U("faq"))],"body":body,"faq":FAQ_ALL,"faq_inline":True,"page_type":"FAQPage"}

def about():
    body = f'''<section class="page-hero"><div class="wrap split"><div><h1>Perché abbiamo creato Hostlio Pro</h1>
<p class="lead">Nei piccoli hotel, reception, vendite e comunicazione con gli ospiti ricadono spesso sulle spalle di una sola persona. Hostlio Pro esiste perché quella persona non resti sommersa dai messaggi di notte e dagli extranet dei canali di giorno.</p></div><div class="hero-img"><img src="/assets/img/brand-courtyard.webp" alt="Cortile di un boutique hotel con piscina e bouganville" width="880" height="804"></div></div></section>
<section class="white rule"><div class="wrap split">
<div class="prose"><h2>Cosa facciamo</h2>
<p>Hostlio Pro è un gestionale per hotel basato sull'intelligenza artificiale, pensato per gli hotel indipendenti. Affidiamo la comunicazione con gli ospiti al nostro assistente AI Lio, riuniamo la distribuzione sulle OTA in un unico calendario tramite Channex e spostiamo il check-in sul telefono dell'ospite.</p>
<h2>Come lavoriamo</h2>
<ul><li>Pubblichiamo i nostri prezzi in modo trasparente e non prendiamo commissioni.</li><li>Sviluppiamo partendo dal lavoro quotidiano reale degli albergatori.</li><li>Niente contratti lunghi: i clienti restano perché sono soddisfatti.</li></ul></div>
<div class="panel"><p class="panel-title">Dati aziendali</p><dl class="list-kv">
<dt>Prodotto</dt><dd>Hostlio Pro (Hostlio)</dd><dt>Società</dt><dd>Loti Members LLC</dd>
<dt>Indirizzo</dt><dd>2108 N ST STE N, Sacramento, CA 95816, USA</dd><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
<dt>Clienti</dt><dd>Hotel indipendenti in oltre 20 paesi</dd></dl></div>
</div></section>'''
    return {"key":"about","title":"Chi siamo | Hostlio Pro","desc":"Hostlio Pro sviluppa un gestionale per hotel basato sull'intelligenza artificiale per hotel indipendenti. Gestito da Loti Members LLC e usato in oltre 20 paesi.",
            "trail":[("Chi siamo", U("about"))],"body":body,"page_type":"AboutPage"}

def contact():
    from build import FORM_ENDPOINT
    act = f' action="{FORM_ENDPOINT}" method="post"' if FORM_ENDPOINT else ""
    body = f'''<section class="page-hero"><div class="wrap split" style="align-items:start">
<div><h1>Richiedi una demo o contattaci</h1>
<p class="lead">Raccontaci in breve il tuo hotel e i canali che usi: in una chiamata di 30 minuti ti mostriamo Hostlio Pro con le tue camere.</p>
<p>Oppure scrivici direttamente: <a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
<form class="contact" data-contact-form data-mail="{EMAIL}" data-subject="Richiesta demo" data-sent="Si è aperta la tua app di posta. Premi invia e la tua richiesta ci arriverà."{act}>
<label>Nome e cognome<input name="name" autocomplete="name" required></label>
<label>Email<input type="email" name="email" autocomplete="email" required></label>
<label>Nome dell'hotel<input name="hotel" autocomplete="organization" required></label>
<label>Numero di camere<select name="rooms"><option>1–10</option><option>11–50</option><option>51–150</option><option>150+</option></select></label>
<label>Paese / città<input name="country" autocomplete="country-name"></label>
<label>Messaggio <span class="hint">Canali che usi, software attuale</span><textarea name="message" rows="4"></textarea></label>
<button class="btn btn-primary" type="submit">Invia richiesta demo</button>
<p class="form-status" role="status" aria-live="polite"></p>
</form></div></section>'''
    return {"key":"contact","title":"Contatti e richiesta demo | Hostlio Pro","desc":"Contatta il team di Hostlio Pro o prenota una demo gratuita di 30 minuti su misura per il tuo hotel. Supporto in inglese e turco, email: " + EMAIL,
            "trail":[("Contatti", U("contact"))],"body":body,"page_type":"ContactPage","no_final":True}

POSTS = [
 {"key":"post-overbooking","title":"Come evitare l'overbooking: 6 passaggi per gli hotel","date":"2026-09-21","desc":"Perché gli hotel finiscono in overbooking e come evitarlo: channel manager, regole di stop sales, margini di disponibilità e cosa fare quando succede comunque."},
 {"key":"post-autoreply","title":"Come rispondere in automatico ai messaggi degli ospiti su Booking.com","date":"2026-09-21","desc":"Tre modi per automatizzare i messaggi degli ospiti di Booking.com: modelli, messaggi programmati e un assistente AI."},
 {"key":"post-ai","title":"Rispondere ai messaggi degli ospiti con l'AI: guida pratica per hotel","date":"2026-09-18",
  "desc":"Vantaggi, rischi e passaggi di configurazione per rispondere con l'AI ai messaggi degli ospiti dell'hotel. Quali domande automatizzare e quali lasciare al tuo team."},
 {"key":"post-pms","title":"Come scegliere il gestionale per hotel (PMS) per una piccola struttura","date":"2026-09-10",
  "desc":"7 criteri per scegliere un PMS per un piccolo hotel o un boutique hotel: channel manager, modello di prezzo, messaggi degli ospiti, accesso da mobile e altro."},
]

def blog():
    items = "".join(f'<article><h2><a href="{U(p["key"])}">{p["title"]}</a></h2><p class="meta"><time datetime="{p["date"]}">{D(p["date"])}</time></p><p>{p["desc"]}</p></article>' for p in POSTS)
    body = f'<section class="page-hero"><div class="wrap"><h1>Blog per albergatori</h1><p class="lead">Articoli pratici sulla gestione di un hotel indipendente, sulla distribuzione e sulla comunicazione con gli ospiti.</p></div></section><section style="padding-top:0"><div class="wrap post-list">{items}</div></section>'
    return {"key":"blog","title":"Blog: guide per hotel indipendenti | Hostlio Pro","desc":"Guide pratiche per albergatori indipendenti su gestione alberghiera, channel manager, distribuzione sulle OTA e comunicazione con gli ospiti tramite AI.",
            "trail":[("Blog", U("blog"))],"body":body,"page_type":"CollectionPage"}

COVERS={"post-ai":("brand-guest-bed",1200,675),"post-pms":("hostlio-lobby",720,900),"post-overbooking":("brand-hotelier",720,900),"post-autoreply":("brand-phone",720,900)}
def article(meta, content, faq=None):
    art = {"@type":"BlogPosting","headline":meta["title"],"description":meta["desc"],"datePublished":meta["date"],"inLanguage":L,"author":{"@type":"Organization","name":"Team di prodotto Hostlio Pro","url":SITE+U("about")},"dateModified":UPDATED,"publisher":{"@id":SITE+"/#org"},
           "mainEntityOfPage":SITE+U(meta["key"]),"image":SITE+"/assets/img/"+COVERS[meta["key"]][0]+".webp"}
    body = f'<article><section class="page-hero"><div class="wrap"><h1 style="max-width:22ch">{meta["title"]}</h1><p class="meta">A cura del <a href="{U("about")}">team di prodotto Hostlio Pro</a>, le persone che sviluppano Hostlio Pro. Pubblicato il <time datetime="{meta["date"]}">{D(meta["date"])}</time>, aggiornato il <time datetime="{UPDATED}">{D(UPDATED)}</time></p></div></section><section style="padding-top:0"><div class="wrap"><figure class="post-cover"><img src="/assets/img/{COVERS[meta["key"]][0]}.webp" alt="" width="{COVERS[meta["key"]][1]}" height="{COVERS[meta["key"]][2]}"></figure><div class="prose">{content}</div></div></section></article>'
    return {"key":meta["key"],"title":meta["title"],"desc":meta["desc"],"og_type":"article",
            "trail":[("Blog",U("blog")),(meta["title"],U(meta["key"]))],"body":body,"schema":[art],"faq":faq or []}

def post_ai():
    c = f'''
<div class="answer"><p><strong>In breve:</strong> la maggior parte dei messaggi che riceve un hotel sono domande ricorrenti (orario del check-in, parcheggio, transfer, colazione). Affidarle a un assistente AI addestrato sulle informazioni del tuo hotel permette agli ospiti di ricevere una risposta in pochi secondi, nella loro lingua. Sconti, reclami e richieste speciali dovrebbero restare al tuo staff.</p></div>
<h2>Quali domande ricevono più spesso gli hotel?</h2>
<p>Negli hotel indipendenti, la maggior parte dei messaggi riguarda pochi argomenti:</p>
<ul><li>Orari di check-in e check-out, arrivo anticipato o partenza posticipata</li><li>Transfer dall'aeroporto e come arrivare</li><li>Parcheggio, colazione, animali ammessi</li><li>Deposito bagagli, caratteristiche delle camere, il quartiere</li><li>Modifiche alla prenotazione e richieste di fattura</li></ul>
<p>Le risposte esistono già in hotel. Il problema è darle nella lingua giusta e all'ora giusta.</p>
<h2>Cosa deve automatizzare l'AI, e cosa no?</h2>
<p>In una buona configurazione, l'assistente chiude le domande informative e passa le decisioni allo staff.</p>
<div class="table-wrap"><table><thead><tr><th>Lascia rispondere l'AI</th><th>Passa allo staff</th></tr></thead><tbody>
<tr><td>Orari, regole, servizi</td><td>Sconti e trattative sul prezzo</td></tr><tr><td>Indicazioni stradali, informazioni sui transfer</td><td>Reclami e rimborsi</td></tr><tr><td>Vendita di transfer e tour</td><td>Situazioni mediche o di sicurezza</td></tr><tr><td>Promemoria dei dettagli della prenotazione</td><td>Richieste per gruppi ed eventi</td></tr></tbody></table></div>
<h2>Configurazione passo dopo passo</h2>
<ol><li><strong>Scrivi la knowledge base del tuo hotel.</strong> Orari, regole, servizi e domande frequenti. Più è chiara, più le risposte sono coerenti.</li>
<li><strong>Collega i tuoi canali.</strong> Riunisci i messaggi di WhatsApp e delle OTA in un'unica casella.</li>
<li><strong>Parti in modalità approvazione.</strong> Per la prima settimana leggi e correggi le risposte prima che vengano inviate.</li>
<li><strong>Definisci le regole di passaggio.</strong> Stabilisci quali argomenti devono arrivare a te.</li>
<li><strong>Passa alla modalità automatica.</strong> Quando le risposte sono coerenti, lascia che l'assistente gestisca completamente le domande informative.</li></ol>
<h2>Perché le risposte multilingue sono importanti</h2>
<p>Gli ospiti che scrivono nella propria lingua forniscono più dettagli e si fidano di più della risposta. Un assistente che risponde in oltre 30 lingue crea questa fiducia anche quando alla reception nessuno parla quella lingua, e tu continui a leggere la conversazione nella tua.</p>
<h2>Come funziona in Hostlio Pro</h2>
<p><a href="{U("ai")}">Lio</a>, l'assistente AI di Hostlio Pro, usa le informazioni del tuo hotel e i dati delle prenotazioni per rispondere ai messaggi di WhatsApp e delle OTA (Booking.com, Airbnb, Expedia) in oltre 30 lingue. I piani includono da 1.000 a 12.000 messaggi AI al mese; trovi i dettagli nella <a href="{U("pricing")}">pagina dei prezzi</a>.</p>'''
    faq = [("L'AI può dare informazioni sbagliate agli ospiti?", "Il rischio è minimo se l'assistente lavora solo con le informazioni fornite dall'hotel e passa allo staff le domande incerte. È consigliabile iniziare in modalità approvazione."),
           ("Gli ospiti sapranno che stanno parlando con un'AI?", "Le risposte sono scritte a nome dell'hotel e con il suo tono. Per trasparenza, l'hotel può indicare nel messaggio di benvenuto che l'assistente è un'AI.")]
    return article(next(p for p in POSTS if p["key"]=="post-ai"), c, faq)

def post_pms():
    c = f'''
<div class="answer"><p><strong>In breve:</strong> il PMS giusto per un piccolo hotel ha un channel manager integrato, prezzi fissi e trasparenti, un'unica casella per i messaggi degli ospiti, accesso da mobile e si configura in giornata. I sistemi enterprise con centinaia di funzioni finiscono spesso inutilizzati dai piccoli team.</p></div>
<h2>1. Un channel manager integrato</h2>
<p>Se vendi contemporaneamente su Booking.com, Airbnb ed Expedia, la disponibilità deve sincronizzarsi all'istante. Un channel manager separato significa un costo in più e un'altra schermata da gestire. La prima cosa da verificare è se il gestionale ne include uno e a quanti canali si collega.</p>
<h2>2. Modello di prezzo</h2>
<p>Alcuni software applicano, oltre al canone mensile, una percentuale sul valore delle prenotazioni: i costi crescono con l'occupazione. Un prezzo mensile fisso rende il budget prevedibile. Con i fornitori che non pubblicano i prezzi, aspettati una trattativa commerciale.</p>
<h2>3. Comunicazione con gli ospiti</h2>
<p>Quando i messaggi sono sparsi tra WhatsApp e le caselle delle OTA, i tempi di risposta ne risentono. Un'unica casella con risposte automatiche è il maggior risparmio di tempo per i piccoli team.</p>
<h2>4. Un planning camere pratico</h2>
<p>Il calendario delle prenotazioni è la schermata che la reception guarda di più. Spostare le camere con il drag-and-drop e vedere a colpo d'occhio il canale di ogni prenotazione velocizza il lavoro quotidiano.</p>
<h2>5. Accesso da mobile</h2>
<p>Spesso i titolari non sono in struttura. Un'app mobile, soprattutto se funziona anche quando manca internet, è un'esigenza concreta.</p>
<h2>6. Check-in online</h2>
<p>Raccogliere i dati degli ospiti prima dell'arrivo fa risparmiare tempo alla reception e semplifica gli obblighi di registrazione degli ospiti.</p>
<h2>7. Configurazione e supporto</h2>
<p>Un piccolo hotel non può permettersi un progetto di implementazione di settimane. Scegli un software che puoi usare il giorno stesso, con supporto nella tua lingua, e metti alla prova il periodo di prova con prenotazioni reali.</p>
<h2>Checklist</h2>
<div class="table-wrap"><table><thead><tr><th>Criterio</th><th>Domanda da porre</th></tr></thead><tbody>
<tr><td>Channel manager</td><td>È incluso e a quanti canali si collega?</td></tr><tr><td>Prezzi</td><td>Il prezzo è fisso, ci sono commissioni, è pubblico?</td></tr>
<tr><td>Messaggistica</td><td>I messaggi di WhatsApp e delle OTA sono in un unico posto, con risposte automatiche?</td></tr><tr><td>Mobile</td><td>Esiste un'app e funziona offline?</td></tr>
<tr><td>Check-in</td><td>C'è il check-in online con firma digitale?</td></tr><tr><td>Prova</td><td>C'è una prova gratuita e si può disdire senza vincoli?</td></tr></tbody></table></div>
<p>Hostlio Pro è stato progettato intorno a questi criteri: scopri le <a href="{U("features")}">funzionalità</a> e i <a href="{U("pricing")}">prezzi</a>.</p>'''
    faq = [("Un piccolo hotel ha bisogno di un PMS?", "Se vendi su più OTA e ricevi decine di messaggi al giorno, sì. Lavorare con fogli di calcolo e con gli extranet delle singole OTA aumenta il rischio di overbooking e di risposte lente."),
           ("Qual è la differenza tra un PMS e un channel manager?", "Un PMS gestisce le operazioni interne dell'hotel (prenotazioni, camere, ospiti); un channel manager distribuisce disponibilità e tariffe sulle OTA. Software come Hostlio Pro riuniscono entrambi in un'unica piattaforma.")]
    return article(next(p for p in POSTS if p["key"]=="post-pms"), c, faq)

def pages():
    import pages_v4
    return [home(), ai(), channel(), checkin(), features(), pricing(), faq_page(), about(), contact(), blog(), post_ai(), post_pms()] + pages_v4.pages(L, article) + __import__("legal_v5").pages(L, article)
