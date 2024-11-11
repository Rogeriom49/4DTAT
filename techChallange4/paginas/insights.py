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
    st.dataframe(globals.df_index.loc['2008'])

with tab3:
    st.subheader('Ano 2011')
    st.dataframe(globals.df_index.loc['2011'])

with tab4:
    st.subheader('Ano 2012')
    st.dataframe(globals.df_index.loc['2012'])

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