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
    ## Extraído do livro Probabilidade e Estatística: Teoria, Simulação e Dados from Professor Francisco Rodrigues, ICMC-USP
    ### Disponível para compra nesse link: https://loja.uiclap.com/titulo/ua158988
    """)
    return


@app.cell
def _():
    import random

    # W: white ball,
    # B: Black ball
    ballot_box = ["W"] * 3000 + ["B"] * 2000

    number_of_simulations = 10000

    black_ball_abs_frequency = 0

    for simulation_index in range(0, number_of_simulations):
        ball = random.choice(ballot_box)
        if ball == "B":
            black_ball_abs_frequency += 1

    black_ball_relative_frequency = black_ball_abs_frequency / number_of_simulations

    print(f"Frequência de bolas prestas: {black_ball_relative_frequency:.2f}")
    return


if __name__ == "__main__":
    app.run()
