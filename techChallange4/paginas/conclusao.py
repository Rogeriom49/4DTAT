import streamlit as st

st.header('**Conclusão**')

st.write(""" O modelo Prophet apresentou um bom desempenho ao capturar as tendências nos preços do petróleo, como evidenciado pelo coeficiente de determinação R² = 0.8937913, indicando que ele explica aproximadamente 89,38% da variação nos preços. Esse valor sugere que o modelo é eficaz em prever os preços com base nos dados fornecidos, oferecendo uma boa capacidade de previsão dentro do conjunto de dados analisados. """)

st.write(""" Entretanto, ao considerar a análise de estacionariedade, o p-valor de 27,81 aponta que os dados não são estacionários, o que significa que os preços do petróleo exibem uma tendência ou estrutura de longo prazo não constante. Isso implica que, apesar da boa performance do modelo, a incerteza aumenta à medida que o horizonte temporal das previsões se expande. Esse fator destaca a necessidade de considerar variáveis externas e sazonais que influenciam os preços, como crises econômicas, geopolíticas e mudanças climáticas. """)

st.write(""" Eventos históricos ilustram como esses fatores externos podem impactar de forma significativa os preços do petróleo: """)

st.write(""" 1998: A queda acentuada nos preços foi causada por crises regionais políticas e climáticas.""")

st.write(""" 2008: Os preços do petróleo superaram os US&#36;100 por barril devido a tensões geopolíticas em países como Irã, Nigéria e Paquistão. """)
st.write(""" 2020 (Pandemia): As restrições globais e bloqueios para conter a disseminação do vírus reduziram drasticamente a demanda, fazendo os preços despencarem para menos de US&#36;20 por barril em abril. """)

st.write(""" Esses exemplos ressaltam a importância de integrar variáveis exógenas, como indicadores econômicos, conflitos geopolíticos e eventos extraordinários, para melhorar a precisão das previsões e proporcionar uma análise mais robusta. """)

st.write(""" Adicionalmente, os seguintes dados estatísticos fornecem uma visão mais aprofundada do comportamento dos preços do petróleo: """)

st.write(""" Desvio padrão de 33,18: A alta volatilidade em torno da média reflete as grandes flutuações características desse mercado no curto prazo. """)

st.write(""" Variância de 1101,22: A variância elevada reforça a ideia de que os preços do petróleo apresentaram grandes oscilações, condizente com a alta volatilidade do mercado. """)

st.write(""" Esses resultados reforçam a noção de que o mercado de petróleo é extremamente volátil e influenciado por uma ampla gama de fatores sazonais, econômicos e geopolíticos, exigindo uma análise contínua e o ajuste dos modelos para levar em consideração essas variáveis. """)

st.divider()

st.header(""" Links Importantes """)

st.markdown(""" [Repositório GitHub](https://github.com/Rogeriom49/4DTAT/tree/main/techChallange4) """)
st.markdown(""" [Dashboard Power BI](https://app.powerbi.com/view?r=eyJrIjoiYmZhZTk3ZjgtMDNkZi00NzU2LTlkYjEtZjUxZDcwODkyY2NlIiwidCI6IjZkYzg3NGNlLWRkMmItNGFhOS05ZjBkLWFkYjkyNjlhNzU4MCJ9) """)
