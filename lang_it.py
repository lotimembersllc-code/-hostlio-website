"""Italian (it) data for the shared modules: build.py, home_v3.py, pages_v4.py, legal_v5.py.
Pure data + functions; no project imports. Links come from the U callable."""

L = "it"
UPDATED_TXT = "23 settembre 2026"
LEGAL_DATE_TXT = "20 aprile 2026"

# ---------------------------------------------------------------- build.UI
UI = {
   "nav": [("features","Funzionalità"),("ai","Assistente AI Lio"),("channel","Channel manager"),("pricing","Prezzi"),("blog","Blog")],
   "top": [("pricing","Prezzi"),("blog","Blog"),("faq","Domande frequenti"),("about","Chi siamo")],
   "login":"Accedi", "trial":"Prova gratis", "demo":"Richiedi una demo", "menu":"Apri il menu",
   "skip":"Vai al contenuto", "home":"Home",
   "lang_label":"Lingua", "crumb_label":"Percorso di navigazione",
   "foot_tag":"Gestionale per hotel con intelligenza artificiale per strutture indipendenti. Messaggi degli ospiti, channel manager e calendario delle prenotazioni in un unico posto.",
   "foot_product":"Prodotto","foot_company":"Azienda","foot_res":"Risorse","foot_sol":"Soluzioni","privacy":"Informativa sulla privacy","terms":"Termini di servizio","delacc":"Elimina account","sol":["Gestionale per boutique hotel","Gestionale per B&B e affittacamere","Gestionale per residence e aparthotel","Gestionale per ostelli","Confronto gestionali per hotel"],
   "foot_about":"Chi siamo","foot_contact":"Contatti","foot_faq":"Domande frequenti",
   "rights":"Tutti i diritti riservati.","updated":"Ultimo aggiornamento",
   "final_h":"Tieni aperta la reception anche stanotte.",
   "final_p":"Prova gratis per 7 giorni. Nessun addebito fino alla fine della prova, disdici quando vuoi.",
   "faq_h":"Domande frequenti",
}

# ---------------------------------------------------------------- build.MEGA
MEGA = {"btn":"Prodotto","cols":[
   ("Ospiti",[("ai","sparkle","Assistente AI Lio","Risposte agli ospiti 24/7 in 30+ lingue"),("checkin","identification-card","Check-in online","Documenti, accompagnatori e firma digitale")]),
   ("Distribuzione",[("channel","arrows-left-right","Channel manager","100+ OTA in un solo calendario"),("features","calendar-dots","Planning camere","Calendario prenotazioni drag-and-drop")]),
   ("Gestione",[("features","van","Transfer e tour","Ricavi extra mentre chatti"),("features","device-mobile","App mobile","App iOS che funziona anche offline")]),
   ("Per tipo di struttura",[("t-boutique","sparkle","Boutique hotel","Hotel da 10–50 camere"),("t-guesthouse","users-three","B&B e affittacamere","Strutture da 1–10 camere"),("t-apart","calendar-dots","Residence e aparthotel","Appartamenti e suite"),("t-hostel","globe-simple","Ostelli","Vendita a posto letto")]),
  ],"feat":("pricing","Confronta i piani","Da $49 al mese, 7 giorni gratis")}

# ---------------------------------------------------------------- build.software_schema / room_rack / 404
SOFT_DESC = "Gestionale per hotel indipendenti con intelligenza artificiale: messaggi agli ospiti 24/7 in oltre 30 lingue, channel manager per oltre 100 OTA, calendario delle prenotazioni e check-in online."
SOFT_FEATURES = ["Assistente AI Lio per gli ospiti (30+ lingue)", "Channel manager (connessioni certificate con 100+ OTA)", "Calendario prenotazioni drag-and-drop", "Check-in online con firma digitale", "Moduli PDF automatici per il visto", "Vendita di transfer e tour", "App mobile che funziona anche offline"]
DAYS = ["Lun","Mar","Mer","Gio","Ven","Sab","Dom"]
RACK = ("Planning camere", "Settembre, 3ª settimana", "Prenotazioni colorate per canale: Booking.com blu, Airbnb pesca, Expedia lilla, Agoda sabbia, dirette verde")
NOTFOUND = ("Pagina non trovata | Hostlio Pro",
            "La pagina che cerchi potrebbe essere stata spostata o rimossa.",
            "Pagina non trovata",
            'L\'indirizzo potrebbe essere cambiato. <a href="{home}">Torna alla home</a>.')

# ---------------------------------------------------------------- home_v3.T
HOME = dict(
  title="Hostlio Pro | Gestionale per hotel con AI e channel manager",
  desc="Gestionale per hotel Hostlio Pro: l'assistente AI Lio risponde agli ospiti 24/7 in 30+ lingue e il channel manager sincronizza 100+ OTA. Prova gratis 7 giorni.",
  h1='Mentre il tuo hotel dorme, <em class="hl">Lio</em> risponde',
  lead="Il gestionale per hotel con intelligenza artificiale pensato per hotel indipendenti e B&B. Prenotazioni, 100+ canali e messaggi degli ospiti in un unico posto, in oltre 30 lingue.",
  try_="Prova gratis", demo="Richiedi una demo", via="Connessioni certificate con:", more="e oltre 100 canali",
  coll_alt1="Cortile di un boutique hotel con bouganville e piscina al tramonto", coll_alt2="Albergatrice sorridente con una tazza di caffè in mano",
  chip1=("Camera 202 venduta","Booking.com, 21:40"), chip2="Chiusa su Airbnb ed Expedia",
  bub_h=("Lio","Receptionist AI, online"), bub_in="Hallo! Ist ein später Check-in möglich?", bub_out="Natürlich! Unsere Rezeption ist rund um die Uhr besetzt.", bub_note="Risposta in tedesco, 4 sec",
  pick_h="Da cosa vuoi iniziare?", pick_p="Scegli ciò che ti serve e prepariamo il tuo account su misura.", pick_none="Puoi sceglierne quanti vuoi.", pick_some="{n} selezionati, provali gratis per 7 giorni.", pick_btn="Inizia", pick_name="interest",
  tiles=[("ai","sparkle","t-peach","Assistente AI Lio","Risposte agli ospiti in 30+ lingue"),("channel","arrows-left-right","t-lilac","Channel manager","Sincronizzazione in tempo reale con 100+ OTA"),("rack","calendar-dots","t-sand","Planning camere","Calendario prenotazioni drag-and-drop"),("checkin","identification-card","t-peach","Check-in online","Documento e firma prima dell'arrivo"),("upsell","van","t-lilac","Transfer e tour","Ricavi extra mentre chatti"),("mobile","device-mobile","t-sand","App mobile","Gestisci l'hotel da dove vuoi")],
  story_h='Sono le <em class="hl">2:14</em> di notte e un ospite scrive',
  story_p="Cosa succede mentre dormi, in tre scene.",
  story=[("brand-night","Albergatore che dorme mentre il telefono si illumina sul comodino","02:14","Un ospite scrive","Un ospite dalla Germania chiede del check-in in tarda serata. Tu stai dormendo profondamente."),
         ("brand-phone","Mano che tiene un telefono con la schermata arancione di risposta di Lio","02:14","Lio risponde subito","Con le informazioni del tuo hotel, nella lingua dell'ospite. Se serve, ti lascia una nota."),
         ("brand-hotelier","Albergatrice che attraversa la hall con il caffè del mattino","08:30","Al mattino è tutto pronto","La conversazione ti aspetta nel pannello, già tradotta. L'ospite è soddisfatto e tu sei riposato.")],
  story_chip="Lio ha risposto",
  tour_h="Gestisci la giornata del tuo hotel <em class=\"hl\">da un'unica schermata</em>", tour_p="Messaggi degli ospiti, prenotazioni, canali e check-in lavorano insieme.", tour_label="Tour del prodotto",
  tabs=["Messaggi","Calendario","Canali","Check-in"],
  st=[("Tutti i messaggi degli ospiti in un'unica casella","WhatsApp e messaggi delle OTA (Booking.com, Airbnb, Expedia) tutti insieme. Lio risponde con le informazioni del tuo hotel e tu vedi solo ciò che richiede il tuo intervento.",["Risposte automatiche in 30+ lingue","Dettagli della prenotazione accanto a ogni messaggio","Ti passa ciò di cui non è sicuro"],"ai","Come funziona Lio"),
      ("Tutta la settimana sul planning camere","Vedi ogni prenotazione con il colore del suo canale. Spostare camere, prolungare soggiorni o bloccare date richiede un solo gesto.",["Cambi camera con drag-and-drop","Prenotazioni colorate per canale","Lo stesso calendario su web e iOS"],"features","Tutte le funzionalità"),
      ("100+ canali, un'unica disponibilità","Sincronizzazione bidirezionale con connessioni di canale certificate. Una camera venduta su un canale si chiude subito sugli altri.",["Tariffe e restrizioni da un'unica schermata","Nuove prenotazioni e cancellazioni arrivano in automatico","Nessun rischio di overbooking"],"channel","Channel manager"),
      ("Il check-in è fatto prima dell'arrivo","Gli ospiti inviano dal telefono dati del documento, accompagnatori e firma tramite un link sicuro.",["Dal browser, senza scaricare app","Accompagnatori in un unico modulo","Firma digitale e consenso"],"checkin","Check-in online")],
  inbox_top=("Posta in arrivo","12 conversazioni aperte"), inbox_note="Traduzione: il check-in è dalle 14:00, possiamo tenere i tuoi bagagli.",
  chan_top=("Canali collegati","Ultima sincronizzazione: adesso"), sync="Sincronizzato",
  ci_top=("Check-in online","Camera 202"), ci_f=[("Nome e cognome","Keiko Sato"),("Nazionalità","Giappone"),("Accompagnatori","1 ospite aggiunto")], ci_sig="Firma",
  bento_h='<em class="hl">Tutto</em> ciò che serve a un hotel', bento_p="Ogni modulo è collegato: niente strumenti separati, niente password separate.",
  b_lio=("Assistente AI Lio","Chiude la maggior parte delle domande degli ospiti prima che tu le veda e ti riassume il resto.","Is breakfast included?","Yes, from 7:30 to 10:30 on the terrace."),
  b_chan=("Channel manager","100+ canali di vendita, un'unica disponibilità."),
  b_rack=("Planning camere","Calendario prenotazioni drag-and-drop."),
  b_ci=("Check-in online","Documento, accompagnatori e firma digitale prima dell'arrivo."),
  b_pdf=("Moduli PDF per il visto","Lettere di alloggio e di invito in un clic.","Lettera di alloggio","PDF"),
  b_tr=("Vendita di transfer e tour","Lio li propone al momento giusto, tu guadagni di più.","Transfer aeroporto","+35 €"),
  b_lang=("30+ lingue","In qualunque lingua scriva l'ospite, risponde in quella lingua."),
  b_mob=("App mobile","Prenotazioni, messaggi e check-in su iOS, anche offline."),
  types_h='Pensato per <em class="hl">ogni tipo di struttura</em>', types_p="Progettato per strutture indipendenti da 1 a 150 camere.",
  types=[("brand-courtyard","Cortile di un boutique hotel con piscina e bouganville","Boutique hotel","10–50 camere","Tanti ospiti internazionali, ogni messaggio è personale."),
         ("gen-hostel","Hall con pareti rivestite in legno e sedute condivise","Ostello","Posti letto e camere","Viaggiatori multilingue, caselle di posta affollate."),
         ("gen-guesthouse","Camera accogliente di un B&B con lampada da scrivania","B&B e affittacamere","1–10 camere","Un turno di notte per chi gestisce tutto da solo."),
         ("gen-apart","Appartamento luminoso con biancheria bianca","Residence e aparthotel","10–40 unità","Check-in online prima dell’arrivo.")],
  plans_h="Un piano per le dimensioni del tuo hotel", plans_p="Un canone mensile fisso, nessun contratto a lungo termine. Ogni piano è gratuito per 7 giorni.",
  early="20% di sconto per i primi 50 clienti, bloccato per sempre", tax='I prezzi non includono le imposte. <a href="{p}">Confronta i piani nel dettaglio</a>.',
  ai_h='Lio, il <em class="hl">turno di notte</em> della tua reception', ai_p="Un assistente AI che lavora con le informazioni del tuo hotel. Risponde agli ospiti, vende servizi extra e lascia a te il resto.",
  ai_wide=("Risponde nella lingua dell'ospite","Una domanda in giapponese riceve una risposta in giapponese, una in arabo una risposta in arabo. Tu leggi la conversazione nella tua lingua."),
  ai_cards=[("van","Vende per te","Propone transfer aeroportuali e tour al momento giusto e ti inoltra la richiesta."),("hand-arrow-up","Sa quando passarti la parola","I messaggi che richiedono una decisione, come sconti, reclami o richieste speciali, vanno al tuo staff."),("calendar-dots","Conosce la prenotazione","Quando l’ospite è abbinato a una prenotazione, le risposte usano camera, date e dettagli della prenotazione.")],
  ai_photo=("brand-guest-phone","Ospite accanto a una finestra che scrive un messaggio sul telefono","Su WhatsApp e sulle OTA","WhatsApp, Booking.com, Airbnb ed Expedia."),
  ai_btn="Scopri Lio",
  answer="<strong>Che cos'è Hostlio Pro?</strong> Hostlio Pro è un gestionale per hotel in cloud (un PMS) per hotel indipendenti e B&B da 1 a 150 camere. Affida la comunicazione con gli ospiti all'intelligenza artificiale, riunisce le prenotazioni delle OTA in un unico calendario e sposta il check-in sul telefono dell'ospite. Si gestisce dal web e da un'app iOS ed è usato in oltre 20 paesi.",
  stats=[("30+","lingue in cui risponde"),("100+","OTA e canali di vendita"),("20+","paesi con hotel su Hostlio Pro"),("7 giorni","di prova gratuita, senza impegno")],
  sup_h="Un team al tuo fianco",
  sup=[("rocket-launch","t-peach","Account in minuti, canali in giornata","Il tuo account è pronto in pochi minuti; aggiungi le tipologie di camera e collega i canali in giornata. Il piano Growth include una call di onboarding individuale."),
       ("lifebuoy","t-lilac","Assistenza in inglese e turco",'Hai un problema? Scrivi al team a <a href="mailto:{e}">{e}</a>.'),
       ("book-open-text","t-sand","Guide",'<a href="{b}">Articoli del blog</a> sulla gestione alberghiera e la distribuzione, più le <a href="{f}">domande frequenti</a>.')],
  sup_img=("gen-support-call","Albergatore che controlla le prenotazioni sul portatile"),
)

# ---------------------------------------------------------------- pages_v4 strings
PV4 = dict(trial="Prova gratis per 7 giorni", demo="Richiedi una demo", plan_h="Quale piano fa per te?",
           cmp_t='Per confrontarlo con altri software alberghieri, consulta il nostro <a href="{c}">confronto gestionali per hotel</a>.',
           see_pricing="Vedi i prezzi")

# ---------------------------------------------------------------- pages_v4.TYPES
def types(U):
    return [
 dict(key="t-guesthouse", img=("gen-guesthouse", "Una camera accogliente di un B&B con lampada da scrivania", 1080, 1350),
  title="Gestionale per B&B e affittacamere con AI | Hostlio Pro",
  desc="Gestionale per B&B e affittacamere: risposte automatiche agli ospiti in 30+ lingue, sincronizzazione Booking.com e Airbnb, check-in online. Da $49/mese.",
  crumb="Gestionale per B&B e affittacamere", h1='Il <em class="hl">gestionale per B&amp;B</em> che risponde agli ospiti al posto tuo',
  lead="In un B&B o in un affittacamere è una sola persona a gestire i messaggi notturni, le prenotazioni su più canali e il check-in. Hostlio Pro le toglie un bel peso.",
  q="Che cos'è un gestionale per B&B?",
  a="Un gestionale per B&B permette alle piccole strutture da 1 a 10 camere di gestire prenotazioni, disponibilità e comunicazione con gli ospiti in un unico posto. Hostlio Pro aggiunge Lio, un assistente AI che risponde alle domande degli ospiti 24/7 in oltre 30 lingue. Il piano Starter costa $49 al mese per strutture fino a 10 camere.",
  pains_h="Quali sono le difficoltà più comuni di B&B e affittacamere?",
  pains=[("Messaggi notturni","Domande su check-in in tarda serata, parcheggio e colazione arrivano a mezzanotte. Lio risponde nella lingua dell'ospite e tu leggi un riepilogo al mattino."),
         ("Più canali","Vendere la stessa camera su Booking.com e Airbnb causa doppie prenotazioni. Il channel manager sincronizza la disponibilità all'istante."),
         ("Documenti e registrazione","Trascrivere i dati degli ospiti alla reception richiede tempo. Il check-in online li raccoglie prima dell'arrivo."),
         ("Budget limitato","I software a commissione costano di più man mano che l'occupazione cresce. Hostlio Pro ha un canone mensile fisso.")],
  plan="Per la maggior parte dei B&B basta il piano <strong>Starter</strong>: fino a 10 camere, 1.000 messaggi AI al mese e messaggistica AI su WhatsApp. Scegli <strong>Pro</strong> se vuoi anche il check-in online e che Lio gestisca i messaggi delle OTA.",
  faq=[("Esiste un gestionale per B&B gratuito?","Puoi provare Hostlio Pro gratis per 7 giorni. Dopo, il piano Starter costa $49 al mese (prezzo early-bird riservato ai primi 50 clienti)."),
       ("È adatto a un B&B con 3 camere?","Sì. Starter è pensato per una struttura fino a 10 camere; il prezzo è lo stesso anche con meno camere."),
       ("Posso usare Airbnb e Booking.com insieme?","Sì. Hostlio Pro sincronizza entrambi, più oltre 100 altri canali, in un unico calendario tramite Channex.")]),
 dict(key="t-boutique", img=("gen-boutique-room", "Cortile di un boutique hotel con piscina e bouganville", 1080, 1350),
  title="Gestionale per boutique hotel con messaggi AI | Hostlio Pro",
  desc="Gestionale per boutique hotel: risposte personali agli ospiti internazionali in 30+ lingue, sincronizzazione con 100+ OTA, check-in online e vendita di transfer.",
  crumb="Gestionale per boutique hotel", h1='Il <em class="hl">gestionale per boutique hotel</em> costruito attorno all\'ospite',
  lead="Ciò che distingue un boutique hotel è l'attenzione personale. Hostlio Pro si occupa delle domande ripetitive, così il tuo team ha più tempo per gli ospiti.",
  q="Che cos'è un gestionale per boutique hotel?",
  a="Un gestionale per boutique hotel è un sistema di gestione alberghiera (PMS) per hotel da circa 10 a 50 camere con un concept distintivo. In Hostlio Pro l'assistente AI Lio risponde ai messaggi degli ospiti con le informazioni dell'hotel e nella lingua dell'ospite, mentre il channel manager mantiene sincronizzate oltre 100 OTA.",
  pains_h="Perché i boutique hotel hanno bisogno di un software dedicato?",
  pains=[("Ospiti multilingue","Molti ospiti arrivano dall'estero. Lio risponde a ogni messaggio nella lingua dell'ospite e con il tono del tuo hotel."),
         ("Ricavi extra","Transfer aeroportuali e tour contano molto per i boutique hotel. Lio li propone al momento giusto."),
         ("Tanto traffico dalle OTA","Le prenotazioni da Booking.com, Expedia e Airbnb compaiono in un unico planning camere, colorate per canale."),
         ("Check-in veloce","Con il check-in online e la firma digitale, gli ospiti ricevono un drink di benvenuto invece di un modulo da compilare.")],
  plan="Per i boutique hotel da 10 a 50 camere consigliamo <strong>Pro</strong>: 5.000 messaggi AI al mese, WhatsApp e caselle delle OTA (Booking.com, Airbnb, Expedia), check-in online, vendita di transfer e tour e l'app iOS.",
  faq=[("Qual è il miglior gestionale per un boutique hotel?","Dipende dal numero di camere, dal profilo degli ospiti e dal budget. Per hotel da 10–50 camere con molti ospiti internazionali che vogliono un prezzo fisso, la messaggistica AI e il channel manager di Hostlio Pro sono una buona scelta. Consulta la nostra pagina di confronto per altre opzioni."),
       ("Posso usare Hostlio Pro con il mio sito web attuale?","Sì. Hostlio Pro non sostituisce il tuo sito: gli ospiti che ti contattano su WhatsApp ricevono risposta da Lio nella stessa casella dei messaggi delle OTA."),
       ("Quanti utenti posso aggiungere?","Consulta la pagina dei prezzi per i dettagli dei piani, oppure chiedi al nostro team durante la demo.")]),
 dict(key="t-apart", img=("gen-apart", "Appartamento luminoso con biancheria bianca", 1080, 1350),
  title="Gestionale per residence: check-in online e OTA | Hostlio Pro",
  desc="Gestionale per residence, aparthotel e appartamenti: sincronizzazione Airbnb e Booking.com, check-in online con firma digitale e messaggi AI in 30+ lingue.",
  crumb="Gestionale per residence e aparthotel", h1='Il <em class="hl">gestionale per residence e aparthotel</em> pensato per la gestione a distanza',
  lead="Residence e aparthotel spesso non hanno una reception o l'hanno solo in certi orari, quindi comunicazione con gli ospiti e check-in avvengono a distanza. Hostlio Pro è fatto per questo.",
  q="Che cos'è un gestionale per residence e aparthotel?",
  a="Un gestionale per residence e aparthotel gestisce prenotazioni, canali e processi degli ospiti per strutture che vendono appartamenti e suite con cucina. In Hostlio Pro gli ospiti inviano i dati del documento e la firma tramite un link di check-in online prima dell'arrivo, e l'assistente AI Lio risponde alle domande sull'accesso in oltre 30 lingue.",
  pains_h="Cosa richiede più tempo in un residence?",
  pains=[("Check-in a distanza","Il modulo di check-in online raccoglie documento, accompagnatori e firma prima dell'arrivo."),
         ("Istruzioni di accesso","Le domande su consegna delle chiavi, Wi-Fi e parcheggio si ripetono. Lio risponde usando le informazioni della tua struttura."),
         ("Canali per soggiorni brevi","La disponibilità su Airbnb e Booking.com si sincronizza all'istante con connessioni certificate."),
         ("Soggiorni più lunghi","Prolungare un soggiorno o cambiare appartamento si fa con il drag-and-drop sul planning camere.")],
  plan="Il check-in online è incluso nei piani Pro e Growth, quindi per residence e aparthotel consigliamo <strong>Pro</strong>. Se gestisci due strutture, guarda il piano <strong>Growth</strong>.",
  faq=[("Hostlio Pro funziona per un residence senza reception?","Sì. Il check-in online e la messaggistica AI svolgono a distanza la raccolta delle informazioni e le risposte alle domande che farebbe una reception."),
       ("Risponde anche ai messaggi di Airbnb?","Con i piani Pro e Growth, i messaggi delle OTA, Airbnb compreso, arrivano nella casella di Lio."),
       ("C'è un limite di unità?","Starter supporta fino a 10 camere o unità, Pro fino a 50 e Growth fino a 150.")]),
 dict(key="t-hostel", img=("gen-hostel", "Hall con pareti rivestite in legno e sedute condivise", 1080, 1350),
  title="Gestionale per ostelli: messaggi multilingue | Hostlio Pro",
  desc="Gestionale per ostelli: sincronizzazione con Hostelworld, Booking.com e 100+ canali, messaggi AI agli ospiti in 30+ lingue e check-in online. 7 giorni gratis.",
  crumb="Gestionale per ostelli", h1='Il <em class="hl">gestionale per ostelli</em> per caselle di posta affollate e multilingue',
  lead="Gli ostelli hanno ospiti internazionali, tanti messaggi e team ridotti. Hostlio Pro gestisce le domande in più lingue e tiene tutti i canali in un unico calendario.",
  q="Che cos'è un gestionale per ostelli?",
  a="Un gestionale per ostelli gestisce prenotazioni, canali e comunicazione con gli ospiti per gli ostelli che vendono posti letto e camere. Hostlio Pro si collega a oltre 100 canali, Hostelworld compreso, con connessioni certificate e risponde alle domande degli ospiti in oltre 30 lingue con il suo assistente AI Lio.",
  pains_h="Di cosa hanno più bisogno gli ostelli?",
  pains=[("Traffico multilingue","I viaggiatori scrivono nella propria lingua. Lio risponde in ognuna di esse."),
         ("Hostelworld e OTA","Hostelworld, Booking.com e gli altri canali condividono un'unica disponibilità."),
         ("Tour e transfer","Tour della città e transfer aeroportuali sono extra molto diffusi negli ostelli; Lio li propone al momento giusto."),
         ("Turno di notte","Le domande notturne non aspettano il mattino; lo staff si occupa solo di ciò che richiede una decisione.")],
  plan="Per gli ostelli con molti messaggi consigliamo <strong>Pro</strong>, con 5.000 messaggi AI al mese. Pianifichiamo insieme la configurazione a posti letto durante la demo.",
  faq=[("Funziona con Hostelworld?","Sì. Hostelworld è tra i canali collegati a Channex."),
       ("È supportata la vendita a posto letto (dormitorio)?","Dipende dalla tua configurazione; pianifichiamo insieme la struttura di camere e posti letto durante la demo."),
       ("Quanti messaggi AI mi servono?","Circa 150 risposte automatiche al giorno corrispondono a circa 4.500 al mese, una quantità adatta al piano Pro.")]),
    ]

# ---------------------------------------------------------------- pages_v4.CMP
def cmp(U):
    return dict(
  title="Confronto gestionali per hotel 2026: prezzi e AI | Hostlio Pro",
  desc="Hostlio Pro, Cloudbeds, Mews, Little Hotelier e HotelRunner a confronto: prezzi pubblicati, prezzo di partenza, commissioni, prova gratuita e messaggi AI.",
  crumb="Confronto gestionali per hotel", h1='<em class="hl">Confronto</em> gestionali per hotel (2026)',
  lead="Abbiamo confrontato cinque gestionali per hotel molto diffusi tra le strutture indipendenti, usando solo ciò che ogni fornitore pubblica sulla propria pagina dei prezzi.",
  q="Quale gestionale per hotel fa per te?",
  a="In breve: per hotel con una sola struttura, 1–150 camere e molti ospiti internazionali, un software a prezzo fisso con la messaggistica AI inclusa (come Hostlio Pro) rende il budget prevedibile. I gruppi con più strutture ed esigenze enterprise possono valutare piattaforme su preventivo come Mews o Cloudbeds; le strutture in Turchia che cercano assistenza locale e una rete B2B possono guardare a HotelRunner; le piccole strutture che vogliono la rete SiteMinder possono considerare Little Hotelier.",
  cols=["Software","Prezzi pubblicati?","A partire da","Commissione sulle prenotazioni","Prova gratuita","Messaggi AI agli ospiti"],
  rows=[("Hostlio Pro","Sì","$49/mese (early bird)","Nessuna, canone mensile fisso","7 giorni","In tutti i piani (Lio, 30+ lingue)"),
        ("Cloudbeds","No, su preventivo","Preventivo","Dichiara di non applicare commissioni aggiuntive sulle prenotazioni da Booking Engine e Channel Manager","Non indicata nella pagina dei prezzi","Non indicati separatamente nella pagina dei prezzi"),
        ("Mews","No, su preventivo","Preventivo","Non indicata nella pagina dei prezzi","Non indicata nella pagina dei prezzi","Riepiloghi AI delle preferenze degli ospiti nel piano Advanced; messaggistica non indicata separatamente"),
        ("Little Hotelier","Calcolati in base al numero di camere","Tramite calcolatore dei prezzi","Commissione dell'1% sulle prenotazioni nel piano Basics","30 giorni","Non indicati nella pagina dei prezzi"),
        ("HotelRunner","Sì (piani principali)","$19,95/mese + 0,75% (Manage)","Dallo 0,75% all'1,25% a seconda del piano","Disponibile","Nel livello Advanced \"Automate\"")],
  when_h="Quale scegliere, e quando?",
  when=[("Hostlio Pro","Una o due strutture, 1–150 camere, tanti ospiti internazionali e un budget mensile fisso."),
        ("Cloudbeds e Mews","Gruppi con più strutture ed esigenze enterprise, come revenue management e un ampio marketplace di integrazioni."),
        ("HotelRunner","Strutture in Turchia che vogliono assistenza locale, una rete di vendita B2B e un canone fisso basso più commissione."),
        ("Little Hotelier","Piccole strutture che vogliono l'infrastruttura SiteMinder e accettano prezzi basati sul numero di camere.")],
  note="Informazioni raccolte il 21 settembre 2026 dalla pagina dei prezzi di ciascun fornitore; prezzi e piani possono cambiare, quindi verifica i dettagli aggiornati sulla pagina di ogni fornitore. Hostlio Pro è parte di questo confronto; abbiamo basato la tabella solo su informazioni pubblicate.",
  src_h="Fonti",
  faq=[("Che cos'è un gestionale per hotel?","Un gestionale per hotel (un PMS) permette a una struttura di gestire prenotazioni, disponibilità delle camere, canali di vendita e informazioni sugli ospiti in un unico posto."),
       ("Quanto costa un gestionale per hotel?","In base ai prezzi pubblicati, i piani partono all'incirca da $20 a $150 al mese; alcuni fornitori aggiungono una commissione sulle prenotazioni dello 0,75–1,25%, altri forniscono solo preventivi."),
       ("Meglio una commissione o un canone fisso?","Con l'aumentare dell'occupazione e delle tariffe medie, i costi a commissione crescono. Un canone mensile fisso è più prevedibile per gli hotel che vogliono un budget stabile.")])

# ---------------------------------------------------------------- pages_v4.GUIDES
def guides(U):
    return [
 dict(key="post-overbooking", date="2026-09-21", title="Come evitare l'overbooking: 6 passi per gli hotel",
  desc="Perché gli hotel finiscono in overbooking e come evitarlo: channel manager, regole di stop-sell, margini di disponibilità e cosa fare se succede comunque.",
  content=f'''<div class="answer"><p><strong>In breve:</strong> l'overbooking consiste nell'accettare più prenotazioni di quelle che puoi ospitare per la stessa camera e le stesse date. Negli hotel indipendenti la causa più comune è l'aggiornamento manuale della disponibilità su più OTA. Un channel manager bidirezionale e in tempo reale elimina gran parte del rischio.</p></div>
<h2>Perché si verifica l'overbooking?</h2>
<ul><li>Aggiornare a mano, separatamente, la disponibilità su Booking.com, Airbnb ed Expedia</li><li>Inserire in ritardo le prenotazioni telefoniche o walk-in</li><li>Cancellazioni e modifiche che arrivano su un canale ma non su un altro</li><li>Sincronizzazione ritardata (oraria) tra i canali</li></ul>
<h2>Evita l'overbooking in 6 passi</h2>
<ol><li><strong>Usa un'unica fonte di disponibilità.</strong> Ogni canale deve leggere la disponibilità da un solo calendario (il tuo PMS).</li>
<li><strong>Scegli una sincronizzazione bidirezionale e in tempo reale.</strong> Quando arriva una prenotazione, la camera deve chiudersi sugli altri canali in pochi secondi.</li>
<li><strong>Inserisci subito le prenotazioni dirette.</strong> Registra immediatamente le vendite telefoniche e walk-in nello stesso calendario.</li>
<li><strong>Gestisci stop-sell e soggiorni minimi da un unico posto.</strong> Modificarli canale per canale favorisce gli errori.</li>
<li><strong>Tieni un piccolo margine nei periodi di punta.</strong> Aprire l'ultima camera solo al tuo canale diretto riduce il rischio.</li>
<li><strong>Controlla regolarmente le mappature dei canali.</strong> Quando aggiungi una tipologia di camera, verifica la mappatura su ogni canale.</li></ol>
<h2>E se succede comunque?</h2>
<p>Avvisa l'ospite subito e con onestà, offri un'alternativa equivalente o migliore (un hotel vicino, un upgrade) e copri i costi extra, come i transfer. Annota quale canale ha causato il problema e perché.</p>
<h2>Come funziona in Hostlio Pro</h2>
<p>Il <a href="{U("channel")}">channel manager</a> di Hostlio Pro sincronizza la disponibilità in modo bidirezionale e in tempo reale su oltre 100 canali con connessioni certificate. Le prenotazioni compaiono in un unico planning camere, colorate per canale.</p>''',
  faq=[("Che cosa significa overbooking?","Si parla di overbooking quando un hotel accetta più prenotazioni di quante ne possa ospitare per la stessa camera e le stesse date; è detto anche doppia prenotazione."),
       ("Un channel manager evita del tutto l'overbooking?","La sincronizzazione bidirezionale in tempo reale elimina gran parte del rischio; le prenotazioni dirette non inserite e le mappature errate delle camere possono comunque causare problemi.")]),
 dict(key="post-autoreply", date="2026-09-21", title="Come rispondere in automatico ai messaggi di Booking.com",
  desc="Tre modi per automatizzare i messaggi degli ospiti di Booking.com: modelli, messaggi programmati e un assistente AI. Quando funziona ciascuno e quali limiti ha.",
  content=f'''<div class="answer"><p><strong>In breve:</strong> ci sono tre modi per automatizzare i messaggi di Booking.com: i modelli di messaggio salvati nell'extranet, i messaggi programmati legati alla fase della prenotazione e un assistente AI che capisce la domanda dell'ospite e risponde con le informazioni del tuo hotel. I modelli vanno bene per le informazioni standard; un assistente AI è adatto alle domande che cambiano da ospite a ospite.</p></div>
<h2>1. Modelli di messaggio</h2>
<p>Salva come modelli le risposte frequenti, come orario di check-in, indicazioni stradali e parcheggio, e inviale con un clic. Sono semplici, ma qualcuno deve comunque leggere il messaggio e scegliere il modello giusto.</p>
<h2>2. Messaggi programmati</h2>
<p>Messaggi inviati automaticamente dopo la prenotazione, il giorno prima dell'arrivo o il giorno della partenza. Gli ospiti ricevono le informazioni prima di chiederle, ma questi messaggi non rispondono alle domande che gli ospiti scrivono in seguito.</p>
<h2>3. Un assistente AI</h2>
<p>Legge il messaggio dell'ospite e scrive una risposta basata sulla tua knowledge base, nella lingua dell'ospite. Funziona al meglio per le domande notturne, in più lingue e fuori dai modelli, e deve lasciare allo staff le decisioni (sconti, reclami).</p>
<div class="table-wrap"><table><thead><tr><th>Metodo</th><th>Ideale per</th><th>Limite</th></tr></thead><tbody>
<tr><td>Modelli</td><td>Informazioni standard</td><td>Qualcuno deve leggere e scegliere</td></tr>
<tr><td>Messaggi programmati</td><td>Informazioni prima dell'arrivo</td><td>Non risponde alle domande in arrivo</td></tr>
<tr><td>Assistente AI</td><td>Domande a qualsiasi ora, in qualsiasi lingua</td><td>Richiede una buona knowledge base</td></tr></tbody></table></div>
<h2>Perché il tempo di risposta conta</h2>
<p>Una risposta rapida prima della prenotazione rende più facile la decisione dell'ospite; una risposta rapida durante il soggiorno incide su soddisfazione e recensioni.</p>
<h2>Come funziona in Hostlio Pro</h2>
<p>Con i piani Pro e Growth, i messaggi delle OTA, Booking.com compreso, arrivano nella casella di <a href="{U("ai")}">Lio, l'assistente AI</a>. Lio risponde con le informazioni del tuo hotel nella lingua dell'ospite e lascia a te ciò di cui non è sicuro.</p>''',
  faq=[("Si può rispondere in automatico ai messaggi di Booking.com?","Sì. I modelli dell'extranet e i messaggi programmati sono strumenti di Booking.com; per risposte automatiche specifiche per ogni domanda serve un assistente AI che legga i messaggi."),
       ("Un assistente AI può dare informazioni sbagliate?","Il rischio è basso quando l'assistente usa solo le informazioni fornite dall'hotel e passa allo staff le domande su cui non è sicuro.")]),
    ]

# ---------------------------------------------------------------- legal_v5
LEGAL_T = {
 "privacy": ("Informativa sulla privacy | Hostlio Pro", "Informativa sulla privacy di Hostlio Pro: quali dati raccogliamo, come li usiamo e condividiamo, sicurezza, conservazione, cookie e i tuoi diritti GDPR.", "Informativa sulla privacy"),
 "terms":   ("Termini di servizio | Hostlio Pro", "Termini di servizio di Hostlio Pro: descrizione del servizio, abbonamenti e pagamenti, disdetta e rimborsi, contenuti generati dall'AI, integrazioni OTA e responsabilità.", "Termini di servizio"),
}
LEGAL_NOTE = 'Ultimo aggiornamento: <time datetime="{iso}">{date}</time>, {addr}. Il presente testo è una traduzione dell\'originale in inglese; in caso di discrepanze prevale la <a href="{en_url}">versione inglese</a>.'

def privacy_body(U, EMAIL, ADDR, ul):
    return f'''<p>La presente Informativa sulla privacy descrive in che modo Hostlio Pro, gestito da Loti Members LLC ("noi" o "nostro"), raccoglie, utilizza e condivide le informazioni quando utilizzi la nostra piattaforma di gestione alberghiera su hostliopro.com.</p>
<h2>1. Informazioni che raccogliamo</h2><p>Raccogliamo le informazioni che ci fornisci direttamente, tra cui:</p>
{ul(["Dati dell'account: nome, indirizzo email, numero di telefono, nome dell'hotel, numero di camere","Dati di pagamento: elaborati in modo sicuro tramite Stripe (non conserviamo i dati delle carte)","Dati dell'hotel: prenotazioni, comunicazioni con gli ospiti, configurazioni delle camere","Dati di utilizzo: il modo in cui interagisci con la nostra piattaforma"])}
<h2>2. Come utilizziamo le tue informazioni</h2><p>Utilizziamo le informazioni raccolte per:</p>
{ul(["Fornire, mantenere e migliorare i nostri servizi","Elaborare i pagamenti e inviare notifiche di fatturazione","Inviare email transazionali e aggiornamenti sul prodotto","Rispondere ai tuoi commenti e alle tue domande","Monitorare e analizzare le modalità di utilizzo per migliorare l'esperienza utente","Adempiere agli obblighi di legge"])}
<h2>3. Condivisione delle informazioni</h2><p>Non vendiamo, scambiamo né noleggiamo i tuoi dati personali a terzi. Possiamo condividere le tue informazioni con:</p>
{ul(["<strong>Fornitori di servizi:</strong> Supabase (database), Make.com (automazione), Stripe (pagamenti), Vercel (hosting), Anthropic (elaborazione AI)","<strong>Channel manager:</strong> Channex API per la sincronizzazione con le OTA (Booking.com, Airbnb, ecc.)","<strong>Obblighi di legge:</strong> quando richiesto dalla legge o per tutelare i nostri diritti"])}
<h2>4. Sicurezza dei dati</h2><p>Adottiamo misure tecniche e organizzative adeguate a proteggere i tuoi dati personali da accessi non autorizzati, alterazioni, divulgazioni o distruzioni. La nostra infrastruttura è conforme a SOC 2 tramite Supabase e i pagamenti sono conformi a PCI DSS tramite Stripe.</p>
<h2>5. Conservazione dei dati</h2><p>Conserviamo i tuoi dati personali per tutto il tempo in cui il tuo account è attivo o per quanto necessario a fornire i servizi. Puoi richiedere in qualsiasi momento la cancellazione dei tuoi dati contattandoci all'indirizzo {EMAIL}.</p>
<h2>6. Diritti previsti dal GDPR</h2><p>Se ti trovi nello Spazio economico europeo, hai il diritto di accedere ai tuoi dati personali, di rettificarli o di cancellarli. Hai inoltre il diritto alla portabilità dei dati e il diritto di opporti al trattamento. Per esercitare questi diritti, contattaci all'indirizzo {EMAIL}.</p>
<h2>7. WhatsApp e messaggistica</h2><p>La nostra piattaforma è integrata con WhatsApp Business API per facilitare le comunicazioni con gli ospiti. Il contenuto dei messaggi viene elaborato per generare risposte AI e non viene utilizzato per finalità di marketing. I numeri di telefono degli ospiti sono conservati esclusivamente per finalità di comunicazione.</p>
<h2>8. Cookie</h2><p>Utilizziamo cookie essenziali per mantenere la tua sessione e le tue preferenze. Non utilizziamo cookie di tracciamento o pubblicitari. Puoi gestire i cookie tramite le impostazioni del tuo browser.</p>
<h2>9. Link a siti di terzi</h2><p>La nostra piattaforma può contenere link a siti web di terzi. Non siamo responsabili delle pratiche in materia di privacy di tali siti e ti invitiamo a leggere le relative informative sulla privacy.</p>
<h2>10. Modifiche alla presente Informativa</h2><p>Potremmo aggiornare periodicamente la presente Informativa sulla privacy. Ti informeremo di eventuali modifiche pubblicando la nuova informativa su questa pagina e aggiornando la data di "Ultimo aggiornamento".</p>
<h2>11. Contatti</h2><p>Per qualsiasi domanda sulla presente Informativa sulla privacy, contattaci:</p>
{ul([f'Email: <a href="mailto:{EMAIL}">{EMAIL}</a>', f"Indirizzo: {ADDR}"])}
<p>Per eliminare il tuo account, consulta la pagina <a href="{U("delacc")}">Elimina il tuo account</a>.</p>'''

def terms_body(U, EMAIL, ADDR, ul):
    pricing = U("pricing")
    privacy = U("privacy")
    return f'''<p>I presenti Termini di servizio ("Termini") disciplinano l'utilizzo di Hostlio Pro, gestito da Loti Members LLC ("Società", "noi" o "nostro"). Accedendo al nostro servizio o utilizzandolo, accetti di essere vincolato dai presenti Termini.</p>
<h2>1. Descrizione del servizio</h2><p>Hostlio Pro è una piattaforma di gestione alberghiera in cloud che offre comunicazione con gli ospiti basata sull'intelligenza artificiale, channel management, calendario planning camere e relativi strumenti per la gestione dell'ospitalità. Il servizio è disponibile in abbonamento su hostliopro.com.</p>
<h2>2. Registrazione dell'account</h2><p>Per utilizzare Hostlio Pro devi creare un account e fornire informazioni accurate e complete. Sei responsabile della riservatezza delle credenziali del tuo account e di tutte le attività svolte tramite il tuo account.</p>
<h2>3. Abbonamento e pagamenti</h2>
{ul(["Gli abbonamenti sono fatturati in anticipo su base mensile o annuale","Tutti i pagamenti sono elaborati in modo sicuro tramite Stripe","Prova gratuita di 7 giorni disponibile: il metodo di pagamento viene richiesto all'iscrizione, ma non viene effettuato alcun addebito fino al termine della prova","Al termine della prova, l'addebito avverrà in base al piano selezionato",f'I prezzi sono espressi in USD. I piani e le tariffe in vigore sono indicati nella nostra <a href="{pricing}">pagina dei prezzi</a>',"I piani annuali prevedono uno sconto del 20%"])}
<h2>4. Disdetta e rimborsi</h2><p>Puoi disdire il tuo abbonamento in qualsiasi momento. La disdetta ha effetto al termine del periodo di fatturazione in corso. Non sono previsti rimborsi per periodi di fatturazione parziali. Per disdire, contattaci all'indirizzo {EMAIL}.</p>
<h2>5. Uso consentito</h2><p>Ti impegni a non:</p>
{ul(["Utilizzare il servizio per scopi illeciti","Violare i termini delle piattaforme OTA (Booking.com, Airbnb, ecc.) attraverso le nostre integrazioni","Tentare di ottenere accesso non autorizzato ai nostri sistemi","Inviare spam o messaggi non richiesti agli ospiti","Rivendere o concedere in sublicenza il servizio senza autorizzazione scritta"])}
<h2>6. Contenuti generati dall'AI</h2><p>Hostlio Pro utilizza l'intelligenza artificiale per generare risposte ai messaggi degli ospiti. Riconosci che i contenuti generati dall'AI possono occasionalmente contenere errori. Sei responsabile della verifica e della gestione delle risposte AI inviate per conto della tua struttura. Non siamo responsabili di eventuali inesattezze nelle comunicazioni generate dall'AI.</p>
<h2>7. Integrazioni con i canali OTA</h2><p>La nostra piattaforma è integrata con canali OTA di terzi (Booking.com, Airbnb, Expedia, ecc.) tramite Channex API. Sei responsabile del rispetto dei termini di servizio di ciascuna piattaforma. Non siamo responsabili di modifiche alle API o alle politiche delle OTA che possano incidere sul funzionamento.</p>
<h2>8. Dati e privacy</h2><p>L'utilizzo di Hostlio Pro è inoltre disciplinato dalla nostra <a href="{privacy}">Informativa sulla privacy</a>, che è incorporata per riferimento nei presenti Termini. Mantieni la titolarità dei tuoi dati. Trattiamo i tuoi dati esclusivamente per fornire il servizio.</p>
<h2>9. Disponibilità del servizio</h2><p>Puntiamo a un uptime del 99,9%, ma non garantiamo un servizio ininterrotto. Possiamo effettuare manutenzioni programmate con preavviso. Non siamo responsabili delle perdite derivanti da interruzioni del servizio.</p>
<h2>10. Proprietà intellettuale</h2><p>Hostlio Pro e tutti i relativi software, design e contenuti sono di proprietà di Loti Members LLC. Non puoi copiare, modificare o distribuire alcuna parte del nostro servizio senza autorizzazione scritta.</p>
<h2>11. Limitazione di responsabilità</h2><p>Nella misura massima consentita dalla legge, Loti Members LLC non sarà responsabile di alcun danno indiretto, incidentale, speciale, consequenziale o punitivo, inclusa la perdita di profitti o di dati, derivante dall'utilizzo del servizio.</p>
<h2>12. Legge applicabile</h2><p>I presenti Termini sono disciplinati dalle leggi dello Stato della California, USA. Eventuali controversie saranno risolte dai tribunali della contea di Sacramento, California.</p>
<h2>13. Modifiche ai Termini</h2><p>Potremmo aggiornare periodicamente i presenti Termini. Ti informeremo delle modifiche rilevanti via email o tramite la piattaforma. L'uso continuato del servizio dopo le modifiche costituisce accettazione dei nuovi Termini.</p>
<h2>14. Contatti</h2><p>Per domande sui presenti Termini, contattaci:</p>
{ul([f'Email: <a href="mailto:{EMAIL}">{EMAIL}</a>', f"Indirizzo: {ADDR}"])}'''
