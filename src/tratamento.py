import pandas as pd


def verificar_dados(df):
    problemas = {}

    # Colunas obrigatórias
    colunas_obrigatorias = [
        "Data",
        "Mês",
        "Categoria",
        "Descrição",
        "Valor",
        "Departamento",
        "Forma de pagamento"
    ]

    colunas_faltantes = [
        coluna
        for coluna in colunas_obrigatorias
        if coluna not in df.columns
    ]

    if colunas_faltantes:
        problemas["colunas_faltantes"] = colunas_faltantes

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

    # Verifica se os valores são numéricos
    if "Valor" in df.columns:
        valores_invalidos = pd.to_numeric(
            df["Valor"],
            errors="coerce"
        ).isnull().sum()

        if valores_invalidos > 0:
            problemas["valores_invalidos"] = int(valores_invalidos)

    # Verifica datas
    if "Data" in df.columns:
        datas_invalidas = pd.to_datetime(
            df["Data"],
            errors="coerce"
        ).isnull().sum()

        if datas_invalidas > 0:
            problemas["datas_invalidas"] = int(datas_invalidas)

    return problemas