"""Takvim yazısı (20 Ekim 2026 planı): "Quanto custa um sistema para hotel? Preços 2026" — yalnız PT (Brezilya).
Resmî siteler 13 Ekim 2026: Hospedin (a partir de R$ 59,90), Little Hotelier/SiteMinder (SiteMinder resmî fiyat akışı, Brezilya, USD,
vergi hariç), Stays, Smoobu, Beds24; HSystem/Desbravador/Omnibees/Cloudbeds teklifle. FNRH Digital: Portaria MTur 41/2025 + 4/2026,
MTur SSS'ye göre 20.04.2026'dan beri zorunlu. Hostlio FNRH'ye göndermez, NF-e kesmez — metin açık."""
import html

SRC = [
 ("Hospedin", "https://hospedin.com"),
 ("SiteMinder: preços (feed oficial de preços, região Brasil, USD)", "https://resources.siteminder.com/services/pricing/2022/data/products/index.php"),
 ("SiteMinder: pricing", "https://www.siteminder.com/pricing/"),
 ("Cloudbeds: preços", "https://www.cloudbeds.com/pt-br/pricing/"),
 ("Desbravador: hotéis e pousadas", "https://www.desbravador.com.br/produtos/hoteis-e-pousadas"),
 ("HSystem", "https://hsystem.com.br"),
 ("Omnibees: pousadas", "https://omnibees.com/segmento/pousadas/"),
 ("Stays: preços", "https://stays.net/precos/"),
 ("Smoobu: preços", "https://www.smoobu.com/pt/precos/"),
 ("Beds24: pricing", "https://beds24.com/en/pricing/pricing"),
 ("Ministério do Turismo: Portaria MTur nº 41/2025 (FNRH Digital)", "https://www.gov.br/turismo/pt-br/centrais-de-conteudo-/publicacoes/atos-normativos-2/2025/portaria-mtur-no-41-de-14-de-novembro-de-2025"),
 ("Ministério do Turismo: Portaria MTur nº 4/2026", "https://www.gov.br/turismo/pt-br/centrais-de-conteudo-/publicacoes/atos-normativos-2/2026/portaria-mtur-no-4-de-18-de-fevereiro-de-2026"),
 ("Ministério do Turismo: perguntas frequentes sobre a FNRH", "https://www.gov.br/turismo/pt-br/acesso-a-informacao/acoes-e-programas/programas-projetos-acoes-obras-e-atividades/ficha-nacional-de-registro-de-hospedes/faq"),
]

def _tbl(head, rows, hl=True):
    h = "".join(f'<th scope="col">{x}</th>' for x in head)
    b = "".join(("<tr class=\"hl\">" if hl and r[0] == "Hostlio Pro" else "<tr>") + f'<th scope="row">{r[0]}</th>'
                + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table class="cmp"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

META = {"pt": dict(key="post-costpt", date="2026-10-13", title="Quanto custa um sistema para hotel? Preços 2026",
                   desc="Preços 2026 de sistemas para hotel e pousada no Brasil: quem publica preço, custo para 10 e 25 quartos, implantação, fidelidade, câmbio e FNRH Digital.")}

def pt(U):
    from build import btn, SIGNUP_URL
    cta = btn("Teste grátis por ⟦trial⟧ dias", SIGNUP_URL) + btn("Ver planos", U("pricing"), "ghost")
    pub = _tbl(["Sistema", "O que é", "Preço publicado", "Observação"], [
        ("Hostlio Pro", "PMS + channel manager + assistente de IA", "⟦price:starter⟧ / ⟦price:pro⟧ / ⟦price:growth⟧ por mês (USD)", "Preço fixo, sem comissão por reserva"),
        ("Hospedin", "PMS em nuvem; channel manager e motor de reservas à parte", "A partir de R$ 59,90 por mês (PMS), conforme o número de UHs", "Taxa de implantação nos módulos extras; assinatura com 1 ano de fidelidade no cartão"),
        ("Little Hotelier", "PMS com channel manager", "Pro: US$ 155 (10 quartos), US$ 249 (até 30 quartos) por mês", "Feed oficial de preços da SiteMinder; impostos à parte"),
        ("SiteMinder", "Channel manager", "US$ 119 (10 quartos), US$ 169 (até 30 quartos) por mês", "Só channel manager; impostos à parte"),
        ("Stays", "Para aluguel por temporada", "R$ 79 a R$ 249 por mês + 1,7% a 2% por reserva", "Fidelidade inicial de 6 meses"),
        ("Beds24", "PMS + channel manager por uso", "A partir de 15,50 € por mês", "Cobrado em euros ou dólares"),
        ("Cloudbeds, Desbravador, HSystem, Omnibees", "Plataformas e módulos", "Sob consulta", "Peça o custo anual completo por escrito")])
    ex = _tbl(["Sistema", "10 quartos / mês", "25 quartos / mês", "Inclui"], [
        ("Hostlio Pro", "⟦price:starter⟧ (Starter)", "⟦price:pro⟧ (Pro)", "PMS, channel manager, app e IA"),
        ("Little Hotelier Pro", "US$ 155", "US$ 249", "PMS com channel manager"),
        ("SiteMinder", "US$ 119", "US$ 169", "Só channel manager")])
    c = f'''<div class="answer"><p><strong>Resposta curta:</strong> no Brasil, poucos sistemas para hotel publicam o preço. Entre os que publicam, o PMS da Hospedin começa em R$ 59,90 por mês (o valor sobe com o número de quartos), e sistemas internacionais como Little Hotelier e SiteMinder cobram em dólar: cerca de US$ 120 a 155 por mês para 10 quartos. A maioria dos fornecedores brasileiros trabalha sob consulta. Para comparar de verdade, some mensalidade, implantação, módulos (channel manager, motor de reservas), fidelidade, impostos e, no caso de cobrança em dólar, o câmbio.</p></div>
<p class="small muted">A Hostlio Pro é um dos produtos comparados, portanto não somos neutros. Usamos apenas informações publicadas nos sites oficiais dos fornecedores e do Ministério do Turismo, consultadas em 13 de outubro de 2026. Preços mudam: confirme sempre no site do fornecedor.</p>
<h2>Quanto custa a Hostlio Pro</h2>
<p>A Hostlio Pro tem três planos com preço fixo: Starter ⟦price:starter⟧ por mês (até ⟦rooms:starter⟧ quartos), Pro ⟦price:pro⟧ (até ⟦rooms:pro⟧) e Growth ⟦price:growth⟧ (até ⟦rooms:growth⟧ quartos e 2 propriedades), em dólares americanos. No pagamento anual há 20% de desconto. Não há comissão por reserva; channel manager, app e o assistente de IA, o Lio, estão incluídos em todos os planos. Teste grátis de ⟦trial⟧ dias.</p>
<div class="cta-row" style="margin-top:12px">{cta}</div>
<h2>Os modelos de preço</h2>
<ul><li><strong>Mensalidade fixa:</strong> o mesmo valor todo mês. É o mais fácil de prever.</li>
<li><strong>Por quarto (UH):</strong> o valor cresce com o número de quartos ou de unidades habitacionais.</li>
<li><strong>Mensalidade + porcentagem por reserva:</strong> comum em sistemas para aluguel por temporada; pesa justamente na alta temporada.</li>
<li><strong>Sob consulta:</strong> o preço vem depois de uma demonstração, conforme o seu hotel.</li></ul>
<h2>Preços publicados em 2026</h2>
{pub}
<h2>Exemplo: pousada de 10 e hotel de 25 quartos</h2>
<p>Mensalidade calculada a partir dos preços publicados. Os sistemas não incluem as mesmas funções: não decida só pelo valor.</p>
{ex}
<p class="small muted">Little Hotelier e SiteMinder: feed oficial de preços da SiteMinder para o Brasil, em dólares e sem impostos; para 25 quartos vale a faixa de até 30 quartos. A Hospedin não publica o valor por número de quartos.</p>
<h2>Custos que não aparecem na mensalidade</h2>
<ul><li><strong>Implantação:</strong> alguns fornecedores cobram uma taxa única para ativar módulos ou fazer a implantação.</li>
<li><strong>Fidelidade:</strong> contratos de 6 ou 12 meses limitam a troca de sistema; veja se a mensalidade sem fidelidade é diferente.</li>
<li><strong>Módulos:</strong> channel manager, motor de reservas e pagamentos podem ser vendidos à parte.</li>
<li><strong>Comissão por reserva:</strong> pequena em cada reserva, grande no fim da alta temporada.</li>
<li><strong>Câmbio e impostos:</strong> sistemas cobrados em dólar ou euro variam com o câmbio, e a compra no exterior pode ter IOF e outros tributos. Confirme com seu contador.</li>
<li><strong>Nota fiscal:</strong> verifique se o sistema emite NF-e ou NFS-e ou se isso fica com outro software.</li>
<li><strong>Comissões das OTAs:</strong> não dependem do sistema, mas costumam ser o maior custo. Veja o líquido por canal na <a href="{U("commission")}">calculadora de comissão de OTA</a>.</li></ul>
<h2>FNRH Digital: o que perguntar ao fornecedor</h2>
<p>Com a Portaria MTur nº 41, de 14 de novembro de 2025, a Ficha Nacional de Registro de Hóspedes passou a ser digital, e a Portaria nº 4, de 18 de fevereiro de 2026, adiou o início: segundo o Ministério do Turismo, a FNRH Digital é obrigatória desde 20 de abril de 2026. O sistema do governo é gratuito e exige Cadastur ativo; um PMS pode se conectar a ele com credenciais próprias, mas o custo dessa integração depende do fornecedor. Pergunte se o sistema envia a ficha automaticamente, se apenas exporta os dados ou se você vai preencher na plataforma do governo.</p>
<h2>Como escolher sem errar</h2>
<ol><li><strong>Some o custo anual completo:</strong> mensalidade, implantação, módulos, fidelidade, impostos e câmbio.</li>
<li><strong>Prefira preço fixo</strong> se a sua temporada é forte: comissões crescem nos melhores meses.</li>
<li><strong>Peça por escrito</strong> o valor anual a quem trabalha sob consulta.</li>
<li><strong>Teste com dados reais:</strong> seus quartos, suas tarifas e pelo menos uma OTA conectada.</li></ol>
<p>Os critérios de escolha estão em <a href="{U("post-pms")}">como escolher um sistema para hotel pequeno e pousada</a>.</p>
<h2>O que a Hostlio Pro não faz</h2>
<p>Para uma comparação honesta: a Hostlio Pro não envia dados à FNRH Digital (o <a href="{U("checkin")}">check-in online</a> coleta os dados do hóspede antes da chegada, mas o registro oficial fica com você), não emite NF-e ou NFS-e e não tem motor de reservas nem cobrança online. É cobrada em dólares. Se esses itens forem indispensáveis, considere um sistema brasileiro ou combine a Hostlio Pro com o seu software fiscal.</p>
'''
    lis = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(n)}</a></li>' for n, u in SRC)
    c += f'<h2>Fontes</h2><p class="small muted">Todas as fontes foram consultadas em 13 de outubro de 2026.</p><ul>{lis}</ul>'
    faq = [("Quanto custa um sistema para pousada?", "Entre os que publicam preço, o PMS da Hospedin começa em R$ 59,90 por mês e sobe com o número de quartos; sistemas internacionais como Little Hotelier cobram em dólar, cerca de US$ 155 por mês para 10 quartos (13 de outubro de 2026). Muitos fornecedores brasileiros trabalham sob consulta."),
           ("O channel manager está incluído no preço?", "Depende: na Hostlio Pro e no Little Hotelier está incluído; na Hospedin é um produto à parte; a SiteMinder é só channel manager."),
           ("A FNRH Digital é obrigatória?", "Sim. Segundo o Ministério do Turismo, a FNRH Digital é obrigatória desde 20 de abril de 2026 (Portarias MTur nº 41/2025 e nº 4/2026). A plataforma do governo é gratuita; a integração com o PMS depende do fornecedor."),
           ("Quanto custa a Hostlio Pro?", "Starter ⟦price:starter⟧, Pro ⟦price:pro⟧ e Growth ⟦price:growth⟧ por mês, em dólares; 20% de desconto no pagamento anual. Teste grátis de ⟦trial⟧ dias.")]
    return c, faq

FN = {"pt": pt}
