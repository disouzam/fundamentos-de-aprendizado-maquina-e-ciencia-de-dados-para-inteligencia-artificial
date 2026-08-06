import marimo

__generated_with = "0.23.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd

    return mo, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Leitura de uma base de dados com problemas artificialmente introduzidos
    """)
    return


@app.cell
def _(pd):
    iris_dataset = pd.read_csv("data/iris-with-errors.csv", header=0)
    n_row_iris, n_col_iris = iris_dataset.shape
    print(f"Númber of rows: {n_row_iris} \nNumber of columns: {n_col_iris}")
    return (iris_dataset,)


@app.cell
def _(iris_dataset):
    iris_dataset.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Inspeção dos dados

    - Número de Linhas e colunas disponíveis (já processado acima pela propriedade shape do dataframe `iris_dataset`)
    - Nomes das variáveis
    - Tipos das colunas (quais são numéricas e quais são categóricas)
    - Qualidade do dataset (valores ausentes? valores duplicados?)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Colunas da base de dados
    """)
    return


@app.cell
def _(iris_dataset, mo):
    iris_cols = list(iris_dataset.columns)

    _md_text = ""
    for _col in iris_cols:
        _md_text += f"\n1. {_col}"

    mo.md(f"As colunas que existem no iris_dataset são: {_md_text}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Tipos de dados das colunas
    """)
    return


@app.cell
def _(iris_dataset, mo):
    iris_data_types = iris_dataset.dtypes

    _md_text = ""

    for col_name, col_type in iris_data_types.items():
        _md_text += f"\n1. **{col_name}**: {col_type}"

    mo.md(f"Os tipos de dados de cada coluna estão listados abaixo: {_md_text}")
    return


if __name__ == "__main__":
    app.run()
