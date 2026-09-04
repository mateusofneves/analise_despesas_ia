import streamlit as st

from src.leitura import ler_excel
from src.tratamento import verificar_dados
from src.estatistica import calcular_estatisticas

st.title("Análise de Despesas com IA")

arquivo = st.file_uploader(
    "Faça o upload do arquivo Excel", 
    type=["xlsx"]
)

if arquivo is not None:
    df = ler_excel(arquivo)

    st.subheader("Dados da planilha")
    st.dataframe(df, use_container_width=True)

    problemas = verificar_dados(df)

    st.subheader("Validação dos dados")

    if not problemas:
        st.success("Nenhum problema encontrado nos dados.")
    else:
        st.warning("Foram encontrados problemas nos dados:")

        for problema, detalhes in problemas.items():
            st.write(f"- {problema}: {detalhes}")