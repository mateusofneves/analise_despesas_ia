import streamlit as st

from src.leitura import ler_excel
from src.tratamento import verificar_dados

from src.estatistica import (
    calcular_estatisticas,
    analisar_categorias,
    analisar_departamentos,
    analisar_meses
)

from src.distribuicoes import analisar_distribuicao
from src.anomalidades import detectar_anomalias

from src.graficos import (
    grafico_por_categoria,
    grafico_por_mes
)

from src.ia import gerar_relatorio


st.title("Análise de Despesas com IA")


arquivo = st.file_uploader(
    "Faça o upload do arquivo Excel",
    type=["xlsx"]
)


if arquivo is not None:

    # LEITURA DOS DADOS

    df = ler_excel(arquivo)

    st.subheader("Dados da planilha")
    st.dataframe(df, use_container_width=True)


    # VALIDAÇÃO DOS DADOS

    problemas = verificar_dados(df)

    st.subheader("Validação dos dados")

    if not problemas:
        st.success("Nenhum problema encontrado nos dados.")

    else:
        st.warning("Foram encontrados problemas nos dados:")

        for problema, detalhes in problemas.items():
            st.write(f"- {problema}: {detalhes}")


    # ESTATÍSTICAS GERAIS

    estatisticas = calcular_estatisticas(df)

    st.subheader("Estatística das despesas")

    st.write(
        f"Quantidade de despesas: "
        f"{estatisticas['quantidade']}"
    )

    st.write(
        f"Total gasto: "
        f"R$ {estatisticas['total']:,.2f}"
    )

    st.write(
        f"Média: "
        f"R$ {estatisticas['media']:,.2f}"
    )

    st.write(
        f"Mediana: "
        f"R$ {estatisticas['mediana']:,.2f}"
    )

    st.write(
        f"Menor despesa: "
        f"R$ {estatisticas['minimo']:,.2f}"
    )

    st.write(
        f"Maior despesa: "
        f"R$ {estatisticas['maximo']:,.2f}"
    )

    st.write(
        f"Variância: "
        f"{estatisticas['variancia']:,.2f}"
    )

    st.write(
        f"Desvio padrão: "
        f"R$ {estatisticas['desvio_padrao']:,.2f}"
    )


    # ANÁLISE POR CATEGORIA

    categorias = analisar_categorias(df)

    st.subheader("Análise por categoria")

    st.write(
        f"Categoria com maior gasto: "
        f"{categorias['maior_categoria']}"
    )

    st.write(
        f"Valor gasto na categoria: "
        f"R$ {categorias['maior_valor']:,.2f}"
    )

    st.dataframe(
        categorias["por_categoria"],
        use_container_width=True
    )


    # ANÁLISE POR DEPARTAMENTO

    departamentos = analisar_departamentos(df)

    st.subheader("Análise por departamento")

    st.write(
        f"Departamento com maior gasto: "
        f"{departamentos['maior_departamento']}"
    )

    st.write(
        f"Valor gasto no departamento: "
        f"R$ {departamentos['maior_valor']:,.2f}"
    )

    st.dataframe(
        departamentos["por_departamento"],
        use_container_width=True
    )


    # ANÁLISE POR MÊS

    meses = analisar_meses(df)

    st.subheader("Análise por mês")

    st.write(
        f"Mês com maior gasto: "
        f"{meses['maior_mes']}"
    )

    st.write(
        f"Valor gasto no mês: "
        f"R$ {meses['maior_valor']:,.2f}"
    )

    st.dataframe(
        meses["por_mes"],
        use_container_width=True
    )


    # ANÁLISE DA DISTRIBUIÇÃO

    distribuicao = analisar_distribuicao(df)

    st.subheader("Análise da distribuição")

    st.write(
        f"Distribuição dos valores: "
        f"{distribuicao['distribuicao']}"
    )

    st.write(
        f"Estatística de Shapiro-Wilk: "
        f"{distribuicao['estatistica_shapiro']:.4f}"
    )

    st.write(
        f"p-valor: "
        f"{distribuicao['p_valor_shapiro']:.4f}"
    )


    # DETECÇÃO DE ANOMALIAS

    anomalias = detectar_anomalias(df)

    st.subheader("Detecção de anomalias")

    st.write(
        f"Q1: "
        f"R$ {anomalias['q1']:,.2f}"
    )

    st.write(
        f"Q3: "
        f"R$ {anomalias['q3']:,.2f}"
    )

    st.write(
        f"IQR: "
        f"R$ {anomalias['iqr']:,.2f}"
    )

    st.write(
        f"Limite inferior: "
        f"R$ {anomalias['limite_inferior']:,.2f}"
    )

    st.write(
        f"Limite superior: "
        f"R$ {anomalias['limite_superior']:,.2f}"
    )

    st.write(
        f"Quantidade de possíveis anomalias: "
        f"{len(anomalias['anomalias'])}"
    )

    if len(anomalias["anomalias"]) > 0:

        st.write(
            "Despesas identificadas como possíveis anomalias:"
        )

        st.dataframe(
            anomalias["anomalias"],
            use_container_width=True
        )

    else:
        st.success(
            "Nenhuma possível anomalia encontrada."
        )


    # VISUALIZAÇÃO

    st.subheader("Visualização das despesas")

    fig_categoria = grafico_por_categoria(df)

    st.pyplot(fig_categoria)

    fig_mes = grafico_por_mes(df)

    st.pyplot(fig_mes)


    # PREPARAÇÃO DOS DADOS PARA A IA

    dados_ia = {

        # Estatísticas gerais

        "quantidade": estatisticas["quantidade"],

        "total": estatisticas["total"],

        "media": estatisticas["media"],

        "mediana": estatisticas["mediana"],

        "minimo": estatisticas["minimo"],

        "maximo": estatisticas["maximo"],

        "variancia": estatisticas["variancia"],

        "desvio_padrao": estatisticas["desvio_padrao"],


        # Distribuição

        "distribuicao": distribuicao["distribuicao"],

        "p_valor_shapiro": distribuicao[
            "p_valor_shapiro"
        ],


        # Anomalias

        "quantidade_anomalias": len(
            anomalias["anomalias"]
        ),

        "limite_inferior": anomalias[
            "limite_inferior"
        ],

        "limite_superior": anomalias[
            "limite_superior"
        ],

        "anomalias": anomalias[
            "anomalias"
        ].to_dict(
            orient="records"
        ),


        # Categorias

        "maior_categoria": categorias[
            "maior_categoria"
        ],

        "maior_categoria_valor": categorias[
            "maior_valor"
        ],

        "categorias": categorias[
            "por_categoria"
        ].to_dict(),


        # Departamentos

        "maior_departamento": departamentos[
            "maior_departamento"
        ],

        "maior_departamento_valor": departamentos[
            "maior_valor"
        ],

        "departamentos": departamentos[
            "por_departamento"
        ].to_dict(),


        # Meses

        "maior_mes": meses[
            "maior_mes"
        ],

        "maior_mes_valor": meses[
            "maior_valor"
        ],

        "meses": meses[
            "por_mes"
        ].to_dict()
    }


    # RELATÓRIO COM IA

    st.subheader(
        "Relatório com Inteligência Artificial"
    )

    if st.button("Gerar relatório com IA"):

        with st.spinner(
            "A IA está analisando os resultados..."
        ):

            relatorio = gerar_relatorio(
                dados_ia
            )

        st.subheader(
            "Relatório administrativo"
        )

        st.write(relatorio)