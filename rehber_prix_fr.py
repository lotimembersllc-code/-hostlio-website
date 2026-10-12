"""Takvim yazısı (23 Ekim 2026 planı): "Prix d'un logiciel de gestion hôtelière en 2026" — yalnız FR.
Resmî siteler 12–13 Ekim 2026: Thaïs (65 € HT/10 ch., 200 € HT/30 ch.; module CM 30–90 €; installation 200–1 000 €), Sirvoy
(hesaplayıcı: Starter 22/42 €, Pro 79/149 €), Little Hotelier ve SiteMinder (SiteMinder resmî fiyat akışı, Fransa, HT),
RoomRaccoon, Beds24; Mews, Septeo (Misterbooking/Asterio/Ulyses), Cloudbeds, Amenitiz, Avirato teklifle.
Mevzuat: impots.gouv.fr e-fatura takvimi; BOFiP ACTU-2026-00073 (kasa: sertifika ya da editör beyanı)."""
import html

SRC = [
 ("Thaïs PMS : tarifs", "https://thais-pms.com/tarifs"),
 ("Sirvoy : pricing", "https://sirvoy.com/pricing/"),
 ("SiteMinder : tarifs", "https://www.siteminder.com/fr/pricing/"),
 ("SiteMinder : grille tarifaire officielle (flux de prix, France)", "https://resources.siteminder.com/services/pricing/2022/data/products/index.php"),
 ("RoomRaccoon : tarifs", "https://roomraccoon.fr/tarifs/"),
 ("Beds24 : pricing", "https://beds24.com/pricing.html"),
 ("Mews : prix", "https://www.mews.com/fr/prix"),
 ("Septeo Hospitality : PMS hôtel", "https://www.septeo.com/fr/hospitality/solutions/pms-hotel"),
 ("Cloudbeds : tarifs", "https://www.cloudbeds.com/fr/tarifs/"),
 ("Amenitiz : tarifs", "https://amenitiz.com/fr/nos-tarifs"),
 ("Avirato : tarifs", "https://avirato.com/fr/tarifs"),
 ("impots.gouv.fr : la facturation électronique", "https://www.impots.gouv.fr/professionnel/je-decouvre-la-facturation-electronique"),
 ("BOFiP : logiciels de caisse (actualité du 25/03/2026)", "https://bofip.impots.gouv.fr/bofip/15035-PGP.html/ACTU-2026-00073"),
]

def _tbl(head, rows, hl=True):
    h = "".join(f'<th scope="col">{x}</th>' for x in head)
    b = "".join(("<tr class=\"hl\">" if hl and r[0] == "Hostlio Pro" else "<tr>") + f'<th scope="row">{r[0]}</th>'
                + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table class="cmp"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

META = {"fr": dict(key="post-prixfr", date="2026-10-13", title="Prix d'un logiciel de gestion hôtelière en 2026",
                   desc="Combien coûte un logiciel de gestion hôtelière en 2026 : prix publiés, coût pour 10 et 25 chambres, frais cachés, facturation électronique et caisse.")}

def fr(U):
    from build import btn, SIGNUP_URL
    cta = btn("Essai gratuit de ⟦trial⟧ jours", SIGNUP_URL) + btn("Voir les tarifs", U("pricing"), "ghost")
    pub = _tbl(["Logiciel", "Type", "Prix publié", "Remarque"], [
        ("Hostlio Pro", "PMS + channel manager + assistant IA", "⟦price:starter⟧ / ⟦price:pro⟧ / ⟦price:growth⟧ par mois (USD)", "Prix fixe, sans commission"),
        ("Thaïs (FR)", "PMS ; channel manager en module", "65 € HT par mois pour 10 chambres, 200 € HT pour 30 chambres", "Module channel manager 30 à 90 € par mois ; installation 200 à 1 000 €"),
        ("Sirvoy", "PMS + channel manager (offre Pro)", "Jusqu'à 10 chambres : Starter 22 €, Pro 79 € ; jusqu'à 50 : 42 € et 149 € par mois", "Channel manager seulement en Pro ; essai 14 jours"),
        ("Little Hotelier", "PMS avec channel manager", "Pro : 129 € (10 chambres), 219 € (jusqu'à 30) par mois", "Grille tarifaire officielle de SiteMinder"),
        ("SiteMinder", "Channel manager", "105 € HT (10 chambres), 155 € HT (jusqu'à 30) par mois", "Pas de PMS"),
        ("RoomRaccoon", "Suite", "Entry 164 € par mois jusqu'à 18 chambres", "3 canaux seulement en Entry"),
        ("Beds24", "PMS + channel manager à l'usage", "12,90 € + 2,60 € par chambre + 0,55 € par lien", "Paramétrage plus technique"),
        ("Mews, Septeo (Misterbooking, Asterio, Ulyses), Cloudbeds, Amenitiz, Avirato", "PMS et suites", "Sur devis", "Demandez le coût annuel complet par écrit")])
    ex = _tbl(["Logiciel", "10 chambres / mois", "25 chambres / mois", "Comprend"], [
        ("Hostlio Pro", "⟦price:starter⟧ (Starter)", "⟦price:pro⟧ (Pro)", "PMS, channel manager, app, IA"),
        ("Beds24", "43,85 €", "86,15 €", "3 et 5 types de chambre sur 3 canaux"),
        ("Sirvoy Pro", "79 €", "149 €", "PMS + channel manager"),
        ("Thaïs + module channel manager", "95 à 155 € HT", "Non publié pour 25 chambres", "PMS 65 € HT + module 30 à 90 € ; installation en plus"),
        ("Little Hotelier Pro", "129 €", "219 €", "PMS avec channel manager"),
        ("RoomRaccoon Entry", "164 €", "228 €", "3 canaux")])
    c = f'''<div class="answer"><p><strong>En bref :</strong> en 2026, un logiciel de gestion hôtelière (PMS) pour un petit hôtel ou une maison d'hôtes coûte, parmi les éditeurs qui publient leurs prix, d'environ 45 à 165 € par mois pour 10 chambres et d'environ 85 à 230 € pour 25 chambres. La plupart des PMS orientés hôtellerie (Mews, Septeo, Cloudbeds, Amenitiz) ne donnent leurs prix que sur devis. Pour comparer, additionnez l'abonnement, l'installation, les modules (channel manager, moteur de réservation, caisse), la TVA et les éventuelles commissions.</p></div>
<p class="small muted">Hostlio Pro figure dans ce comparatif : nous ne sommes pas neutres. Les chiffres viennent des pages et calculateurs officiels des éditeurs, consultés les 12 et 13 octobre 2026 ; HT ou TTC seulement quand l'éditeur le précise. Les prix changent : vérifiez toujours la page de l'éditeur.</p>
<h2>Combien coûte Hostlio Pro</h2>
<p>Hostlio Pro propose trois forfaits à prix fixe : Starter ⟦price:starter⟧ par mois (jusqu'à ⟦rooms:starter⟧ chambres), Pro ⟦price:pro⟧ (jusqu'à ⟦rooms:pro⟧) et Growth ⟦price:growth⟧ (jusqu'à ⟦rooms:growth⟧ chambres et 2 établissements), en dollars américains, avec 20 % de remise en paiement annuel. Pas de commission sur les réservations ; channel manager, application mobile et Lio, l'assistant IA, sont inclus dans tous les forfaits. Essai gratuit de ⟦trial⟧ jours.</p>
<div class="cta-row" style="margin-top:12px">{cta}</div>
<h2>Les modèles de prix</h2>
<ul><li><strong>Abonnement fixe :</strong> le même montant chaque mois, le plus simple à budgéter.</li>
<li><strong>Par chambre ou par tranche :</strong> le prix monte avec le nombre de chambres.</li>
<li><strong>Commission par réservation :</strong> faible en basse saison, lourde en haute saison.</li>
<li><strong>Sur devis :</strong> le prix est donné après une démonstration, selon votre établissement.</li></ul>
<h2>Prix publiés en 2026</h2>
{pub}
<h2>Exemple : 10 et 25 chambres</h2>
<p>Coût mensuel calculé à partir des prix publiés et des calculateurs officiels. Les offres ne comprennent pas les mêmes fonctions : ne choisissez pas sur le seul prix.</p>
{ex}
<p class="small muted">Little Hotelier et SiteMinder : grille tarifaire officielle de SiteMinder pour la France ; pour 25 chambres, la tranche jusqu'à 30. Sirvoy, Beds24 et RoomRaccoon : calculateurs officiels. Thaïs : tarifs publiés pour 10 et 30 chambres.</p>
<h2>Les coûts qu'on ne voit pas dans l'abonnement</h2>
<ul><li><strong>Installation et formation :</strong> certains éditeurs les facturent à part (chez Thaïs, de 200 à 1 000 €).</li>
<li><strong>Modules :</strong> channel manager, moteur de réservation, paiement ou caisse peuvent être vendus séparément.</li>
<li><strong>HT ou TTC :</strong> comparez des montants homogènes ; beaucoup de grilles ne le précisent pas.</li>
<li><strong>Engagement :</strong> vérifiez la durée minimale et les conditions de résiliation.</li>
<li><strong>Commissions OTA :</strong> elles ne dépendent pas du logiciel, mais c'est souvent le poste le plus lourd. Calculez votre net par canal avec le <a href="{U("commission")}">calculateur de commissions OTA</a>.</li></ul>
<h2>Facturation électronique et caisse : ce que 2026 change</h2>
<p>Depuis le 1er septembre 2026, toutes les entreprises doivent pouvoir <strong>recevoir</strong> des factures électroniques. L'obligation d'<strong>émettre</strong> des factures électroniques s'applique aux PME et micro-entreprises à partir du 1er septembre 2027 ; l'e-reporting suit le même calendrier. Demandez à votre éditeur comment il se raccorde à une plateforme agréée.</p>
<p>Si vous encaissez des particuliers avec un logiciel de caisse, il doit être inaltérable et sécurisé. Selon le BOFiP, on le prouve par un certificat délivré par un organisme accrédité (par exemple NF525) ou, depuis le 21 février 2026, par une attestation individuelle de l'éditeur. Pensez aussi à la taxe de séjour et à la fiche de police pour les clients étrangers : demandez ce que le logiciel prend en charge.</p>
<h2>Bien choisir sans se tromper</h2>
<ol><li><strong>Calculez le coût annuel complet</strong> : abonnement, installation, modules, TVA, commissions.</li>
<li><strong>Préférez un prix fixe</strong> si votre saison est forte.</li>
<li><strong>Demandez le prix par écrit</strong> aux éditeurs sur devis, modules compris.</li>
<li><strong>Testez avec vos données</strong> : vos chambres, vos prix et au moins une OTA connectée.</li></ol>
<p>Pour les critères de choix, lisez <a href="{U("post-pms")}">comment choisir un logiciel de gestion hôtelière pour un petit hôtel</a> ; pour la distribution, <a href="{U("post-cmfr")}">les meilleurs channel managers pour petits hôtels</a>.</p>
<h2>Ce que Hostlio Pro ne fait pas</h2>
<p>Pour une comparaison honnête : Hostlio Pro n'a pas de module de caisse ni de facturation électronique, ne déclare pas la taxe de séjour et n'envoie pas de fiche de police ; il n'a pas non plus de moteur de réservation ni d'encaissement en ligne, et il est facturé en dollars. Si ces fonctions sont indispensables, un PMS français plus complet peut mieux vous convenir.</p>
'''
    lis = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(n)}</a></li>' for n, u in SRC)
    c += f'<h2>Sources</h2><p class="small muted">Toutes les sources ont été consultées les 12 et 13 octobre 2026.</p><ul>{lis}</ul>'
    faq = [("Combien coûte un logiciel de gestion hôtelière ?", "Parmi les éditeurs qui publient leurs prix, environ 45 à 165 € par mois pour 10 chambres et 85 à 230 € pour 25 chambres (octobre 2026), selon ce qui est inclus. Beaucoup de PMS orientés hôtellerie fonctionnent sur devis."),
           ("Le channel manager est-il compris dans le prix ?", "Cela dépend : il est inclus chez Hostlio Pro, Little Hotelier et RoomRaccoon ; chez Sirvoy seulement dans l'offre Pro ; chez Thaïs c'est un module à 30 à 90 € par mois ; SiteMinder est un channel manager seul."),
           ("La certification NF525 est-elle obligatoire ?", "Le logiciel de caisse doit être inaltérable et sécurisé. Selon le BOFiP, cela se prouve par un certificat d'un organisme accrédité (par exemple NF525) ou, depuis le 21 février 2026, par une attestation individuelle de l'éditeur."),
           ("Combien coûte Hostlio Pro ?", "Starter ⟦price:starter⟧, Pro ⟦price:pro⟧ et Growth ⟦price:growth⟧ par mois (USD), 20 % de remise en annuel, essai gratuit de ⟦trial⟧ jours.")]
    return c, faq

FN = {"fr": fr}
