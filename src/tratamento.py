import pandas as pd


def verificar_dados(df):

    problemas = {}

    # Verifica valores vazios
    valores_vazios = df.isnull().sum()

    if valores_vazios.sum() > 0:
        problemas["valores_vazios"] = valores_vazios[
            valores_vazios > 0
        ].to_dict()

    # Verifica linhas duplicadas
    duplicados = df.duplicated().sum()

    if duplicados > 0:
        problemas["linhas_duplicadas"] = int(duplicados)

    return problemas