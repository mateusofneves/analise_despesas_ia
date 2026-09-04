# Análise de Despesas com Inteligência Artificial

Sistema desenvolvido em **Python** para análise de despesas administrativas utilizando **Estatística, Probabilidade e Inteligência Artificial**.

A aplicação recebe uma planilha Excel, processa os dados, realiza análises estatísticas, identifica possíveis anomalias e utiliza IA para interpretar os resultados e gerar um **relatório administrativo**.

---

## Objetivo

Transformar dados de despesas em informações úteis para apoiar a tomada de decisões administrativas.

O diferencial do projeto é que a **análise estatística é realizada pelo Python**, enquanto a **Inteligência Artificial interpreta os resultados** e gera o relatório.

### Fluxo

```text
Excel
 ↓
Leitura e validação
 ↓
Análise estatística
 ↓
Distribuição dos dados
 ↓
Detecção de anomalias
 ↓
Análise por categoria, departamento e mês
 ↓
Gráficos
 ↓
Inteligência Artificial
 ↓
Relatório administrativo
```

---

## Funcionalidades

- Importação de arquivos Excel (`.xlsx`)
- Validação dos dados
- Estatística descritiva
- Análise por categoria
- Análise por departamento
- Análise mensal
- Teste de normalidade de Shapiro-Wilk
- Detecção de possíveis anomalias utilizando IQR
- Geração de gráficos
- Interpretação dos resultados com Inteligência Artificial
- Geração automática de relatório administrativo

---

## Análises Estatísticas

O sistema calcula:

- Quantidade de despesas
- Total gasto
- Média
- Mediana
- Menor valor
- Maior valor
- Variância
- Desvio padrão

Também é analisada a distribuição dos valores utilizando o teste de **Shapiro-Wilk**.

Quando os dados apresentam comportamento não normal, o sistema utiliza o **Intervalo Interquartil (IQR)** para identificar possíveis valores atípicos.

> Uma anomalia estatística não significa necessariamente fraude ou erro. Ela representa um valor que merece investigação.

---

## Inteligência Artificial

Após realizar os cálculos, o sistema envia para a IA apenas os resultados relevantes da análise, e não a planilha inteira.

A IA atua como um analista administrativo, interpretando:

- Resultados financeiros
- Distribuição dos dados
- Categorias
- Departamentos
- Evolução mensal
- Possíveis anomalias

O relatório gerado apresenta:

- Resumo executivo
- Análise financeira
- Análise da distribuição
- Análise por categoria
- Análise por departamento
- Evolução mensal
- Possíveis anomalias
- Pontos de atenção
- Recomendações
- Conclusão

A IA é instruída a **não inventar informações** e a **diferenciar resultados estatísticos de interpretações**.

---

## Aplicação

O sistema pode ser aplicado em empresas para auxiliar na análise de:

- Despesas administrativas
- Gastos por departamento
- Gastos por categoria
- Evolução dos custos
- Valores fora do comportamento esperado

A proposta é reduzir a análise manual de planilhas e facilitar a identificação de informações relevantes para gestores.

---

## Tecnologias

- Python
- Pandas
- NumPy
- SciPy
- Matplotlib
- OpenPyXL
- Streamlit
- OpenAI API
- python-dotenv

---

## Estrutura

```text
analise_despesas_ia/
│
├── app.py
├── data/
│   └── exemplo_despesas.xlsx
│
├── src/
│   ├── leitura.py
│   ├── tratamento.py
│   ├── estatistica.py
│   ├── distribuicoes.py
│   ├── anomalidades.py
│   ├── graficos.py
│   ├── ia.py
│   └── relatorio.py
│
├── outputs/
│   ├── graficos/
│   └── relatorios/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Como executar

1. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

2. Configure a chave da API no arquivo `.env`:

   ```env
   OPENAI_API_KEY=sua_chave_aqui
   ```

3. Execute a aplicação:

   ```bash
   streamlit run app.py
   ```

4. Depois, basta acessar a aplicação pelo navegador e enviar uma planilha `.xlsx`.

> ⚠️ O arquivo `.env` não deve ser enviado para o GitHub.

---

## Aplicação Acadêmica

O projeto demonstra a aplicação prática de conceitos de:

- Probabilidade
- Distribuições de probabilidade
- Estatística
- Análise de dados
- Inteligência Artificial
- Visualização de dados

A proposta conecta conceitos matemáticos a um problema administrativo realista, utilizando Python para realizar a análise e IA para interpretar os resultados.

---

## Próximas Atualizações

Entre as melhorias planejadas estão:

- Dashboard mais moderno
- Novos tipos de gráficos
- Exportação dos relatórios em PDF/DOCX
- Filtros e análises mais avançadas
- Recomendações mais específicas
- Previsão de despesas utilizando Machine Learning
- Novos métodos de detecção de anomalias
- Integração com bancos de dados e APIs

---

## Conclusão

O projeto demonstra como **Estatística + Probabilidade + Inteligência Artificial** podem ser combinadas para transformar dados brutos em informações úteis para uma organização.

O Python realiza os cálculos e análises quantitativas, enquanto a IA transforma esses resultados em uma interpretação clara e em um relatório administrativo.

Assim, a aplicação funciona como uma ferramenta de apoio à análise e tomada de decisão baseada em dados.