import marimo

__generated_with = "0.23.13"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np

    return mo, np, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## URLs dos datasets
    """)
    return


@app.cell
def _():
    iris_with_errors_url = r"https://raw.githubusercontent.com/disouzam/fundamentos-de-aprendizado-maquina-e-ciencia-de-dados-para-inteligencia-artificial/refs/heads/main/data-versioned/iris-with-errors.csv"
    return (iris_with_errors_url,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. Leia novamente a base `iris-with-errors.csv`, faça a limpeza dos dados e remova as duas últimas colunas.
    """)
    return


@app.cell
def _(iris_with_errors_url, read_csv_with_diagnostics):
    iris_dataset_with_errors = read_csv_with_diagnostics(iris_with_errors_url)
    return (iris_dataset_with_errors,)


@app.cell
def _(iris_dataset_with_errors):
    iris_dataset_with_errors
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Remoção de nulos e '?' no dataset
    """)
    return


@app.cell
def _(dropna_with_diagnostics, iris_dataset_with_errors, mo):
    iris_dataset_with_errors_after_dropping_na, _md_text = dropna_with_diagnostics(
        iris_dataset_with_errors
    )
    mo.md(_md_text)
    return (iris_dataset_with_errors_after_dropping_na,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Remoção de duplicatas
    """)
    return


@app.cell
def _(
    drop_duplicates_with_diagnostics,
    iris_dataset_with_errors_after_dropping_na,
    mo,
):
    iris_dataset_after_dropping_duplicates, _md_text = drop_duplicates_with_diagnostics(
        iris_dataset_with_errors_after_dropping_na
    )
    mo.md(_md_text)
    return (iris_dataset_after_dropping_duplicates,)


@app.cell
def _(iris_dataset_after_dropping_duplicates):
    iris_dataset_after_dropping_duplicates
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Remoção das últimas duas colunas
    """)
    return


@app.cell
def _(iris_dataset_after_dropping_duplicates):
    last_two_columns_iris_dataset_with_errors = list(
        iris_dataset_after_dropping_duplicates.columns
    )[-2:]
    last_two_columns_iris_dataset_with_errors
    return (last_two_columns_iris_dataset_with_errors,)


@app.cell
def _(
    iris_dataset_after_dropping_duplicates,
    last_two_columns_iris_dataset_with_errors,
):
    iris_dataset_after_dropping_duplicates_after_column_removal = (
        iris_dataset_after_dropping_duplicates.drop(
            columns=last_two_columns_iris_dataset_with_errors
        )
    )
    return (iris_dataset_after_dropping_duplicates_after_column_removal,)


@app.cell
def _(iris_dataset_after_dropping_duplicates_after_column_removal):
    iris_dataset_after_dropping_duplicates_after_column_removal
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Funções especializadas
    """)
    return


@app.cell
def _(pd):
    def read_csv_with_diagnostics(url_or_path: str):
        df = pd.read_csv(url_or_path, header=0)
        n_row, n_col = df.shape
        print(f"Númber of rows: {n_row} \nNumber of columns: {n_col}")

        return df

    return (read_csv_with_diagnostics,)


@app.cell
def _(np, pd):
    def dropna_with_diagnostics(df: pd.DataFrame):
        cleaned_dataset = df.replace("?", np.nan)
        cleaned_dataset = cleaned_dataset.dropna()

        original_shape = df.shape
        cleaned_shape = cleaned_dataset.shape

        md_text = ""
        row_change = original_shape[0] - cleaned_shape[0]
        col_change = original_shape[1] - cleaned_shape[1]

        if row_change == 0:
            md_text += "\nNão houve alteração no número de linhas do dataset.\n"
        else:
            percent_reduction = (row_change) / original_shape[0] * 100
            md_text += f"\nHouve uma redução de **{percent_reduction:.2f}%** no número de linhas com a eliminação de **{row_change}** linhas com valores ausentes.\n"

        if col_change == 0:
            md_text += "\n**Não houve alteração no número de colunas** do dataset.\n"
        else:
            percent_reduction = (col_change) / original_shape[1] * 100
            md_text += f"\nHouve uma redução de **{percent_reduction:.2f}%** no número de colunas com a eliminação de **{col_change} ** colunas com valores ausentes.\n"

        return cleaned_dataset, md_text

    return (dropna_with_diagnostics,)


@app.cell
def _(pd):
    def drop_duplicates_with_diagnostics(df: pd.DataFrame):
        md_text = ""
        cleaned_shape = df.shape
        no_duplicates_dataset = df.drop_duplicates()

        no_duplicates_shape = no_duplicates_dataset.shape

        row_change = cleaned_shape[0] - no_duplicates_shape[0]
        col_change = cleaned_shape[1] - no_duplicates_shape[1]

        if row_change == 0:
            md_text += "\nNão houve alteração no número de linhas do dataset iris.\n"
        else:
            percent_reduction = (row_change) / cleaned_shape[0] * 100
            md_text += f"\nHouve uma redução de **{percent_reduction:.2f}%** no número de linhas com a eliminação de **{row_change}** linhas duplicadas.\n"

        if col_change == 0:
            md_text += (
                "\n**Não houve alteração no número de colunas** do dataset iris.\n"
            )
        else:
            percent_reduction = (col_change) / cleaned_shape[1] * 100
            md_text += f"\nHouve uma redução de **{percent_reduction:.2f}%** no número de colunas com a eliminação de **{col_change} ** colunas duplicadas.\n"

        return no_duplicates_dataset, md_text

    return (drop_duplicates_with_diagnostics,)


if __name__ == "__main__":
    app.run()
