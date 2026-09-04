import streamlit as st

from src.leitura import ler_excel
from src.tratamento import verificar_dados
from src.estatistica import calcular_estatisticas
from src.distribuicoes import analisar_distribuicao
from src.anomalidades import detectar_anomalias
from src.graficos import grafico_por_categoria, grafico_por_mes

st.title("Análise de Despesas com IA")

arquivo = st.file_uploader(
    "Faça o upload do arquivo Excel", 
    type=["xlsx"]
)

if arquivo is not None:


    # Função para ler um arquivo Excel e retornar um DataFrame.

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


    # Função para calcular estatísticas básicas de um DataFrame.

    estatisticas = calcular_estatisticas(df)

    st.subheader("Estatística das despesas")

    st.write(f"Quantidade de despesas: {estatisticas['quantidade']}")
    st.write(f"Total gasto: R$ {estatisticas['total']:,.2f}")
    st.write(f"Média: R$ {estatisticas['media']:,.2f}")
    st.write(f"Mediana: R$ {estatisticas['mediana']:,.2f}")
    st.write(f"Menor despesa: R$ {estatisticas['minimo']:,.2f}")
    st.write(f"Maior despesa: R$ {estatisticas['maximo']:,.2f}")
    st.write(f"Variância: {estatisticas['variancia']:,.2f}")
    st.write(f"Desvio padrão: R$ {estatisticas['desvio_padrao']:,.2f}")


    #Função para analisar a distribuição dos dados de um DataFrame.

    distribuicao = analisar_distribuicao(df)

    st.subheader("Análise da distribuição")

    st.write(
        f"Distribuição dos valores: {distribuicao['distribuicao']}"
    )

    st.write(
        f"Estatística de Shapiro-Wilk: "
        f"{distribuicao['estatistica_shapiro']:.4f}"
        )

    st.write(
        f"p-valor: "
        f"{distribuicao['p_valor_shapiro']:.4f}"
    )

    # Função para detectar anomalias em um DataFrame.

    anomalias = detectar_anomalias(df)

    st.subheader("Detecção de anomalias")

    st.write(f"Q1: R$ {anomalias['q1']:,.2f}")
    st.write(f"Q3: R$ {anomalias['q3']:,.2f}")
    st.write(f"IQR: R$ {anomalias['iqr']:,.2f}")

    st.write(
        f"Limite inferior: R$ "
        f"{anomalias['limite_inferior']:,.2f}"
    )

    st.write(
        f"Limite superior: R$ "
        f"{anomalias['limite_superior']:,.2f}"
    )

    st.write(
        f"Quantidade de possíveis anomalias: "
        f"{len(anomalias['anomalias'])}"
    )

    if len(anomalias["anomalias"]) > 0:
        st.write("Despesas identificadas como possíveis anomalias:")
        st.dataframe(
            anomalias["anomalias"],
            use_container_width=True
        )
    else:
        st.success("Nenhuma possível anomalia encontrada.")

    # Função para gerar gráficos de um DataFrame.
    
    st.subheader("Visualização das despesas")

    fig_categoria = grafico_por_categoria(df)
    st.pyplot(fig_categoria)

    fig_mes = grafico_por_mes(df)
    st.pyplot(fig_mes)
