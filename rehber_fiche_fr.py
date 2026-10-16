"""Takvim yazısı: "Fiche de police : la déclaration des clients étrangers (guide 2026)" — yalnız FR.
Resmî kaynaklar 16 Ekim 2026: CESEDA R814-1/2/3 (décret 2020-1734), arrêté 1.10.2015 (model), service-public F33458/F17452, CNIL.
Ceza: CESEDA'da özel ceza YOK (R610-5 bağlantısı resmî kaynakta yok → yazılmaz). Elektronik doldurma açıkça düzenlenmemiş.
Hostlio fiche'i doldurmaz/saklamaz/iletmez; online check-in (Pro/Growth) verilerin bir kısmını önceden toplar."""
import html

SRC = [
 ("CESEDA, art. R814-1", "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000042804990"),
 ("CESEDA, art. R814-2", "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000042804988"),
 ("CESEDA, art. R814-3", "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000042804986"),
 ("Arrêté du 1er octobre 2015 relatif au modèle de fiche individuelle de police", "https://www.legifrance.gouv.fr/loda/id/JORFTEXT000031285813/"),
 ("Service-public : fiche de police dans un hébergement touristique (F33458)", "https://www.service-public.gouv.fr/particuliers/vosdroits/F33458"),
 ("Service-public : chambres d'hôtes (F17452)", "https://entreprendre.service-public.gouv.fr/vosdroits/F17452"),
 ("CNIL : la fiche de police dans les établissements", "https://www.cnil.fr/fr/cnil-direct/question/touriste-etranger-en-france-la-fiche-de-police-dans-les-etablissements-de"),
]

def _tbl(head, rows):
    h = "".join(f'<th scope="col">{x}</th>' for x in head)
    b = "".join("<tr>" + f'<th scope="row">{r[0]}</th>' + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table class="cmp"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

META = {"fr": dict(key="post-fichepolice", date="2026-10-16", title="Fiche de police : la déclaration des clients étrangers (2026)",
                   desc="Fiche individuelle de police en 2026 : qui doit la remplir, quels clients (UE compris), quelles données, conservation 6 mois, transmission et RGPD.")}

def fr(U):
    from build import btn, SIGNUP_URL
    cta = btn("Essai gratuit de ⟦trial⟧ jours", SIGNUP_URL) + btn("Voir le check-in en ligne", U("checkin"), "ghost")
    data = _tbl(["Donnée", "Précision"], [
        ("Nom et prénoms", "Du client étranger"),
        ("Date et lieu de naissance", ""),
        ("Nationalité", ""),
        ("Domicile habituel", "L'adresse où le client vit habituellement"),
        ("Téléphone mobile et adresse e-mail", ""),
        ("Date d'arrivée et date de départ prévue", ""),
        ("Enfants de moins de 15 ans", "Peuvent figurer sur la fiche de l'adulte qui les accompagne")])
    c = f'''<div class="answer"><p><strong>En bref :</strong> en France, les hôtels, chambres d'hôtes, meublés de tourisme, campings et résidences de tourisme doivent faire remplir et signer une <strong>fiche individuelle de police</strong> par chaque client étranger dès son arrivée, <strong>y compris les ressortissants de l'Union européenne</strong>. La fiche indique notamment l'identité, la nationalité, le domicile, le téléphone, l'e-mail et les dates du séjour. Elle se conserve <strong>6 mois</strong> et n'est remise à la police ou à la gendarmerie que sur leur demande, éventuellement sous forme dématérialisée.</p></div>
<p class="small muted">Ce guide est informatif et ne constitue pas un conseil juridique. Il s'appuie sur les articles R814-1 à R814-3 du CESEDA, l'arrêté du 1er octobre 2015 et les fiches de service-public.gouv.fr et de la CNIL, consultés le 16 octobre 2026.</p>
<h2>Qui doit la remplir ?</h2>
<p>L'article R814-1 du CESEDA vise les hôteliers, les exploitants de villages et maisons familiales de vacances, de résidences et villages résidentiels de tourisme, les loueurs de meublés de tourisme et de <a href="{U("post-chdhotes")}">chambres d'hôtes</a> et les exploitants de terrains de camping et de caravanage. Ils doivent « remplir, ou faire remplir, et signer par l'étranger, dès son arrivée » la fiche. Les personnes qui louent des locaux nus ne sont pas concernées.</p>
<h2>Quels clients sont concernés ?</h2>
<p>Tout client qui n'a pas la nationalité française, y compris les ressortissants européens, selon service-public.gouv.fr. Cela vaut pour les loueurs professionnels comme non professionnels. Un client qui refuse de remplir la fiche peut se voir refuser l'hébergement.</p>
<h2>Quelles informations ?</h2>
<p>Le modèle de fiche est fixé par l'arrêté du 1er octobre 2015. L'article R814-2 liste notamment :</p>
{data}
<h2>Conservation et transmission</h2>
<ul><li><strong>Durée :</strong> les fiches se conservent pendant 6 mois (R814-3).</li>
<li><strong>Transmission :</strong> il n'y a pas d'envoi automatique ; les fiches sont remises aux services de police et unités de gendarmerie <strong>sur leur demande</strong>.</li>
<li><strong>Format :</strong> la transmission peut se faire sous forme dématérialisée, par exemple par e-mail.</li>
<li><strong>Données personnelles :</strong> la CNIL rappelle que le client doit être informé de son droit d'accès et de rectification, et que les données ne vont qu'aux services de police et de gendarmerie, pour les finalités prévues.</li></ul>
<p>Les textes parlent de « remplir et signer » sans préciser le support. Un formulaire en ligne peut aider à recueillir les informations à l'avance, mais vérifiez que vous pouvez produire la fiche signée demandée par les autorités.</p>
<h2>Sanctions</h2>
<p>Le CESEDA ne prévoit pas de sanction spécifique pour la fiche de police. Ce n'est pas une raison de la négliger : en cas de contrôle, vous devez pouvoir présenter les fiches des 6 derniers mois.</p>
<h2>À ne pas confondre</h2>
<ul><li><strong>Taxe de séjour :</strong> elle se collecte et se reverse à la commune ; c'est une obligation fiscale distincte.</li>
<li><strong>Déclaration des chambres d'hôtes en mairie :</strong> une démarche faite une fois, avant de commencer l'activité.</li></ul>
<h2>Comment Hostlio Pro peut vous aider (et ce qu'il ne fait pas)</h2>
<p>Avec le <a href="{U("checkin")}">check-in en ligne</a> de Hostlio Pro (forfaits Pro et Growth), le client remplit ses informations avant d'arriver et peut scanner son document avec son téléphone : la lecture se fait sur l'appareil et aucune image n'est conservée. Vous avez ainsi une partie des informations à l'avance et le client signe en ligne. Pour être clair : <strong>Hostlio Pro ne remplit pas la fiche de police à votre place, ne la conserve pas pour vous et ne la transmet pas</strong>. Vérifiez que les informations recueillies couvrent bien celles de la fiche, et gardez la fiche selon les règles ci-dessus.</p>
<div class="cta-row" style="margin-top:12px">{cta}</div>
'''
    lis = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(n)}</a></li>' for n, u in SRC)
    c += f'<h2>Sources</h2><p class="small muted">Toutes les sources ont été consultées le 16 octobre 2026.</p><ul>{lis}</ul>'
    faq = [("La fiche de police est-elle obligatoire pour les clients européens ?", "Oui. Selon service-public.gouv.fr, tout client qui n'a pas la nationalité française doit remplir la fiche, y compris les ressortissants de l'Union européenne."),
           ("Combien de temps faut-il conserver les fiches de police ?", "Six mois (CESEDA, R814-3). Elles sont remises à la police ou à la gendarmerie uniquement sur leur demande."),
           ("Faut-il envoyer les fiches de police à la police ?", "Non, pas systématiquement. Il n'y a pas de transmission automatique : vous les remettez sur demande des services de police ou de gendarmerie, éventuellement sous forme dématérialisée."),
           ("Les enfants doivent-ils avoir leur propre fiche ?", "Les données des enfants de moins de 15 ans peuvent figurer sur la fiche de l'adulte qui les accompagne (CESEDA, R814-2)."),
           ("Hostlio Pro remplit-il la fiche de police ?", "Non. Le check-in en ligne de Hostlio Pro recueille une partie des informations du client avant l'arrivée, mais la fiche, sa conservation et sa remise restent sous votre responsabilité.")]
    return c, faq

FN = {"fr": fr}
