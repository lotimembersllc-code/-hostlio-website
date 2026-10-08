from build import btn, icon, logo, url, room_rack, channel_strip, faq_block, SIGNUP_URL, EMAIL, UPDATED, CHECK, software_schema, SITE, PLANS
L = "pt"
def U(k): return url(k, L)

MESES = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
def D(iso):
    y, m, d = iso[:10].split("-")
    return f"{int(d)} de {MESES[int(m)-1]} de {y}"

PLAN_TXT = {
 "starter": ("Para pousadas pequenas e hotéis boutique", ["1 propriedade, até 10 quartos","⟦quota:starter⟧ mensagens de IA / mês","Sincronização de reservas das OTAs (100+ canais)","Mensagens de IA no WhatsApp","Sugestões da Lio toda manhã","Calendário de reservas (mapa de reservas)","Formulários de visto em PDF automáticos"]),
 "pro":     ("Para hotéis de uma propriedade em crescimento", ["1 propriedade, até 50 quartos","⟦quota:pro⟧ mensagens de IA / mês","Tudo do Starter","WhatsApp + caixas de entrada das OTAs (Booking.com, Airbnb, Expedia)","A Lio recebe pedidos de reserva no WhatsApp (com sua aprovação)","Insights de IA sobre avaliações e mensagens","Check-in online com assinatura digital","Venda de transfers, passeios e extras","App móvel"]),
 "growth":  ("Para equipes que administram duas propriedades", ["Até 2 propriedades, 150 quartos no total","⟦quota:growth⟧ mensagens de IA / mês","Tudo do Pro","Resumo semanal com IA","Sincronização de canais prioritária","Suporte prioritário (próximo dia útil)","Chamada de onboarding personalizada","Opções white-label"]),
}

def plans_html():
    out = []
    for p in PLANS:
        for_, feats = PLAN_TXT[p["id"]]
        pop = p["id"] == "pro"
        lis = "".join(f"<li>{CHECK}<span>{f}</span></li>" for f in feats)
        out.append(f'''<article class="plan{" pop" if pop else ""}" aria-labelledby="plan-{p["id"]}">
{'<span class="tag">Mais popular</span>' if pop else ""}
<h3 id="plan-{p["id"]}">{p["name"]}</h3><p class="for">{for_}</p>
<div class="price num"><b data-price="{p["id"]}">⟦price:{p["id"]}⟧</b><span class="muted">/ mês</span></div>
<p class="small muted num" style="margin:0" data-eb>Preço de lançamento (normalmente <s data-regular="{p["id"]}">⟦regular:{p["id"]}⟧</s>)</p>
<ul>{lis}</ul>
{btn("Começar com o "+p["name"], SIGNUP_URL+"?plan="+p["id"], "primary" if pop else "ghost")}
</article>''')
    return '<div class="plans">' + "".join(out) + "</div>"

FAQ_CORE = [
 ("O que é o Hostlio Pro?", "O Hostlio Pro é um sistema para hotel (PMS hoteleiro) com inteligência artificial, feito para hotéis independentes, hotéis boutique e pousadas. Ele reúne em uma só plataforma a Lio, uma assistente de IA que responde às mensagens dos hóspedes 24 horas por dia em mais de 30 idiomas, um channel manager conectado a mais de 100 OTAs, um calendário de reservas com arrastar e soltar e o check-in online."),
 ("Quanto custa o Hostlio Pro?", "São três planos: Starter por ⟦price:starter⟧/mês, Pro por ⟦price:pro⟧/mês e Growth por ⟦price:growth⟧/mês. Esses preços incluem um desconto de lançamento de ⟦eb_pct⟧ para os primeiros 50 clientes, garantido enquanto a assinatura estiver ativa. Os preços normais são ⟦regular:starter⟧, ⟦regular:pro⟧ e ⟦regular:growth⟧."),
 ("Existe um período de teste grátis?", "Sim. Todos os planos incluem 7 dias de teste grátis. O cartão é cadastrado na inscrição, mas nada é cobrado até o fim do teste, e você pode cancelar antes disso. Não há contratos de longo prazo e você pode cancelar quando quiser."),
 ("Com quais OTAs o Hostlio Pro se conecta?", "Por meio da Channex, o Hostlio Pro se conecta a mais de 100 canais, entre eles Booking.com, Airbnb, Expedia, Agoda, Trip.com, Hotels.com, Hotelbeds, Hostelworld e Google Hotels. Disponibilidade, tarifas e reservas ficam sincronizadas em todos eles."),
 ("Em quais idiomas a Lio responde?", "A Lio responde em mais de 30 idiomas, incluindo inglês, turco, árabe, russo, alemão, japonês e chinês. Ela responde no idioma do hóspede, e você vê a tradução no seu painel."),
]

def home():
    import home_v3
    return home_v3.home(L, plans_html, FAQ_CORE)

def ai():
    body = f'''
<section class="page-hero"><div class="wrap split">
<div><h1>Lio, a assistente de IA para mensagens de hóspedes</h1>
<p class="lead">A Lio é uma assistente de IA treinada com as informações do seu hotel. Ela responde às mensagens dos hóspedes no WhatsApp e nas caixas de entrada das OTAs (Booking.com, Airbnb, Expedia) em mais de 30 idiomas, a qualquer hora.</p>
<div class="cta-row">{btn("Teste a Lio grátis por 7 dias", SIGNUP_URL)}</div></div>
<div class="panel typing"><p class="panel-title">WhatsApp, 02:47</p>
<div class="msg in" style="background:var(--bg)" lang="de">Hallo! Unser Flug landet um 1 Uhr. Können Sie uns abholen, und ist ein später Check-in möglich?</div>
<div class="msg out" lang="de">Natürlich! Unser Flughafentransfer kostet 35 € für bis zu 3 Gäste. Soll ich ihn für Ihre Ankunft um 1 Uhr buchen? Später Check-in ist kein Problem.<small lang="pt">Lio, alemão</small></div>
<p class="small muted" style="margin:10px 0 0">Pedido de transfer criado e repassado para a sua equipe.</p></div>
</div></section>

<section class="white rule"><div class="wrap">
<div class="answer"><p><strong>O que é uma assistente de IA para mensagens de hóspedes em hotéis?</strong> É um software que responde automaticamente às perguntas que os hóspedes fazem antes e depois da reserva, usando as informações do próprio hotel. A Lio repassa para a sua equipe as mensagens que não consegue responder ou que exigem uma decisão humana (pedidos de desconto, reclamações, pedidos especiais).</p></div>
<h2 style="margin-top:64px">O que a Lio faz</h2><div class="rows">
<div class="row"><h3>Uma só caixa de entrada</h3><div><p>Mensagens do WhatsApp e das OTAs (Booking.com, Airbnb, Expedia) chegam em uma única tela. A Lio vincula automaticamente cada hóspede à sua reserva.</p></div></div>
<div class="row"><h3>Mais de 30 idiomas, com tradução automática</h3><div><p>O hóspede escreve em japonês, a Lio responde em japonês e você lê a conversa no seu idioma. As respostas manuais também são traduzidas para o idioma do hóspede.</p></div></div>
<div class="row"><h3>Conhece o seu hotel</h3><div><p>Horários de check-in e check-out, estacionamento, política para pets, horário do café da manhã, transporte e características dos quartos. Cadastre uma vez e a Lio usa essas informações de forma consistente em todas as respostas.</p></div></div>
<div class="row"><h3>Uma assistente que vende</h3><div><p>A Lio não só responde perguntas: ela oferece transfers do aeroporto, city tours e serviços extras no momento certo e repassa o pedido para a sua equipe.</p></div></div>
<div class="row"><h3>Recebe pedidos de reserva</h3><div><p>Nos planos Pro e Growth, quando um hóspede pergunta por um quarto no WhatsApp, a Lio coleta as datas, o número de hóspedes e o quarto preferido e informa o preço com base nas suas tarifas e disponibilidade. O pedido chega para você e vira reserva quando você aprova.</p></div></div>
<div class="row"><h3>Sugestões toda manhã</h3><div><p>Toda manhã, as Sugestões da Lio apontam ajustes de preço, tarefas da operação (quartos aguardando limpeza, pedidos pendentes), configurações que faltam e oportunidades de receita. Nada muda sem sua aprovação, e as sugestões de preço ficam dentro dos limites que você define. Em todos os planos.</p></div></div>
<div class="row"><h3>Insights de avaliações e mensagens</h3><div><p>Nos planos Pro e Growth, a Lio resume os temas de reclamação e de elogio que se repetem nas avaliações e mensagens dos hóspedes. O resumo semanal com IA está incluído no Growth e é opcional no Pro.</p></div></div>
<div class="row"><h3>Você mantém o controle</h3><div><p>Nos primeiros dias, você pode aprovar as respostas da Lio antes do envio. Você decide quais assuntos a Lio resolve sozinha e quais ela repassa para você.</p></div></div>
</div></div></section>

<section><div class="wrap">
<div class="section-head"><h2>Cota de mensagens de IA por plano</h2><p>Uma mensagem é uma única resposta que a Lio envia a um hóspede.</p></div>
<div class="table-wrap"><table><thead><tr><th>Plano</th><th class="c">Mensagens de IA / mês</th><th>Canais de mensagens</th></tr></thead><tbody>
<tr><th>Starter</th><td class="c num">⟦quota:starter⟧</td><td>WhatsApp</td></tr>
<tr><th>Pro</th><td class="c num">⟦quota:pro⟧</td><td>WhatsApp + caixas de entrada das OTAs (Booking.com, Airbnb, Expedia)</td></tr>
<tr><th>Growth</th><td class="c num">⟦quota:growth⟧</td><td>WhatsApp + caixas de entrada das OTAs (Booking.com, Airbnb, Expedia)</td></tr>
</tbody></table></div>
</div></section>
'''
    faq = [
     ("E se a Lio der uma informação errada?", "A Lio usa apenas as informações do hotel e os dados de reserva que você fornece. Quando não tem certeza, ela repassa a mensagem para você em vez de adivinhar. Você também pode aprovar cada resposta antes do envio."),
     ("Ela também responde às mensagens do Booking.com e do Airbnb?", "Sim. Nos planos Pro e Growth, as mensagens das OTAs chegam à caixa de entrada da Lio e são respondidas da mesma forma."),
     ("A Lio consegue receber reservas?", "Sim, nos planos Pro e Growth e sempre com a sua aprovação. Quando um hóspede escreve no WhatsApp, a Lio pergunta as datas, o número de hóspedes e o quarto preferido, informa o preço com base nas suas tarifas e disponibilidade e repassa o pedido para você. Ele só vira reserva depois que você aprova; a Lio nunca confirma uma reserva sozinha. Pedidos de serviços extras, como transfers e passeios, funcionam do mesmo jeito."),
     ("O que acontece quando a cota de mensagens acaba?", "As mensagens continuam chegando e aparecem no seu painel; apenas as respostas automáticas ficam pausadas. Você pode migrar para um plano superior para aumentar a cota."),
     FAQ_CORE[4],
    ]
    return {"key":"ai","title":"IA para Mensagens de Hóspedes em 30+ Idiomas | Hostlio Pro",
            "desc":"A Lio, assistente de IA do Hostlio Pro, responde aos hóspedes 24h no WhatsApp, Booking.com, Airbnb e Expedia em 30+ idiomas e recebe pedidos de reserva.",
            "trail":[("Assistente de IA Lio", U("ai"))],"body":body,"faq":faq}

def channel():
    body = f'''
<section class="page-hero"><div class="wrap split">
<div><h1>Um channel manager para mais de 100 OTAs</h1>
<p class="lead">Gerencie disponibilidade, tarifas e reservas no Booking.com, Airbnb, Expedia, Agoda e em mais de 100 outros canais a partir de um único calendário. O Hostlio Pro sincroniza em tempo real e nos dois sentidos.</p>
<div class="cta-row">{btn("Comece o teste grátis de 7 dias", SIGNUP_URL)}</div></div>
<div class="panel"><p class="panel-title">Canais conectados</p><div class="chan-list">
<div><span>Booking.com</span><span class="pill">Sincronizado</span></div>
<div><span>Airbnb</span><span class="pill">Sincronizado</span></div>
<div><span>Expedia</span><span class="pill">Sincronizado</span></div>
<div><span>Agoda</span><span class="pill">Sincronizado</span></div>
<div><span>Google Hotels</span><span class="pill">Sincronizado</span></div>
</div></div>
</div></section>
<section class="white rule"><div class="wrap">
<div class="answer"><p><strong>O que é um channel manager?</strong> É um software que mantém a disponibilidade e as tarifas do hotel sincronizadas enquanto ele vende quartos em vários canais online ao mesmo tempo. Quando um quarto é vendido em um canal, ele é fechado imediatamente em todos os outros, evitando reservas duplicadas (overbooking).</p></div>
<h2 style="margin-top:64px">O que o channel manager faz</h2><div class="rows">
<div class="row"><h3>Sincronização bidirecional</h3><div><p>Novas reservas, alterações e cancelamentos entram automaticamente no mapa de reservas, e as mudanças que você faz no calendário vão para todos os canais.</p></div></div>
<div class="row"><h3>Tarifas e restrições</h3><div><p>Envie tarifas, estadias mínimas e fechamentos de venda por tipo de quarto para todos os canais a partir de uma única tela.</p></div></div>
<div class="row"><h3>Mapa de reservas com cores</h3><div><p>Veja rapidamente de qual canal veio cada reserva. Troque os quartos arrastando e soltando.</p></div></div>
<div class="row"><h3>Integrado às mensagens</h3><div><p>As mensagens dos hóspedes de reservas das OTAs chegam à caixa de entrada da Lio com o hóspede, o quarto e as datas ao lado de cada conversa.</p></div></div>
</div></div></section>
<section><div class="wrap"><div class="section-head"><h2>Principais canais compatíveis</h2><p>A lista segue a nossa rede de conexões certificadas. Sentiu falta de algum canal? Fale com a gente.</p></div>
<div class="table-wrap"><table><thead><tr><th>Canal</th><th>Tipo</th></tr></thead><tbody>
<tr><th>Booking.com</th><td>OTA</td></tr><tr><th>Airbnb</th><td>Aluguel por temporada</td></tr><tr><th>Expedia, Hotels.com</th><td>OTA</td></tr>
<tr><th>Agoda, Trip.com</th><td>OTA (foco na Ásia)</td></tr><tr><th>Hotelbeds</th><td>Atacadista (bedbank)</td></tr><tr><th>Hostelworld</th><td>Marketplace de hostels</td></tr><tr><th>Google Hotels</th><td>Metabuscador</td></tr>
</tbody></table></div></div></section>
'''
    faq = [FAQ_CORE[3],
     ("O channel manager está incluído em todos os planos?", "Sim. Starter, Pro e Growth incluem sincronização com mais de 100 OTAs. O Growth acrescenta sincronização prioritária."),
     ("É difícil trocar o meu channel manager atual?", "Não. Crie seus tipos de quarto no Hostlio Pro e mapeie suas contas das OTAs pela Channex. Nossa equipe de onboarding ajuda durante a migração."),
    ]
    return {"key":"channel","title":"Channel Manager para Hotel com 100+ OTAs | Hostlio Pro",
            "desc":"O channel manager do Hostlio Pro sincroniza disponibilidade e tarifas em tempo real com 100+ OTAs (Booking.com, Airbnb, Expedia, Agoda) sem overbooking.",
            "trail":[("Channel manager", U("channel"))],"body":body,"faq":faq}

def checkin():
    body = f'''
<section class="page-hero"><div class="wrap split">
<div><h1>Check&#8209;in online com assinatura digital</h1>
<p class="lead">Antes da chegada, os hóspedes escaneiam o documento com o celular, adicionam os acompanhantes e assinam. Nenhuma imagem do documento é armazenada. A entrega da chave leva poucos minutos.</p>
<div class="cta-row">{btn("Teste o Pro grátis por 7 dias", SIGNUP_URL+"?plan=pro")}</div></div>
<div class="panel"><p class="panel-title">Check-in online, quarto 202</p>
<div class="field"><span>Nome completo</span><div>Keiko Sato</div></div>
<div class="field"><span>Nacionalidade</span><div>Japão</div></div>
<div class="field"><span>Documento</span><div>Passaporte escaneado, sem imagem salva</div></div>
<div class="field"><span>Acompanhantes</span><div>1 hóspede adicionado</div></div>
<div class="field"><span>Assinatura</span><div class="sig">Assinatura digital recebida</div></div>
</div>
</div></section>
<section class="white rule"><div class="wrap">
<div class="answer"><p><strong>Como funciona o check-in online?</strong> O Hostlio Pro envia a quem fez a reserva um link pessoal, seguro e com prazo de validade. Por esse link, o hóspede escaneia com a câmera do celular a zona de leitura mecânica (MRZ) do passaporte ou da carteira de identidade. A leitura acontece no próprio navegador do hóspede e os dados são preenchidos automaticamente. Depois ele adiciona os acompanhantes e assina o formulário digitalmente. Na reserva ficam salvos apenas os dados extraídos e a assinatura; nenhuma imagem do documento é enviada ou armazenada.</p></div>
<h2 style="margin-top:64px">Recursos do check-in online</h2><div class="rows">
<div class="row"><h3>Link seguro</h3><div><p>Um link baseado em token, exclusivo de cada reserva. Ele abre apenas o formulário daquela reserva.</p></div></div>
<div class="row"><h3>Leitura do documento sem guardar imagens</h3><div><p>A zona de leitura mecânica do passaporte ou da carteira de identidade é lida no próprio aparelho do hóspede. Só ficam salvos nome, número do documento, nacionalidade, data de nascimento e validade, nunca uma foto do documento. Documentos sem zona de leitura mecânica são preenchidos à mão.</p></div></div>
<div class="row"><h3>Acompanhantes</h3><div><p>Todos que vão ficar no quarto são adicionados em um único formulário, e ninguém precisa digitar dados na recepção.</p></div></div>
<div class="row"><h3>Assinatura digital e consentimento</h3><div><p>Os hóspedes aceitam as regras da casa e o consentimento de dados assinando na tela. O registro assinado fica armazenado com a reserva.</p></div></div>
<div class="row"><h3>Privacidade desde a concepção</h3><div><p>Os dados dos hóspedes podem ser excluídos mediante solicitação, e o texto de consentimento faz parte do formulário.</p></div></div>
<div class="row"><h3>Exportação para registros oficiais</h3><div><p>Os dados coletados dos hóspedes podem ser exportados em um formato que você pode usar para as exigências locais de registro de hóspedes.</p></div></div>
</div></div></section>
<section class="dark on-dark"><div class="wrap"><div class="section-head"><h2>Três passos para o hóspede</h2></div>
<ol class="steps"><li><h3>Abrir o link</h3><p>Abrir o link pessoal recebido após a confirmação da reserva (enviado automaticamente por e-mail ou compartilhado pelo hotel).</p></li>
<li><h3>Escanear o documento</h3><p>Escanear o passaporte ou a identidade com o celular: os dados são preenchidos automaticamente e nenhuma imagem é guardada. Depois, informar os acompanhantes.</p></li>
<li><h3>Assinar</h3><p>Aceitar as regras da casa e assinar na tela. Na recepção, é só pegar a chave.</p></li></ol>
</div></section>
'''
    faq = [("Quais planos incluem o check-in online?", "O check-in online com assinatura digital está incluído nos planos Pro e Growth."),
           ("O hóspede precisa baixar um aplicativo?", "Não. O formulário de check-in abre no navegador; não é preciso baixar nenhum aplicativo."),
           ("E se o hóspede não preencher o link?", "Faça o check-in da forma habitual. A equipe também pode escanear o documento na recepção com o app do Hostlio Pro; a leitura é feita no aparelho e nenhuma imagem é guardada."),
           ("As fotos dos documentos ficam armazenadas?", "Não. A zona de leitura mecânica (MRZ) do documento é lida no celular do hóspede, ou no aparelho do hotel com o app do Hostlio Pro, e só ficam salvos os dados extraídos e a assinatura. Passaportes e documentos de identidade com MRZ podem ser escaneados; os demais são preenchidos à mão.")]
    return {"key":"checkin","title":"Check-in Online com Assinatura Digital | Hostlio Pro",
            "desc":"Check-in online do Hostlio Pro: o hóspede escaneia o documento (sem guardar imagens), adiciona acompanhantes e assina pelo celular. Sem fila na recepção.",
            "trail":[("Check-in online", U("checkin"))],"body":body,"faq":faq}

def features():
    body = f'''
<section class="page-hero"><div class="wrap split"><div><h1>Tudo o que o Hostlio Pro oferece</h1>
<p class="lead">Os módulos de que um hotel independente precisa no dia a dia: comunicação com hóspedes, distribuição, reservas, check-in e receita extra.</p></div><div class="hero-img"><img src="/assets/img/gen-team-desk.webp" alt="" width="1080" height="1350"></div></div></section>
<section class="white rule"><div class="wrap"><h2 class="sr-only">Módulos</h2><div class="rows">
<div class="row"><h3>Assistente de IA Lio</h3><div><p>Respostas aos hóspedes 24 horas por dia em mais de 30 idiomas. Mensagens do WhatsApp e das OTAs (Booking.com, Airbnb, Expedia) em uma só caixa de entrada.</p><a href="{U("ai")}">Saiba mais sobre a Lio</a></div></div>
<div class="row"><h3>Channel manager</h3><div><p>Sincronização de disponibilidade, tarifas e reservas com mais de 100 OTAs com conexões certificadas.</p><a href="{U("channel")}">Channel manager</a></div></div>
<div class="row"><h3>Mapa de reservas</h3><div><p>Calendário de reservas com arrastar e soltar. Trocas de quarto, prorrogações e bloqueios em um só gesto.</p></div></div>
<div class="row"><h3>Check-in online</h3><div><p>Link seguro, acompanhantes, leitura do documento (sem guardar imagens) e assinatura digital.</p><a href="{U("checkin")}">Check-in online</a></div></div>
<div class="row"><h3>Formulários de visto em PDF automáticos</h3><div><p>Gere cartas-convite e declarações de hospedagem do hotel para pedidos de visto a partir dos dados da reserva, com um clique.</p></div></div>
<div class="row"><h3>Venda de transfers e passeios</h3><div><p>A Lio sugere transfers do aeroporto e passeios durante a conversa e repassa o pedido para a sua equipe.</p></div></div>
<div class="row"><h3>Sugestões da Lio e insights de IA</h3><div><p>Toda manhã a Lio prepara sugestões sobre preços, operação (quartos aguardando limpeza, pedidos pendentes), configurações que faltam e oportunidades de receita. Nada muda sem sua aprovação, e as sugestões de preço respeitam os limites que você define. Nos planos Pro e Growth, ela também resume as reclamações e os elogios que se repetem em avaliações e mensagens.</p></div></div>
<div class="row"><h3>Relatórios e equipe</h3><div><p>Relatórios de ocupação, ADR, RevPAR e desempenho por canal, com relatório semanal e mensal por e-mail. Seis funções de equipe com permissões próprias e todas as notificações em um só lugar.</p></div></div>
<div class="row"><h3>App para celular</h3><div><p>Gerencie reservas, mensagens e check-ins fora do hotel com o app para iOS e Android. Ele continua funcionando offline e sincroniza quando você volta a ficar online.</p></div></div>
</div></div></section>
<section><div class="wrap"><div class="section-head"><h2>Funcionalidades por plano</h2></div>
<div class="table-wrap"><table><thead><tr><th>Funcionalidade</th><th class="c">Starter</th><th class="c">Pro</th><th class="c">Growth</th></tr></thead><tbody>
<tr><th>Propriedades</th><td class="c">1</td><td class="c">1</td><td class="c">2</td></tr>
<tr><th>Limite de quartos</th><td class="c num">10</td><td class="c num">50</td><td class="c num">150</td></tr>
<tr><th>Mensagens de IA / mês</th><td class="c num">⟦quota:starter⟧</td><td class="c num">⟦quota:pro⟧</td><td class="c num">⟦quota:growth⟧</td></tr>
<tr><th>Sincronização com mais de 100 OTAs</th><td class="c">Sim</td><td class="c">Sim</td><td class="c">Prioritária</td></tr>
<tr><th>Mensagens de IA no WhatsApp</th><td class="c">Sim</td><td class="c">Sim</td><td class="c">Sim</td></tr>
<tr><th>Sugestões da Lio toda manhã (nada muda sem sua aprovação)</th><td class="c">Sim</td><td class="c">Sim</td><td class="c">Sim</td></tr>
<tr><th>Pedidos de reserva e de serviços extras pela Lio no WhatsApp</th><td class="c">Não</td><td class="c">Sim</td><td class="c">Sim</td></tr>
<tr><th>Insights de IA sobre avaliações e mensagens de hóspedes</th><td class="c">Não</td><td class="c">Sim</td><td class="c">Sim</td></tr>
<tr><th>Resumo semanal com IA</th><td class="c">Não</td><td class="c">Opcional</td><td class="c">Sim</td></tr>
<tr><th>Caixas de entrada das OTAs (Booking.com, Airbnb, Expedia)</th><td class="c">Não</td><td class="c">Sim</td><td class="c">Sim</td></tr>
<tr><th>Calendário (mapa de reservas)</th><td class="c">Sim</td><td class="c">Sim</td><td class="c">Sim</td></tr>
<tr><th>Formulários de visto em PDF</th><td class="c">Sim</td><td class="c">Sim</td><td class="c">Sim</td></tr>
<tr><th>Check-in online e assinatura digital</th><td class="c">Não</td><td class="c">Sim</td><td class="c">Sim</td></tr>
<tr><th>Venda de transfers e passeios</th><td class="c">Não</td><td class="c">Sim</td><td class="c">Sim</td></tr>
<tr><th>App para iOS e Android</th><td class="c">Não</td><td class="c">Sim</td><td class="c">Sim</td></tr>
<tr><th>Suporte prioritário e chamada de onboarding</th><td class="c">Não</td><td class="c">Não</td><td class="c">Sim</td></tr>
<tr><th>White-label</th><td class="c">Não</td><td class="c">Não</td><td class="c">Sim</td></tr>
</tbody></table></div></div></section>
'''
    return {"key":"features","title":"Funcionalidades do Sistema para Hotel | Hostlio Pro",
            "desc":"Recursos do Hostlio Pro: assistente de IA, channel manager com 100+ OTAs, mapa de reservas, check-in online, vistos em PDF, venda de transfers e app.",
            "trail":[("Funcionalidades", U("features"))],"body":body,"faq":[FAQ_CORE[0], FAQ_CORE[3]]}

def pricing():
    body = f'''
<section class="page-hero"><div class="wrap"><h1>Preços do Hostlio Pro</h1>
<p class="lead">Uma mensalidade fixa. Sem comissão por reserva, sem taxa de implantação. Teste qualquer plano grátis por 7 dias.</p></div></section>
<section style="padding-top:0"><div class="wrap"><h2 class="sr-only">Planos</h2>
<span class="billing-note">⟦eb_pct⟧ de desconto para os primeiros 50 clientes, garantido para sempre</span>
{plans_html()}
<p class="small muted" style="margin-top:18px">Preços em dólares americanos, sem impostos. Última atualização: <time datetime="{UPDATED}">{D(UPDATED)}</time>.</p>
</div></section>
<section class="white rule"><div class="wrap">
<div class="section-head"><h2>Qual plano é ideal para você?</h2></div>
<div class="rows">
<div class="row"><h3>Starter</h3><div><p>Pousadas e hotéis boutique com até 10 quartos, que enviam menos de ⟦quota:starter⟧ respostas por mês e querem começar com sincronização de canais e respostas por IA.</p></div></div>
<div class="row"><h3>Pro</h3><div><p>Hotéis de 11 a 50 quartos que querem que a Lio cuide também das mensagens das OTAs, usar o check-in online e vender transfers e passeios.</p></div></div>
<div class="row"><h3>Growth</h3><div><p>Duas propriedades ou até 150 quartos, quando você precisa de suporte prioritário, onboarding personalizado e uso white-label.</p></div></div>
</div></div></section>
'''
    faq = [FAQ_CORE[1], FAQ_CORE[2],
      ("Vocês cobram comissão por reserva?", "Não. O Hostlio Pro é uma assinatura mensal fixa; não fica com nenhuma porcentagem do valor das reservas."),
      ("Existe opção de cobrança anual?", "Sim. As assinaturas são cobradas mensal ou anualmente de forma antecipada, e os planos anuais têm 20% de desconto (Termos de serviço, seção 3)."),
      ("Posso trocar de plano?", "Sim. Faça upgrade ou downgrade quando quiser; a mudança vale a partir do próximo período de cobrança."),
      ("Por quanto tempo vale o desconto de lançamento?", "Ele vale para os primeiros 50 clientes, e o seu preço fica garantido enquanto a sua assinatura continuar ativa.")]
    return {"key":"pricing","title":"Preços do Sistema para Hotel: desde ⟦price:starter⟧/mês | Hostlio Pro",
            "desc":"Preços do Hostlio Pro: Starter ⟦price:starter⟧, Pro ⟦price:pro⟧ e Growth ⟦price:growth⟧ por mês. Sem comissão nem taxa de implantação, 7 dias grátis. Compare os planos.",
            "trail":[("Preços", U("pricing"))],"body":body,"faq":faq,"schema":[software_schema(L, detailed=True)]}

FAQ_ALL = FAQ_CORE + [
 ("Para que tipos de hotel o Hostlio Pro foi feito?", "Para propriedades independentes de 1 a 150 quartos, como hotéis boutique, hotéis urbanos, pousadas, apart-hotéis e hostels."),
 ("Existe um app para celular?", "Sim. Os planos Pro e Growth incluem um app para iOS e Android. Ele funciona sem conexão com a internet e sincroniza os dados quando você volta a ficar online."),
 ("Como funciona o check-in online?", "Os hóspedes recebem um link pessoal e seguro, escaneiam o documento pelo celular (nenhuma imagem é guardada) e enviam, antes da chegada, os acompanhantes e a assinatura digital. Disponível nos planos Pro e Growth."),
 ("Para que serve o recurso de formulários de visto em PDF?", "Ele transforma automaticamente os dados da reserva em declarações de hospedagem e cartas-convite do hotel em PDF para hóspedes que precisam de visto."),
 ("Meus dados estão seguros?", "Os dados são transmitidos por conexões criptografadas, e os dados de cada hotel ficam isolados das outras propriedades com regras de acesso por linha. Os dados dos hóspedes podem ser excluídos mediante solicitação."),
 ("Quanto tempo leva a implantação?", "Sua conta fica pronta em minutos. A maioria dos hotéis conecta os canais no mesmo dia: cadastre os tipos de quarto e os quartos, autorize a conexão na extranet de cada OTA e mapeie os quartos. O plano Growth inclui uma chamada de onboarding personalizada."),
 ("Em quais idiomas o suporte é oferecido?", "O painel e o suporte estão disponíveis em inglês e turco. Fale com a gente em " + EMAIL + "."),
]

def faq_page():
    body = f'''<section class="page-hero"><div class="wrap"><h1>Perguntas frequentes</h1>
<p class="lead">As dúvidas mais comuns sobre as funcionalidades, os preços e a implantação do Hostlio Pro. Não encontrou sua resposta? <a href="{U("contact")}">Escreva para nós</a>.</p></div></section>
<section style="padding-top:0"><div class="wrap">{faq_block(FAQ_ALL, L, heading=False, wrap=False)}</div></section>'''
    return {"key":"faq","title":"Perguntas Frequentes sobre o Hostlio Pro",
            "desc":"Perguntas frequentes sobre o Hostlio Pro, sistema para hotel: preços, teste grátis, integração com OTAs, assistente de IA Lio, check-in online e segurança.",
            "trail":[("Perguntas frequentes", U("faq"))],"body":body,"faq":FAQ_ALL,"faq_inline":True,"page_type":"FAQPage"}

def about():
    body = f'''<section class="page-hero"><div class="wrap split"><div><h1>Por que criamos o Hostlio Pro</h1>
<p class="lead">Em hotéis pequenos, a recepção, as vendas e a comunicação com os hóspedes muitas vezes ficam nas costas de uma só pessoa. O Hostlio Pro existe para que essa pessoa não fique soterrada por mensagens à noite e por telas de canais durante o dia.</p></div><div class="hero-img"><img src="/assets/img/gen-shutters.webp" alt="" width="1080" height="1350"></div></div></section>
<section class="white rule"><div class="wrap split">
<div class="prose"><h2>O que fazemos</h2>
<p>O Hostlio Pro é um software de gestão hoteleira com inteligência artificial para hotéis independentes. Entregamos a comunicação com os hóspedes à nossa assistente de IA Lio, reunimos a distribuição nas OTAs em um único calendário com conexões certificadas e levamos o check-in para o celular do hóspede.</p>
<h2>Como trabalhamos</h2>
<ul><li>Publicamos nossos preços abertamente e não cobramos comissão.</li><li>Desenvolvemos a partir do trabalho real do dia a dia dos hoteleiros.</li><li>Sem contratos longos; os clientes ficam porque estão satisfeitos.</li></ul></div>
<div class="panel"><p class="panel-title">Dados da empresa</p><dl class="list-kv">
<dt>Produto</dt><dd>Hostlio Pro (Hostlio)</dd><dt>Empresa</dt><dd>Loti Members LLC</dd>
<dt>Endereço</dt><dd>2108 N ST STE N, Sacramento, CA 95816, USA</dd><dt>E-mail</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
<dt>Clientes</dt><dd>Hotéis independentes em mais de 20 países</dd></dl></div>
</div></section>'''
    return {"key":"about","title":"Sobre o Hostlio Pro | Sistema para Hotel com IA","desc":"O Hostlio Pro desenvolve software de gestão hoteleira com IA para hotéis independentes. Operado pela Loti Members LLC e usado em mais de 20 países.",
            "trail":[("Sobre nós", U("about"))],"body":body,"page_type":"AboutPage"}

def contact():
    from build import FORM_ENDPOINT
    act = f' action="{FORM_ENDPOINT}" method="post"' if FORM_ENDPOINT else ""
    body = f'''<section class="page-hero"><div class="wrap split" style="align-items:start">
<div><h1>Agende uma demonstração ou fale com a gente</h1>
<p class="lead">Conte um pouco sobre o seu hotel e os canais que você usa, e mostramos o Hostlio Pro com os seus próprios quartos em uma chamada de 30 minutos.</p>
<p>Ou envie um e-mail direto: <a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
<form class="contact" data-contact-form data-mail="{EMAIL}" data-subject="Pedido de demonstração" data-sent="Seu aplicativo de e-mail foi aberto. Clique em enviar e o seu pedido chegará até nós."{act}>
<label>Nome completo<input name="name" autocomplete="name" required></label>
<label>E-mail<input type="email" name="email" autocomplete="email" required></label>
<label>Nome do hotel<input name="hotel" autocomplete="organization" required></label>
<label>Número de quartos<select name="rooms"><option>1–10</option><option>11–50</option><option>51–150</option><option>150+</option></select></label>
<label>País / cidade<input name="country" autocomplete="country-name"></label>
<label>Mensagem <span class="hint">Canais que você usa, sistema atual</span><textarea name="message" rows="4"></textarea></label>
<button class="btn btn-primary" type="submit">Enviar pedido de demonstração</button>
<p class="form-status" role="status" aria-live="polite"></p>
</form></div></section>'''
    return {"key":"contact","title":"Contato e Demonstração | Hostlio Pro","desc":"Fale com a equipe do Hostlio Pro ou agende uma demo grátis de 30 minutos adaptada ao seu hotel. Suporte em inglês e turco, e-mail: " + EMAIL,
            "trail":[("Contato", U("contact"))],"body":body,"page_type":"ContactPage","no_final":True}

POSTS = [
 {"key":"post-overbooking","title":"Como evitar overbooking: 6 passos para hotéis","date":"2026-09-21","desc":"Por que acontece overbooking em hotéis e como evitar: channel manager, regras de fechamento de vendas, margens de disponibilidade e o que fazer quando acontece mesmo assim."},
 {"key":"post-autoreply","title":"Como responder automaticamente às mensagens do Booking.com","date":"2026-09-21","desc":"Três formas de automatizar as mensagens dos hóspedes do Booking.com: modelos, mensagens programadas e uma assistente de IA."},
 {"key":"post-ai","title":"Como responder às mensagens de hóspedes com IA: guia prático","date":"2026-09-18",
  "desc":"Benefícios, riscos e como configurar a IA para responder às mensagens dos hóspedes do hotel. Quais perguntas automatizar e quais deixar com a sua equipe."},
 {"key":"post-pms","title":"Como escolher um sistema para hotel pequeno","date":"2026-09-10",
  "desc":"7 critérios para escolher o PMS de um hotel pequeno ou boutique: channel manager, modelo de preços, mensagens com hóspedes, acesso pelo celular e mais."},
]

def blog():
    items = "".join(f'<article><h2><a href="{U(p["key"])}">{p["title"]}</a></h2><p class="meta"><time datetime="{p["date"]}">{D(p["date"])}</time></p><p>{p["desc"]}</p></article>' for p in POSTS)
    body = f'<section class="page-hero"><div class="wrap"><h1>Blog para hoteleiros</h1><p class="lead">Conteúdo prático sobre a gestão de um hotel independente, distribuição e comunicação com hóspedes.</p></div></section><section style="padding-top:0"><div class="wrap post-list">{items}</div></section>'
    return {"key":"blog","title":"Blog: Guias para Hotéis Independentes | Hostlio Pro","desc":"Guias práticos para hoteleiros independentes sobre gestão hoteleira, channel manager, distribuição nas OTAs e comunicação com hóspedes usando IA.",
            "trail":[("Blog", U("blog"))],"body":body,"page_type":"CollectionPage"}

COVERS={"post-ai":("gen-checkin-phone",1080,1350),"post-pms":("gen-owner-laptop",1080,1350),"post-overbooking":("gen-reception",1080,1350),"post-autoreply":("gen-night-desk",1080,1350)}
def article(meta, content, faq=None):
    art = {"@type":"BlogPosting","headline":meta["title"],"description":meta["desc"],"datePublished":meta["date"],"inLanguage":L,"author":{"@type":"Organization","name":"Equipe de produto do Hostlio Pro","url":SITE+U("about")},"dateModified":UPDATED,"publisher":{"@id":SITE+"/#org"},
           "mainEntityOfPage":SITE+U(meta["key"]),"image":SITE+"/assets/img/"+COVERS[meta["key"]][0]+".webp"}
    body = f'<article><section class="page-hero"><div class="wrap"><h1 style="max-width:22ch">{meta["title"]}</h1><p class="meta">Pela <a href="{U("about")}">equipe de produto do Hostlio Pro</a>, as pessoas que desenvolvem o Hostlio Pro. Publicado em <time datetime="{meta["date"]}">{D(meta["date"])}</time>, atualizado em <time datetime="{UPDATED}">{D(UPDATED)}</time></p></div></section><section style="padding-top:0"><div class="wrap"><figure class="post-cover"><img src="/assets/img/{COVERS[meta["key"]][0]}.webp" alt="" width="{COVERS[meta["key"]][1]}" height="{COVERS[meta["key"]][2]}"></figure><div class="prose">{content}</div></div></section></article>'
    return {"key":meta["key"],"title":meta["title"],"desc":meta["desc"],"og_type":"article",
            "trail":[("Blog",U("blog")),(meta["title"],U(meta["key"]))],"body":body,"schema":[art],"faq":faq or []}

def post_ai():
    c = f'''
<div class="answer"><p><strong>Resposta curta:</strong> A maioria das mensagens que um hotel recebe são perguntas repetidas (horário de check-in, estacionamento, transfers, café da manhã). Ao entregá-las a uma assistente de IA treinada com as informações do próprio hotel, os hóspedes recebem resposta em segundos, no idioma deles. Descontos, reclamações e pedidos especiais devem continuar com a sua equipe.</p></div>
<h2>Quais são as perguntas mais comuns nos hotéis?</h2>
<p>Em hotéis independentes, a maioria das mensagens gira em torno de poucos assuntos:</p>
<ul><li>Horários de check-in e check-out, chegada antecipada ou saída tardia</li><li>Transfers do aeroporto e como chegar</li><li>Estacionamento, café da manhã, política para pets</li><li>Guarda-volumes, características dos quartos, a região</li><li>Alterações de reserva e pedidos de nota fiscal</li></ul>
<p>As respostas já existem no hotel. O problema é dá-las no idioma certo e na hora certa.</p>
<h2>O que a IA deve automatizar e o que não deve?</h2>
<p>Em uma boa configuração, a assistente resolve as perguntas de informação e repassa as decisões para a equipe.</p>
<div class="table-wrap"><table><thead><tr><th>Deixe a IA responder</th><th>Repasse para a equipe</th></tr></thead><tbody>
<tr><td>Horários, regras, comodidades</td><td>Descontos e negociação de preço</td></tr><tr><td>Como chegar, informações de transfer</td><td>Reclamações e compensações</td></tr><tr><td>Venda de transfers e passeios</td><td>Situações médicas ou de segurança</td></tr><tr><td>Lembrar os hóspedes dos detalhes da reserva</td><td>Pedidos de grupos e eventos</td></tr></tbody></table></div>
<h2>Configuração passo a passo</h2>
<ol><li><strong>Escreva a base de conhecimento do hotel.</strong> Horários, regras, comodidades e perguntas frequentes. Quanto mais clara, mais consistentes as respostas.</li>
<li><strong>Conecte os seus canais.</strong> Reúna as mensagens do WhatsApp e das OTAs (Booking.com, Airbnb, Expedia) em uma só caixa de entrada.</li>
<li><strong>Comece no modo de aprovação.</strong> Na primeira semana, leia e corrija as respostas antes do envio.</li>
<li><strong>Defina regras de repasse.</strong> Determine quais assuntos chegam até você.</li>
<li><strong>Passe para o modo automático.</strong> Quando as respostas estiverem consistentes, deixe a assistente cuidar totalmente das perguntas de informação.</li></ol>
<h2>Por que respostas em vários idiomas importam</h2>
<p>Hóspedes que escrevem no próprio idioma compartilham mais detalhes e confiam mais na resposta. Uma assistente que responde em mais de 30 idiomas cria essa confiança mesmo quando ninguém na recepção fala o idioma, e você continua lendo a conversa no seu.</p>
<h2>Como funciona no Hostlio Pro</h2>
<p>A assistente de IA do Hostlio Pro, a <a href="{U("ai")}">Lio</a>, usa as informações do seu hotel e os dados das reservas para responder a mensagens do WhatsApp e das OTAs (Booking.com, Airbnb, Expedia) em mais de 30 idiomas. Os planos incluem de ⟦quota:starter⟧ a ⟦quota:growth⟧ mensagens de IA por mês; veja os detalhes na <a href="{U("pricing")}">página de preços</a>.</p>'''
    faq = [("A IA pode dar informações erradas aos hóspedes?", "O risco é mínimo quando a assistente trabalha apenas com as informações fornecidas pelo hotel e repassa as perguntas duvidosas para a equipe. Recomenda-se começar no modo de aprovação."),
           ("Os hóspedes vão saber que estão falando com uma IA?", "As respostas são escritas em nome do hotel e no tom dele. Por transparência, o hotel pode informar na mensagem de boas-vindas que a assistente é uma IA.")]
    return article(next(p for p in POSTS if p["key"]=="post-ai"), c, faq)

def post_pms():
    c = f'''
<div class="answer"><p><strong>Resposta curta:</strong> O sistema para hotel (PMS) certo para um hotel pequeno tem channel manager integrado, preço fixo e transparente, uma só caixa de entrada para as mensagens dos hóspedes, acesso pelo celular e implantação no mesmo dia. Sistemas corporativos com centenas de funções costumam ficar subutilizados por equipes pequenas.</p></div>
<h2>1. Channel manager integrado</h2>
<p>Se você vende no Booking.com, Airbnb e Expedia ao mesmo tempo, a disponibilidade precisa ser sincronizada na hora. Um channel manager separado significa custo extra e mais uma tela. Verificar se o PMS inclui um e a quantos canais ele se conecta é a primeira coisa a fazer.</p>
<h2>2. Modelo de preços</h2>
<p>Alguns sistemas cobram uma porcentagem do valor das reservas além da mensalidade, e o custo sobe junto com a ocupação. Um preço mensal fixo deixa o seu orçamento previsível. Com fornecedores que não publicam os preços, espere passar por um processo de vendas.</p>
<h2>3. Comunicação com hóspedes</h2>
<p>Quando as mensagens ficam espalhadas entre o WhatsApp e as caixas de entrada das OTAs, o tempo de resposta piora. Uma só caixa de entrada com respostas automáticas é o que mais economiza tempo para equipes pequenas.</p>
<h2>4. Um mapa de reservas prático</h2>
<p>O calendário de reservas é a tela que a recepção mais olha. Trocar quartos arrastando e soltando e ver de relance o canal de cada reserva agilizam o trabalho do dia a dia.</p>
<h2>5. Acesso pelo celular</h2>
<p>Muitas vezes o proprietário não está no hotel. Um app para celular, principalmente um que funcione durante quedas de internet, é uma necessidade real.</p>
<h2>6. Check-in online</h2>
<p>Coletar os dados dos hóspedes antes da chegada economiza tempo na recepção e simplifica as exigências de registro de hóspedes.</p>
<h2>7. Implantação e suporte</h2>
<p>Um hotel pequeno não aguenta um projeto de implantação de semanas. Escolha um sistema que você possa usar no mesmo dia, com suporte no seu idioma, e faça o teste com reservas reais.</p>
<h2>Checklist</h2>
<div class="table-wrap"><table><thead><tr><th>Critério</th><th>Pergunta a fazer</th></tr></thead><tbody>
<tr><td>Channel manager</td><td>Está incluído e a quantos canais se conecta?</td></tr><tr><td>Preços</td><td>O preço é fixo, há comissão, o valor é público?</td></tr>
<tr><td>Mensagens</td><td>As mensagens de WhatsApp e das OTAs ficam em um só lugar, com respostas automáticas?</td></tr><tr><td>Celular</td><td>Existe um app e ele funciona offline?</td></tr>
<tr><td>Check-in</td><td>Há check-in online com assinatura digital?</td></tr><tr><td>Teste</td><td>Há teste grátis e cancelamento sem fidelidade?</td></tr></tbody></table></div>
<p>O Hostlio Pro foi criado com base nesses critérios: veja as <a href="{U("features")}">funcionalidades</a> e os <a href="{U("pricing")}">preços</a>.</p>'''
    faq = [("Um hotel pequeno precisa de um PMS?", "Se você vende em várias OTAs e recebe dezenas de mensagens por dia, sim. Trabalhar com planilhas e extranets separadas das OTAs aumenta o risco de overbooking e de respostas lentas."),
           ("Qual é a diferença entre um PMS e um channel manager?", "Um PMS administra as operações internas do hotel (reservas, quartos, hóspedes); um channel manager distribui disponibilidade e tarifas para as OTAs. Sistemas como o Hostlio Pro reúnem os dois em uma só plataforma.")]
    return article(next(p for p in POSTS if p["key"]=="post-pms"), c, faq)

def pages():
    import pages_v4
    return [home(), ai(), channel(), checkin(), features(), pricing(), faq_page(), about(), contact(), blog(), post_ai(), post_pms()] + pages_v4.pages(L, article) + __import__("legal_v5").pages(L, article)
