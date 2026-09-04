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