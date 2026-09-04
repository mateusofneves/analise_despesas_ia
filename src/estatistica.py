import pandas as pd


def calcular_estatisticas(df):
    valores = pd.to_numeric(df["Valor"], errors="coerce").dropna()

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
    dados = df.groupby("Mês")["Valor"].sum()

    dados = dados.sort_values(ascending=False)

    return {
        "por_mes": dados,
        "maior_mes": dados.index[0],
        "maior_valor": dados.iloc[0]
    }