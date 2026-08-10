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
    ## 1. Leia novamente a base `iris-with-errors.csv`, faça a limpeza dos dados e remova as duas últimas colunas.
    """)
    return


if __name__ == "__main__":
    app.run()
