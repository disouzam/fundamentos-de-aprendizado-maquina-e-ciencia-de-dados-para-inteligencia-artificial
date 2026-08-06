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

    Página 9 - Capítulo 1: Probabilidades

    ### Enunciado:

    Uma urna contém fichas numeradas de 1 a 20. Supondo que alguém escolha uma dessas fichas ao acaso, qual é a probabilidade de que a ficha escolhida contenha um número maior do que 9
    """)
    return


@app.cell
def _():
    import random as rnd

    number_of_balls = 20  # Fichas / bolas na urna

    ballot_box = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
    ]

    sucess_frequency = 0  # Número de ocorrências do número > 9

    simulation_number = 10000000

    rnd.seed(42)  # Para reproducibilidade

    for n in range(0, simulation_number):
        picked_number = rnd.choice(ballot_box)
        if picked_number > 9:
            sucess_frequency += 1

    print("Frequência =", sucess_frequency / simulation_number)
    return (rnd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Inicialização mais compacta da lista
    """)
    return


@app.cell
def _(rnd):
    number_of_balls_2 = 20  # Fichas / bolas na urna

    ballot_box_2 = list(range(1, 21, 1))

    sucess_frequency_2 = 0  # Número de ocorrências do número > 9

    simulation_number_2 = 10

    rnd.seed(42)  # Para reproducibilidade

    for n_2 in range(0, simulation_number_2):
        picked_number_2 = rnd.choice(ballot_box_2)
        if picked_number_2 > 9:
            sucess_frequency_2 += 1

    print("Frequência =", sucess_frequency_2 / simulation_number_2)
    return


if __name__ == "__main__":
    app.run()
