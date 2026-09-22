"""Brazilian Portuguese (pt) data for the shared modules (build, home_v3, pages_v4, legal_v5).
Pure data + functions; no project imports. Links come from the U callable passed in."""

L = "pt"
UPDATED_TXT = "21 de setembro de 2026"
LEGAL_DATE_TXT = "20 de abril de 2026"

# ------------------------------------------------------------------ build.UI
UI = {
   "nav": [("features","Funcionalidades"),("ai","Assistente de IA Lio"),("channel","Channel manager"),("pricing","Preços"),("blog","Blog")],
   "top": [("pricing","Preços"),("blog","Blog"),("faq","Perguntas frequentes"),("about","Sobre nós")],
   "login":"Entrar", "trial":"Teste grátis", "demo":"Agendar demonstração", "menu":"Abrir menu",
   "skip":"Pular para o conteúdo", "home":"Início",
   "lang_label":"Idioma", "crumb_label":"Trilha de navegação",
   "foot_tag":"Sistema para hotel com inteligência artificial para hotéis independentes. Mensagens de hóspedes, gestão de canais e calendário de reservas em um só lugar.",
   "foot_product":"Produto","foot_company":"Empresa","foot_res":"Recursos","foot_sol":"Soluções","privacy":"Política de privacidade","terms":"Termos de serviço","delacc":"Excluir conta",
   "sol":["Sistema para hotel boutique","Sistema para pousadas","Sistema para apart-hotel","Sistema para hostels","Comparativo de sistemas para hotel"],
   "foot_about":"Sobre nós","foot_contact":"Contato","foot_faq":"Perguntas frequentes",
   "rights":"Todos os direitos reservados.","updated":"Última atualização",
   "final_h":"Mantenha sua recepção aberta esta noite também.",
   "final_p":"Teste grátis por 7 dias. Nada é cobrado até o fim do teste, cancele quando quiser.",
   "faq_h":"Perguntas frequentes",
}

# ------------------------------------------------------------------ build.MEGA
MEGA = {"btn":"Produto","cols":[
   ("Hóspedes",[("ai","sparkle","Assistente de IA Lio","Respostas 24/7 aos hóspedes em 30+ idiomas"),("checkin","identification-card","Check-in online","Documento, acompanhantes e assinatura digital")]),
   ("Distribuição",[("channel","arrows-left-right","Channel manager","100+ OTAs em um só calendário"),("features","calendar-dots","Mapa de reservas","Calendário de reservas com arrastar e soltar")]),
   ("Operação",[("features","van","Transfers e passeios","Receita extra enquanto você conversa"),("features","device-mobile","App móvel","iOS que funciona até off-line")]),
   ("Por tipo de hospedagem",[("t-boutique","sparkle","Hotéis boutique","Hotéis de 10 a 50 quartos"),("t-guesthouse","users-three","Pousadas","Hospedagens de 1 a 10 quartos"),("t-apart","calendar-dots","Apart-hotéis","Apartamentos e suítes"),("t-hostel","globe-simple","Hostels","Venda por cama")]),
  ],"feat":("pricing","Compare os planos","A partir de US$ 49 por mês, 7 dias grátis")}

# ------------------------------------------------------------------ build.software_schema / room_rack / 404
SOFT_DESC = "Sistema para hotel com inteligência artificial para hotéis independentes: mensagens com hóspedes 24/7 em 30+ idiomas, channel manager com 100+ OTAs, calendário de reservas e check-in online."
SOFT_FEATURES = ["Assistente de IA Lio para hóspedes (30+ idiomas)", "Channel manager (100+ OTAs via Channex)", "Calendário de reservas com arrastar e soltar", "Check-in online com assinatura digital", "Formulários de visto em PDF automáticos", "Venda de transfers e passeios", "App móvel que funciona off-line"]
DAYS = ["Seg","Ter","Qua","Qui","Sex","Sáb","Dom"]
RACK = ("Mapa de reservas", "Setembro, semana 3", "Reservas com cores por canal: Booking.com em azul, Airbnb em pêssego, Expedia em lilás, Agoda em areia, diretas em verde")
NOTFOUND = ("Página não encontrada | Hostlio Pro",
            "A página que você procura pode ter sido movida ou removida. Volte para a página inicial do Hostlio Pro e encontre o que precisa.",
            "Esta página não foi encontrada",
            'O endereço pode ter mudado. <a href="{home}">Volte para a página inicial</a>.')

# ------------------------------------------------------------------ home_v3.T
HOME = dict(
  title="Sistema para Hotel com IA e Channel Manager | Hostlio Pro",
  desc="Sistema para hotel Hostlio Pro: o assistente de IA Lio responde aos hóspedes 24/7 em 30+ idiomas e o channel manager sincroniza 100+ OTAs. Teste 7 dias grátis.",
  h1='Enquanto seu hotel dorme, <em class="hl">Lio</em> responde',
  lead="Sistema para hotel com inteligência artificial para hotéis independentes e pousadas. Reservas, 100+ canais e mensagens de hóspedes em um só lugar, em 30+ idiomas.",
  try_="Teste grátis", demo="Agendar demonstração", via="Conectado via Channex:", more="e mais 100+",
  coll_alt1="Pátio de hotel boutique com buganvílias e piscina ao pôr do sol", coll_alt2="Dono de hotel sorridente segurando uma xícara de café",
  chip1=("Quarto 202 vendido","Booking.com, 21:40"), chip2="Fechado no Airbnb e na Expedia",
  bub_h=("Lio","Recepcionista de IA, online"), bub_in="Hallo! Ist ein später Check-in möglich?", bub_out="Natürlich! Unsere Rezeption ist rund um die Uhr besetzt.", bub_note="Respondido em alemão, 4 s",
  pick_h="Por onde você quer começar?", pick_p="Escolha o que importa e preparamos sua conta com base nisso.", pick_none="Escolha quantos quiser.", pick_some="{n} selecionados, teste grátis por 7 dias.", pick_btn="Começar", pick_name="interest",
  tiles=[("ai","sparkle","t-peach","Assistente de IA Lio","Respostas aos hóspedes em 30+ idiomas"),("channel","arrows-left-right","t-lilac","Channel manager","Sincronização em tempo real com 100+ OTAs"),("rack","calendar-dots","t-sand","Mapa de reservas","Calendário de reservas com arrastar e soltar"),("checkin","identification-card","t-peach","Check-in online","Documento e assinatura antes da chegada"),("upsell","van","t-lilac","Transfers e passeios","Receita extra enquanto você conversa"),("mobile","device-mobile","t-sand","App móvel","Gerencie o hotel de qualquer lugar")],
  story_h='<em class="hl">2h14 da madrugada</em>, um hóspede está escrevendo',
  story_p="O que acontece enquanto você dorme, em três quadros.",
  story=[("brand-night","Dono de hotel dormindo, com o celular acendendo no criado-mudo","02:14","Um hóspede envia uma mensagem","Um hóspede da Alemanha pergunta sobre check-in tardio. Você está em sono profundo."),
         ("brand-phone","Mão segurando um celular com a tela laranja de resposta do Lio","02:14","Lio responde na hora","Com as informações do seu hotel, no idioma do próprio hóspede. Se for preciso, deixa um recado para você."),
         ("brand-hotelier","Dono de hotel atravessando o lobby com o café da manhã","08:30","De manhã, tudo resolvido","A conversa espera por você no painel, já traduzida. Hóspede satisfeito e você descansado.")],
  story_chip="Lio respondeu",
  tour_h='Gerencie o dia do seu hotel <em class="hl">em uma só tela</em>', tour_p="Mensagens de hóspedes, reservas, canais e check-in funcionam juntos.", tour_label="Tour pelo produto",
  tabs=["Mensagens","Calendário","Canais","Check-in"],
  st=[("Todas as mensagens de hóspedes em uma só caixa de entrada","WhatsApp e as caixas de entrada das OTAs (Booking.com, Airbnb, Expedia) juntos. Lio responde com as informações do seu hotel, e você só vê o que realmente precisa de você.",["Respostas automáticas em 30+ idiomas","Dados da reserva ao lado de cada mensagem","Repassa a você o que não tem certeza"],"ai","Como o Lio funciona"),
      ("A semana inteira no mapa de reservas","Veja cada reserva na cor do seu canal. Trocar de quarto, estender a estadia ou bloquear datas exige um único gesto.",["Troca de quarto com arrastar e soltar","Reservas com cores por canal","O mesmo calendário na web e no iOS"],"features","Todas as funcionalidades"),
      ("100+ canais, uma só disponibilidade","Sincronização bidirecional via Channex. Um quarto vendido em um canal fecha nos outros na hora.",["Tarifas e restrições em uma só tela","Novas reservas e cancelamentos entram sozinhos","Sem risco de overbooking"],"channel","Channel manager"),
      ("O check-in fica pronto antes da chegada","O hóspede envia os dados do documento, os acompanhantes e a assinatura pelo celular, por meio de um link seguro.",["No navegador, sem baixar app","Acompanhantes em um único formulário","Assinatura digital e consentimento"],"checkin","Check-in online")],
  inbox_top=("Caixa de entrada","12 conversas abertas"), inbox_note="Tradução: o check-in é a partir das 14h, podemos guardar sua bagagem.",
  chan_top=("Canais conectados","Última sincronização: agora mesmo"), sync="Sincronizado",
  ci_top=("Check-in online","Quarto 202"), ci_f=[("Nome completo","Keiko Sato"),("Nacionalidade","Japão"),("Acompanhantes","1 hóspede adicionado")], ci_sig="Assinatura",
  bento_h='<em class="hl">Tudo</em> o que um hotel precisa', bento_p="Todos os módulos estão conectados: nada de ferramentas separadas nem de senhas separadas.",
  b_lio=("Assistente de IA Lio","Resolve a maioria das dúvidas dos hóspedes antes mesmo de você vê-las e resume o restante.","Is breakfast included?","Yes, from 7:30 to 10:30 on the terrace."),
  b_chan=("Channel manager","100+ canais de venda via Channex, uma só disponibilidade."),
  b_rack=("Mapa de reservas","Calendário de reservas com arrastar e soltar."),
  b_ci=("Check-in online","Documento, acompanhantes e assinatura digital antes da chegada."),
  b_pdf=("Formulários de visto em PDF","Cartas de hospedagem e de convite com um clique.","Carta de hospedagem","PDF"),
  b_tr=("Venda de transfers e passeios","Lio oferece no momento certo; você fatura mais.","Transfer do aeroporto","+35 €"),
  b_lang=("30+ idiomas","No idioma em que o hóspede escrever, nesse idioma vem a resposta."),
  b_mob=("App móvel","Reservas, mensagens e check-ins no iOS, até off-line."),
  types_h='Feito para <em class="hl">todo tipo de hospedagem</em>', types_p="Pensado para hospedagens independentes de 10 a 150 quartos.",
  types=[("brand-courtyard","Pátio de hotel boutique com piscina e buganvílias","Hotel boutique","10–50 quartos","Muitos hóspedes estrangeiros, cada mensagem pessoal."),
         ("hostlio-lobby","Lobby com painéis de madeira e área de convivência","Hostel","Camas e quartos","Viajantes de vários idiomas, caixas de entrada cheias."),
         ("hostlio-phone","Quarto aconchegante de pousada com luminária de mesa","Pousada","1–10 quartos","Um turno da noite para uma equipe de uma pessoa só."),
         ("hostlio-room","Apartamento claro com roupa de cama branca","Apart-hotel","10–40 unidades","Check-in online para uma chegada sem chaves.")],
  plans_h="Um plano para o tamanho do seu hotel", plans_p="Mensalidade fixa, sem contrato de longo prazo. Todos os planos são grátis por 7 dias.",
  early="20% de desconto para os 50 primeiros clientes, garantido para sempre", tax='Preços sem impostos. <a href="{p}">Compare os planos em detalhes</a>.',
  ai_h='Lio, o <em class="hl">turno da noite</em> da sua recepção', ai_p="Um assistente de IA que trabalha com as informações do seu hotel. Responde aos hóspedes, vende extras e deixa o restante com você.",
  ai_wide=("Respostas no idioma do hóspede","Uma pergunta em japonês recebe resposta em japonês; uma em árabe, resposta em árabe. Você lê a conversa no seu idioma."),
  ai_cards=[("van","Vende por você","Oferece transfers do aeroporto e passeios no momento certo e vincula o pedido à reserva."),("hand-arrow-up","Sabe quando repassar","Mensagens que exigem uma decisão, como descontos, reclamações ou pedidos especiais, vão para a sua equipe."),("calendar-dots","Conhece a reserva","Qual hóspede, qual quarto, quais datas: cada resposta usa os dados da reserva.")],
  ai_photo=("brand-guest-phone","Hóspede junto à janela digitando uma mensagem no celular","Em todos os canais","WhatsApp, Booking.com, Airbnb e Expedia."),
  ai_btn="Conheça o Lio",
  answer="<strong>O que é o Hostlio Pro?</strong> O Hostlio Pro é um sistema para hotel na nuvem (um PMS hoteleiro) para hotéis independentes e pousadas de 10 a 150 quartos. Ele entrega a comunicação com os hóspedes à inteligência artificial, reúne as reservas das OTAs em um só calendário e leva o check-in para o celular do hóspede. É gerenciado pela web e por um app para iOS, e usado em mais de 20 países.",
  stats=[("30+","idiomas atendidos"),("100+","OTAs e canais de venda"),("20+","países com hotéis usando Hostlio Pro"),("7 dias","de teste grátis, sem compromisso")],
  sup_h="Uma equipe ao seu lado",
  sup=[("rocket-launch","t-peach","Configuração no mesmo dia","Cadastre os tipos de quarto e conecte os canais. O plano Growth inclui uma chamada individual de implantação."),
       ("lifebuoy","t-lilac","Suporte em inglês e turco",'Travou em algo? Fale com a equipe em <a href="mailto:{e}">{e}</a>.'),
       ("book-open-text","t-sand","Guias",'<a href="{b}">Artigos no blog</a> sobre gestão hoteleira e distribuição, além de <a href="{f}">perguntas frequentes</a>.')],
  sup_img=("hostlio-owner","Dono de hotel conferindo reservas no notebook"),
)

# ------------------------------------------------------------------ pages_v4 strings
PV4 = dict(trial="Teste grátis por 7 dias", demo="Agendar demonstração", plan_h="Qual plano é o ideal?",
           cmp_t='Para comparar com outros sistemas para hotel, veja nosso <a href="{c}">comparativo de sistemas para hotel</a>.',
           see_pricing="Ver preços")

# ------------------------------------------------------------------ pages_v4.TYPES
def types(U):
    return [
 dict(key="t-guesthouse", img=("hostlio-phone","Quarto aconchegante de pousada com luminária de mesa"),
  title="Sistema para Pousada com Assistente de IA | Hostlio Pro",
  desc="Sistema para pousada: respostas automáticas aos hóspedes em 30+ idiomas, sincronização com Booking.com e Airbnb e check-in online. A partir de US$ 49/mês.",
  crumb="Sistema para pousadas", h1='<em class="hl">Sistema para pousada</em> que responde aos hóspedes por você',
  lead="Em uma pousada, uma só pessoa cuida das mensagens tarde da noite, das reservas em vários canais e do check-in. O Hostlio Pro tira esse peso das costas dela.",
  q="O que é um sistema para pousada?",
  a="Um sistema para pousada permite que pequenas hospedagens de 1 a 10 quartos gerenciem reservas, disponibilidade e comunicação com hóspedes em um só lugar. O Hostlio Pro acrescenta o Lio, um assistente de IA que responde às perguntas dos hóspedes 24/7 em mais de 30 idiomas. O plano Starter custa US$ 49 por mês para hospedagens de até 10 quartos.",
  pains_h="Quais são as maiores dificuldades das pousadas?",
  pains=[("Mensagens à noite","Perguntas sobre check-in tardio, estacionamento e café da manhã chegam à meia-noite. Lio responde no idioma do hóspede e você lê um resumo pela manhã."),
         ("Vários canais","Vender o mesmo quarto no Booking.com e no Airbnb gera reservas duplicadas. O channel manager sincroniza a disponibilidade na hora."),
         ("Documentos e registro","Digitar os dados dos hóspedes na recepção leva tempo. O check-in online coleta tudo antes da chegada."),
         ("Orçamento apertado","Sistemas cobrados por comissão ficam mais caros à medida que a ocupação cresce. O Hostlio Pro tem mensalidade fixa.")],
  plan="Para a maioria das pousadas, o plano <strong>Starter</strong> é suficiente: até 10 quartos, 1.000 mensagens de IA por mês e respostas de IA no WhatsApp. Escolha o <strong>Pro</strong> se também quiser check-in online e o Lio cuidando das mensagens das OTAs.",
  faq=[("Existe sistema para pousada grátis?","Você pode testar o Hostlio Pro grátis por 7 dias. Depois disso, o Starter custa US$ 49 por mês (preço promocional de lançamento para os 50 primeiros clientes)."),
       ("Serve para uma pousada de 3 quartos?","Sim. O Starter foi pensado para uma hospedagem de até 10 quartos; o preço é o mesmo com menos quartos."),
       ("Posso usar Airbnb e Booking.com juntos?","Sim. O Hostlio Pro sincroniza os dois, além de mais de 100 outros canais, em um só calendário via Channex.")]),
 dict(key="t-boutique", img=("brand-courtyard","Pátio de hotel boutique com piscina e buganvílias", 880, 804),
  title="Sistema para Hotel Boutique com IA para Hóspedes | Hostlio Pro",
  desc="Sistema para hotel boutique: respostas pessoais a hóspedes estrangeiros em 30+ idiomas, sincronização com 100+ OTAs, check-in online e venda de transfers.",
  crumb="Sistema para hotel boutique", h1='<em class="hl">Sistema para hotel boutique</em> pensado para o hóspede',
  lead="O que diferencia um hotel boutique é a atenção pessoal. O Hostlio Pro assume as perguntas repetitivas para que sua equipe tenha mais tempo para os hóspedes.",
  q="O que é um sistema para hotel boutique?",
  a="Um sistema para hotel boutique é um software de gestão hoteleira (PMS hoteleiro) para hotéis de cerca de 10 a 50 quartos com um conceito próprio. No Hostlio Pro, o assistente de IA Lio responde às mensagens dos hóspedes com as informações do próprio hotel e no idioma do hóspede, e o channel manager mantém mais de 100 OTAs sincronizadas.",
  pains_h="Por que hotéis boutique precisam de um sistema específico?",
  pains=[("Hóspedes de vários idiomas","Muitos hóspedes vêm do exterior. Lio responde a cada mensagem no idioma do hóspede e no tom do seu hotel."),
         ("Receita extra","Transfers do aeroporto e passeios fazem diferença para hotéis boutique. Lio oferece esses serviços no momento certo."),
         ("Muito tráfego das OTAs","Reservas do Booking.com, da Expedia e do Airbnb aparecem em um só mapa de reservas, com cores por canal."),
         ("Check-in rápido","Com check-in online e assinatura digital, o hóspede recebe um drinque de boas-vindas em vez de um formulário.")],
  plan="Para hotéis boutique de 10 a 50 quartos, recomendamos o <strong>Pro</strong>: 5.000 mensagens de IA por mês, WhatsApp e caixas de entrada das OTAs (Booking.com, Airbnb, Expedia), check-in online, venda de transfers e passeios e o app para iOS.",
  faq=[("Qual é o melhor sistema para hotel boutique?","Depende do número de quartos, do perfil dos hóspedes e do orçamento. Para hotéis de 10 a 50 quartos com muitos hóspedes estrangeiros e que querem preço fixo, as mensagens por IA e o channel manager do Hostlio Pro são uma boa escolha. Veja nossa página de comparativo para outras opções."),
       ("Posso usar o Hostlio Pro com o site que já tenho?","Sim. O Hostlio Pro funciona ao lado do seu site atual; as reservas das OTAs são sincronizadas e as mensagens de hóspedes do WhatsApp e das OTAs chegam a uma só caixa de entrada."),
       ("Quantos usuários posso adicionar?","Veja a página de preços para os detalhes de cada plano ou pergunte à nossa equipe durante a demonstração.")]),
 dict(key="t-apart", img=("hostlio-room","Apartamento claro com roupa de cama branca"),
  title="Sistema para Apart-Hotel com Check-in Online | Hostlio Pro",
  desc="Sistema para apart-hotel e flats: sincronização com Airbnb e Booking.com, check-in online com assinatura digital e mensagens com hóspedes por IA em 30+ idiomas.",
  crumb="Sistema para apart-hotel", h1='<em class="hl">Sistema para apart-hotel</em> com operação remota',
  lead="Apart-hotéis muitas vezes não têm recepção ou funcionam em horário reduzido, então a comunicação com o hóspede e o check-in acontecem a distância. O Hostlio Pro foi feito para isso.",
  q="O que é um sistema para apart-hotel?",
  a="Um sistema para apart-hotel gerencia reservas, canais e processos de hóspedes em hospedagens que vendem apartamentos e suítes com cozinha. No Hostlio Pro, o hóspede envia os dados do documento e a assinatura por um link de check-in online antes da chegada, e o assistente de IA Lio responde às dúvidas sobre acesso em 30+ idiomas.",
  pains_h="O que mais toma tempo em um apart-hotel?",
  pains=[("Check-in remoto","O formulário de check-in online coleta documento, acompanhantes e assinatura antes da chegada."),
         ("Instruções de acesso","Perguntas sobre entrega de chaves, Wi-Fi e estacionamento se repetem. Lio responde com base nas informações da sua hospedagem."),
         ("Canais de estadia curta","A disponibilidade no Airbnb e no Booking.com é sincronizada na hora via Channex."),
         ("Estadias longas","Estender uma estadia ou trocar de apartamento é só arrastar e soltar no mapa de reservas.")],
  plan="O check-in online está incluído nos planos Pro e Growth, por isso recomendamos o <strong>Pro</strong> para apart-hotéis. Se você administra duas propriedades, veja o <strong>Growth</strong>.",
  faq=[("O Hostlio Pro funciona em um apart-hotel sem recepção?","Sim. O check-in online e as mensagens por IA fazem a distância o trabalho de coletar informações e responder dúvidas que uma recepção faria."),
       ("Ele responde às mensagens do Airbnb?","Nos planos Pro e Growth, as mensagens das OTAs, incluindo o Airbnb, chegam à caixa de entrada do Lio."),
       ("Existe limite de unidades?","O Starter atende até 10, o Pro até 50 e o Growth até 150 quartos ou unidades.")]),
 dict(key="t-hostel", img=("hostlio-lobby","Lobby com painéis de madeira e área de convivência"),
  title="Sistema para Hostels: Mensagens em 30+ Idiomas | Hostlio Pro",
  desc="Sistema para hostels: sincronização com Hostelworld, Booking.com e 100+ canais, mensagens com hóspedes por IA em 30+ idiomas e check-in online. 7 dias grátis.",
  crumb="Sistema para hostels", h1='<em class="hl">Sistema para hostels</em> com caixas de entrada cheias e multilíngues',
  lead="Hostels têm hóspedes internacionais, grande volume de mensagens e equipes pequenas. O Hostlio Pro cuida das perguntas em vários idiomas e mantém os canais em um só calendário.",
  q="O que é um sistema para hostels?",
  a="Um sistema para hostels gerencia reservas, canais e comunicação com hóspedes em hostels que vendem camas e quartos. O Hostlio Pro se conecta a mais de 100 canais, incluindo o Hostelworld, via Channex, e responde às perguntas dos hóspedes em 30+ idiomas com seu assistente de IA Lio.",
  pains_h="Do que os hostels mais precisam?",
  pains=[("Tráfego multilíngue","Os viajantes escrevem no próprio idioma. Lio responde em cada um deles."),
         ("Hostelworld e OTAs","Hostelworld, Booking.com e outros canais compartilham uma só disponibilidade."),
         ("Passeios e transfers","City tours e transfers do aeroporto são extras comuns em hostels; Lio oferece no momento certo."),
         ("Turno da noite","Perguntas feitas à noite não esperam até de manhã; a equipe só cuida do que exige uma decisão.")],
  plan="Para hostels com grande volume, recomendamos o <strong>Pro</strong>, com 5.000 mensagens de IA por mês. Vamos planejar juntos a sua configuração por cama durante a demonstração.",
  faq=[("Funciona com o Hostelworld?","Sim. O Hostelworld está entre os canais conectados ao Channex."),
       ("A venda por cama (dormitório) é suportada?","Depende da sua configuração; vamos planejar juntos a estrutura de quartos e camas durante a demonstração."),
       ("De quantas mensagens de IA eu preciso?","Cerca de 150 respostas automáticas por dia dão aproximadamente 4.500 por mês, o que se encaixa no plano Pro.")]),
    ]

# ------------------------------------------------------------------ pages_v4.CMP
def cmp(U):
    return dict(
  title="Comparativo de Sistemas para Hotel 2026: Preços | Hostlio Pro",
  desc="Hostlio Pro, Cloudbeds, Mews, Little Hotelier e HotelRunner comparados: preços publicados, preço inicial, taxas por reserva, teste grátis e mensagens por IA.",
  crumb="Comparativo de sistemas para hotel", h1='<em class="hl">Comparativo</em> de sistemas para hotel (2026)',
  lead="Comparamos cinco sistemas de gestão hoteleira populares entre hotéis independentes, usando apenas o que cada fornecedor publica na sua própria página de preços.",
  q="Qual sistema para hotel é o ideal para você?",
  a="Resposta curta: para hotéis com uma única propriedade, de 10 a 150 quartos e muitos hóspedes estrangeiros, um sistema de preço fixo com mensagens por IA incluídas (como o Hostlio Pro) mantém o orçamento previsível. Grupos com várias propriedades e necessidades corporativas podem considerar plataformas com preço sob consulta, como Mews ou Cloudbeds; propriedades na Turquia que buscam suporte local e uma rede B2B podem olhar o HotelRunner; pequenas propriedades que querem a rede da SiteMinder podem considerar o Little Hotelier.",
  cols=["Sistema","Preços publicados?","A partir de","Taxa por reserva","Teste grátis","Mensagens com hóspedes por IA"],
  rows=[("Hostlio Pro","Sim","US$ 49/mês (preço de lançamento)","Nenhuma, mensalidade fixa","7 dias","Todos os planos (Lio, 30+ idiomas)"),
        ("Cloudbeds","Não, sob consulta","Sob consulta","Informa que não cobra comissão adicional sobre reservas do Booking Engine e do Channel Manager","Não informado na página de preços","Não informado separadamente na página de preços"),
        ("Mews","Não, sob consulta","Sob consulta","Não informado na página de preços","Não informado na página de preços","Resumos de preferências dos hóspedes por IA no plano Advanced; mensagens não informadas separadamente"),
        ("Little Hotelier","Calculado pelo número de quartos","Pela calculadora de preços","Taxa de 1% por reserva no plano Basics","30 dias","Não informado na página de preços"),
        ("HotelRunner","Sim (planos principais)","US$ 19,95/mês + 0,75% (Manage)","De 0,75% a 1,25%, conforme o plano","Disponível","No nível Advanced \"Automate\"")],
  when_h="Qual escolher, e quando?",
  when=[("Hostlio Pro","Uma ou duas propriedades, de 10 a 150 quartos, muito tráfego de hóspedes estrangeiros e orçamento mensal fixo."),
        ("Cloudbeds e Mews","Grupos com várias propriedades e necessidades corporativas, como revenue management e um grande marketplace de integrações."),
        ("HotelRunner","Propriedades na Turquia que querem suporte local, uma rede de vendas B2B e uma taxa fixa baixa mais comissão."),
        ("Little Hotelier","Pequenas propriedades que querem a infraestrutura da SiteMinder e aceitam preço baseado no número de quartos.")],
  note="Informações reunidas em 21 de setembro de 2026 a partir da página de preços de cada fornecedor; preços e planos podem mudar, então confira a página de cada fornecedor para ver os dados atuais. O Hostlio Pro é parte interessada neste comparativo; baseamos a tabela apenas em informações publicadas.",
  src_h="Fontes",
  faq=[("O que é um software de gestão hoteleira?","Um software de gestão hoteleira (um PMS hoteleiro) permite que uma hospedagem gerencie reservas, disponibilidade de quartos, canais de venda e informações dos hóspedes em um só lugar."),
       ("Quanto custa um sistema para hotel?","Com base nos preços publicados, os planos começam entre cerca de US$ 20 e US$ 150 por mês; alguns fornecedores acrescentam uma taxa de 0,75–1,25% por reserva, e outros só trabalham com preço sob consulta."),
       ("É melhor pagar comissão ou mensalidade fixa?","À medida que a ocupação e a diária média sobem, o custo baseado em comissão cresce. Uma mensalidade fixa é mais previsível para hotéis que querem um orçamento fixo.")],
    )

# ------------------------------------------------------------------ pages_v4.GUIDES
def guides(U):
    return [
 dict(key="post-overbooking", date="2026-09-21", title="Como evitar overbooking: 6 passos para hotéis",
  desc="Por que os hotéis sofrem com overbooking e como evitá-lo: channel manager, regras de stop-sell, margem de disponibilidade e o que fazer se acontecer mesmo assim.",
  content=f'''<div class="answer"><p><strong>Resposta curta:</strong> Overbooking é aceitar mais reservas do que você consegue hospedar para o mesmo quarto e as mesmas datas. Em hotéis independentes, a causa mais comum é atualizar a disponibilidade à mão em várias OTAs. Um channel manager bidirecional e em tempo real elimina a maior parte do risco.</p></div>
<h2>Por que o overbooking acontece?</h2>
<ul><li>Atualizar a disponibilidade no Booking.com, no Airbnb e na Expedia separadamente, à mão</li><li>Lançar com atraso as reservas feitas por telefone ou no balcão</li><li>Cancelamentos e alterações que chegam a um canal, mas não a outro</li><li>Sincronização com atraso (de hora em hora) entre os canais</li></ul>
<h2>Evite o overbooking em 6 passos</h2>
<ol><li><strong>Use uma única fonte de disponibilidade.</strong> Todos os canais devem ler a disponibilidade de um só calendário (o seu PMS).</li>
<li><strong>Escolha sincronização bidirecional e em tempo real.</strong> Quando chega uma reserva, o quarto deve fechar nos outros canais em segundos.</li>
<li><strong>Lance as reservas diretas imediatamente.</strong> Registre as vendas por telefone e no balcão no mesmo calendário na hora.</li>
<li><strong>Gerencie stop-sells e estadias mínimas em um só lugar.</strong> Alterá-los canal por canal abre espaço para erros.</li>
<li><strong>Mantenha uma pequena margem na alta temporada.</strong> Abrir o último quarto apenas no seu canal direto reduz o risco.</li>
<li><strong>Confira os mapeamentos dos canais regularmente.</strong> Ao adicionar um tipo de quarto, confirme o mapeamento em todos os canais.</li></ol>
<h2>E se acontecer mesmo assim?</h2>
<p>Avise o hóspede logo e com sinceridade, ofereça uma alternativa equivalente ou melhor (um hotel próximo, um upgrade) e cubra os custos extras, como transfers. Registre qual canal causou o problema e por quê.</p>
<h2>Como funciona no Hostlio Pro</h2>
<p>O <a href="{U("channel")}">channel manager</a> do Hostlio Pro sincroniza a disponibilidade de forma bidirecional e em tempo real em mais de 100 canais via Channex. As reservas aparecem em um só mapa de reservas, com cores por canal.</p>''',
  faq=[("O que significa overbooking?","Overbooking é quando um hotel aceita mais reservas do que consegue hospedar para o mesmo quarto e as mesmas datas, também chamado de reserva duplicada."),
       ("Um channel manager evita totalmente o overbooking?","A sincronização bidirecional em tempo real elimina a maior parte do risco; reservas diretas não lançadas e mapeamentos de quartos errados ainda podem causar problemas.")]),
 dict(key="post-autoreply", date="2026-09-21", title="Como responder automaticamente às mensagens do Booking.com",
  desc="Três formas de automatizar as mensagens de hóspedes do Booking.com: modelos, mensagens programadas e um assistente de IA. Quando cada uma funciona e onde falha.",
  content=f'''<div class="answer"><p><strong>Resposta curta:</strong> Há três formas de automatizar as mensagens do Booking.com: modelos de mensagem salvos na extranet, mensagens programadas de acordo com a etapa da reserva e um assistente de IA que entende a pergunta do hóspede e responde com as informações do seu hotel. Os modelos servem para informações padrão; um assistente de IA serve para as perguntas que mudam a cada hóspede.</p></div>
<h2>1. Modelos de mensagem</h2>
<p>Salve respostas frequentes, como horário de check-in, como chegar e estacionamento, como modelos e envie-as com um clique. São simples, mas alguém ainda precisa ler a mensagem e escolher o modelo certo.</p>
<h2>2. Mensagens programadas</h2>
<p>Mensagens enviadas automaticamente após a reserva, um dia antes da chegada ou no dia da saída. O hóspede é informado antes mesmo de perguntar, mas elas não respondem às perguntas que ele escrever depois.</p>
<h2>3. Um assistente de IA</h2>
<p>Ele lê a mensagem do hóspede e escreve uma resposta a partir da sua base de conhecimento, no idioma do hóspede. Funciona melhor para perguntas feitas à noite, em vários idiomas e fora dos modelos, e deve repassar as decisões (descontos, reclamações) à equipe.</p>
<div class="table-wrap"><table><thead><tr><th>Método</th><th>Funciona melhor para</th><th>Limitação</th></tr></thead><tbody>
<tr><td>Modelos</td><td>Informações padrão</td><td>Alguém precisa ler e escolher</td></tr>
<tr><td>Mensagens programadas</td><td>Informações antes da chegada</td><td>Não responde às perguntas recebidas</td></tr>
<tr><td>Assistente de IA</td><td>Perguntas a qualquer hora, em qualquer idioma</td><td>Precisa de uma boa base de conhecimento</td></tr></tbody></table></div>
<h2>Por que o tempo de resposta importa</h2>
<p>Uma resposta rápida antes da reserva facilita a decisão do hóspede; uma resposta rápida durante a estadia influencia a satisfação e as avaliações.</p>
<h2>Como funciona no Hostlio Pro</h2>
<p>Nos planos Pro e Growth, as mensagens das OTAs, incluindo o Booking.com, chegam à caixa de entrada do <a href="{U("ai")}">Lio, o assistente de IA</a>. O Lio responde com as informações do seu hotel, no idioma do hóspede, e deixa com você o que ele não tem certeza.</p>''',
  faq=[("Dá para responder automaticamente às mensagens do Booking.com?","Sim. Os modelos da extranet e as mensagens programadas são ferramentas do próprio Booking.com; respostas automáticas específicas para cada pergunta exigem um assistente de IA que leia as mensagens."),
       ("Um assistente de IA pode dar informações erradas?","O risco é baixo quando o assistente usa apenas as informações fornecidas pelo hotel e repassa as perguntas incertas à equipe.")]),
    ]

# ------------------------------------------------------------------ legal_v5
LEGAL_T = {
 "privacy": ("Política de Privacidade | Hostlio Pro",
             "Política de privacidade do Hostlio Pro: quais dados coletamos, como os usamos e compartilhamos, segurança e retenção de dados, cookies e seus direitos sob o GDPR.",
             "Política de privacidade"),
 "terms":   ("Termos de Serviço | Hostlio Pro",
             "Termos de serviço do Hostlio Pro: descrição do serviço, assinaturas e pagamentos, cancelamento e reembolsos, conteúdo gerado por IA, integrações com OTAs e responsabilidade.",
             "Termos de serviço"),
}
LEGAL_NOTE = 'Última atualização: <time datetime="{iso}">{date}</time>, {addr}. Este texto é uma tradução do original em inglês; em caso de divergência, prevalece a <a href="{en_url}">versão em inglês</a>.'

def privacy_body(U, EMAIL, ADDR, ul):
    return f'''<p>Esta Política de Privacidade descreve como o Hostlio Pro, operado pela Loti Members LLC ("nós" ou "nosso"), coleta, usa e compartilha informações quando você utiliza nossa plataforma de gestão hoteleira em hostliopro.com.</p>
<h2>1. Informações que coletamos</h2><p>Coletamos as informações que você nos fornece diretamente, incluindo:</p>
{ul(["Informações da conta: nome, endereço de e-mail, número de telefone, nome do hotel, número de quartos","Informações de pagamento: processadas com segurança pela Stripe (não armazenamos dados de cartão)","Dados do hotel: reservas, comunicações com hóspedes, configurações de quartos","Dados de uso: a forma como você interage com nossa plataforma"])}
<h2>2. Como usamos suas informações</h2><p>Usamos as informações que coletamos para:</p>
{ul(["Fornecer, manter e aprimorar nossos serviços","Processar pagamentos e enviar notificações de cobrança","Enviar e-mails transacionais e atualizações do produto","Responder a seus comentários e perguntas","Monitorar e analisar padrões de uso para aprimorar a experiência do usuário","Cumprir obrigações legais"])}
<h2>3. Compartilhamento de informações</h2><p>Não vendemos, trocamos nem alugamos suas informações pessoais a terceiros. Podemos compartilhar suas informações com:</p>
{ul(["<strong>Prestadores de serviços:</strong> Supabase (banco de dados), Make.com (automação), Stripe (pagamentos), Vercel (hospedagem), Anthropic (processamento de IA)","<strong>Channel managers:</strong> API da Channex para sincronização com OTAs (Booking.com, Airbnb etc.)","<strong>Exigências legais:</strong> quando exigido por lei ou para proteger nossos direitos"])}
<h2>4. Segurança dos dados</h2><p>Adotamos medidas técnicas e organizacionais adequadas para proteger suas informações pessoais contra acesso, alteração, divulgação ou destruição não autorizados. Nossa infraestrutura está em conformidade com o SOC 2 por meio da Supabase, e os pagamentos estão em conformidade com o PCI DSS por meio da Stripe.</p>
<h2>5. Retenção de dados</h2><p>Mantemos suas informações pessoais enquanto sua conta estiver ativa ou pelo tempo necessário para a prestação dos serviços. Você pode solicitar a exclusão dos seus dados a qualquer momento entrando em contato conosco pelo e-mail {EMAIL}.</p>
<h2>6. Direitos previstos no GDPR</h2><p>Se você estiver localizado no Espaço Econômico Europeu, tem o direito de acessar, corrigir ou excluir seus dados pessoais. Você também tem direito à portabilidade dos dados e de se opor ao tratamento. Para exercer esses direitos, entre em contato conosco pelo e-mail {EMAIL}.</p>
<h2>7. WhatsApp e mensagens</h2><p>Nossa plataforma é integrada à API do WhatsApp Business para facilitar a comunicação com os hóspedes. O conteúdo das mensagens é processado para gerar respostas de IA e não é usado para fins de marketing. Os números de telefone dos hóspedes são armazenados apenas para fins de comunicação.</p>
<h2>8. Cookies</h2><p>Usamos cookies essenciais para manter sua sessão e suas preferências. Não usamos cookies de rastreamento nem de publicidade. Você pode controlar os cookies nas configurações do seu navegador.</p>
<h2>9. Links de terceiros</h2><p>Nossa plataforma pode conter links para sites de terceiros. Não somos responsáveis pelas práticas de privacidade desses sites e recomendamos que você leia as respectivas políticas de privacidade.</p>
<h2>10. Alterações nesta política</h2><p>Podemos atualizar esta Política de Privacidade periodicamente. Notificaremos você sobre quaisquer alterações publicando a nova política nesta página e atualizando a data de "Última atualização".</p>
<h2>11. Fale conosco</h2><p>Se tiver dúvidas sobre esta Política de Privacidade, entre em contato conosco:</p>
{ul([f'E-mail: <a href="mailto:{EMAIL}">{EMAIL}</a>', f"Endereço: {ADDR}"])}
<p>Para excluir sua conta, consulte <a href="/delete-account">Excluir sua conta</a>.</p>'''

def terms_body(U, EMAIL, ADDR, ul):
    pricing = U("pricing")
    privacy = U("privacy")
    return f'''<p>Estes Termos de Serviço ("Termos") regem o uso que você faz do Hostlio Pro, operado pela Loti Members LLC ("Empresa", "nós" ou "nosso"). Ao acessar ou utilizar nosso serviço, você concorda em ficar vinculado a estes Termos.</p>
<h2>1. Descrição do serviço</h2><p>O Hostlio Pro é uma plataforma de gestão hoteleira baseada na nuvem que oferece comunicação com hóspedes com inteligência artificial, gestão de canais, calendário de mapa de reservas e ferramentas relacionadas de gestão de hospedagem. O serviço está disponível mediante assinatura em hostliopro.com.</p>
<h2>2. Cadastro da conta</h2><p>Para usar o Hostlio Pro, você deve criar uma conta e fornecer informações precisas e completas. Você é responsável por manter a confidencialidade das credenciais da sua conta e por todas as atividades realizadas nela.</p>
<h2>3. Assinatura e pagamentos</h2>
{ul(["As assinaturas são cobradas mensal ou anualmente, de forma antecipada","Todos os pagamentos são processados com segurança pela Stripe","Teste grátis de 7 dias disponível — um meio de pagamento é solicitado na inscrição, mas nenhuma cobrança é feita até o término do período de teste","Após o período de teste, você será cobrado de acordo com o plano selecionado",f'Os preços são em USD. Os planos e valores vigentes estão listados em nossa <a href="{pricing}">página de preços</a>',"Os planos anuais oferecem 20% de desconto"])}
<h2>4. Cancelamento e reembolsos</h2><p>Você pode cancelar sua assinatura a qualquer momento. O cancelamento entra em vigor ao final do período de cobrança em curso. Não oferecemos reembolso de períodos de cobrança parciais. Para cancelar, entre em contato conosco pelo e-mail {EMAIL}.</p>
<h2>5. Uso aceitável</h2><p>Você concorda em não:</p>
{ul(["Usar o serviço para qualquer finalidade ilícita","Violar os termos das plataformas OTA (Booking.com, Airbnb etc.) por meio de nossas integrações","Tentar obter acesso não autorizado aos nossos sistemas","Enviar spam ou mensagens não solicitadas aos hóspedes","Revender ou sublicenciar o serviço sem autorização por escrito"])}
<h2>6. Conteúdo gerado por IA</h2><p>O Hostlio Pro usa inteligência artificial para gerar respostas às mensagens dos hóspedes. Você reconhece que o conteúdo gerado por IA pode ocasionalmente conter erros. Você é responsável por revisar e gerenciar as respostas de IA enviadas em nome da sua hospedagem. Não nos responsabilizamos por eventuais imprecisões nas comunicações geradas por IA.</p>
<h2>7. Integrações com canais OTA</h2><p>Nossa plataforma é integrada a canais OTA de terceiros (Booking.com, Airbnb, Expedia etc.) por meio da API da Channex. Você é responsável por cumprir os termos de serviço de cada plataforma. Não nos responsabilizamos por mudanças nas APIs ou nas políticas das OTAs que possam afetar o funcionamento.</p>
<h2>8. Dados e privacidade</h2><p>O uso que você faz do Hostlio Pro também é regido por nossa <a href="{privacy}">Política de Privacidade</a>, incorporada a estes Termos por referência. Você mantém a titularidade dos seus dados. Tratamos seus dados exclusivamente para prestar o serviço.</p>
<h2>9. Disponibilidade do serviço</h2><p>Buscamos 99,9% de disponibilidade, mas não garantimos um serviço ininterrupto. Podemos realizar manutenções programadas mediante aviso prévio. Não nos responsabilizamos por perdas decorrentes de interrupções do serviço.</p>
<h2>10. Propriedade intelectual</h2><p>O Hostlio Pro e todos os softwares, designs e conteúdos relacionados são de propriedade da Loti Members LLC. Você não pode copiar, modificar ou distribuir nenhuma parte do nosso serviço sem autorização por escrito.</p>
<h2>11. Limitação de responsabilidade</h2><p>Na máxima extensão permitida por lei, a Loti Members LLC não será responsável por quaisquer danos indiretos, incidentais, especiais, consequenciais ou punitivos, incluindo lucros cessantes ou perda de dados, decorrentes do uso que você faz do serviço.</p>
<h2>12. Lei aplicável</h2><p>Estes Termos são regidos pelas leis do Estado da Califórnia, EUA. Quaisquer controvérsias serão resolvidas nos tribunais do Condado de Sacramento, Califórnia.</p>
<h2>13. Alterações nos Termos</h2><p>Podemos atualizar estes Termos periodicamente. Notificaremos você sobre alterações relevantes por e-mail ou pela plataforma. O uso continuado do serviço após as alterações constitui aceitação dos novos Termos.</p>
<h2>14. Contato</h2><p>Para dúvidas sobre estes Termos, entre em contato conosco:</p>
{ul([f'E-mail: <a href="mailto:{EMAIL}">{EMAIL}</a>', f"Endereço: {ADDR}"])}'''
