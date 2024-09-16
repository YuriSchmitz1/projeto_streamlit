import streamlit as st
import pandas as pd

st.set_page_config(
    page_title= "Meu sistema",
                page_icon='🦈',
                layout="wide",
)
lateral = st.sidebar
data= lateral.date_input("Selecione a data")
cidade = lateral.selectbox("Selecione a cidade:",
                           ["Belo horizonte","Rio de janeiro","SÃO PAULO"]
                           )

@st.cache_data
def carregar_dados():
    dados= pd.read_csv("acidentes.csv")
    return dados 

dados = carregar_dados()
st.session_state["dados"] = dados 
st.session_state["data"]= data
st.session_state["cidade"]= cidade 

st.title ("Dados")
col1, col2 = st.columns(2)


tabela= col1.dataframe(dados)

mostrar_grafico= st.toggle("Mostrar grafico")
if mostrar_grafico:
    municipos = dados["municipio"].value_counts()
    col2.bar_chart(municipos)

st.subheader("Cidade")
st.write(f"A cidade selecionada foi:  {cidade}")

