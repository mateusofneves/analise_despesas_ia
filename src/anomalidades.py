import pandas as pd


def detectar_anomalias(df):
    df = df.copy()

    valores = pd.to_numeric(
        df["Valor"],
        errors="coerce"
    )

    # Calcula os quartis
    q1 = valores.quantile(0.25)
    q3 = valores.quantile(0.75)

    # Intervalo interquartil
    iqr = q3 - q1

    # Limites para identificação de anomalias
    limite_inferior = q1 - (1.5 * iqr)
    limite_superior = q3 + (1.5 * iqr)

    # Identifica os valores fora dos limites
    anomalias = df[
        (valores < limite_inferior) |
        (valores > limite_superior)
    ].copy()

    return {
        "q1": q1,
        "q3": q3,
        "iqr": iqr,
        "limite_inferior": limite_inferior,
        "limite_superior": limite_superior,
        "anomalias": anomalias
    }