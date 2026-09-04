import pandas as pd


def calcular_estatisticas(df):
    valores = pd.to_numeric(
        df["Valor"],
        errors="coerce"
    ).dropna()

    estatisticas = {
        "quantidade": len(valores),
        "total": valores.sum(),
        "media": valores.mean(),
        "mediana": valores.median(),
        "minimo": valores.min(),
        "maximo": valores.max(),
        "variancia": valores.var(),
        "desvio_padrao": valores.std()
    }

    return estatisticas


def analisar_categorias(df):
    dados = df.groupby("Categoria")["Valor"].sum()

    dados = dados.sort_values(ascending=False)

    return {
        "por_categoria": dados,
        "maior_categoria": dados.index[0],
        "maior_valor": dados.iloc[0]
    }


def analisar_departamentos(df):
    dados = df.groupby("Departamento")["Valor"].sum()

    dados = dados.sort_values(ascending=False)

    return {
        "por_departamento": dados,
        "maior_departamento": dados.index[0],
        "maior_valor": dados.iloc[0]
    }


def analisar_meses(df):
    df = df.copy()

    # Converte a data para datetime
    df["Data"] = pd.to_datetime(
        df["Data"],
        errors="coerce"
    )

    # Agrupa cronologicamente pela data
    dados = (
        df.dropna(subset=["Data"])
        .groupby(df["Data"].dt.to_period("M"))["Valor"]
        .sum()
    )

    # Converte o índice para texto
    dados.index = dados.index.astype(str)

    return {
        "por_mes": dados,
        "maior_mes": dados.idxmax(),
        "maior_valor": dados.max()
    }