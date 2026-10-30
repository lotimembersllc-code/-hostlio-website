"""Takvim yazısı: "Taxe de séjour 2026 : calcul, tarifs et déclaration" — yalnız FR.
Resmî kaynaklar 16 Ekim 2026: collectivites-locales.gouv.fr guide pratique (juin 2026, fiches 1–11), barèmes 2026 ve 2027 (2027 = 2026),
entreprendre.service-public F31635, impots.gouv.fr. Légifrance otomatik okunamadı → madde numaraları resmî rehberden.
LF 2026 metni doğrulanamadı (rehber değişiklik göstermiyor; Senato I-478 geri çekildi). Gecikme faizi oranı doğrulanamadı → yazılmaz.
Hostlio vergiyi hesaplamaz/beyan etmez."""
import html

_D = "https://www.collectivites-locales.gouv.fr/files/files/2.%20G%C3%A9rer%20les%20finances%20publiques%20locales/3.%20La%20fiscalit%C3%A9%20locale/Fiscalit%C3%A9%20indirecte%20locale/Taxe%20de%20s%C3%A9jour/"
SRC = [
 ("Collectivites-locales.gouv.fr : la taxe de séjour", "https://www.collectivites-locales.gouv.fr/gerer-les-finances-publiques-locales/fiscalite-locale/fiscalite-indirecte-locale/taxe-de-sejour"),
 ("Guide pratique des taxes de séjour (8e édition, juin 2026)", "https://www.collectivites-locales.gouv.fr/gerer-les-finances-publiques-locales/fiscalite-locale/fiscalite-indirecte-locale/taxe-de-sejour/guide-pratique-les-taxes-de-sejour"),
 ("Barème des tarifs 2026", _D + "TS_TarifsMax2026-1.pdf"),
 ("Barème des tarifs 2027", _D + "TS_TarifsMax2027.pdf"),
 ("Guide pratique, fiche 4 : exonérations", _D + "Fiche%204%20%28Juin%202026%29.pdf"),
 ("Guide pratique, fiche 6 : calcul", _D + "Fiche%206%20%28Juin%202026%29.pdf"),
 ("Guide pratique, fiche 9 : déclaration et reversement", _D + "Fiche%209%20%28Juin%202026%29.pdf"),
 ("Guide pratique, fiche 11 : sanctions", _D + "Fiche%2011%20%28Juin%202026%29.pdf"),
 ("Entreprendre.service-public : taxe de séjour (F31635)", "https://entreprendre.service-public.gouv.fr/vosdroits/F31635"),
 ("Impots.gouv.fr : taxe de séjour", "https://www.impots.gouv.fr/taxe-de-sejour"),
 ("Consultation des tarifs par commune", "https://taxesejour.impots.gouv.fr/FR/"),
]

def _tbl(head, rows):
    h = "".join(f'<th scope="col">{x}</th>' for x in head)
    b = "".join("<tr>" + f'<th scope="row">{r[0]}</th>' + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table class="cmp"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

META = {"fr": dict(key="post-taxefr", date="2026-10-16", title="Taxe de séjour 2026 : tarifs, calcul et déclaration",
                   desc="Taxe de séjour 2026 : barème par catégorie, taxes additionnelles, exonérations, exemple de calcul pour un hôtel 3 étoiles, déclaration et sanctions.")}

def fr(U):
    from build import btn, SIGNUP_URL
    cta = btn("Essai gratuit de ⟦trial⟧ jours", SIGNUP_URL) + btn("Voir les fonctionnalités", U("features"), "ghost")
    bareme = _tbl(["Catégorie d'hébergement", "Tarif plancher", "Tarif plafond"], [
        ("Palaces", "0,70 €", "4,90 €"),
        ("Hôtels, résidences et meublés de tourisme 5 étoiles", "0,70 €", "3,60 €"),
        ("4 étoiles", "0,70 €", "2,60 €"),
        ("3 étoiles", "0,50 €", "1,70 €"),
        ("2 étoiles, villages de vacances 4 et 5 étoiles", "0,30 €", "1,00 €"),
        ("1 étoile, villages de vacances 1 à 3 étoiles, <strong>chambres d'hôtes</strong>, auberges collectives", "0,20 €", "0,80 €"),
        ("Campings 3 à 5 étoiles, aires de camping-cars (par 24 h)", "0,20 €", "0,60 €"),
        ("Campings 1 et 2 étoiles, ports de plaisance", "0,20 €", "0,20 €"),
        ("Hébergements non classés ou en attente de classement", "1 % du prix de la nuitée par personne", "5 %, dans la limite du tarif le plus élevé voté par la commune")])
    add = _tbl(["Taxe additionnelle", "Taux", "Où"], [
        ("Départementale", "10 %", "Si le département l'a votée"),
        ("Société des grands projets", "15 %", "Île-de-France"),
        ("Île-de-France Mobilités", "200 %", "Île-de-France, depuis le 1er janvier 2024"),
        ("Régionales (lignes nouvelles)", "34 %", "Bouches-du-Rhône, Var, Alpes-Maritimes ; Sud-Ouest (GPSO) ; Hérault, Aude, Pyrénées-Orientales")])
    exemple = _tbl(["Étape", "Calcul", "Montant"], [
        ("Nuitées taxables", "2 adultes × 3 nuits (l'enfant est exonéré)", "6"),
        ("Part communale", "6 × 1,50 €", "9,00 €"),
        ("Taxe départementale 10 %", "6 × 0,15 €", "0,90 €"),
        ("Total à collecter", "", "<strong>9,90 €</strong>")])
    c = f'''<div class="answer"><p><strong>En bref :</strong> la taxe de séjour est payée par le client qui n'est pas domicilié dans la commune et collectée par l'hébergeur, qui la reverse à la commune ou à l'intercommunalité. Le tarif dépend de la catégorie : en 2026, il va de 0,20 € à 0,80 € par personne et par nuit pour une chambre d'hôtes et de 0,50 € à 1,70 € pour un hôtel 3 étoiles. Pour les hébergements non classés, c'est un pourcentage de 1 % à 5 % du prix de la nuit. S'y ajoutent souvent une taxe départementale de 10 % et, dans certaines régions, d'autres taxes additionnelles. Le barème 2027 publié par l'État est identique.</p></div>
<p class="small muted">Ce guide est informatif et ne constitue pas un conseil fiscal. Il s'appuie sur le guide pratique des taxes de séjour publié par la DGCL (juin 2026), les barèmes officiels 2026 et 2027 et service-public.gouv.fr, consultés le 16 octobre 2026. Le tarif exact est fixé par votre commune : vérifiez sa délibération.</p>
<h2>Qui paie, qui collecte ?</h2>
<p>La taxe de séjour « au réel » est due par les personnes qui séjournent dans la commune sans y être domiciliées. L'hébergeur la facture au client en plus du prix de la chambre, la collecte avant son départ et la reverse à la commune. Le montant applicable est celui en vigueur à la date du séjour, pas à la date de réservation.</p>
<p>Il existe aussi une taxe de séjour « forfaitaire » : c'est alors l'hébergeur qui la doit, calculée sur la capacité d'accueil et le nombre de nuits d'ouverture, qu'il la répercute ou non dans ses prix. Une commune peut combiner les deux régimes selon la nature des hébergements (par exemple hôtels au réel, campings au forfait). Les hébergements non classés sont toujours au réel.</p>
<p>Quand la réservation passe par une plateforme qui encaisse le paiement pour un loueur non professionnel, c'est la plateforme qui collecte la taxe. Pour un hôtel qui vend sur Booking.com ou Expedia, vérifiez dans votre contrat qui collecte : dans le doute, c'est à vous de le faire.</p>
<h2>Le barème 2026 par catégorie</h2>
<p>Chaque commune choisit son tarif entre le plancher et le plafond fixés par la loi. Les montants s'entendent par personne et par nuit.</p>
{bareme}
<p>Les chambres d'hôtes ont un tarif unique (0,20 € à 0,80 €), quels que soient les services proposés. Une simple chambre chez l'habitant, en revanche, relève du régime des hébergements non classés. Pour choisir un outil adapté aux maisons d'hôtes, lisez notre guide <a href="{U("post-chdhotes")}">logiciel chambres d'hôtes</a>.</p>
<h2>Hébergements non classés : le calcul en pourcentage</h2>
<p>La commune vote un taux unique entre 1 % et 5 %. Il s'applique au prix de la nuitée hors taxes divisé par le nombre total d'occupants, y compris ceux qui sont exonérés. Le petit-déjeuner, les frais de réservation et les commissions de plateforme ne font pas partie de la base. Le résultat est plafonné au tarif le plus élevé adopté par la commune, donc au maximum 4,90 €.</p>
<h2>Les taxes additionnelles</h2>
<p>Sur le tarif communal s'ajoutent, selon votre localisation, une ou plusieurs taxes additionnelles calculées en pourcentage du tarif communal :</p>
{add}
<p>En Île-de-France, la majoration de 200 % au profit d'Île-de-France Mobilités s'applique automatiquement depuis 2024. Chaque taxe additionnelle se calcule sur le tarif communal arrondi, avec un arrondi au centime à chaque étape.</p>
<h2>Qui est exonéré ?</h2>
<ul><li>les mineurs ;</li>
<li>les titulaires d'un contrat de travail saisonnier employés dans la commune ;</li>
<li>les personnes bénéficiant d'un hébergement d'urgence ou d'un relogement temporaire ;</li>
<li>les personnes qui occupent des locaux dont le loyer est inférieur à un montant fixé par la commune.</li></ul>
<p>Les fonctionnaires en mission et les stagiaires ne sont pas exonérés. Au régime forfaitaire, ces exonérations ne s'appliquent pas : la commune peut prévoir un abattement de 10 % à 80 % selon la durée d'ouverture.</p>
<h2>Exemple de calcul pour un hôtel 3 étoiles</h2>
<p>Hypothèse : la commune applique 1,50 € par personne et par nuit aux hôtels 3 étoiles, au réel, et le département a voté la taxe additionnelle de 10 %. Deux adultes et un enfant de 12 ans séjournent trois nuits.</p>
{exemple}
<p>Le même séjour en Île-de-France coûterait 4,88 € par adulte et par nuit (1,50 € + 0,15 € + 0,23 € + 3,00 €), soit 29,28 € pour les six nuitées. Indiquez la taxe de séjour sur une ligne séparée de la facture.</p>
<h2>Déclaration, reversement et registre</h2>
<ul><li><strong>Dates de reversement :</strong> elles sont fixées par la délibération de votre commune. Les plateformes reversent deux fois par an, avant le 30 juin et le 31 décembre.</li>
<li><strong>État récapitulatif :</strong> à chaque reversement, l'hébergeur transmet pour chaque logement la date de perception, la date de début du séjour, l'adresse, le nombre de personnes, le nombre de nuitées, le prix de la nuit pour un hébergement non classé, le montant collecté, les motifs d'exonération et, le cas échéant, le numéro d'enregistrement. La taxe principale et les taxes additionnelles apparaissent séparément.</li>
<li><strong>Régime forfaitaire :</strong> la déclaration se fait au moins un mois avant le début de la période de perception.</li>
<li><strong>Tarifs de votre commune :</strong> ils sont publiés chaque année sur <a href="https://taxesejour.impots.gouv.fr/FR/" rel="nofollow noopener">taxesejour.impots.gouv.fr</a>. Les communes doivent délibérer avant le 1er juillet pour l'année suivante.</li></ul>
<p>Si un client part sans payer, signalez-le au maire dans les 8 jours ; sinon la taxe reste due par l'hébergeur.</p>
<h2>Sanctions</h2>
<p>Depuis 2019, le président du tribunal judiciaire peut, à la demande de la commune, prononcer des amendes :</p>
<ul><li>150 € par omission ou inexactitude dans la déclaration, jusqu'à 12 500 € par déclaration ;</li>
<li>750 € à 12 500 € pour un état récapitulatif absent, incomplet ou en retard, ou pour une taxe non collectée ;</li>
<li>750 € à 2 500 € pour une taxe collectée mais non reversée.</li></ul>
<p>La commune peut aussi procéder à une taxation d'office après une mise en demeure restée sans réponse pendant 30 jours.</p>
<h2>Ce qui change en 2027</h2>
<p>Les plafonds sont revalorisés chaque année selon l'inflation. Pour 2027, l'inflation retenue est de 0,9 % et, après arrondi, le barème publié par l'État est identique à celui de 2026. Votre commune peut toutefois modifier son propre tarif : sa délibération pour 2027 devait être prise avant le 1er juillet 2026.</p>
<h2>Ce que fait Hostlio Pro (et ce qu'il ne fait pas)</h2>
<p>Hostlio Pro ne calcule pas la taxe de séjour et ne fait ni la déclaration ni le reversement. Il centralise vos réservations, vos nuitées et vos clients dans un seul <a href="{U("features")}">logiciel de gestion hôtelière</a> et permet d'exporter les réservations en Excel pour préparer votre état récapitulatif. Pour les clients étrangers, pensez aussi à la <a href="{U("post-fichepolice")}">fiche de police</a>.</p>
<div class="cta-row" style="margin-top:12px">{cta}</div>
'''
    lis = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(n)}</a></li>' for n, u in SRC)
    c += f'<h2>Sources</h2><p class="small muted">Sources consultées le 16 octobre 2026.</p><ul>{lis}</ul>'
    faq = [("Quel est le tarif de la taxe de séjour en 2026 ?", "Il dépend de la catégorie et de la commune : de 0,20 € à 0,80 € par personne et par nuit pour une chambre d'hôtes, de 0,50 € à 1,70 € pour un hôtel 3 étoiles, jusqu'à 4,90 € pour un palace. Les hébergements non classés paient 1 % à 5 % du prix de la nuit par personne."),
           ("Qui doit payer la taxe de séjour ?", "Le client qui n'est pas domicilié dans la commune. L'hébergeur la collecte et la reverse à la commune ; au régime forfaitaire, elle est due par l'hébergeur."),
           ("Les enfants paient-ils la taxe de séjour ?", "Non. Les mineurs sont exonérés au régime réel."),
           ("Hostlio Pro calcule-t-il la taxe de séjour ?", "Non. Hostlio Pro ne calcule ni ne reverse la taxe de séjour, mais vous pouvez exporter vos réservations en Excel pour préparer la déclaration.")]
    return c, faq

FN = {"fr": fr}
