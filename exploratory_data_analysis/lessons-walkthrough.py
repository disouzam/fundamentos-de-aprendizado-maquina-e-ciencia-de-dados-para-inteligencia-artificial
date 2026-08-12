import marimo

__generated_with = "0.23.13"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    _Nota: esse notebook contém códigos extraídos e/ou adaptados da lição sobre Análise Exploratória de Dados, do professor Francisco Rodrigues (ICMC-USP) - @prof-francisco-rodrigues - https://github.com/prof-francisco-rodrigues. Parte das adaptações deve-se às necessidades do marimo para gerir as dependências entre células; parte é customização / adições que introduzi para seguir minhas preferências de estilo de codificação._
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Histograma de frequências
    """)
    return


@app.cell
def _():
    import matplotlib.pyplot as plt

    numbers_list = [
        21,
        22,
        23,
        4,
        5,
        6,
        77,
        8,
        9,
        10,
        31,
        32,
        33,
        34,
        35,
        36,
        37,
        18,
        49,
        50,
        100,
    ]

    _, axes = plt.subplots(1, 2, figsize=(10, 6))

    axes[0].hist(numbers_list, bins=10, density=False, edgecolor="black", alpha=0.7)
    axes[0].set_xlabel("Valores de x")
    axes[0].set_ylabel("Frequência")
    axes[0].set_title("Frequência absoluta")

    axes[1].hist(numbers_list, bins=10, density=True, edgecolor="black", alpha=0.7)
    axes[1].set_xlabel("Valores de x")
    axes[1].set_ylabel("Densidade")
    axes[1].set_title("Frequência relativa")

    plt.tight_layout(w_pad=3)
    plt.show()
    return (plt,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Gráfico de barras para variáveis categóricas
    """)
    return


@app.cell
def _(plt):
    import pandas as pd

    assessment_list = [
        "Bom",
        "Ruim",
        "Ótimo",
        "Regular",
        "Regular",
        "Ótimo",
        "Ótimo",
        "Bom",
        "Ótimo",
        "Bom",
        "Ótimo",
    ]

    assessment_series = pd.Series(assessment_list)

    frequencies = assessment_series.value_counts().sort_index()

    _, ax_bar_plot = plt.subplots()
    ax_bar_plot.bar(frequencies.index, frequencies)
    ax_bar_plot.set_xlabel("Categoria")
    ax_bar_plot.set_ylabel("Frequência")
    ax_bar_plot.set_title("Frequência das respostas")
    ax_bar_plot.tick_params("x", rotation=45)
    ax_bar_plot.tick_params("y", rotation=45)
    plt.show()
    return frequencies, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ordenação das barras pela frequência absoluta
    """)
    return


@app.cell
def _(frequencies, plt):
    sorted_frequencies = frequencies.copy()
    sorted_frequencies = sorted_frequencies.sort_values(ascending=False)

    _, ax_bar_plot2 = plt.subplots()
    ax_bar_plot2.bar(sorted_frequencies.index, sorted_frequencies)
    ax_bar_plot2.set_xlabel("Categoria")
    ax_bar_plot2.set_ylabel("Frequência")
    ax_bar_plot2.set_title("Frequência das respostas")
    ax_bar_plot2.tick_params("x", rotation=45)
    ax_bar_plot2.tick_params("y", rotation=45)
    plt.show()
    return (sorted_frequencies,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Gráfico de setores (ou de pizza)
    """)
    return


@app.cell
def _(frequencies, plt, sorted_frequencies):
    _, ax_pizza_chart = plt.subplots(1, 2, figsize=(10, 6))

    ax_pizza_chart[0].set_title("Proporção das respostas - Ordenadas por valor")
    ax_pizza_chart[0].pie(
        sorted_frequencies,
        labels=sorted_frequencies.index,
        autopct="%1.1f%%",
        startangle=0,
    )

    ax_pizza_chart[1].set_title("Proporção das respostas - Ordenadas por índice")
    ax_pizza_chart[1].pie(
        frequencies, labels=frequencies.index, autopct="%1.1f%%", startangle=0
    )

    plt.tight_layout(w_pad=3)
    plt.axis("equal")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Gráfico de dispersão (scatter plot)
    """)
    return


@app.cell
def _(plt):
    import numpy as np

    number_of_points = 100
    np.random.seed(42)
    x_values = np.linspace(-1, 1, number_of_points)
    noise = np.random.uniform(-1, 1, number_of_points)
    sigma = 0.5

    y_values = 0.8 * x_values + sigma * noise

    _, ax_scatterplot = plt.subplots(1, 1, figsize=(7, 5))
    ax_scatterplot.scatter(x_values, y_values, s=100, edgecolor="black", alpha=0.8)
    ax_scatterplot.set_xlabel("X")
    ax_scatterplot.set_ylabel("Y")
    ax_scatterplot.set_title("Exemplo de scatterplot")
    ax_scatterplot.grid(True)
    plt.show()
    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Mapa de calor (ou heatmap)
    """)
    return


@app.cell
def _(np, plt):
    import seaborn as sns

    array = np.array(
        [
            [0.1234, 1.4567, 0.7890, 0.1234],
            [0.9876, 0.0000, 0.5432, 0.6789],
            [0.1111, 0.2222, 0.0000, 0.3333],
            [0.4444, 0.5555, 0.6666, 0.0000],
        ]
    )

    _, ax_heatmap = plt.subplots(1, 1, figsize=(7, 5))
    sns.heatmap(array, annot=True, fmt=".2f", cmap="viridis", ax=ax_heatmap)
    ax_heatmap.set_title("Exemplo de mapa de calor")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Medidas de posição
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Moda
    """)
    return


@app.cell
def _(mo):
    from collections import Counter

    numbers_list2 = [1, 2, 3, 1, 2, 3, 4, 1, 3, 6, 4, 1]

    counting = Counter(numbers_list2)
    mode = counting.most_common(1)[0]

    _md_text = f"**Dados**: {numbers_list2}\n"
    _md_text += f"\n**Frequências**: {counting}\n"
    _md_text += f"\n**Moda**: {mode[0]} — aparece **{mode[1]}** vezes"
    mo.md(_md_text)
    return (Counter,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dados multimodais
    """)
    return


@app.cell
def _(Counter, mo):
    numbers_list3 = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4]

    counting_3 = Counter(numbers_list3)

    greatest_frequency = max(counting_3.values())

    modes_3 = [
        value for value, freq in counting_3.items() if freq == greatest_frequency
    ]

    _md_text = f"**Dados**: {numbers_list3}\n"
    _md_text += f"\n**Frequências**: {counting_3}\n"
    _md_text += f"\n**Moda**: {modes_3}"
    mo.md(_md_text)
    return (numbers_list3,)


@app.cell
def _(numbers_list3, pd, plt):
    frequencies_of_numbers_list_3 = pd.Series(numbers_list3).value_counts().sort_index()

    _, ax_bar_plot3 = plt.subplots()
    ax_bar_plot3.bar(frequencies_of_numbers_list_3.index, frequencies_of_numbers_list_3)

    ax_bar_plot3.set_xlabel("Valor")
    ax_bar_plot3.set_ylabel("Frequência")
    ax_bar_plot3.set_title("Frequência dos valores de X")
    ax_bar_plot3.tick_params("x", rotation=45)
    ax_bar_plot3.tick_params("y", rotation=45)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Média e mediana
    """)
    return


@app.cell
def _(np):
    numbers_list4 = [1, 1, 1, 2, 2, 3, 4, 5, 5, 5]

    print("Dados:", numbers_list4)
    print("Média:", np.mean(numbers_list4))
    print("Mediana:", np.median(numbers_list4))
    return (numbers_list4,)


@app.cell
def _(np, numbers_list4):
    numbers_list5 = numbers_list4.copy()
    numbers_list5[-1] = 5 * 20

    print("Dados com valor extremo:", numbers_list5)
    print("Média:", np.mean(numbers_list5))
    print("Mediana:", np.median(numbers_list5))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Média e mediana em distribuições diferentes
    """)
    return


@app.cell
def _(np, plt):
    Y_normal = np.random.normal(loc=0, scale=10, size=500)

    media_normal = np.mean(Y_normal)
    mediana_normal = np.median(Y_normal)

    Y_exp = np.random.exponential(scale=1, size=500)

    media_exp = np.mean(Y_exp)
    mediana_exp = np.median(Y_exp)

    _, mean_medians_charts = plt.subplots(1, 2, figsize=(10, 6))

    mean_medians_charts[0].hist(
        Y_normal, bins=25, density=True, edgecolor="black", alpha=0.7
    )
    mean_medians_charts[0].axvline(
        media_normal, color="blue", label="Média", linewidth=2
    )
    mean_medians_charts[0].axvline(
        mediana_normal, color="red", label="Mediana", linewidth=2, linestyle="--"
    )
    mean_medians_charts[0].set_xlabel("x")
    mean_medians_charts[0].set_ylabel("Densidade")
    mean_medians_charts[0].set_title("Distribuição normal: média e mediana")

    mean_medians_charts[1].hist(
        Y_exp, bins=25, density=True, edgecolor="black", alpha=0.7
    )
    mean_medians_charts[1].axvline(media_exp, color="blue", label="Média", linewidth=2)
    mean_medians_charts[1].axvline(
        mediana_exp, color="red", label="Mediana", linewidth=2, linestyle="--"
    )
    mean_medians_charts[1].set_xlabel("x")
    mean_medians_charts[1].set_ylabel("Densidade")
    mean_medians_charts[1].set_title("Distribuição exponencial: média e mediana")
    mean_medians_charts[1].legend()

    plt.tight_layout(w_pad=3)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Quantis
    """)
    return


@app.cell
def _(np):
    numbers_list6 = [1, 1, 1, 2, 2, 3, 4, 5, 5, 100]

    q1 = np.quantile(numbers_list6, 0.25)
    q2 = np.quantile(numbers_list6, 0.50)
    q3 = np.quantile(numbers_list6, 0.75)

    print("Dados:", numbers_list6)
    print("Média:", np.mean(numbers_list6))
    print("Mediana:", np.median(numbers_list6))
    print("Primeiro quartil Q1:", q1)
    print("Segundo quartil Q2:", q2)
    print("Terceiro quartil Q3:", q3)
    print("Intervalo interquartil IQR:", q3 - q1)
    return (numbers_list6,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Boxplot
    """)
    return


@app.cell
def _(np, numbers_list6, plt):
    _, boxplots = plt.subplots(1, 2, figsize=(10, 6))

    boxplots[0].boxplot(numbers_list6)
    boxplots[0].set_ylabel("Valores")
    boxplots[0].set_xlabel("Lista pequena")
    boxplots[0].set_xticklabels([f"n={len(numbers_list6)}"])
    boxplots[0].set_title("Exemplo de boxplot para uma lista pequena")

    large_list = np.random.normal(loc=100, scale=20, size=200)

    boxplots[1].boxplot(large_list)
    boxplots[1].set_ylabel("Valores")
    boxplots[1].set_xlabel("Lista grande")
    boxplots[1].set_xticklabels([f"n={len(large_list)}"])
    boxplots[1].set_title("Exemplo de boxplot para uma lista grande")

    plt.show()
    return


if __name__ == "__main__":
    app.run()
