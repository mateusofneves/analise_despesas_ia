import pandas as pd

def ler_excel(arquivo):
    
    """
    Lê um arquivo Excel e retorna um DataFrame do pandas.

    Parâmetros:
    arquivo (str): O caminho para o arquivo Excel.

    Retorna:
    pd.DataFrame: Um DataFrame contendo os dados do arquivo Excel.
    """
    try:
        df = pd.read_excel(arquivo)
        return df
    except Exception as e:
        print(f"Erro ao ler o arquivo Excel: {e}")
        return None