import matplotlib.pyplot as plt


def grafico_por_categoria(df):
    dados = df.groupby("Categoria")["Valor"].sum()

    fig, ax = plt.subplots()

    dados.sort_values(ascending=False).plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Despesas por Categoria")
    ax.set_xlabel("Categoria")
    ax.set_ylabel("Valor (R$)")

    plt.xticks(rotation=45)
    plt.tight_layout()

    return fig


def grafico_por_mes(df):
    dados = df.groupby("Mês")["Valor"].sum()

    fig, ax = plt.subplots()

    dados.plot(
        kind="line",
        marker="o",
        ax=ax
    )

    ax.set_title("Despesas por Mês")
    ax.set_xlabel("Mês")
    ax.set_ylabel("Valor (R$)")

    plt.tight_layout()

    return fig