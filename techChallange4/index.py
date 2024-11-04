import streamlit as st

st.set_page_config(layout='wide', 
                   page_title='Tech Challenge 4')

pages = [
        st.Page(page="paginas/introducao.py", title="Introdução", default=True),
        st.Page(page="paginas/tecnologias.py", title="Técnologias"),
        st.Page(page="paginas/eda.py", title="EDA"),
        st.Page(page="paginas/insights.py", title="Insights"),
        st.Page(page="paginas/modelo.py", title="Modelo"),
        st.Page(page="paginas/dashboard.py", title="Dashboard"),
        st.Page(page="paginas/conclusao.py", title="Conclusão")
]

pg = st.navigation(pages)

pg.run()

