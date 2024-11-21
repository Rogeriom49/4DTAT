import streamlit as st
import globals

st.header('**Insights**')


tab1, tab2,tab3,tab4, tab5, tab6, tab7 = st.tabs(globals.insights)

with tab1:
    st.subheader('Ano 1998')
    
    st.write(f""" No período  de 1997 a 1998, o valor do petróleo obteve uma significativa queda, resultada pela combinação de crises regionais, políticas internacionais e mudanças climáticas. A crise econômica no sudeste asiático em 1997 desempenhou um papel crucial na contração da demanda global de petróleo, reduzindo-a em aproximadamente 400 mil barris por dia (b/d). Essa crise afetou diretamente as economias de países como Tailândia, Indonésia e Coreia do Sul, diminuindo a capacidade de consumo de petróleo em uma das regiões com crescimento econômico mais dinâmico da década. Essa queda na demanda impactou a estabilidade do preço do barril, que já estava sensível a mudanças no cenário internacional. """) 
    
    st.write(f""" Paralelamente, o programa “Petróleo por Alimentos”, implementado pela ONU em 1996, permitiu que o Iraque voltasse a exportar petróleo sob determinadas condições, após o embargo imposto durante a Guerra do Golfo. Esse programa adicionou cerca de 1,5 milhão de b/d ao mercado internacional, o que contribuiu significativamente para o aumento da oferta. A reintrodução do petróleo iraquiano trouxe consequências econômicas globais, pois somou uma quantidade substancial de petróleo ao mercado em um período de baixa demanda. """) 
    
    st.write(f""" Outro fator importante que contribuiu para o excesso de oferta foi uma sequência de invernos excepcionalmente amenos no hemisfério norte entre 1996 e 1998. As temperaturas mais altas reduziram a demanda por energia para aquecimento, particularmente em países da América do Norte e Europa, que tradicionalmente consomem grandes volumes de petróleo e derivados no inverno. Esse clima mais ameno contribuiu para um menor consumo global, ampliando o excesso de oferta no mercado. """) 

    st.write(f""" Esses fatores combinados resultaram em um excedente de oferta, o desequilíbrio fez com que o preço do barril desabasse para cerca de US$ 10, refletindo um cenário de baixa demanda e excesso de oferta que pressionou o valor do petróleo a níveis mínimos. """) 
    
    st.write(f""" Esse período revela a importância de políticas de controle de oferta e de medidas internacionais para equilibrar o mercado, que se mostrou vulnerável a choques externos e flutuações climáticas. A análise desses eventos históricos permite uma melhor compreensão dos mecanismos que afetam o mercado de petróleo, com lições para a formulação de políticas econômicas e energéticas em períodos de crise. """)         



with tab2:
    st.subheader('Ano 2008')
    st.write(""" Em 2008, o mercado de petróleo viveu uma história em dois atos: inicialmente, os preços ultrapassaram a marca de 100 dólares por barril e dispararam vertiginosamente até atingirem 147,50 dólares. Em seguida, uma queda abrupta e sem precedentes nos valores desencadeou sérios problemas de abastecimento """)
    
    st.write(""" No início do ano, o barril ultrapassou os 100 dólares, e por quase seis meses os preços bateram recordes sucessivos, alcançando o pico em julho. No entanto, a partir desse ponto, os preços começaram a despencar em uma velocidade ainda maior do que haviam subido, caindo para 39,35 dólares em Londres no início de dezembro. """)
    
    st.write(""" Diversos fatores contribuíram para a disparada dos preços no primeiro semestre: tensões geopolíticas envolvendo países como Irã, Nigéria e Paquistão; o equilíbrio delicado entre uma oferta restrita e a crescente demanda dos mercados emergentes; a percepção de que as reservas de petróleo estão se esgotando e são cada vez mais difíceis de acessar; e o intenso interesse dos fundos de investimento por commodities. """)
    
    st.write(""" Os fundos, de fato, utilizaram o petróleo como proteção contra a inflação, criando um ciclo vicioso: o medo da alta dos preços levou a mais investimentos no petróleo, o que, por sua vez, impulsionou ainda mais os preços – justamente o principal motor da inflação. """)
    
    st.write(""" Entretanto, após a falência do banco americano Lehman Brothers, em setembro, essa dinâmica mudou completamente. Com o temor de uma deflação, investidores abandonaram o petróleo em busca de liquidez imediata. """)
    
    st.write(""" Simultaneamente, o alto preço do petróleo começou a reduzir o consumo de combustíveis nos países desenvolvidos. Nos Estados Unidos, por exemplo, muitos motoristas deixaram seus veículos de grande porte parados. A demanda global, pela primeira vez em 25 anos, deu sinais de retração, de acordo com previsões da Agência Internacional de Energia. """)
    
    st.write(""" Assim, o ano terminou com os preços em baixa e superpetroleiros ancorados em alguns portos sendo usados como depósitos flutuantes. """)

with tab3:
    st.subheader('Ano 2011')
    st.write(""" Em 2011, os preços do petróleo registraram níveis historicamente altos, com o Brent Crude frequentemente ultrapassando a marca de US$ 100 por barril durante grande parte do ano. 
    Essa elevação nos preços foi atribuída a uma combinação de fatores econômicos, geopolíticos e climáticos que pressionaram o mercado global de energia. """)

    st.write(""" A instabilidade no Oriente Médio e no Norte da África, impulsionada pela Primavera Árabe, gerou incertezas significativas no fornecimento de petróleo. A guerra civil na Líbia, um dos maiores exportadores de petróleo do mundo, reduziu drasticamente sua produção, contribuindo para o desequilíbrio na oferta global. Além disso, o aumento das tensões envolvendo o programa nuclear do Irã intensificou os temores quanto à segurança no Estreito de Ormuz, um ponto estratégico por onde transitam cerca de 20% do petróleo mundial. """)

    st.write(""" No cenário econômico, a recuperação global após a crise financeira de 2008-2009 aumentou a demanda por petróleo, especialmente nos mercados emergentes como China e Índia. Esses países, em meio à rápida industrialização e ao crescimento no transporte, exerceram uma pressão significativa sobre os preços. Outro fator econômico relevante foi a política de estímulo monetário nos Estados Unidos, conhecida como "Quantitative Easing", que resultou na desvalorização do dólar. Como o petróleo é cotado em dólares, essa desvalorização tornou a commodity mais cara nos mercados internacionais. """)

    st.write(""" Além disso, eventos climáticos também desempenharam um papel, como tempestades e outros fenômenos naturais que afetam regiões produtoras, gerando interrupções temporárias na produção e logística. O aumento nos estoques estratégicos por parte de algumas nações, temendo instabilidade no fornecimento, também contribuiu para a pressão nos preços. """)

    st.write(""" Esses elementos, combinados, fizeram de 2011 um ano marcante para o mercado de petróleo, ressaltando como fatores geopolíticos e econômicos podem impactar a dinâmica de uma das commodities mais estratégicas do mundo.""")

with tab4:
    st.subheader('Ano 2012')
    st.write(""" Em 2012, os preços do petróleo estavam em níveis relativamente altos e altamente voláteis, refletindo um cenário econômico e geopolítico complexo. O preço do petróleo Brent, oscilou entre &#36;90 e &#36;125 por barril, atingindo picos durante determinados períodos do ano devido a uma série de fatores que afetaram tanto a oferta quanto a demanda. Este contexto de preços elevados foi marcado por uma interação de forças globais, com implicações significativas para a economia mundial e o mercado de energia. """)

    st.write(""" O ano de 2012 foi particularmente afetado por tensões geopolíticas no Oriente Médio e na região do Norte da África. Em resposta ao programa nuclear do Irã, os Estados Unidos e a União Europeia impuseram sanções econômicas severas, incluindo um embargo às exportações de petróleo iraniano. O Irã, que era um dos maiores produtores de petróleo da OPEP, viu sua capacidade de exportação reduzida drasticamente, o que diminuiu a oferta global e aumentou a incerteza nos mercados de energia. Essas sanções resultaram em uma pressão crescente sobre os preços, especialmente devido ao papel estratégico do Irã no fornecimento de petróleo para mercados como a Ásia e a Europa. """)

    st.write(""" Além disso, conflitos internos e instabilidade política em países como Síria e Líbia criaram interrupções na produção de petróleo, exacerbando as preocupações com a segurança do fornecimento. A guerra civil na Síria e a instabilidade na Líbia, que era um grande exportador de petróleo, também impactaram negativamente o mercado, uma vez que os traders temiam que esses conflitos se espalhassem para outras regiões produtoras de petróleo. Tais fatores geopolíticos impulsionaram ainda mais a volatilidade dos preços, com os investidores reagindo a cada novo desenvolvimento. """)

    st.write(""" Por outro lado, a demanda global por petróleo continuou a ser sustentada por economias emergentes, especialmente China e Índia, que registraram taxas de crescimento robustas, apesar das dificuldades nos mercados desenvolvidos. A China, o maior consumidor de petróleo do mundo, manteve um nível elevado de importações de petróleo para atender à sua crescente demanda por energia. A Índia também apresentou uma demanda considerável, embora menor em comparação com a China, o que ajudou a equilibrar as quedas de consumo em mercados tradicionais, como os Estados Unidos e a Europa. """)

    st.write(""" Esses países emergentes, em especial a China, tornaram-se fundamentais para manter os preços elevados, já que seus setores industriais e de transportes dependem fortemente do petróleo. A urbanização acelerada e o crescimento da classe média na Ásia contribuíram para um aumento substancial na demanda por combustíveis e produtos petroquímicos, o que, por sua vez, manteve os preços sustentados durante o ano. """)

    st.write(""" 2012 também marcou um ponto de inflexão importante no mercado de petróleo com o crescimento da produção de petróleo de xisto (shale oil) nos Estados Unidos. Embora os EUA ainda não fossem um exportador líquido de petróleo, a produção de petróleo não convencional aumentou substancialmente, reduzindo a necessidade de importações de petróleo e diminuindo a dependência do petróleo estrangeiro. A tecnologia de fraturamento hidráulico e perfuração horizontal, que estava se tornando mais eficiente, permitiu aos EUA expandir sua produção de petróleo em um ritmo impressionante. """)

    st.write(""" Esse aumento na produção doméstica de petróleo foi um fator importante para as perspectivas de longo prazo para o mercado de petróleo. Embora não tenha sido suficiente para transformar os EUA em um exportador líquido, a redução das importações e o aumento da produção interna alteraram o equilíbrio no mercado global de energia. Os analistas começaram a perceber que os EUA poderiam ter um impacto maior sobre os preços do petróleo nas décadas seguintes, especialmente se a produção de shale oil continuasse a crescer. """)

    st.write(""" A Organização dos Países Exportadores de Petróleo (OPEP) desempenhou um papel crucial na tentativa de estabilizar o mercado em 2012, ajustando sua produção de petróleo. A Arábia Saudita, o maior produtor da OPEP, assumiu o papel de "produtor swing", aumentando ou diminuindo sua produção conforme necessário para manter os preços em níveis desejáveis. Isso ajudou a equilibrar a oferta e a demanda, mas a OPEP também enfrentou desafios devido ao aumento da produção em outros lugares, como os EUA e outros países fora da organização, como o Brasil e o Canadá, que estavam explorando novas fontes de petróleo. """)

    st.write(""" A OPEP também observou a desaceleração da demanda global, especialmente na Europa, que estava lidando com os efeitos da crise da dívida soberana. Isso teve um impacto negativo na demanda de petróleo, especialmente em economias mais afetadas pela crise, como a Grécia, Espanha e Itália. O crescimento lento nas economias da zona do euro limitou a expansão da demanda de petróleo nesses mercados, fazendo com que os preços enfrentem uma pressão de baixa em determinados momentos do ano. """)

    st.write(""" Apesar de os preços do petróleo terem se mantido elevados em 2012, o contexto econômico global gerou incertezas. A recuperação econômica lenta, particularmente nos mercados desenvolvidos, e a redução na confiança dos consumidores influenciam a demanda por petróleo, limitando a aceleração dos preços. No entanto, as baixas taxas de juros nos EUA e estímulos econômicos na Europa impulsionaram a liquidez global e favoreceu o aumento de investimentos em commodities, o que, em parte, sustentou os preços do petróleo. """)

    st.write(""" Em suma, o mercado de petróleo de 2012 foi caracterizado por uma combinação de tensões geopolíticas, crescimento robusto nos mercados emergentes, a revolução do shale oil nos EUA e os ajustes de produção da OPEP. Essas forças se entrelaçaram para criar um ambiente de preços elevados e voláteis, estabelecendo as bases para um mercado de petróleo em transformação nas décadas seguintes. A trajetória de preços em 2012 refletiu um mercado global em constante evolução, com implicações significativas tanto para os produtores quanto para os consumidores de petróleo. """)

with tab5:
    st.subheader("Boom e Queda do Shale Oil nos EUA")
    st.write(f""" O boom e queda do óleo de xisto nos Estados Unidos foi um dos eventos mais marcantes no mercado de petróleo recente, com início em 2014, impulsionado pelo aumento significativo da produção de petróleo de xisto, viabilizado por avanços tecnológicos como o fraturamento hidráulico (fracking) e a perfuração horizontal. Esses métodos possibilitam uma exploração de petróleo de forma mais eficiente e econômica, tornando os EUA o maior produtor mundial de petróleo. Com isso, a oferta global de petróleo superou a demanda, provocando uma queda gradual nos preços, que passou de mais de &#36;100.00 por barril no início de 2014 para menos de &#36;30.00 no início de 2016. """) 

    st.write(f""" A queda nos preços atingiu níveis críticos, gerando dificuldades financeiras para muitos produtores de óleo de xisto, cujos custos de produção eram mais altos em comparação com os países membros da Organização dos Países Exportadores de Petróleo (OPEP). Em resposta a esta situação, a OPEP, juntamente com outros grandes produtores de petróleo, decidiu implementar cortes de produção no final de 2016, o que ajudou a estabilizar os preços e marcou o fim desse ciclo """)  

    st.write(f""" Esse evento trouxe impactos significativos, como a crise econômica em países altamente dependentes das exportações de petróleo, como Venezuela e Rússia, e mudanças na dinâmica do mercado, diminuindo a influência da OPEP devido ao crescimento da produção norte-americana. Essa situação evidenciou como a produção de óleo de xisto transformou o mercado global de energia, destacando a vulnerabilidade dos mercados tradicionais diante de novas tecnologias e estratégias de produção. """) 

with tab6:
    st.subheader('Pandemia de COVID-19')

    st.write(f""" A pandemia de COVID-19 foi um dos eventos globais mais impactantes no mercado de petróleo, com início em março de 2020, quando vários países implementaram bloqueios e restrições rigorosas para conter a propagação do vírus. Essas medidas provocaram uma redução drástica na demanda global por petróleo, especialmente nos setores de transporte e aviação, que foram severamente afetados pelas restrições de mobilidade e viagens. Como resultado, os preços do petróleo Brent caíram para níveis historicamente baixos, chegando a menos de &#36;20 por barril em abril de 2020. Esse foi um dos momentos mais dramáticos no mercado de energia, marcado até mesmo por preços negativos no WTI (West Texas Intermediate ), referência nos EUA, devido ao excesso de oferta e à falta de capacidade de armazenamento. """) 

    st.write(f""" O impacto direto sobre os preços começou a diminuir a partir de meados de 2020, com a flexibilização gradual das restrições e o início da recuperação econômica em algumas regiões. No entanto, a demanda global pelo petróleo só começou a se normalizar em 2021, com o avanço da vacinação e a retomada das atividades econômicas. Durante esse período, a OPEP e os seus aliados (OPEP+) desempenharam um papel fundamental na estabilização do mercado, ajustando os níveis de produção para equilibrar a oferta e a procura. """) 

    st.write(f""" Esse evento destacou a vulnerabilidade do mercado de petróleo a crises inesperadas e a importância de mecanismos de adaptação por parte dos grandes produtores. Além disso, a pandemia acelerou a transição energética, com diversos países buscando investir em fontes de energia renovável como parte de suas estratégias de recuperação econômica. """)               
     

with tab7:
    st.subheader('Ano 2022')
    st.write(f""" A guerra entre Rússia e Ucrânia produziu um aumento de preço rápido no mercado de petróleo e esse aumento foi acentuado não apenas pelo cenário de guerra, mas também pela dependência energética de países europeus e asiáticos, que enfrentam um cenário de escassez e alta de custos em suas cadeias de fornecimento, já que sendo membro da OPEP+ e um dos maiores produtores globais, a Rússia, sofre sanções que limitam sua capacidade de exportação.  """)      
    st.write(f""" As flutuações no preço do petróleo Brent durante essa guerra evidenciam a vulnerabilidade dos mercados globais a conflitos envolvendo grandes produtores de energia. O estudo desses impactos revela que, em situações de sanções e restrições comerciais, a capacidade de adaptação e de reorganização das cadeias de fornecimento exerce influência significativa sobre a estabilização de preços. A análise dos efeitos deste conflito destaca a importância de políticas energéticas diversificadas e de reservas estratégicas para mitigar riscos associados à dependência de fornecedores em regiões geopoliticamente instáveis.  """)      