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
Você é um analista administrativo especializado em análise
estatística e financeira de despesas empresariais.

Sua tarefa é interpretar os resultados calculados previamente
por um sistema Python e produzir um relatório administrativo
profissional.

IMPORTANTE:
- Não invente informações.
- Não suponha causas que não estejam nos dados.
- Uma anomalia estatística NÃO significa necessariamente fraude,
  erro ou irregularidade.
- Diferencie fatos observados de interpretações.
- Utilize os valores fornecidos para justificar suas conclusões.
- Seja objetivo e profissional.

========================
ESTATÍSTICAS GERAIS
========================

Quantidade de despesas: {dados['quantidade']}
Total gasto: R$ {dados['total']:.2f}
Média: R$ {dados['media']:.2f}
Mediana: R$ {dados['mediana']:.2f}
Menor despesa: R$ {dados['minimo']:.2f}
Maior despesa: R$ {dados['maximo']:.2f}
Variância: {dados['variancia']:.2f}
Desvio padrão: R$ {dados['desvio_padrao']:.2f}

========================
DISTRIBUIÇÃO
========================

Classificação da distribuição:
{dados['distribuicao']}

p-valor do teste de Shapiro-Wilk:
{dados['p_valor_shapiro']:.4f}

========================
ANOMALIAS
========================

Quantidade de possíveis anomalias:
{dados['quantidade_anomalias']}

Limite inferior:
R$ {dados['limite_inferior']:.2f}

Limite superior:
R$ {dados['limite_superior']:.2f}

Possíveis despesas anômalas encontradas:

{dados['anomalias']}

========================
CATEGORIAS
========================

Categoria com maior gasto:
{dados['maior_categoria']}

Valor:
R$ {dados['maior_categoria_valor']:.2f}

Ranking de categorias:
{dados['categorias']}

========================
DEPARTAMENTOS
========================

Departamento com maior gasto:
{dados['maior_departamento']}

Valor:
R$ {dados['maior_departamento_valor']:.2f}

Ranking de departamentos:
{dados['departamentos']}

========================
ANÁLISE MENSAL
========================

Mês com maior gasto:
{dados['maior_mes']}

Valor:
R$ {dados['maior_mes_valor']:.2f}

Gastos por mês:
{dados['meses']}

========================
ANÁLISE
========================

Produza o relatório com as seguintes seções:

1. Resumo executivo

Apresente os principais resultados encontrados,
destacando total gasto, quantidade de despesas e
principais pontos de atenção.

2. Análise financeira

Interprete média, mediana, desvio padrão e amplitude
dos valores.

3. Análise da distribuição

Explique o resultado do teste de Shapiro-Wilk e o que
a distribuição encontrada significa para a análise.

4. Análise por categoria

Identifique a categoria com maior impacto financeiro
e destaque diferenças relevantes entre as categorias.

5. Análise por departamento

Identifique o departamento com maior gasto e destaque
os principais resultados encontrados.

6. Evolução mensal

Analise o comportamento dos gastos ao longo dos meses
e destaque períodos de maior ou menor gasto.

7. Possíveis anomalias

Explique a quantidade de possíveis anomalias,
os limites estatísticos utilizados e cite as principais
despesas identificadas.

Deixe claro que anomalias são pontos que merecem investigação,
não evidências de fraude ou irregularidade.

8. Pontos de atenção

Liste os principais pontos que um responsável administrativo
deveria acompanhar.

9. Recomendações

Apresente recomendações práticas baseadas exclusivamente
nos resultados disponíveis.

10. Conclusão

Faça uma conclusão curta sobre o comportamento geral
das despesas.

Utilize títulos, subtítulos e listas quando ajudarem
na organização.

O relatório deve ter linguagem profissional, adequada
para apresentação a um gestor ou responsável administrativo.
"""

    resposta = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    return resposta.output_text