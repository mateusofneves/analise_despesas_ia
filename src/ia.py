import os
from dotenv import load_dotenv
from openai import OpenAI


# Carrega as variáveis do arquivo .env
load_dotenv()

# Pega a chave da API
api_key = os.getenv("OPENAI_API_KEY")

# Cria o cliente
client = OpenAI(api_key=api_key)


def perguntar_ia(pergunta):
    resposta = client.responses.create(
        model="gpt-5.6-luna",
        input=pergunta
    )

    return resposta.output_text


def gerar_relatorio(dados):
    prompt = f"""
Você é um analista administrativo especializado em análise de despesas empresariais.

Analise os resultados estatísticos abaixo e produza um relatório administrativo
claro, objetivo e profissional.

RESULTADOS DA ANÁLISE:

Quantidade de despesas: {dados['quantidade']}
Total gasto: R$ {dados['total']:.2f}
Média das despesas: R$ {dados['media']:.2f}
Mediana: R$ {dados['mediana']:.2f}
Menor despesa: R$ {dados['minimo']:.2f}
Maior despesa: R$ {dados['maximo']:.2f}
Variância: {dados['variancia']:.2f}
Desvio padrão: R$ {dados['desvio_padrao']:.2f}

Distribuição dos valores: {dados['distribuicao']}
p-valor do teste de Shapiro-Wilk: {dados['p_valor_shapiro']:.4f}

Quantidade de possíveis anomalias: {dados['quantidade_anomalias']}
Limite superior para anomalias: R$ {dados['limite_superior']:.2f}

O relatório deve conter:

1. Resumo executivo
2. Principais resultados financeiros
3. Interpretação da distribuição dos gastos
4. Análise das possíveis anomalias
5. Pontos de atenção
6. Recomendações administrativas

Não invente informações que não estejam nos dados fornecidos.
Deixe claro quando uma conclusão não puder ser determinada apenas pelos dados.
"""

    resposta = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    return resposta.output_text