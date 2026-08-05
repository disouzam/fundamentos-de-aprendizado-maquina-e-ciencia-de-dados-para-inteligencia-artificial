import marimo

__generated_with = "0.23.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exemplo e códigos do livro Probabilidade e Estatística: Teoria, Simulação e Dados

    **Disponível para compra pelo link:** https://loja.uiclap.com/titulo/ua158988

    Página 10 - Capítulo 1: Probabilidades
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Simulação do lançamento de uma moeda
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    import random as rnd

    frequencies = []
    simulations = []

    max_simulations = 1000
    simulations_index = np.arange(1, max_simulations + 1)

    probability = 0.5
    coin = ["head", "tail"]
    rnd.seed(42)

    # Simulation
    for sim in simulations_index:
        heads = 0

        for flip in range(0, sim):
            flip_result = rnd.choice(coin)
            if flip_result == "head":
                heads += 1

        frequencies.append(heads / sim)
        simulations.append(sim)

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.xlim([0, max_simulations])
    plt.ylim([0, 1])
    plt.plot(
        simulations,
        frequencies,
        linestyle="-",
        color="blue",
        linewidth=2,
        label="Valor simulado",
    )
    plt.axhline(y=probability, color="black", linestyle="--", label="Valor teórico")
    plt.ylabel("Fraction of heads", fontsize=20)
    plt.xlabel("Number of experiments", fontsize=20)
    plt.legend(fontsize=15)
    return


if __name__ == "__main__":
    app.run()
