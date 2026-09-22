"""French (fr) data for the shared modules: build.py, home_v3.py, pages_v4.py, legal_v5.py.
Pure data + functions; no project imports. Links come from the U callable passed in."""

L = "fr"
UPDATED_TXT = "21 septembre 2026"
LEGAL_DATE_TXT = "20 avril 2026"

# ------------------------------------------------------------------ build.UI
UI = {
   "nav": [("features","Fonctionnalités"),("ai","Assistant IA Lio"),("channel","Channel manager"),("pricing","Tarifs"),("blog","Blog")],
   "top": [("pricing","Tarifs"),("blog","Blog"),("faq","FAQ"),("about","À propos")],
   "login":"Connexion", "trial":"Essai gratuit", "demo":"Demander une démo", "menu":"Ouvrir le menu",
   "skip":"Aller au contenu", "home":"Accueil",
   "lang_label":"Langue", "crumb_label":"Fil d’Ariane",
   "foot_tag":"Logiciel de gestion hôtelière propulsé par l’IA pour les hôtels indépendants. Messagerie clients, gestion des canaux et calendrier des réservations réunis au même endroit.",
   "foot_product":"Produit","foot_company":"Entreprise","foot_res":"Ressources","foot_sol":"Solutions","privacy":"Politique de confidentialité","terms":"Conditions d’utilisation","delacc":"Supprimer le compte","sol":["Logiciel pour hôtel boutique","Logiciel pour chambres d’hôtes","Logiciel pour résidences hôtelières","Logiciel pour auberges de jeunesse","Comparatif des logiciels hôteliers"],
   "foot_about":"À propos","foot_contact":"Contact","foot_faq":"FAQ",
   "rights":"Tous droits réservés.","updated":"Dernière mise à jour",
   "final_h":"Votre réception reste ouverte ce soir aussi.",
   "final_p":"Essayez gratuitement pendant 7 jours. Aucun prélèvement avant la fin de l’essai, résiliable à tout moment.",
   "faq_h":"Questions fréquentes",
}

# ------------------------------------------------------------------ build.MEGA
MEGA = {"btn":"Produit","cols":[
   ("Clients",[("ai","sparkle","Assistant IA Lio","Réponses aux clients 24h/24 en 30+ langues"),("checkin","identification-card","Check-in en ligne","Pièce d’identité, accompagnants et signature électronique")]),
   ("Distribution",[("channel","arrows-left-right","Channel manager","100+ OTA sur un seul calendrier"),("features","calendar-dots","Planning des chambres","Calendrier des réservations en glisser-déposer")]),
   ("Exploitation",[("features","van","Transferts et excursions","Des revenus en plus pendant la conversation"),("features","device-mobile","Application mobile","Sur iOS, même hors connexion")]),
   ("Par type d’établissement",[("t-boutique","sparkle","Hôtels boutique","Hôtels de 10 à 50 chambres"),("t-guesthouse","users-three","Chambres d’hôtes","Établissements de 1 à 10 chambres"),("t-apart","calendar-dots","Résidences hôtelières","Appartements et suites"),("t-hostel","globe-simple","Auberges de jeunesse","Vente au lit")]),
  ],"feat":("pricing","Comparer les formules","À partir de 49 $ par mois, 7 jours offerts")}

# ------------------------------------------------------------------ build.software_schema / room_rack / 404
SOFT_DESC = "Logiciel de gestion hôtelière propulsé par l’IA pour les hôtels indépendants : messagerie clients 24h/24 en 30+ langues, channel manager pour 100+ OTA, calendrier des réservations et check-in en ligne."
SOFT_FEATURES = ["Assistant IA Lio pour les clients (30+ langues)", "Channel manager (100+ OTA via Channex)", "Calendrier des réservations en glisser-déposer", "Check-in en ligne avec signature électronique", "Formulaires de visa PDF automatiques", "Vente de transferts et d’excursions", "Application mobile utilisable hors connexion"]
DAYS = ["Lun","Mar","Mer","Jeu","Ven","Sam","Dim"]
RACK = ("Planning des chambres", "Septembre, semaine 3", "Réservations colorées par canal : Booking.com en bleu, Airbnb en pêche, Expedia en lilas, Agoda en sable, direct en vert")
NOTFOUND = ("Page introuvable | Hostlio Pro", "La page que vous cherchez a peut-être été déplacée ou supprimée.", "Page introuvable",
            'L’adresse a peut-être changé. <a href="{home}">Revenir à l’accueil</a>.')

# ------------------------------------------------------------------ home_v3.T
HOME = dict(
  title="Hostlio Pro | Logiciel de gestion hôtelière avec IA",
  desc="Logiciel de gestion hôtelière Hostlio Pro : l’assistant IA Lio répond aux clients 24h/24 en 30+ langues et le channel manager synchronise 100+ OTA. 7 jours offerts.",
  h1='Pendant que votre hôtel dort, <em class="hl">Lio</em> répond',
  lead="Le logiciel de gestion hôtelière propulsé par l’IA pour les hôtels indépendants et les chambres d’hôtes. Réservations, 100+ canaux et messages clients au même endroit, en 30+ langues.",
  try_="Essai gratuit", demo="Demander une démo", via="Connecté via Channex :", more="et 100+ autres",
  coll_alt1="Cour d’un hôtel boutique avec bougainvilliers et piscine au coucher du soleil", coll_alt2="Hôtelier souriant tenant une tasse de café",
  chip1=("Chambre 202 vendue","Booking.com, 21:40"), chip2="Fermée sur Airbnb et Expedia",
  bub_h=("Lio","Réceptionniste IA, en ligne"), bub_in="Hallo! Ist ein später Check-in möglich?", bub_out="Natürlich! Unsere Rezeption ist rund um die Uhr besetzt.", bub_note="Répondu en allemand, 4 s",
  pick_h="Par quoi voulez-vous commencer ?", pick_p="Choisissez ce qui compte pour vous, nous configurons votre compte en conséquence.", pick_none="Choisissez-en autant que vous voulez.", pick_some="{n} sélectionné(s), essayez-les gratuitement pendant 7 jours.", pick_btn="Commencer", pick_name="interest",
  tiles=[("ai","sparkle","t-peach","Assistant IA Lio","Réponses aux clients en 30+ langues"),("channel","arrows-left-right","t-lilac","Channel manager","Synchro en temps réel avec 100+ OTA"),("rack","calendar-dots","t-sand","Planning des chambres","Calendrier des réservations en glisser-déposer"),("checkin","identification-card","t-peach","Check-in en ligne","Identité et signature avant l’arrivée"),("upsell","van","t-lilac","Transferts et excursions","Des revenus en plus pendant la conversation"),("mobile","device-mobile","t-sand","Application mobile","Gérez l’hôtel où que vous soyez")],
  story_h='<em class="hl">2 h 14</em>, un client écrit',
  story_p="Ce qui se passe pendant votre sommeil, en trois images.",
  story=[("brand-night","Hôtelier endormi, un téléphone qui s’allume sur la table de nuit","02:14","Un client envoie un message","Un client venu d’Allemagne demande s’il peut arriver tard. Vous dormez profondément."),
         ("brand-phone","Main tenant un téléphone affichant l’écran de réponse orange de Lio","02:14","Lio répond aussitôt","Avec les informations de votre hôtel, dans la langue du client. Et vous laisse une note si besoin."),
         ("brand-hotelier","Hôtelier traversant le hall avec son café du matin","08:30","Au réveil, tout est réglé","La conversation vous attend dans votre tableau de bord, traduite. Un client satisfait, et vous reposé.")],
  story_chip="Lio a répondu",
  tour_h='Pilotez la journée de votre hôtel <em class="hl">depuis un seul écran</em>', tour_p="Messages clients, réservations, canaux et check-in fonctionnent ensemble.", tour_label="Visite du produit",
  tabs=["Messages","Calendrier","Canaux","Check-in"],
  st=[("Tous les messages clients dans une seule boîte","WhatsApp et messages des OTA (Booking.com, Airbnb, Expedia) réunis. Lio répond avec les informations de votre hôtel, et vous ne voyez que ce qui a besoin de vous.",["Réponses automatiques en 30+ langues","Détails de la réservation à côté de chaque message","Vous transmet ce dont il n’est pas sûr"],"ai","Comment fonctionne Lio"),
      ("Toute votre semaine sur le planning des chambres","Chaque réservation apparaît dans la couleur de son canal. Changer de chambre, prolonger un séjour ou bloquer des dates se fait d’un seul geste.",["Changements de chambre en glisser-déposer","Réservations colorées par canal","Le même calendrier sur le web et sur iOS"],"features","Toutes les fonctionnalités"),
      ("100+ canaux, une seule disponibilité","Synchronisation bidirectionnelle via Channex. Une chambre vendue sur un canal se ferme instantanément sur les autres.",["Tarifs et restrictions depuis un seul écran","Nouvelles réservations et annulations intégrées automatiquement","Aucun risque de surréservation"],"channel","Channel manager"),
      ("Le check-in est fait avant l’arrivée","Les clients envoient leurs informations d’identité, leurs accompagnants et leur signature depuis leur téléphone, via un lien sécurisé.",["Dans le navigateur, sans application à télécharger","Accompagnants dans un seul formulaire","Signature électronique et consentement"],"checkin","Check-in en ligne")],
  inbox_top=("Boîte de réception","12 conversations ouvertes"), inbox_note="Traduction : le check-in est à partir de 14 h, nous pouvons garder vos bagages.",
  chan_top=("Canaux connectés","Dernière synchro : à l’instant"), sync="Synchronisé",
  ci_top=("Check-in en ligne","Chambre 202"), ci_f=[("Nom complet","Keiko Sato"),("Nationalité","Japon"),("Accompagnants","1 personne ajoutée")], ci_sig="Signature",
  bento_h='<em class="hl">Tout</em> ce dont un hôtel a besoin', bento_p="Chaque module est connecté : pas d’outils séparés, pas de mots de passe multiples.",
  b_lio=("Assistant IA Lio","Règle la plupart des questions des clients avant même que vous les voyiez et vous résume le reste.","Is breakfast included?","Yes, from 7:30 to 10:30 on the terrace."),
  b_chan=("Channel manager","100+ canaux de vente via Channex, une seule disponibilité."),
  b_rack=("Planning des chambres","Calendrier des réservations en glisser-déposer."),
  b_ci=("Check-in en ligne","Identité, accompagnants et signature électronique avant l’arrivée."),
  b_pdf=("Formulaires de visa PDF","Attestations d’hébergement et lettres d’invitation en un clic.","Attestation d’hébergement","PDF"),
  b_tr=("Vente de transferts et d’excursions","Lio les propose au bon moment ; vous gagnez plus.","Transfert aéroport","+35 €"),
  b_lang=("30+ langues","Dans la langue où le client écrit, dans cette langue il reçoit sa réponse."),
  b_mob=("Application mobile","Réservations, messages et check-ins sur iOS, même hors connexion."),
  types_h='Conçu pour <em class="hl">tous les types d’établissements</em>', types_p="Pensé pour les établissements indépendants de 10 à 150 chambres.",
  types=[("brand-courtyard","Cour d’un hôtel boutique avec piscine et bougainvilliers","Hôtel boutique","10–50 chambres","Beaucoup de clients internationaux, chaque message est personnel."),
         ("gen-hostel","Hall aux boiseries avec espace commun","Auberge de jeunesse","Lits et chambres","Voyageurs multilingues, boîtes de réception chargées."),
         ("gen-guesthouse","Chambre d’hôtes chaleureuse avec une lampe de bureau","Chambres d’hôtes","1–10 chambres","Une équipe de nuit pour une équipe d’une seule personne."),
         ("gen-apart","Appartement lumineux au linge de lit blanc","Résidence hôtelière","10–40 logements","Le check-in en ligne pour une arrivée sans clé.")],
  plans_h="Une formule adaptée à la taille de votre hôtel", plans_p="Un abonnement mensuel fixe, sans engagement de longue durée. Chaque formule est gratuite pendant 7 jours.",
  early="20 % de réduction pour les 50 premiers clients, garantie à vie", tax='Prix hors taxes. <a href="{p}">Comparer les formules en détail</a>.',
  ai_h='Lio, <em class="hl">l’équipe de nuit</em> de votre réception', ai_p="Un assistant IA qui s’appuie sur les informations de votre hôtel. Il répond aux clients, vend des services en plus et vous laisse le reste.",
  ai_wide=("Répond dans la langue du client","Une question en japonais reçoit une réponse en japonais, une question en arabe une réponse en arabe. Vous lisez la conversation dans votre propre langue."),
  ai_cards=[("van","Vend pour vous","Propose transferts aéroport et excursions au bon moment et rattache la demande à la réservation."),("hand-arrow-up","Sait passer la main","Les messages qui demandent une décision, comme les remises, les réclamations ou les demandes particulières, vont à votre équipe."),("calendar-dots","Connaît la réservation","Quel client, quelle chambre, quelles dates : chaque réponse s’appuie sur les détails de la réservation.")],
  ai_photo=("brand-guest-phone","Cliente près d’une fenêtre écrivant un message sur son téléphone","Sur WhatsApp et les OTA","WhatsApp, Booking.com, Airbnb et Expedia."),
  ai_btn="Découvrir Lio",
  answer="<strong>Qu’est-ce que Hostlio Pro ?</strong> Hostlio Pro est un logiciel de gestion hôtelière dans le cloud (un PMS hôtelier) pour les hôtels indépendants et les chambres d’hôtes de 10 à 150 chambres. Il confie la communication avec les clients à l’IA, regroupe les réservations des OTA dans un seul calendrier et déplace le check-in sur le téléphone du client. Il se gère depuis le web et une application iOS, et il est utilisé dans plus de 20 pays.",
  stats=[("30+","langues prises en charge"),("100+","OTA et canaux de vente"),("20+","pays avec des hôtels Hostlio Pro"),("7 jours","d’essai gratuit, sans engagement")],
  sup_h="Une équipe à vos côtés",
  sup=[("rocket-launch","t-peach","Mise en place le jour même","Ajoutez vos types de chambres et connectez vos canaux. La formule Growth inclut un appel d’intégration individuel."),
       ("lifebuoy","t-lilac","Assistance en anglais et en turc",'Un blocage ? Contactez l’équipe à <a href="mailto:{e}">{e}</a>.'),
       ("book-open-text","t-sand","Guides",'Des <a href="{b}">articles de blog</a> sur la gestion hôtelière et la distribution, ainsi que des <a href="{f}">questions fréquentes</a>.')],
  sup_img=("gen-support-call","Hôtelier consultant les réservations sur un ordinateur portable"),
)

# ------------------------------------------------------------------ pages_v4
PV4 = dict(trial="Essayez gratuitement pendant 7 jours", demo="Demander une démo", plan_h="Quelle formule choisir ?",
           cmp_t='Pour comparer avec d’autres logiciels hôteliers, consultez notre <a href="{c}">comparatif des logiciels hôteliers</a>.',
           see_pricing="Voir les tarifs")

def types(U):
    return [
 dict(key="t-guesthouse", img=("gen-guesthouse", "Chambre d’hôtes chaleureuse avec une lampe de bureau", 1080, 1350),
  title="Logiciel pour chambres d’hôtes avec IA | Hostlio Pro",
  desc="Logiciel de gestion pour chambres d’hôtes : réponses automatiques aux clients en 30+ langues, synchro Booking.com et Airbnb, check-in en ligne. Dès 49 $/mois.",
  crumb="Logiciel pour chambres d’hôtes", h1='Le <em class="hl">logiciel pour chambres d’hôtes</em> qui répond aux clients à votre place',
  lead="Dans des chambres d’hôtes, une seule personne gère les messages tardifs, les réservations sur plusieurs canaux et le check-in. Hostlio Pro allège sa charge.",
  q="Qu’est-ce qu’un logiciel pour chambres d’hôtes ?",
  a="Un logiciel pour chambres d’hôtes permet aux petits établissements de 1 à 10 chambres de gérer réservations, disponibilités et communication avec les clients au même endroit. Hostlio Pro y ajoute Lio, un assistant IA qui répond aux questions des clients 24h/24 dans plus de 30 langues. La formule Starter coûte 49 $ par mois pour les établissements jusqu’à 10 chambres.",
  pains_h="Quelles sont les principales difficultés des chambres d’hôtes ?",
  pains=[("Messages de nuit","Arrivée tardive, parking, petit-déjeuner : les questions tombent à minuit. Lio répond dans la langue du client et vous lisez un résumé le matin."),
         ("Plusieurs canaux","Vendre la même chambre sur Booking.com et Airbnb provoque des doubles réservations. Le channel manager synchronise les disponibilités instantanément."),
         ("Identité et enregistrement","Saisir les informations des clients à l’accueil prend du temps. Le check-in en ligne les recueille avant l’arrivée."),
         ("Budget serré","Les logiciels à commission coûtent plus cher à mesure que le taux d’occupation augmente. Hostlio Pro est un abonnement mensuel fixe.")],
  plan="Pour la plupart des chambres d’hôtes, la formule <strong>Starter</strong> suffit : jusqu’à 10 chambres, 1 000 messages IA par mois et la messagerie IA sur WhatsApp. Choisissez <strong>Pro</strong> si vous voulez aussi le check-in en ligne et que Lio gère les messages des OTA.",
  faq=[("Existe-t-il un logiciel gratuit pour chambres d’hôtes ?","Vous pouvez essayer Hostlio Pro gratuitement pendant 7 jours. Ensuite, la formule Starter coûte 49 $ par mois (prix de lancement pour les 50 premiers clients)."),
       ("Convient-il à des chambres d’hôtes de 3 chambres ?","Oui. Starter est conçu pour un établissement jusqu’à 10 chambres ; le prix est le même avec moins de chambres."),
       ("Puis-je utiliser Airbnb et Booking.com ensemble ?","Oui. Hostlio Pro synchronise les deux, ainsi que 100+ autres canaux, sur un seul calendrier via Channex.")]),
 dict(key="t-boutique", img=("gen-boutique-room", "Cour d’un hôtel boutique avec piscine et bougainvilliers", 1080, 1350),
  title="Logiciel pour hôtel boutique et messagerie IA | Hostlio Pro",
  desc="Logiciel pour hôtel boutique : réponses personnalisées aux clients internationaux en 30+ langues, synchro 100+ OTA, check-in en ligne et vente de transferts.",
  crumb="Logiciel pour hôtel boutique", h1='Un <em class="hl">logiciel pour hôtel boutique</em> pensé autour du client',
  lead="Ce qui distingue un hôtel boutique, c’est l’attention personnelle. Hostlio Pro prend en charge les questions répétitives pour que votre équipe ait plus de temps pour les clients.",
  q="Qu’est-ce qu’un logiciel pour hôtel boutique ?",
  a="Un logiciel pour hôtel boutique est un système de gestion hôtelière (PMS) destiné aux hôtels d’environ 10 à 50 chambres au concept affirmé. Dans Hostlio Pro, l’assistant IA Lio répond aux messages des clients avec les informations propres à l’hôtel et dans la langue du client, et le channel manager synchronise plus de 100 OTA.",
  pains_h="Pourquoi les hôtels boutique ont-ils besoin d’un logiciel dédié ?",
  pains=[("Clients multilingues","Beaucoup de clients viennent de l’étranger. Lio répond à chaque message dans la langue du client et sur le ton de votre hôtel."),
         ("Revenus complémentaires","Les transferts aéroport et les excursions comptent pour un hôtel boutique. Lio les propose au bon moment."),
         ("Trafic OTA important","Les réservations Booking.com, Expedia et Airbnb apparaissent sur un seul planning des chambres, colorées par canal."),
         ("Check-in rapide","Grâce au check-in en ligne et à la signature électronique, les clients reçoivent une boisson de bienvenue au lieu d’un formulaire.")],
  plan="Pour les hôtels boutique de 10 à 50 chambres, nous recommandons <strong>Pro</strong> : 5 000 messages IA par mois, WhatsApp et messagerie des OTA (Booking.com, Airbnb, Expedia), check-in en ligne, vente de transferts et d’excursions et application iOS.",
  faq=[("Quel est le meilleur logiciel pour un hôtel boutique ?","Cela dépend du nombre de chambres, du profil des clients et du budget. Pour les hôtels de 10 à 50 chambres qui accueillent beaucoup de clients internationaux et veulent un prix fixe, la messagerie IA et le channel manager de Hostlio Pro sont un bon choix. Consultez notre page comparative pour d’autres options."),
       ("Lio répond-il aux messages des OTA ?","Oui, avec Pro et Growth : les messages Booking.com, Airbnb et Expedia arrivent dans la même boîte de réception que WhatsApp, et Lio y répond. Starter synchronise les réservations des OTA et répond aux clients sur WhatsApp."),
       ("Combien d’utilisateurs puis-je ajouter ?","Consultez la page des tarifs pour le détail des formules, ou posez la question à notre équipe pendant la démo.")]),
 dict(key="t-apart", img=("gen-apart", "Appartement lumineux au linge de lit blanc", 1080, 1350),
  title="Logiciel pour résidence hôtelière et aparthotel | Hostlio Pro",
  desc="Logiciel pour résidence hôtelière et appart’hôtel : synchro Airbnb et Booking.com, check-in en ligne avec signature électronique et messagerie IA en 30+ langues.",
  crumb="Logiciel pour résidences hôtelières", h1='Un <em class="hl">logiciel pour résidences hôtelières</em> géré à distance',
  lead="Les résidences hôtelières n’ont souvent pas de réception, ou des horaires limités : la communication avec les clients et le check-in se font à distance. Hostlio Pro est conçu pour cela.",
  q="Qu’est-ce qu’un logiciel pour résidence hôtelière ?",
  a="Un logiciel pour résidence hôtelière (aparthotel) gère les réservations, les canaux et le parcours client des établissements qui vendent des appartements et des suites équipés d’une cuisine. Dans Hostlio Pro, les clients envoient leurs informations d’identité et leur signature via un lien de check-in en ligne avant l’arrivée, et l’assistant IA Lio répond aux questions d’accès en 30+ langues.",
  pains_h="Qu’est-ce qui prend le plus de temps dans une résidence hôtelière ?",
  pains=[("Check-in à distance","Le formulaire de check-in en ligne recueille l’identité, les accompagnants et la signature avant l’arrivée."),
         ("Instructions d’accès","Remise des clés, Wi-Fi, parking : les questions se répètent. Lio y répond à partir des informations de votre établissement."),
         ("Canaux de courte durée","Les disponibilités Airbnb et Booking.com se synchronisent instantanément via Channex."),
         ("Séjours plus longs","Prolonger un séjour ou changer d’appartement se fait par glisser-déposer sur le planning des chambres.")],
  plan="Le check-in en ligne est inclus dans Pro et Growth ; nous recommandons donc <strong>Pro</strong> pour les résidences hôtelières. Si vous gérez deux établissements, regardez <strong>Growth</strong>.",
  faq=[("Hostlio Pro fonctionne-t-il pour une résidence hôtelière sans réception ?","Oui. Le check-in en ligne et la messagerie IA prennent en charge, à distance, la collecte d’informations et les réponses aux questions qu’assurerait une réception."),
       ("Répond-il aux messages Airbnb ?","Avec Pro et Growth, les messages des OTA, y compris Airbnb, arrivent dans la boîte de réception de Lio."),
       ("Y a-t-il une limite de logements ?","Starter prend en charge jusqu’à 10 chambres ou logements, Pro 50 et Growth 150.")]),
 dict(key="t-hostel", img=("gen-hostel", "Hall aux boiseries avec espace commun", 1080, 1350),
  title="Logiciel pour auberge de jeunesse et hostel | Hostlio Pro",
  desc="Logiciel pour auberge de jeunesse et hostel : synchro Hostelworld, Booking.com et 100+ canaux, messagerie IA en 30+ langues et check-in en ligne. 7 jours offerts.",
  crumb="Logiciel pour auberges de jeunesse", h1='Un <em class="hl">logiciel pour auberges de jeunesse</em> aux boîtes de réception chargées et multilingues',
  lead="Les auberges de jeunesse accueillent des clients du monde entier, reçoivent beaucoup de messages et fonctionnent avec de petites équipes. Hostlio Pro gère les questions multilingues et réunit les canaux sur un seul calendrier.",
  q="Qu’est-ce qu’un logiciel pour auberge de jeunesse ?",
  a="Un logiciel pour auberge de jeunesse (hostel) gère les réservations, les canaux et la communication avec les clients des établissements qui vendent des lits et des chambres. Hostlio Pro se connecte à plus de 100 canaux, dont Hostelworld, via Channex et répond aux questions des clients en 30+ langues grâce à son assistant IA Lio.",
  pains_h="De quoi les auberges de jeunesse ont-elles le plus besoin ?",
  pains=[("Trafic multilingue","Les voyageurs écrivent dans leur propre langue. Lio répond dans chacune d’elles."),
         ("Hostelworld et OTA","Hostelworld, Booking.com et les autres canaux partagent une seule disponibilité."),
         ("Excursions et transferts","Visites de la ville et transferts aéroport sont des extras courants en auberge ; Lio les propose au bon moment."),
         ("Équipe de nuit","Les questions nocturnes n’attendent pas le matin ; l’équipe ne traite que ce qui demande une décision.")],
  plan="Pour les auberges à fort volume de messages, nous recommandons <strong>Pro</strong> avec 5 000 messages IA par mois. Préparons ensemble votre configuration au lit pendant la démo.",
  faq=[("Fonctionne-t-il avec Hostelworld ?","Oui. Hostelworld fait partie des canaux connectés à Channex."),
       ("La vente au lit (dortoirs) est-elle prise en charge ?","Cela dépend de votre configuration ; préparons ensemble la structure de vos chambres et de vos lits pendant la démo."),
       ("De combien de messages IA ai-je besoin ?","Environ 150 réponses automatiques par jour représentent à peu près 4 500 messages par mois, ce qui correspond à la formule Pro.")]),
    ]

def cmp(U):
    return dict(
  title="Comparatif des logiciels hôteliers 2026 | Hostlio Pro",
  desc="Hostlio Pro, Cloudbeds, Mews, Little Hotelier et HotelRunner comparés : tarifs publiés, prix de départ, commissions, essai gratuit et messagerie IA.",
  crumb="Comparatif des logiciels hôteliers", h1='<em class="hl">Comparatif</em> des logiciels hôteliers (2026)',
  lead="Nous avons comparé cinq logiciels de gestion hôtelière populaires auprès des hôtels indépendants, en nous appuyant uniquement sur ce que chaque éditeur publie sur sa propre page de tarifs.",
  q="Quel logiciel hôtelier vous convient ?",
  a="Réponse courte : pour les hôtels à établissement unique de 10 à 150 chambres qui accueillent beaucoup de clients internationaux, un logiciel à prix fixe incluant la messagerie IA (comme Hostlio Pro) garde le budget prévisible. Les groupes multi-établissements aux besoins de grand compte peuvent envisager des plateformes sur devis comme Mews ou Cloudbeds ; les établissements en Turquie qui veulent un support local et un réseau B2B peuvent regarder HotelRunner ; les petits établissements qui souhaitent profiter du réseau SiteMinder peuvent envisager Little Hotelier.",
  cols=["Logiciel","Tarifs publiés ?","À partir de","Commission sur les réservations","Essai gratuit","Messagerie IA pour les clients"],
  rows=[("Hostlio Pro","Oui","49 $/mois (prix de lancement)","Aucune, abonnement mensuel fixe","7 jours","Toutes les formules (Lio, 30+ langues)"),
        ("Cloudbeds","Non, sur devis","Devis","Indique ne prélever aucune commission supplémentaire sur les réservations du Booking Engine et du Channel Manager","Non indiqué sur la page de tarifs","Non indiqué séparément sur la page de tarifs"),
        ("Mews","Non, sur devis","Devis","Non indiqué sur la page de tarifs","Non indiqué sur la page de tarifs","Résumés IA des préférences des clients dans Advanced ; messagerie non indiquée séparément"),
        ("Little Hotelier","Calculés selon le nombre de chambres","Via un simulateur de prix","Frais de réservation de 1 % dans Basics","30 jours","Non indiqué sur la page de tarifs"),
        ("HotelRunner","Oui (formules de base)","19,95 $/mois + 0,75 % (Manage)","De 0,75 % à 1,25 % selon la formule","Disponible","Dans le niveau Advanced « Automate »")],
  when_h="Lequel choisir, et quand ?",
  when=[("Hostlio Pro","Un ou deux établissements, 10 à 150 chambres, beaucoup de clients internationaux et un budget mensuel fixe."),
        ("Cloudbeds et Mews","Groupes multi-établissements aux besoins de grand compte, comme le revenue management et une large place de marché d’intégrations."),
        ("HotelRunner","Établissements en Turquie qui veulent un support local, un réseau de vente B2B et un faible abonnement fixe plus commission."),
        ("Little Hotelier","Petits établissements qui souhaitent l’infrastructure SiteMinder et acceptent une tarification selon le nombre de chambres.")],
  note="Informations recueillies le 21 septembre 2026 sur la page de tarifs de chaque éditeur ; les prix et les formules peuvent changer, vérifiez donc la page de chaque éditeur pour les informations à jour. Hostlio Pro est partie prenante de ce comparatif ; nous avons établi le tableau uniquement à partir d’informations publiées.",
  src_h="Sources",
  faq=[("Qu’est-ce qu’un logiciel de gestion hôtelière ?","Un logiciel de gestion hôtelière (un PMS) permet à un établissement de gérer les réservations, la disponibilité des chambres, les canaux de vente et les informations des clients au même endroit."),
       ("Combien coûte un logiciel hôtelier ?","D’après les prix publiés, les formules démarrent entre 20 $ et 150 $ environ par mois ; certains éditeurs ajoutent des frais de réservation de 0,75 à 1,25 %, d’autres ne fournissent que des devis."),
       ("Vaut-il mieux une commission ou un abonnement fixe ?","Quand le taux d’occupation et le prix moyen augmentent, le coût d’un modèle à commission augmente aussi. Un abonnement mensuel fixe est plus prévisible pour les hôtels qui veulent maîtriser leur budget.")])

def guides(U):
    return [
 dict(key="post-overbooking", date="2026-09-21", title="Comment éviter la surréservation : 6 étapes pour les hôtels",
  desc="Pourquoi les hôtels subissent la surréservation et comment l’éviter : channel manager, stop-sell, marges de disponibilité et que faire si elle survient.",
  content=f'''<div class="answer"><p><strong>Réponse courte :</strong> la surréservation (overbooking) consiste à accepter plus de réservations que vous ne pouvez en accueillir pour la même chambre et les mêmes dates. Dans les hôtels indépendants, la cause la plus fréquente est la mise à jour manuelle des disponibilités sur plusieurs OTA. Un channel manager bidirectionnel en temps réel élimine l’essentiel du risque.</p></div>
<h2>Pourquoi la surréservation se produit-elle ?</h2>
<ul><li>Mettre à jour les disponibilités sur Booking.com, Airbnb et Expedia séparément, à la main</li><li>Saisir en retard les réservations par téléphone ou au comptoir</li><li>Des annulations et modifications qui atteignent un canal mais pas un autre</li><li>Une synchronisation différée (toutes les heures) entre les canaux</li></ul>
<h2>Éviter la surréservation en 6 étapes</h2>
<ol><li><strong>Utilisez une seule source de disponibilité.</strong> Chaque canal doit lire les disponibilités depuis un seul calendrier (votre PMS).</li>
<li><strong>Choisissez une synchronisation bidirectionnelle en temps réel.</strong> Quand une réservation arrive, la chambre doit se fermer sur les autres canaux en quelques secondes.</li>
<li><strong>Saisissez immédiatement les réservations directes.</strong> Ajoutez tout de suite les ventes par téléphone et au comptoir dans le même calendrier.</li>
<li><strong>Gérez les stop-sell et les durées minimales de séjour au même endroit.</strong> Les modifier canal par canal favorise les erreurs.</li>
<li><strong>Gardez une petite marge en haute saison.</strong> N’ouvrir la dernière chambre qu’à votre canal direct réduit le risque.</li>
<li><strong>Vérifiez régulièrement les correspondances des canaux.</strong> Quand vous ajoutez un type de chambre, confirmez la correspondance sur chaque canal.</li></ol>
<h2>Et si cela arrive malgré tout ?</h2>
<p>Prévenez le client rapidement et honnêtement, proposez une alternative équivalente ou meilleure (un hôtel voisin, un surclassement) et prenez en charge les frais supplémentaires comme les transferts. Notez quel canal en est à l’origine et pourquoi.</p>
<h2>Comment cela fonctionne dans Hostlio Pro</h2>
<p>Le <a href="{U("channel")}">channel manager</a> de Hostlio Pro synchronise les disponibilités de manière bidirectionnelle et en temps réel sur plus de 100 canaux via Channex. Les réservations apparaissent sur un seul planning des chambres, colorées par canal.</p>''',
  faq=[("Que signifie surréservation (overbooking) ?","La surréservation, c’est lorsqu’un hôtel accepte plus de réservations qu’il ne peut en accueillir pour la même chambre et les mêmes dates ; on parle aussi de double réservation."),
       ("Un channel manager empêche-t-il totalement la surréservation ?","Une synchronisation bidirectionnelle en temps réel élimine l’essentiel du risque ; les réservations directes non saisies et les erreurs de correspondance des chambres peuvent toutefois encore poser problème.")]),
 dict(key="post-autoreply", date="2026-09-21", title="Comment répondre automatiquement aux messages Booking.com",
  desc="Trois façons d’automatiser les messages des clients Booking.com : modèles, messages programmés et assistant IA. Quand chacune fonctionne, et où elle atteint ses limites.",
  content=f'''<div class="answer"><p><strong>Réponse courte :</strong> il existe trois façons d’automatiser les messages Booking.com : les modèles de messages enregistrés dans l’extranet, les messages programmés selon l’étape de la réservation, et un assistant IA qui comprend la question du client et répond à partir des informations de votre hôtel. Les modèles conviennent aux informations standard ; un assistant IA convient aux questions qui diffèrent d’un client à l’autre.</p></div>
<h2>1. Modèles de messages</h2>
<p>Enregistrez les réponses fréquentes, comme l’heure du check-in, l’itinéraire et le parking, sous forme de modèles et envoyez-les en un clic. C’est simple, mais quelqu’un doit encore lire le message et choisir le bon modèle.</p>
<h2>2. Messages programmés</h2>
<p>Des messages envoyés automatiquement après la réservation, la veille de l’arrivée ou le jour du départ. Les clients sont informés avant même de poser la question, mais ces messages ne répondent pas aux questions que les clients écrivent ensuite.</p>
<h2>3. Un assistant IA</h2>
<p>Il lit le message du client et rédige une réponse à partir de votre base de connaissances, dans la langue du client. C’est la méthode la plus efficace pour les questions posées la nuit, en plusieurs langues ou hors modèle, et il doit transmettre les décisions (remises, réclamations) à votre équipe.</p>
<div class="table-wrap"><table><thead><tr><th>Méthode</th><th>Idéale pour</th><th>Limite</th></tr></thead><tbody>
<tr><td>Modèles</td><td>Informations standard</td><td>Quelqu’un doit lire et choisir</td></tr>
<tr><td>Messages programmés</td><td>Informations avant l’arrivée</td><td>Ne répond pas aux questions reçues</td></tr>
<tr><td>Assistant IA</td><td>Questions à toute heure, dans toutes les langues</td><td>Nécessite une bonne base de connaissances</td></tr></tbody></table></div>
<h2>Pourquoi le temps de réponse compte</h2>
<p>Une réponse rapide avant la réservation facilite la décision du client ; une réponse rapide pendant le séjour influence sa satisfaction et ses avis.</p>
<h2>Comment cela fonctionne dans Hostlio Pro</h2>
<p>Avec Pro et Growth, les messages des OTA, y compris ceux de Booking.com, arrivent dans la boîte de réception de <a href="{U("ai")}">Lio, l’assistant IA</a>. Lio répond avec les informations de votre hôtel dans la langue du client et vous laisse ce dont il n’est pas sûr.</p>''',
  faq=[("Peut-on répondre automatiquement aux messages Booking.com ?","Oui. Les modèles de l’extranet et les messages programmés sont des outils propres à Booking.com ; des réponses automatiques adaptées à chaque question nécessitent un assistant IA qui lit les messages."),
       ("Un assistant IA peut-il donner de mauvaises informations ?","Le risque est faible lorsque l’assistant n’utilise que les informations fournies par l’hôtel et transmet à l’équipe les questions dont il n’est pas sûr.")]),
    ]

# ------------------------------------------------------------------ legal_v5
LEGAL_T = {
 "privacy": ("Politique de confidentialité | Hostlio Pro", "Politique de confidentialité de Hostlio Pro : données collectées, utilisation et partage, sécurité, conservation des données, cookies et vos droits au titre du RGPD.", "Politique de confidentialité"),
 "terms":   ("Conditions d’utilisation | Hostlio Pro", "Conditions d’utilisation de Hostlio Pro : description du service, abonnements et paiements, résiliation et remboursements, contenu généré par l’IA, intégrations OTA et responsabilité.", "Conditions d’utilisation"),
}
LEGAL_NOTE = 'Dernière mise à jour : <time datetime="{iso}">{date}</time>, {addr}. Ce texte est une traduction de l’original anglais ; en cas de divergence, la <a href="{en_url}">version anglaise</a> prévaut.'

def privacy_body(U, EMAIL, ADDR, ul):
    return f'''<p>La présente Politique de confidentialité décrit la manière dont Hostlio Pro, exploité par Loti Members LLC (« nous », « notre » ou « nos »), collecte, utilise et partage des informations lorsque vous utilisez notre plateforme de gestion hôtelière sur hostliopro.com.</p>
<h2>1. Informations que nous collectons</h2><p>Nous collectons les informations que vous nous fournissez directement, notamment :</p>
{ul(["Informations de compte : nom, adresse e-mail, numéro de téléphone, nom de l’hôtel, nombre de chambres","Informations de paiement : traitées de manière sécurisée par Stripe (nous ne conservons pas les données de carte)","Données de l’hôtel : réservations, communications avec les clients, configuration des chambres","Données d’utilisation : la manière dont vous interagissez avec notre plateforme"])}
<h2>2. Utilisation de vos informations</h2><p>Nous utilisons les informations collectées pour :</p>
{ul(["Fournir, maintenir et améliorer nos services","Traiter les paiements et envoyer les notifications de facturation","Envoyer des e-mails transactionnels et des informations sur les évolutions du produit","Répondre à vos commentaires et à vos questions","Surveiller et analyser les tendances d’utilisation afin d’améliorer l’expérience utilisateur","Respecter nos obligations légales"])}
<h2>3. Partage des informations</h2><p>Nous ne vendons, n’échangeons ni ne louons vos informations personnelles à des tiers. Nous pouvons partager vos informations avec :</p>
{ul(["<strong>Prestataires de services :</strong> Supabase (base de données), Make.com (automatisation), Stripe (paiements), Vercel (hébergement), Anthropic (traitement par IA)","<strong>Channel managers :</strong> l’API Channex pour la synchronisation avec les OTA (Booking.com, Airbnb, etc.)","<strong>Obligations légales :</strong> lorsque la loi l’exige ou pour protéger nos droits"])}
<h2>4. Sécurité des données</h2><p>Nous mettons en œuvre des mesures techniques et organisationnelles appropriées pour protéger vos informations personnelles contre tout accès, toute modification, toute divulgation ou toute destruction non autorisés. Notre infrastructure est conforme à la norme SOC 2 par l’intermédiaire de Supabase, et les paiements sont conformes à la norme PCI DSS par l’intermédiaire de Stripe.</p>
<h2>5. Conservation des données</h2><p>Nous conservons vos informations personnelles aussi longtemps que votre compte est actif ou que cela est nécessaire à la fourniture des services. Vous pouvez demander la suppression de vos données à tout moment en nous contactant à l’adresse {EMAIL}.</p>
<h2>6. Droits au titre du RGPD</h2><p>Si vous vous trouvez dans l’Espace économique européen, vous disposez d’un droit d’accès, de rectification et d’effacement de vos données personnelles. Vous disposez également d’un droit à la portabilité des données et d’un droit d’opposition au traitement. Pour exercer ces droits, contactez-nous à l’adresse {EMAIL}.</p>
<h2>7. WhatsApp et messagerie</h2><p>Notre plateforme s’intègre à l’API WhatsApp Business afin de faciliter la communication avec les clients. Le contenu des messages est traité pour générer des réponses par IA et n’est pas utilisé à des fins marketing. Les numéros de téléphone des clients sont conservés uniquement à des fins de communication.</p>
<h2>8. Cookies</h2><p>Nous utilisons des cookies essentiels pour maintenir votre session et vos préférences. Nous n’utilisons pas de cookies de suivi ni de cookies publicitaires. Vous pouvez gérer les cookies dans les paramètres de votre navigateur.</p>
<h2>9. Liens vers des sites tiers</h2><p>Notre plateforme peut contenir des liens vers des sites web de tiers. Nous ne sommes pas responsables des pratiques de ces sites en matière de confidentialité et vous invitons à consulter leurs politiques de confidentialité.</p>
<h2>10. Modifications de la présente politique</h2><p>Nous pouvons mettre à jour la présente Politique de confidentialité de temps à autre. Nous vous informerons de toute modification en publiant la nouvelle politique sur cette page et en actualisant la date de « Dernière mise à jour ».</p>
<h2>11. Nous contacter</h2><p>Pour toute question concernant la présente Politique de confidentialité, veuillez nous contacter :</p>
{ul([f'E-mail : <a href="mailto:{EMAIL}">{EMAIL}</a>', f"Adresse : {ADDR}"])}
<p>Pour supprimer votre compte, consultez la page <a href="{U("delacc")}">Supprimer votre compte</a>.</p>'''

def terms_body(U, EMAIL, ADDR, ul):
    return f'''<p>Les présentes Conditions d’utilisation (les « Conditions ») régissent votre utilisation de Hostlio Pro, exploité par Loti Members LLC (la « Société », « nous », « notre » ou « nos »). En accédant à notre service ou en l’utilisant, vous acceptez d’être lié par les présentes Conditions.</p>
<h2>1. Description du service</h2><p>Hostlio Pro est une plateforme de gestion hôtelière dans le cloud qui fournit une communication avec les clients assistée par IA, la gestion des canaux, un calendrier de planning des chambres et des outils de gestion hôtelière associés. Le service est proposé sur abonnement sur hostliopro.com.</p>
<h2>2. Création de compte</h2><p>Pour utiliser Hostlio Pro, vous devez créer un compte et fournir des informations exactes et complètes. Vous êtes responsable de la confidentialité de vos identifiants de compte et de toutes les activités effectuées sous votre compte.</p>
<h2>3. Abonnement et paiements</h2>
{ul(["Les abonnements sont facturés d’avance, mensuellement ou annuellement","Tous les paiements sont traités de manière sécurisée par Stripe","Essai gratuit de 7 jours disponible : un moyen de paiement est demandé à l’inscription, mais aucun prélèvement n’est effectué avant la fin de l’essai","À l’issue de l’essai, vous serez facturé selon la formule choisie",f'Les prix sont exprimés en USD. Les formules et tarifs en vigueur figurent sur notre <a href="{U("pricing")}">page des tarifs</a>',"Les formules annuelles bénéficient d’une réduction de 20 %"])}
<h2>4. Résiliation et remboursements</h2><p>Vous pouvez résilier votre abonnement à tout moment. La résiliation prend effet à la fin de la période de facturation en cours. Nous n’accordons pas de remboursement pour les périodes de facturation partielles. Pour résilier, contactez-nous à l’adresse {EMAIL}.</p>
<h2>5. Utilisation acceptable</h2><p>Vous vous engagez à ne pas :</p>
{ul(["Utiliser le service à des fins illicites","Enfreindre les conditions des plateformes OTA (Booking.com, Airbnb, etc.) par l’intermédiaire de nos intégrations","Tenter d’obtenir un accès non autorisé à nos systèmes","Envoyer des spams ou des messages non sollicités aux clients","Revendre ou concéder en sous-licence le service sans autorisation écrite"])}
<h2>6. Contenu généré par l’IA</h2><p>Hostlio Pro utilise l’intelligence artificielle pour générer des réponses aux messages des clients. Vous reconnaissez que le contenu généré par l’IA peut occasionnellement comporter des erreurs. Il vous appartient de vérifier et de gérer les réponses de l’IA envoyées au nom de votre établissement. Nous déclinons toute responsabilité quant aux inexactitudes des communications générées par l’IA.</p>
<h2>7. Intégrations des canaux OTA</h2><p>Notre plateforme s’intègre à des canaux OTA tiers (Booking.com, Airbnb, Expedia, etc.) via l’API Channex. Il vous appartient de respecter les conditions d’utilisation de chaque plateforme. Nous ne sommes pas responsables des modifications des API ou des politiques des OTA susceptibles d’affecter le fonctionnement du service.</p>
<h2>8. Données et confidentialité</h2><p>Votre utilisation de Hostlio Pro est également régie par notre <a href="{U("privacy")}">Politique de confidentialité</a>, qui est intégrée par renvoi aux présentes Conditions. Vous restez propriétaire de vos données. Nous traitons vos données uniquement pour fournir le service.</p>
<h2>9. Disponibilité du service</h2><p>Nous visons une disponibilité de 99,9 % mais ne garantissons pas un service ininterrompu. Nous pouvons effectuer des opérations de maintenance programmées avec un préavis. Nous ne sommes pas responsables des pertes résultant d’interruptions du service.</p>
<h2>10. Propriété intellectuelle</h2><p>Hostlio Pro ainsi que l’ensemble des logiciels, designs et contenus associés sont la propriété de Loti Members LLC. Vous ne pouvez copier, modifier ou distribuer aucune partie de notre service sans autorisation écrite.</p>
<h2>11. Limitation de responsabilité</h2><p>Dans toute la mesure permise par la loi, Loti Members LLC ne saurait être tenue responsable des dommages indirects, accessoires, spéciaux, consécutifs ou punitifs, y compris la perte de bénéfices ou de données, résultant de votre utilisation du service.</p>
<h2>12. Droit applicable</h2><p>Les présentes Conditions sont régies par le droit de l’État de Californie (États-Unis). Tout litige sera tranché par les tribunaux du comté de Sacramento, en Californie.</p>
<h2>13. Modifications des Conditions</h2><p>Nous pouvons mettre à jour les présentes Conditions de temps à autre. Nous vous informerons des modifications importantes par e-mail ou via la plateforme. La poursuite de l’utilisation du service après ces modifications vaut acceptation des nouvelles Conditions.</p>
<h2>14. Contact</h2><p>Pour toute question concernant les présentes Conditions, contactez-nous :</p>
{ul([f'E-mail : <a href="mailto:{EMAIL}">{EMAIL}</a>', f"Adresse : {ADDR}"])}'''
