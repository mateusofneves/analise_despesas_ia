import pandas as pd
import numpy as np
from scipy import stats


def analisar_distribuicao(df):
    valores = pd.to_numeric(df["Valor"], errors="coerce").dropna()

    media = valores.mean()
    desvio_padrao = valores.std()

    # Teste de normalidade
    estatistica, p_valor = stats.shapiro(valores)

    if p_valor > 0.05:
        distribuicao = "Aproximadamente normal"
    else:
        distribuicao = "Não normal"

    return {
        "media": media,
        "desvio_padrao": desvio_padrao,
        "estatistica_shapiro": estatistica,
        "p_valor_shapiro": p_valor,
        "distribuicao": distribuicao
    }