"""Takvim yazısı: "Logiciel chambres d'hôtes : comment choisir (2026)" — yalnız FR.
Resmî kaynaklar 16 Ekim 2026: Code du tourisme L324-3, D324-13/14, L324-4, D324-15, R324-16; CGCT L2333-30/33/34;
service-public F17452 (micro-BIC 83 600 €), CESEDA R814-1. Yazılım rakamları 12–13 Ekim (Elloha, Sirvoy, Little Hotelier feed).
Hostlio: Starter 10 odaya kadar; online check-in yalnız Pro/Growth (metin bunu söyler)."""
import html

SRC = [
 ("Service-public : chambres d'hôtes (F17452)", "https://entreprendre.service-public.gouv.fr/vosdroits/F17452"),
 ("Code du tourisme, art. L324-3", "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006813153"),
 ("Code du tourisme, art. D324-13", "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006813408"),
 ("Code du tourisme, art. L324-4", "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000020898921"),
 ("Service-public : déclaration de chambres d'hôtes (Cerfa 13566)", "https://www.service-public.gouv.fr/particuliers/vosdroits/R76415"),
 ("Service-public : fiche de police (F33458)", "https://www.service-public.gouv.fr/particuliers/vosdroits/F33458"),
 ("Elloha : channel manager", "https://elloha.com/channel-manager-sans-commission"),
 ("Sirvoy : pricing", "https://sirvoy.com/pricing/"),
 ("Amenitiz", "https://amenitiz.com/fr"),
 ("Beds24 : pricing", "https://beds24.com/pricing.html"),
]

def _tbl(head, rows, hl=True):
    h = "".join(f'<th scope="col">{x}</th>' for x in head)
    b = "".join(("<tr class=\"hl\">" if hl and r[0] == "Hostlio Pro" else "<tr>") + f'<th scope="row">{r[0]}</th>'
                + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table class="cmp"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

META = {"fr": dict(key="post-chdhotes", date="2026-10-16", title="Logiciel chambres d'hôtes : comment choisir (2026)",
                   desc="Quel logiciel pour des chambres d'hôtes en 2026 : planning, channel manager, messages, prix publiés et règles (5 chambres, mairie, taxe de séjour).")}

def fr(U):
    from build import btn, SIGNUP_URL
    cta = btn("Essai gratuit de ⟦trial⟧ jours", SIGNUP_URL) + btn("Voir les tarifs", U("pricing"), "ghost")
    regles = _tbl(["Règle", "Ce que dit le texte", "Source"], [
        ("Taille", "5 chambres au maximum, 15 personnes au maximum, nuitée et petit-déjeuner fournis ensemble, accueil par l'habitant", "Code du tourisme, D324-13"),
        ("Équipement", "Chaque chambre donne accès à une salle d'eau et à un WC ; linge de maison fourni", "D324-14"),
        ("Déclaration", "Déclaration préalable en mairie (Cerfa 13566, en ligne possible) ; nouvelle déclaration à chaque changement", "L324-4, D324-15"),
        ("Taxe de séjour", "Collectée par le loueur et reversée à la commune ; barème de 0,20 à 0,80 € par personne et par nuit", "CGCT L2333-30, L2333-34"),
        ("Clients étrangers", "Fiche individuelle de police, y compris pour les ressortissants européens ; conservation 6 mois", "CESEDA R814-1 à R814-3")], hl=False)
    rows = [
      ("Hostlio Pro (Starter)", "PMS + channel manager + assistant IA sur WhatsApp", "⟦price:starter⟧ par mois (USD), jusqu'à ⟦rooms:starter⟧ chambres", "⟦trial⟧ jours"),
      ("Elloha", "Channel manager + moteur de réservation (site web dans l'offre Magic)", "49 € (Connect) ou 59 € (Magic) par mois", "21 jours, sans carte"),
      ("Sirvoy", "PMS ; channel manager dans l'offre Pro", "Jusqu'à 10 chambres : Starter 22 €, Pro 79 € par mois", "14 jours, sans carte"),
      ("Beds24", "PMS + channel manager à l'usage", "12,90 € + 2,60 € par chambre + 0,55 € par lien", "Gratuit"),
      ("Amenitiz", "Tout-en-un ; chambres d'hôtes à partir de 3 chambres", "Sur devis", "Démo")]
    c = f'''<div class="answer"><p><strong>En bref :</strong> pour des chambres d'hôtes (5 chambres au maximum), il n'est pas nécessaire d'avoir un PMS d'hôtel complet. Il vous faut un planning clair, un channel manager pour ne jamais vendre deux fois la même chambre sur Booking.com et Airbnb, une façon simple de répondre aux messages des clients et un prix fixe adapté à quelques chambres. Parmi les prix publiés, comptez d'environ 20 à 80 € par mois. Le logiciel ne remplace pas vos obligations : déclaration en mairie, taxe de séjour et fiche de police pour les clients étrangers restent à votre charge.</p></div>
<p class="small muted">Hostlio Pro figure dans ce comparatif : nous ne sommes pas neutres. Les règles viennent des textes officiels (Code du tourisme, CGCT, CESEDA, service-public.gouv.fr) consultés le 16 octobre 2026 ; les prix des pages officielles des éditeurs, consultées les 12 et 13 octobre 2026. Ce guide n'est pas un conseil juridique ou fiscal.</p>
<h2>Les règles à connaître en 2026</h2>
{regles}
<p>Pour le statut fiscal et social (micro-BIC, immatriculation), la fiche officielle <a href="https://entreprendre.service-public.gouv.fr/vosdroits/F17452" rel="nofollow noopener">F17452</a> est à jour : en 2026, le micro-BIC s'applique sous 83 600 € de recettes. La loi Le Meur de 2024 vise surtout les meublés de tourisme ; la déclaration des chambres d'hôtes en mairie n'a pas changé.</p>
<h2>Ce qu'un logiciel doit faire pour des chambres d'hôtes</h2>
<ul><li><strong>Un planning lisible</strong> de vos 2 à 5 chambres, avec les réservations directes et celles des plateformes au même endroit.</li>
<li><strong>Un channel manager</strong> qui ferme la chambre partout dès qu'elle est réservée. C'est ce qui évite le surbooking entre Booking.com, Airbnb et vos réservations directes. Voir <a href="{U("post-cmfr")}">les meilleurs channel managers pour petits hôtels</a>.</li>
<li><strong>Les messages des clients au même endroit</strong> : heure d'arrivée, petit-déjeuner, parking, accès. Quand vous êtes seul à gérer, une réponse automatique avec vos propres informations fait gagner beaucoup de temps.</li>
<li><strong>Une application mobile</strong>, parce qu'en chambres d'hôtes on gère souvent depuis la cuisine ou le jardin.</li>
<li><strong>Un prix fixe adapté</strong> à quelques chambres, sans commission ni engagement.</li></ul>
<h2>Comparatif des solutions pour quelques chambres</h2>
{_tbl(["Solution", "Type", "Prix publié", "Essai"], rows)}
<p>Elloha est surtout un channel manager avec moteur de réservation ; Sirvoy et Beds24 sont des PMS simples et économiques ; Amenitiz vise les chambres d'hôtes à partir de 3 chambres, sur devis. Pour les prix des logiciels plus complets, voir <a href="{U("post-prixfr")}">le prix d'un logiciel de gestion hôtelière en 2026</a>.</p>
<h2>Hostlio Pro pour des chambres d'hôtes</h2>
<p>Le forfait Starter de Hostlio Pro (⟦price:starter⟧ par mois, jusqu'à ⟦rooms:starter⟧ chambres) comprend le planning, le channel manager connecté à plus de 100 OTA, l'application iOS et Android et Lio, l'assistant IA qui répond à vos clients sur WhatsApp dans leur langue avec les informations de votre maison. Le check-in en ligne avec signature est dans les forfaits Pro et Growth. Ce que Hostlio Pro ne fait pas : pas de moteur de réservation ni d'encaissement en ligne, pas de déclaration de taxe de séjour et pas de transmission de fiche de police. Il est facturé en dollars.</p>
<div class="cta-row" style="margin-top:12px">{cta}</div>
<h2>Comment choisir</h2>
<ol><li><strong>Comptez vos canaux</strong> : si vous vendez sur Booking.com et Airbnb, le channel manager est indispensable.</li>
<li><strong>Regardez le coût annuel</strong> plutôt que le prix d'appel.</li>
<li><strong>Testez avec vos vraies chambres</strong> et une plateforme connectée pendant l'essai gratuit.</li>
<li><strong>Prévoyez vos obligations</strong> : taxe de séjour et <a href="{U("post-fichepolice")}">fiche de police</a> se gèrent en dehors du logiciel si celui-ci ne les prend pas en charge.</li></ol>
'''
    lis = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(n)}</a></li>' for n, u in SRC)
    c += f'<h2>Sources</h2><p class="small muted">Textes officiels consultés le 16 octobre 2026 ; pages des éditeurs les 12 et 13 octobre 2026.</p><ul>{lis}</ul>'
    faq = [("Combien de chambres peut-on avoir en chambres d'hôtes ?", "Cinq chambres au maximum, pour une capacité de quinze personnes, avec la nuitée et le petit-déjeuner fournis ensemble et un accueil par l'habitant (Code du tourisme, D324-13)."),
           ("Faut-il déclarer ses chambres d'hôtes ?", "Oui, à la mairie avant de commencer, avec le Cerfa 13566 (possible en ligne), puis à chaque changement (L324-4 et D324-15)."),
           ("Faut-il un channel manager pour des chambres d'hôtes ?", "Si vous vendez sur plusieurs plateformes, oui : il ferme la chambre partout dès qu'elle est réservée et évite le surbooking."),
           ("Combien coûte un logiciel pour chambres d'hôtes ?", "Parmi les prix publiés, environ 20 à 80 € par mois pour quelques chambres (octobre 2026). Hostlio Pro Starter coûte ⟦price:starter⟧ par mois, channel manager et assistant IA compris.")]
    return c, faq

FN = {"fr": fr}
