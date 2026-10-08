from build import store_badges, btn, icon, logo, url, room_rack, channel_strip, faq_block, SIGNUP_URL, EMAIL, UPDATED, CHECK, software_schema, SITE, PLANS
import ozellik_ekleri as FX
import derin_sayfalar as DS
L = "fr"
def U(k): return url(k, L)

MOIS = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]
def D(iso):
    y, m, d = iso[:10].split("-")
    d = int(d)
    return ("1er" if d == 1 else str(d)) + " " + MOIS[int(m)-1] + " " + y

PLAN_TXT = {
 "starter": ("Pour les chambres d'hôtes et les petits hôtels boutique", ["1 établissement, jusqu'à 10 chambres, 3 utilisateurs","⟦quota:starter⟧ messages IA / mois","Synchronisation des réservations OTA (100+ canaux)","Messagerie IA sur WhatsApp","Suggestions de Lio chaque matin","Planning des chambres (calendrier des réservations)","Attestation d'hébergement pour visa (PDF)","Application iOS et Android"]),
 "pro":     ("Pour les hôtels indépendants en croissance", ["1 établissement, jusqu'à 50 chambres, 8 utilisateurs","⟦quota:pro⟧ messages IA / mois","Tout le forfait Starter","WhatsApp + messagerie des OTA (Booking.com, Airbnb, Expedia)","Lio prend les demandes de réservation sur WhatsApp (avec votre accord)","Analyses IA des avis et des messages","Check-in en ligne avec signature électronique","Vente de transferts, d'excursions et d'extras"]),
 "growth":  ("Pour les équipes qui gèrent deux établissements", ["Jusqu'à 2 établissements, 150 chambres au total, 20 utilisateurs","⟦quota:growth⟧ messages IA / mois","Tout le forfait Pro","Synthèse IA hebdomadaire","Synchronisation des canaux prioritaire","Support prioritaire (jour ouvré suivant)","Appel de prise en main personnalisé","Options marque blanche"]),
}

def plans_html():
    out = []
    for p in PLANS:
        for_, feats = PLAN_TXT[p["id"]]
        pop = p["id"] == "pro"
        lis = "".join(f"<li>{CHECK}<span>{f}</span></li>" for f in feats)
        out.append(f'''<article class="plan{" pop" if pop else ""}" aria-labelledby="plan-{p["id"]}">
{'<span class="tag">Le plus populaire</span>' if pop else ""}
<h3 id="plan-{p["id"]}">{p["name"]}</h3><p class="for">{for_}</p>
<div class="price num"><b data-price="{p["id"]}">⟦price:{p["id"]}⟧</b><span class="muted">/ mois</span></div>
<p class="small muted num" style="margin:0" data-eb>Prix de lancement (normalement <s data-regular="{p["id"]}">⟦regular:{p["id"]}⟧</s>)</p>
<ul>{lis}</ul>
{btn("Commencer avec "+p["name"], SIGNUP_URL+"?plan="+p["id"], "primary" if pop else "ghost")}
</article>''')
    return '<div class="plans">' + "".join(out) + "</div>"

FAQ_CORE = [
 ("Qu'est-ce que Hostlio Pro ?", "Hostlio Pro est un logiciel de gestion hôtelière (PMS) propulsé par l'IA, conçu pour les hôtels indépendants, les hôtels boutique et les chambres d'hôtes. Il réunit sur une seule plateforme Lio, un assistant IA qui répond aux messages des clients 24 h/24 et 7 j/7 dans plus de 30 langues, un channel manager connecté à plus de 100 OTA, un calendrier de réservations en glisser-déposer et le check-in en ligne."),
 ("Combien coûte Hostlio Pro ?", "Il existe trois forfaits : Starter à ⟦price:starter⟧/mois, Pro à ⟦price:pro⟧/mois et Growth à ⟦price:growth⟧/mois. Ces prix incluent une remise de lancement de ⟦eb_pct⟧ réservée aux 50 premiers clients, garantie tant que vous restez abonné. Les prix normaux sont de ⟦regular:starter⟧, ⟦regular:pro⟧ et ⟦regular:growth⟧."),
 ("Y a-t-il un essai gratuit ?", "Oui. Chaque forfait comprend un essai gratuit de 7 jours. Une carte bancaire est demandée à l'inscription, mais aucun prélèvement n'a lieu avant la fin de l'essai, et vous pouvez résilier à tout moment avant. Aucun engagement de longue durée."),
 ("À quelles OTA Hostlio Pro est-il connecté ?", "Via Channex, Hostlio Pro se connecte à plus de 100 canaux, dont Booking.com, Airbnb, Expedia, Agoda, Trip.com, Hotels.com, Hotelbeds, Hostelworld et Google Hotels. Disponibilités, tarifs et réservations restent synchronisés sur l'ensemble de ces canaux."),
 ("Dans quelles langues Lio répond-il ?", "Lio répond dans plus de 30 langues, dont l'anglais, le turc, l'arabe, le russe, l'allemand, le japonais et le chinois. Il répond dans la langue du client, et vous voyez une traduction dans votre tableau de bord."),
]

def home():
    import home_v3
    return home_v3.home(L, plans_html, FAQ_CORE)

def ai():
    body = f'''
<section class="page-hero"><div class="wrap split">
<div><h1>Lio, l'assistant IA de messagerie client pour hôtels</h1>
<p class="lead">Lio est un assistant IA formé avec les informations de votre hôtel. Il répond aux messages des clients sur WhatsApp et dans les messageries des OTA (Booking.com, Airbnb, Expedia), dans plus de 30 langues, à toute heure.</p>
<div class="cta-row">{btn("Essayez Lio gratuitement pendant 7 jours", SIGNUP_URL)}</div></div>
<div class="panel typing"><p class="panel-title">WhatsApp, 02:47</p>
<div class="msg in" style="background:var(--bg)" lang="de">Hallo! Unser Flug landet um 1 Uhr. Können Sie uns abholen, und ist ein später Check-in möglich?</div>
<div class="msg out" lang="de">Natürlich! Unser Flughafentransfer kostet 35 € für bis zu 3 Gäste. Soll ich ihn für Ihre Ankunft um 1 Uhr buchen? Später Check-in ist kein Problem.<small lang="fr">Lio, allemand</small></div>
<p class="small muted" style="margin:10px 0 0">Demande de transfert créée et transmise à votre équipe.</p></div>
</div></section>

<section class="white rule"><div class="wrap">
<div class="answer"><p><strong>Qu'est-ce qu'un assistant IA de messagerie client pour hôtels ?</strong> Un logiciel qui répond automatiquement aux questions que les clients posent avant et après leur réservation, à partir des informations propres à l'hôtel. Lio transmet à votre équipe les messages auxquels il ne peut pas répondre ou qui demandent une décision humaine (demandes de remise, réclamations, demandes particulières).</p></div>
<h2 style="margin-top:64px">Ce que fait Lio</h2><div class="rows">
<div class="row"><h3>Une seule boîte de réception</h3><div><p>Les messages WhatsApp et ceux des OTA (Booking.com, Airbnb, Expedia) arrivent sur un seul écran. Lio associe automatiquement chaque client à sa réservation.</p></div></div>
<div class="row"><h3>Plus de 30 langues, traduction automatique</h3><div><p>Le client écrit en japonais et Lio répond en japonais ; vous voyez la traduction de la réponse de Lio dans votre langue. Les réponses que vous rédigez vous-même partent telles quelles, sans traduction automatique.</p></div></div>
<div class="row"><h3>Il connaît votre hôtel</h3><div><p>Horaires d'arrivée et de départ, parking, animaux acceptés, horaires du petit-déjeuner, transports et équipements des chambres. Saisissez-les une fois, et Lio les utilise de façon cohérente dans chaque réponse.</p></div></div>
<div class="row"><h3>Un assistant qui vend</h3><div><p>Lio ne se contente pas de répondre : il propose au bon moment transferts aéroport, visites de la ville et prestations supplémentaires, puis transmet la demande à votre équipe.</p></div></div>
<div class="row"><h3>Il prend les demandes de réservation</h3><div><p>Avec les forfaits Pro et Growth, quand un client demande une chambre sur WhatsApp, Lio recueille les dates, le nombre de personnes et la chambre souhaitée, puis annonce un prix calculé à partir de vos tarifs et disponibilités. La demande vous est transmise et devient une réservation une fois que vous l'avez validée.</p></div></div>
<div class="row"><h3>Des suggestions chaque matin</h3><div><p>Chaque matin, les Suggestions de Lio portent sur les prix, l'exploitation (chambres à nettoyer, demandes en attente), les réglages manquants et les opportunités de revenus. Rien ne change sans votre accord, et les suggestions de prix restent dans les limites que vous avez fixées. Inclus dans tous les forfaits.</p></div></div>
<div class="row"><h3>Ce que disent vos clients</h3><div><p>Avec Pro et Growth, Lio résume les sujets de plainte et de satisfaction qui reviennent dans les avis et les messages de vos clients. Une synthèse IA hebdomadaire est incluse dans Growth et proposée en option avec Pro.</p></div></div>
<div class="row"><h3>Vous gardez la main</h3><div><p>Les premiers jours, vous pouvez valider les réponses de Lio avant leur envoi. Vous décidez quels sujets Lio traite seul et lesquels il vous transmet.</p></div></div>
</div></div></section>

<section><div class="wrap">
<div class="section-head"><h2>Quota de messages IA par forfait</h2><p>Un message correspond à une réponse envoyée par Lio à un client.</p></div>
<div class="table-wrap"><table><thead><tr><th>Forfait</th><th class="c">Messages IA / mois</th><th>Canaux de messagerie</th></tr></thead><tbody>
<tr><th>Starter</th><td class="c num">⟦quota:starter⟧</td><td>WhatsApp</td></tr>
<tr><th>Pro</th><td class="c num">⟦quota:pro⟧</td><td>WhatsApp + messageries OTA (Booking.com, Airbnb, Expedia)</td></tr>
<tr><th>Growth</th><td class="c num">⟦quota:growth⟧</td><td>WhatsApp + messageries OTA (Booking.com, Airbnb, Expedia)</td></tr>
</tbody></table></div>
</div></section>
'''
    faq = [
     ("Et si Lio donne une information erronée ?", "Lio utilise uniquement les informations de l'hôtel et les données de réservation que vous fournissez. Lorsqu'il n'est pas sûr, il vous transmet le message au lieu de deviner. Vous pouvez aussi valider chaque réponse avant son envoi."),
     ("Répond-il aussi aux messages Booking.com et Airbnb ?", "Oui. Avec les forfaits Pro et Growth, les messages OTA arrivent dans la boîte de réception de Lio et reçoivent une réponse de la même manière."),
     ("Lio peut-il prendre des réservations ?", "Oui, avec les forfaits Pro et Growth, et toujours avec votre accord. Quand un client écrit sur WhatsApp, Lio lui demande les dates, le nombre de personnes et la chambre souhaitée, annonce un prix calculé à partir de vos tarifs et disponibilités, puis vous transmet la demande. Elle ne devient une réservation qu'après votre validation : Lio ne confirme jamais une réservation seul. Les demandes de services comme les transferts ou les excursions suivent le même principe."),
     ("Que se passe-t-il quand le quota de messages est épuisé ?", "Pas de surprise : le compteur d'utilisation du tableau de bord passe à l'orange à 80 % et, à 100 %, le titulaire du compte reçoit un e-mail et une notification push. Lio continue de répondre un peu au-delà de la limite ; les réponses automatiques sont suspendues vers 110 %. Les messages continuent d'arriver et s'affichent dans votre tableau de bord, et votre équipe peut y répondre à la main. Vous pouvez passer à un forfait supérieur pour augmenter votre quota."),
     FAQ_CORE[4],
    ]
    return {"key":"ai","title":"Messagerie client IA pour hôtel en 30+ langues | Hostlio Pro",
            "desc":"Lio, l'assistant IA de Hostlio Pro, répond aux clients de votre hôtel sur WhatsApp et sur les OTA 24 h/24 en 30+ langues et prend les demandes de réservation.",
            "trail":[("Assistant IA Lio", U("ai"))],"body":body,"faq":faq}

def channel():
    body = f'''
<section class="page-hero"><div class="wrap split">
<div><h1>Un channel manager pour plus de 100 OTA</h1>
<p class="lead">Gérez disponibilités, tarifs et réservations sur Booking.com, Airbnb, Expedia, Agoda et plus de 100 autres canaux depuis un seul calendrier. Hostlio Pro synchronise tout en temps réel et dans les deux sens.</p>
<div class="cta-row">{btn("Commencer l'essai gratuit de 7 jours", SIGNUP_URL)}</div></div>
<div class="panel"><p class="panel-title">Canaux connectés</p><div class="chan-list">
<div><span>Booking.com</span><span class="pill">Synchronisé</span></div>
<div><span>Airbnb</span><span class="pill">Synchronisé</span></div>
<div><span>Expedia</span><span class="pill">Synchronisé</span></div>
<div><span>Agoda</span><span class="pill">Synchronisé</span></div>
<div><span>Google Hotels</span><span class="pill">Synchronisé</span></div>
</div></div>
</div></section>
<section class="white rule"><div class="wrap">
<div class="answer"><p><strong>Qu'est-ce qu'un channel manager ?</strong> Un logiciel qui maintient à jour les disponibilités et les tarifs d'un hôtel lorsqu'il vend ses chambres sur plusieurs canaux en ligne à la fois. Dès qu'une chambre est vendue sur un canal, elle est immédiatement fermée sur tous les autres, ce qui évite les doubles réservations (surbooking).</p></div>
<h2 style="margin-top:64px">Ce que fait le channel manager</h2><div class="rows">
<div class="row"><h3>Synchronisation bidirectionnelle</h3><div><p>Nouvelles réservations, modifications et annulations s'affichent automatiquement sur le planning des chambres, et les changements faits dans le calendrier sont envoyés à tous les canaux.</p></div></div>
<div class="row"><h3>Tarifs et restrictions</h3><div><p>Envoyez tarifs, durées minimales de séjour et arrêts de vente par type de chambre à tous les canaux depuis un seul écran.</p></div></div>
<div class="row"><h3>Planning des chambres en couleurs</h3><div><p>Voyez d'un coup d'œil de quel canal provient chaque réservation. Réattribuez les chambres par glisser-déposer.</p></div></div>
<div class="row"><h3>Relié à la messagerie</h3><div><p>Les messages des clients ayant réservé via une OTA arrivent dans la boîte de réception de Lio, avec le client, la chambre et les dates à côté de chaque conversation.</p></div></div>
{FX.channel_rows(L)}
</div></div></section>
<section><div class="wrap"><div class="section-head"><h2>Principaux canaux pris en charge</h2><p>La liste suit notre réseau de connexions certifiées. Un canal manque ? Contactez-nous.</p></div>
<div class="table-wrap"><table><thead><tr><th>Canal</th><th>Type</th></tr></thead><tbody>
<tr><th>Booking.com</th><td>OTA</td></tr><tr><th>Airbnb</th><td>Location courte durée</td></tr><tr><th>Expedia, Hotels.com</th><td>OTA</td></tr>
<tr><th>Agoda, Trip.com</th><td>OTA (orientée Asie)</td></tr><tr><th>Hotelbeds</th><td>Grossiste (bedbank)</td></tr><tr><th>Hostelworld</th><td>Plateforme d'auberges de jeunesse</td></tr><tr><th>Google Hotels</th><td>Métamoteur</td></tr>
</tbody></table></div></div></section>
{DS.more(L,"channel")}
'''
    faq = [FAQ_CORE[3],
     ("Le channel manager est-il inclus dans tous les forfaits ?", "Oui. Starter, Pro et Growth incluent tous la synchronisation avec plus de 100 OTA. Growth y ajoute la synchronisation prioritaire."),
     FX.FX[L]["ch_switch"],
    ]
    return {"key":"channel","title":"Channel manager hôtelier pour 100+ OTA | Hostlio Pro",
            "desc":"Le channel manager Hostlio Pro synchronise en temps réel disponibilités et tarifs sur 100+ OTA (Booking.com, Airbnb, Expedia, Agoda) sans surbooking.",
            "trail":[("Channel manager", U("channel"))],"body":body,"faq":faq+DS.faq(L,"channel")}

def checkin():
    body = f'''
<section class="page-hero"><div class="wrap split">
<div><h1>Check&#8209;in en ligne avec signature électronique</h1>
<p class="lead">Avant leur arrivée, les clients scannent leur pièce d'identité avec leur téléphone, ajoutent leurs accompagnants et signent. Aucune image du document n'est conservée. La remise des clés ne prend que quelques minutes.</p>
<div class="cta-row">{btn("Essayez Pro gratuitement pendant 7 jours", SIGNUP_URL+"?plan=pro")}</div></div>
<div class="panel"><p class="panel-title">Check-in en ligne, chambre 202</p>
<div class="field"><span>Nom complet</span><div>Keiko Sato</div></div>
<div class="field"><span>Nationalité</span><div>Japon</div></div>
<div class="field"><span>Document</span><div>Passeport scanné, aucune image conservée</div></div>
<div class="field"><span>Accompagnants</span><div>1 accompagnant ajouté</div></div>
<div class="field"><span>Signature</span><div class="sig">Signature électronique reçue</div></div>
</div>
</div></section>
<section class="white rule"><div class="wrap">
<div class="answer"><p><strong>Comment fonctionne le check-in en ligne ?</strong> Hostlio Pro envoie à la personne qui a réservé un lien sécurisé, personnel et à durée limitée. Depuis ce lien, le client scanne avec l'appareil photo de son téléphone la bande de lecture automatique (MRZ) de son passeport ou de sa carte d'identité. La lecture se fait dans son propre navigateur et les champs se remplissent automatiquement. Il ajoute ensuite d'éventuels accompagnants, puis signe le formulaire électroniquement. Seules les données extraites et la signature sont enregistrées dans la réservation ; aucune image du document n'est envoyée ni conservée.</p></div>
<h2 style="margin-top:64px">Fonctionnalités du check-in en ligne</h2><div class="rows">
<div class="row"><h3>Lien sécurisé</h3><div><p>Un lien à jeton, propre à chaque réservation. Il n'ouvre que le formulaire de cette réservation.</p></div></div>
{FX.checkin_row(L)}
<div class="row"><h3>Scan du document sans conserver d'image</h3><div><p>La bande de lecture automatique du passeport ou de la carte d'identité est lue sur l'appareil du client. Seuls le nom, le numéro du document, la nationalité, la date de naissance et la date d'expiration sont enregistrés, jamais une photo du document. Les documents sans bande de lecture automatique sont saisis à la main.</p></div></div>
<div class="row"><h3>Accompagnants</h3><div><p>Toutes les personnes séjournant dans la chambre sont ajoutées dans un seul formulaire : plus personne n'a à saisir ses données à la réception.</p></div></div>
<div class="row"><h3>Signature électronique et consentement</h3><div><p>Les clients acceptent le règlement intérieur et le consentement au traitement des données en signant à l'écran. Les signatures sont supprimées automatiquement 30 jours après le départ.</p></div></div>
<div class="row"><h3>Confidentialité dès la conception</h3><div><p>Les données des clients peuvent être supprimées sur demande, et le texte de consentement fait partie du formulaire.</p></div></div>
<div class="row"><h3>Export pour les déclarations officielles</h3><div><p>Les données collectées peuvent être exportées dans un format utilisable pour les obligations locales d'enregistrement des clients.</p></div></div>
</div></div></section>
<section class="dark on-dark"><div class="wrap"><div class="section-head"><h2>Trois étapes pour le client</h2></div>
<ol class="steps"><li><h3>Ouvrir le lien</h3><p>Touchez le lien envoyé après la confirmation de la réservation.</p></li>
<li><h3>Scanner le document</h3><p>Scannez votre passeport ou votre carte d'identité avec votre téléphone : les champs se remplissent automatiquement et aucune image n'est conservée. Indiquez ensuite vos accompagnants.</p></li>
<li><h3>Signer</h3><p>Acceptez le règlement intérieur et signez à l'écran. À la réception, il ne reste qu'à récupérer la clé.</p></li></ol>
</div></section>
{DS.more(L,"checkin")}
'''
    faq = [("Quels forfaits incluent le check-in en ligne ?", "Le check-in en ligne avec signature électronique est inclus dans les forfaits Pro et Growth."),
           ("Le client doit-il télécharger une application ?", "Non. Le formulaire de check-in s'ouvre dans le navigateur ; aucune application n'est à télécharger."),
           ("Et si un client ne remplit pas le formulaire ?", "Enregistrez-le de la manière habituelle. Votre équipe peut aussi scanner le document à la réception depuis le panneau web, avec la caméra de l'ordinateur ou de la tablette ; la lecture se fait sur l'appareil et aucune image n'est conservée."),
           ("Les photos des pièces d'identité sont-elles conservées ?", "Non. La bande de lecture automatique (MRZ) du document est lue sur le téléphone du client, ou à la réception, sur l'appareil de l'hôtel, depuis le panneau web, et seules les données extraites et la signature sont enregistrées. Les passeports et cartes d'identité dotés d'une MRZ peuvent être scannés ; les autres documents sont saisis à la main.")]
    return {"key":"checkin","title":"Check-in en ligne avec signature électronique | Hostlio Pro",
            "desc":"Check-in en ligne : vos clients scannent leur pièce d'identité (aucune image conservée), ajoutent leurs accompagnants et signent depuis leur mobile.",
            "trail":[("Check-in en ligne", U("checkin"))],"body":body,"faq":faq+DS.faq(L,"checkin")}

def features():
    body = f'''
<section class="page-hero"><div class="wrap split"><div><h1>Toutes les fonctionnalités du logiciel hôtelier Hostlio Pro</h1>
<p class="lead">Les modules dont un hôtel indépendant a besoin au quotidien : communication client, distribution, réservations, check-in et revenus complémentaires.</p></div><div class="hero-img"><img src="/assets/img/gen-team-desk.webp" alt="" width="1080" height="1350"></div></div></section>
<section class="white rule"><div class="wrap"><h2 class="sr-only">Modules</h2><div class="rows">
<div class="row"><h3>Assistant IA Lio</h3><div><p>Réponses aux clients 24 h/24, 7 j/7, dans plus de 30 langues. Messages WhatsApp et OTA (Booking.com, Airbnb, Expedia) dans une seule boîte de réception.</p><a href="{U("ai")}">En savoir plus sur Lio</a></div></div>
<div class="row"><h3>Channel manager</h3><div><p>Synchronisation des disponibilités, tarifs et réservations avec plus de 100 OTA par connexions certifiées.</p><a href="{U("channel")}">Channel manager</a></div></div>
<div class="row"><h3>Planning des chambres</h3><div><p>Calendrier de réservations en glisser-déposer. Faites glisser une réservation pour changer de chambre, et repérez d'un coup d'œil chambres libres et conflits.</p></div></div>
<div class="row"><h3>Check-in en ligne</h3><div><p>Lien sécurisé, accompagnants, scan de la pièce d'identité (aucune image conservée) et signature électronique.</p><a href="{U("checkin")}">Check-in en ligne</a></div></div>
<div class="row"><h3>Documents pour le client</h3><div><p>À partir de la réservation, préparez l'attestation d'hébergement demandée pour un visa ou une invitation, ou un reçu de séjour avec dates, prix par nuit et total. Choisissez le français, l'anglais, le turc, l'espagnol, l'italien ou le portugais (la langue du client est proposée), puis imprimez ou enregistrez en PDF. La fiche d'enregistrement du client se télécharge aussi en PDF.</p></div></div>
<div class="row"><h3>Vente de transferts et d'excursions</h3><div><p>Lio propose transferts aéroport et excursions pendant la conversation et transmet la demande à votre équipe.</p></div></div>
<div class="row"><h3>Suggestions de Lio et analyses IA</h3><div><p>Chaque matin, Lio prépare des suggestions sur les prix, l'exploitation (chambres à nettoyer, demandes en attente), les réglages manquants et les opportunités de revenus. Rien ne change sans votre accord, et les suggestions de prix restent dans les limites que vous fixez. Avec Pro et Growth, les plaintes et compliments récurrents dans les avis et les messages sont aussi résumés.</p></div></div>
<div class="row"><h3>Application mobile</h3><div><p>Gérez réservations, messages et check-ins hors de l'hôtel avec l'application iOS et Android.</p>{store_badges("fr")}</div></div>
</div></div></section>
{FX.features_more(L)}
<section><div class="wrap"><div class="section-head"><h2>Fonctionnalités par forfait</h2></div>
<div class="table-wrap"><table><thead><tr><th>Fonctionnalité</th><th class="c">Starter</th><th class="c">Pro</th><th class="c">Growth</th></tr></thead><tbody>
<tr><th>Établissements</th><td class="c">1</td><td class="c">1</td><td class="c">2</td></tr>
<tr><th>Nombre de chambres max.</th><td class="c num">10</td><td class="c num">50</td><td class="c num">150</td></tr>
<tr><th>Utilisateurs (comptes du personnel)</th><td class="c num">3</td><td class="c num">8</td><td class="c num">20</td></tr>
<tr><th>Messages IA / mois</th><td class="c num">⟦quota:starter⟧</td><td class="c num">⟦quota:pro⟧</td><td class="c num">⟦quota:growth⟧</td></tr>
<tr><th>Synchronisation avec plus de 100 OTA</th><td class="c">Oui</td><td class="c">Oui</td><td class="c">Prioritaire</td></tr>
<tr><th>Messagerie IA sur WhatsApp</th><td class="c">Oui</td><td class="c">Oui</td><td class="c">Oui</td></tr>
<tr><th>Suggestions de Lio chaque matin (rien ne change sans votre accord)</th><td class="c">Oui</td><td class="c">Oui</td><td class="c">Oui</td></tr>
<tr><th>Demandes de réservation et de services via Lio sur WhatsApp</th><td class="c">Non</td><td class="c">Oui</td><td class="c">Oui</td></tr>
<tr><th>Analyses IA des avis et des messages clients</th><td class="c">Non</td><td class="c">Oui</td><td class="c">Oui</td></tr>
<tr><th>Synthèse IA hebdomadaire</th><td class="c">Non</td><td class="c">En option</td><td class="c">Oui</td></tr>
<tr><th>Messagerie des OTA (Booking.com, Airbnb, Expedia)</th><td class="c">Non</td><td class="c">Oui</td><td class="c">Oui</td></tr>
<tr><th>Planning des chambres</th><td class="c">Oui</td><td class="c">Oui</td><td class="c">Oui</td></tr>
<tr><th>Attestation d'hébergement pour visa (PDF)</th><td class="c">Oui</td><td class="c">Oui</td><td class="c">Oui</td></tr>
<tr><th>Check-in en ligne et signature électronique</th><td class="c">Non</td><td class="c">Oui</td><td class="c">Oui</td></tr>
<tr><th>Vente de transferts et d'excursions</th><td class="c">Non</td><td class="c">Oui</td><td class="c">Oui</td></tr>
<tr><th>Application mobile iOS et Android</th><td class="c">Oui</td><td class="c">Oui</td><td class="c">Oui</td></tr>
<tr><th>Support prioritaire et appel de prise en main</th><td class="c">Non</td><td class="c">Non</td><td class="c">Oui</td></tr>
<tr><th>Marque blanche</th><td class="c">Non</td><td class="c">Non</td><td class="c">Oui</td></tr>
{FX.table_rows(L)}
</tbody></table></div></div></section>
'''
    return {"key":"features","title":"Fonctions du logiciel de gestion hôtelière | Hostlio Pro",
            "desc":"Hostlio Pro inclut : assistant IA, channel manager 100+ OTA, planning des chambres, check-in en ligne, attestations pour visa et application mobile.",
            "trail":[("Fonctionnalités", U("features"))],"body":body,"faq":[FAQ_CORE[0], FAQ_CORE[3]]+FX.faq(L,"faq_import","faq_roles","faq_reports")}

def pricing():
    body = f'''
<section class="page-hero"><div class="wrap"><h1>Tarifs de Hostlio Pro</h1>
<p class="lead">Un abonnement mensuel fixe. Aucune commission sur les réservations, aucuns frais d'installation. Essayez n'importe quel forfait gratuitement pendant 7 jours.</p></div></section>
<section style="padding-top:0"><div class="wrap"><h2 class="sr-only">Forfaits</h2>
<span class="billing-note">⟦eb_pct⟧ de réduction pour les 50 premiers clients, garantie à vie</span>
{plans_html()}
<p class="small muted" style="margin-top:18px">Prix en dollars américains, hors taxes. Dernière mise à jour : <time datetime="{UPDATED}">{D(UPDATED)}</time>.</p>
</div></section>
<section class="white rule"><div class="wrap">
<div class="section-head"><h2>Quel forfait vous convient ?</h2></div>
<div class="rows">
<div class="row"><h3>Starter</h3><div><p>Chambres d'hôtes et hôtels boutique jusqu'à 10 chambres, qui envoient moins de ⟦quota:starter⟧ réponses par mois et veulent démarrer avec la synchronisation des canaux et les réponses IA.</p></div></div>
<div class="row"><h3>Pro</h3><div><p>Hôtels de 11 à 50 chambres qui veulent que Lio gère aussi les messages OTA, utiliser le check-in en ligne et vendre transferts et excursions.</p></div></div>
<div class="row"><h3>Growth</h3><div><p>Deux établissements ou jusqu'à 150 chambres, lorsque vous avez besoin d'un support prioritaire, d'une prise en main personnalisée et d'une utilisation en marque blanche.</p></div></div>
</div></div></section>
'''
    faq = [FAQ_CORE[1], FAQ_CORE[2],
      ("Prenez-vous une commission sur chaque réservation ?", "Non. Hostlio Pro est un abonnement mensuel fixe ; il ne prélève aucun pourcentage sur le montant des réservations."),
      ("Existe-t-il une facturation annuelle ?", "Oui. Les abonnements sont facturés mensuellement ou annuellement, à l'avance, et les forfaits annuels bénéficient d'une remise de 20 % (Conditions d'utilisation, section 3)."),
      ("Puis-je changer de forfait ?", "Oui. Passez à un forfait supérieur ou inférieur à tout moment. Le changement s'applique immédiatement et la différence de prix est calculée au prorata sur votre prochaine facture."),
      ("Combien de temps dure la remise de lancement ?", "Elle s'applique aux 50 premiers clients, et votre prix reste garanti tant que votre abonnement se poursuit.")]
    return {"key":"pricing","title":"Tarifs du logiciel hôtelier : dès ⟦price:starter⟧/mois | Hostlio Pro",
            "desc":"Tarifs Hostlio Pro : Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ par mois. Sans commission ni frais d'installation, essai gratuit 7 jours. Comparez les offres.",
            "trail":[("Tarifs", U("pricing"))],"body":body,"faq":faq,"schema":[software_schema(L, detailed=True)]}

FAQ_ALL = FAQ_CORE + [
 ("À quels types d'hôtels s'adresse Hostlio Pro ?", "Aux établissements indépendants de 1 à 150 chambres : hôtels boutique, hôtels urbains, chambres d'hôtes, résidences hôtelières et auberges de jeunesse."),
 ("Existe-t-il une application mobile ?", "Oui. Tous les forfaits, Starter compris, incluent l'application iOS et Android. Gérez réservations, messages et check-ins hors de l'hôtel."),
 ("Comment fonctionne le check-in en ligne ?", "Les clients reçoivent un lien sécurisé personnel, scannent leur pièce d'identité avec leur téléphone (aucune image n'est conservée) et envoient avant leur arrivée leurs accompagnants et leur signature électronique. Disponible avec Pro et Growth."),
 ("À quoi sert l'attestation d'hébergement pour visa ?", "Pour les clients qui ont besoin d'un visa, elle prépare en un clic une attestation d'hébergement à partir des données de réservation, à joindre à une demande de visa ou d'invitation. Vous pouvez l'enregistrer en PDF ou l'imprimer."),
 ("Mes données sont-elles sécurisées ?", "Les données transitent par des connexions chiffrées, et les données de chaque hôtel sont isolées de celles des autres établissements grâce à des règles d'accès au niveau des lignes. Les données des clients peuvent être supprimées sur demande."),
 ("Combien de temps prend la mise en place ?", "Votre compte est prêt en quelques minutes. La plupart des hôtels connectent leurs canaux le jour même : ajoutez types de chambres et chambres, autorisez la connexion dans l’extranet de chaque OTA et associez les chambres. Le forfait Growth inclut un appel de prise en main personnalisé."),
 ("Dans quelles langues le support est-il proposé ?", "Le support est assuré en anglais et en turc. Le tableau de bord, l'application mobile et le formulaire de check-in des clients sont disponibles en 6 langues : français, anglais, turc, espagnol, italien et portugais. Écrivez-nous à " + EMAIL + "."),
] + FX.faq(L,"faq_import","faq_roles","faq_reports","faq_owner")

def faq_page():
    body = f'''<section class="page-hero"><div class="wrap"><h1>Questions fréquentes</h1>
<p class="lead">Les questions les plus courantes sur les fonctionnalités, les tarifs et la mise en place de Hostlio Pro. Vous ne trouvez pas votre réponse ? <a href="{U("contact")}">Écrivez-nous</a>.</p></div></section>
<section style="padding-top:0"><div class="wrap">{faq_block(FAQ_ALL, L, heading=False, wrap=False)}</div></section>'''
    return {"key":"faq","title":"FAQ Hostlio Pro : questions fréquentes",
            "desc":"FAQ sur le logiciel de gestion hôtelière Hostlio Pro : tarifs, essai gratuit, intégrations OTA, assistant IA Lio, check-in en ligne et sécurité.",
            "trail":[("FAQ", U("faq"))],"body":body,"faq":FAQ_ALL,"faq_inline":True,"page_type":"FAQPage"}

def about():
    body = f'''<section class="page-hero"><div class="wrap split"><div><h1>Pourquoi nous avons créé Hostlio Pro</h1>
<p class="lead">Dans les petits hôtels, la réception, la vente et la communication avec les clients reposent souvent sur les épaules d'une seule personne. Hostlio Pro existe pour que cette personne ne soit plus submergée par les messages la nuit et par les extranets des canaux le jour.</p></div><div class="hero-img"><img src="/assets/img/gen-shutters.webp" alt="" width="1080" height="1350"></div></div></section>
<section class="white rule"><div class="wrap split">
<div class="prose"><h2>Ce que nous faisons</h2>
<p>Hostlio Pro est un logiciel de gestion hôtelière propulsé par l'IA pour les hôtels indépendants. Nous confions la communication client à notre assistant IA Lio, réunissons la distribution sur les OTA dans un seul calendrier et transférons le check-in sur le téléphone du client.</p>
<h2>Notre façon de travailler</h2>
<ul><li>Nous publions nos prix ouvertement et ne prenons aucune commission.</li><li>Nous partons du travail quotidien réel des hôteliers.</li><li>Pas de contrats longs : nos clients restent parce qu'ils sont satisfaits.</li></ul></div>
<div class="panel"><p class="panel-title">Informations sur l'entreprise</p><dl class="list-kv">
<dt>Produit</dt><dd>Hostlio Pro (Hostlio)</dd><dt>Société</dt><dd>Loti Members LLC</dd>
<dt>Adresse</dt><dd>2108 N ST STE N, Sacramento, CA 95816, USA</dd><dt>E-mail</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
<dt>Clients</dt><dd>Hôtels indépendants dans plus de 20 pays</dd></dl></div>
</div></section>'''
    return {"key":"about","title":"À propos de Hostlio Pro","desc":"Hostlio Pro crée un logiciel de gestion hôtelière à base d'IA pour les hôtels indépendants. Exploité par Loti Members LLC et utilisé dans plus de 20 pays.",
            "trail":[("À propos", U("about"))],"body":body,"page_type":"AboutPage"}

def contact():
    from build import FORM_ENDPOINT
    act = f' action="{FORM_ENDPOINT}" method="post"' if FORM_ENDPOINT else ""
    body = f'''<section class="page-hero"><div class="wrap split" style="align-items:start">
<div><h1>Demandez une démo ou contactez-nous</h1>
<p class="lead">Présentez-nous brièvement votre hôtel et les canaux que vous utilisez : nous vous montrerons Hostlio Pro avec vos propres chambres lors d'un appel de 30 minutes.</p>
<p>Écrivez-nous directement : <a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
<form class="contact" data-contact-form data-mail="{EMAIL}" data-subject="Demande de démo" data-sent="Votre messagerie s'est ouverte. Cliquez sur Envoyer pour que votre demande nous parvienne."{act}>
<label>Nom complet<input name="name" autocomplete="name" required></label>
<label>E-mail<input type="email" name="email" autocomplete="email" required></label>
<label>Nom de l'hôtel<input name="hotel" autocomplete="organization" required></label>
<label>Nombre de chambres<select name="rooms"><option>1–10</option><option>11–50</option><option>51–150</option><option>150+</option></select></label>
<label>Pays / ville<input name="country" autocomplete="country-name"></label>
<label>Message <span class="hint">Canaux utilisés, logiciel actuel</span><textarea name="message" rows="4"></textarea></label>
<button class="btn btn-primary" type="submit">Envoyer la demande de démo</button>
<p class="form-status" role="status" aria-live="polite"></p>
</form></div></section>'''
    return {"key":"contact","title":"Contact et demande de démo | Hostlio Pro","desc":"Contactez l'équipe Hostlio Pro ou réservez une démo gratuite de 30 minutes adaptée à votre hôtel. Support en anglais et turc, e-mail : " + EMAIL,
            "trail":[("Contact", U("contact"))],"body":body,"page_type":"ContactPage","no_final":True}

POSTS = [
 {"key":"post-overbooking","title":"Comment éviter le surbooking : 6 étapes pour les hôtels","date":"2026-09-21","desc":"Pourquoi les hôtels se retrouvent en surbooking et comment l'éviter : channel manager, arrêts de vente, marges de disponibilité et que faire si cela arrive malgré tout."},
 {"key":"post-autoreply","title":"Répondre automatiquement aux messages clients Booking.com","date":"2026-09-21","desc":"Trois façons d'automatiser les messages des clients Booking.com : modèles de réponse, messages programmés et assistant IA."},
 {"key":"post-ai","title":"Répondre aux clients de l'hôtel avec l'IA : guide pratique","date":"2026-09-18",
  "desc":"Avantages, risques et mise en place : répondre avec l'IA aux messages de vos clients. Quelles questions automatiser, lesquelles laisser à l'équipe."},
 {"key":"post-pms","title":"Logiciel de gestion hôtelière pour petit hôtel : guide 2026","date":"2026-09-10",
  "desc":"Choisir un logiciel de gestion hôtelière pour un petit hôtel : 7 critères, modèles de prix, channel manager et check-in en ligne. Dès ⟦price:starter⟧/mois."},
]

def blog():
    items = "".join(f'<article><h2><a href="{U(p["key"])}">{p["title"]}</a></h2><p class="meta"><time datetime="{p["date"]}">{D(p["date"])}</time></p><p>{p["desc"]}</p></article>' for p in [dict(p, **{k: v for k, v in __import__("pages_v4").post_meta(L).get(p["key"], {}).items() if k in ("title", "desc")}) for p in POSTS])
    body = f'<section class="page-hero"><div class="wrap"><h1>Le blog des hôteliers</h1><p class="lead">Des articles pratiques sur la gestion d\'un hôtel indépendant, la distribution et la communication avec les clients.</p></div></section><section style="padding-top:0"><div class="wrap post-list">{items}</div></section>'
    return {"key":"blog","title":"Blog : guides pour hôtels indépendants | Hostlio Pro","desc":"Guides pratiques pour hôteliers indépendants : gestion hôtelière, channel manager, distribution sur les OTA et communication client avec l'IA.",
            "trail":[("Blog", U("blog"))],"body":body,"page_type":"CollectionPage"}

COVERS={"post-ai":("gen-checkin-phone",1080,1350),"post-pms":("gen-owner-laptop",1080,1350),"post-overbooking":("gen-reception",1080,1350),"post-autoreply":("gen-night-desk",1080,1350)}
def article(meta, content, faq=None):
    art = {"@type":"BlogPosting","headline":meta["title"],"description":meta["desc"],"datePublished":meta["date"],"inLanguage":L,"author":{"@type":"Organization","name":"Équipe produit Hostlio Pro","url":SITE+U("about")},"dateModified":UPDATED,"publisher":{"@id":SITE+"/#org"},
           "mainEntityOfPage":SITE+U(meta["key"]),"image":SITE+"/assets/img/"+COVERS[meta["key"]][0]+".webp"}
    body = f'<article><section class="page-hero"><div class="wrap"><h1 style="max-width:22ch">{meta["title"]}</h1><p class="meta">Par l\'<a href="{U("about")}">équipe produit Hostlio Pro</a>, celle qui conçoit Hostlio Pro. Publié le <time datetime="{meta["date"]}">{D(meta["date"])}</time>, mis à jour le <time datetime="{UPDATED}">{D(UPDATED)}</time></p></div></section><section style="padding-top:0"><div class="wrap"><figure class="post-cover"><img src="/assets/img/{COVERS[meta["key"]][0]}.webp" alt="" width="{COVERS[meta["key"]][1]}" height="{COVERS[meta["key"]][2]}"></figure><div class="prose">{content}</div></div></section></article>'
    return {"key":meta["key"],"title":meta["title"],"desc":meta["desc"],"og_type":"article",
            "trail":[("Blog",U("blog")),(meta["title"],U(meta["key"]))],"body":body,"schema":[art],"faq":faq or []}

def post_ai():
    c = f'''
<div class="answer"><p><strong>Réponse courte :</strong> la plupart des messages reçus par un hôtel sont des questions récurrentes (heure d'arrivée, parking, transferts, petit-déjeuner). Les confier à un assistant IA formé avec les informations de votre hôtel permet aux clients d'obtenir une réponse en quelques secondes, dans leur langue. Les remises, les réclamations et les demandes particulières doivent rester entre les mains de votre équipe.</p></div>
<h2>Quelles questions les hôtels reçoivent-ils le plus ?</h2>
<p>Dans les hôtels indépendants, la plupart des messages portent sur quelques sujets :</p>
<ul><li>Horaires d'arrivée et de départ, arrivée anticipée ou départ tardif</li><li>Transferts aéroport et accès à l'hôtel</li><li>Parking, petit-déjeuner, animaux acceptés</li><li>Consigne à bagages, équipements des chambres, le quartier</li><li>Modifications de réservation et demandes de facture</li></ul>
<p>Les réponses existent déjà à l'hôtel. Le problème, c'est de les donner dans la bonne langue, au bon moment.</p>
<h2>Que doit automatiser l'IA, et que ne doit-elle pas automatiser ?</h2>
<p>Dans une bonne configuration, l'assistant traite les questions d'information et laisse les décisions à l'équipe.</p>
<div class="table-wrap"><table><thead><tr><th>Laisser l'IA répondre</th><th>Transmettre à l'équipe</th></tr></thead><tbody>
<tr><td>Horaires, règles, équipements</td><td>Remises et négociation de prix</td></tr><tr><td>Itinéraires, informations sur les transferts</td><td>Réclamations et dédommagements</td></tr><tr><td>Vente de transferts et d'excursions</td><td>Situations médicales ou de sécurité</td></tr><tr><td>Rappel des détails de la réservation</td><td>Demandes de groupes et d'événements</td></tr></tbody></table></div>
<h2>Mise en place étape par étape</h2>
<ol><li><strong>Rédigez la base de connaissances de votre hôtel.</strong> Horaires, règles, équipements et questions fréquentes. Plus elle est claire, plus les réponses sont cohérentes.</li>
<li><strong>Connectez vos canaux.</strong> Réunissez les messages WhatsApp et OTA dans une seule boîte de réception.</li>
<li><strong>Commencez en mode validation.</strong> La première semaine, relisez et corrigez les réponses avant leur envoi.</li>
<li><strong>Définissez les règles de transfert.</strong> Déterminez quels sujets doivent vous revenir.</li>
<li><strong>Passez en mode automatique.</strong> Une fois les réponses cohérentes, laissez l'assistant gérer entièrement les questions d'information.</li></ol>
<h2>Pourquoi les réponses multilingues comptent</h2>
<p>Les clients qui écrivent dans leur propre langue donnent plus de détails et font davantage confiance à la réponse. Un assistant qui répond dans plus de 30 langues crée cette confiance même quand personne à la réception ne parle la langue, et vous lisez toujours la conversation dans la vôtre.</p>
<h2>Comment cela fonctionne dans Hostlio Pro</h2>
<p><a href="{U("ai")}">Lio</a>, l'assistant IA de Hostlio Pro, utilise les informations de votre hôtel et les données de réservation pour répondre aux messages WhatsApp et OTA (Booking.com, Airbnb, Expedia) dans plus de 30 langues. Les forfaits incluent entre ⟦quota:starter⟧ et ⟦quota:growth⟧ messages IA par mois ; consultez la <a href="{U("pricing")}">page Tarifs</a> pour plus de détails.</p>'''
    faq = [("L'IA peut-elle donner de fausses informations aux clients ?", "Le risque est minime lorsque l'assistant s'appuie uniquement sur les informations fournies par l'hôtel et transmet à l'équipe les questions dont il n'est pas sûr. Il est recommandé de commencer en mode validation."),
           ("Les clients sauront-ils qu'ils parlent à une IA ?", "Les réponses sont rédigées au nom de l'hôtel et dans son ton. Par souci de transparence, l'hôtel peut indiquer dans le message d'accueil que l'assistant est une IA.")]
    return article(next(p for p in POSTS if p["key"]=="post-ai"), c, faq)

def post_pms():
    c = f'''
<div class="answer"><p><strong>Réponse courte :</strong> le bon logiciel de gestion hôtelière (PMS) pour un petit hôtel intègre un channel manager, propose un prix fixe et transparent, une boîte de réception unique pour les messages clients, un accès mobile et une mise en place le jour même. Les systèmes conçus pour les grands groupes, avec des centaines de fonctionnalités, restent souvent inexploités par les petites équipes.</p></div>
<h2>1. Un channel manager intégré</h2>
<p>Si vous vendez en même temps sur Booking.com, Airbnb et Expedia, les disponibilités doivent se synchroniser instantanément. Un channel manager séparé, c'est un coût supplémentaire et un écran de plus. Vérifiez d'abord si le PMS en inclut un, et à combien de canaux il se connecte.</p>
<h2>2. Le modèle tarifaire</h2>
<p>Certains logiciels prélèvent un pourcentage sur le montant des réservations en plus de l'abonnement mensuel : les coûts augmentent alors avec le taux d'occupation. Un prix mensuel fixe rend votre budget prévisible. Avec les éditeurs qui ne publient pas leurs prix, attendez-vous à un processus commercial.</p>
<h2>3. La communication client</h2>
<p>Lorsque les messages sont dispersés entre WhatsApp et les messageries des OTA, les délais de réponse s'allongent. Une boîte de réception unique avec des réponses automatiques est le plus grand gain de temps pour les petites équipes.</p>
<h2>4. Un planning des chambres pratique</h2>
<p>Le calendrier des réservations est l'écran que la réception consulte le plus. Déplacer les chambres par glisser-déposer et voir d'un coup d'œil le canal de chaque réservation accélère le travail quotidien.</p>
<h2>5. L'accès mobile</h2>
<p>Les propriétaires sont souvent loin de leur établissement. Pouvoir suivre les arrivées, les disponibilités et les messages depuis son téléphone, avec une application mobile ou au moins une interface adaptée au smartphone, est un véritable besoin.</p>
<h2>6. Le check-in en ligne</h2>
<p>Collecter les informations des clients avant leur arrivée fait gagner du temps à la réception et simplifie les obligations d'enregistrement des clients.</p>
<h2>7. Mise en place et support</h2>
<p>Un petit hôtel ne peut pas se permettre un projet de déploiement de plusieurs semaines. Choisissez un logiciel utilisable le jour même, avec un support dans votre langue, et testez l'essai avec de vraies réservations.</p>
<h2>Liste de contrôle</h2>
<div class="table-wrap"><table><thead><tr><th>Critère</th><th>Question à poser</th></tr></thead><tbody>
<tr><td>Channel manager</td><td>Est-il inclus, et à combien de canaux se connecte-t-il ?</td></tr><tr><td>Tarifs</td><td>Le prix est-il fixe, y a-t-il une commission, le prix est-il public ?</td></tr>
<tr><td>Messagerie</td><td>Les messages WhatsApp et OTA sont-ils réunis au même endroit, avec des réponses automatiques ?</td></tr><tr><td>Mobile</td><td>Existe-t-il une application mobile ou une interface utilisable sur smartphone ?</td></tr>
<tr><td>Check-in</td><td>Y a-t-il un check-in en ligne avec signature électronique ?</td></tr><tr><td>Essai</td><td>Y a-t-il un essai gratuit et une résiliation sans engagement ?</td></tr></tbody></table></div>
<p>Hostlio Pro a été conçu autour de ces critères : découvrez les <a href="{U("features")}">fonctionnalités</a> et les <a href="{U("pricing")}">tarifs</a>.</p>'''
    faq = [("Un petit hôtel a-t-il besoin d'un PMS ?", "Si vous vendez sur plusieurs OTA et recevez des dizaines de messages par jour, oui. Travailler avec des tableurs et des extranets OTA séparés augmente le risque de surbooking et de réponses tardives."),
           ("Quelle est la différence entre un PMS et un channel manager ?", "Un PMS gère les opérations internes de l'hôtel (réservations, chambres, clients) ; un channel manager distribue les disponibilités et les tarifs sur les OTA. Un logiciel comme Hostlio Pro réunit les deux sur une seule plateforme.")]
    return article(next(p for p in POSTS if p["key"]=="post-pms"), c, faq)

def pages():
    import pages_v4
    return [home(), ai(), channel(), checkin(), features(), pricing(), faq_page(), about(), contact(), blog(), post_ai(), post_pms()] + pages_v4.pages(L, article) + __import__("legal_v5").pages(L, article)
