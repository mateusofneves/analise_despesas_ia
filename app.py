import streamlit as st

from leitura import ler_excel

st.title("Análise de Despesas com IA")

arquivo = st.file_uploader(
    "Faça o upload do arquivo Excel", 
    type=["xlsx"]
)

if arquivo is not None:
    df = ler_excel(arquivo)

    st.subheader("Dados da planilha")

    st.dataframe(df, use_container_width=True)