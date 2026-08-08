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
    # Inspeção dos dados

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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Valores ausentes
    """)
    return


@app.cell
def _(iris_dataset, mo):
    absent_data_values = iris_dataset.isna().sum()

    _md_text = ""

    columns_with_no_absent_values = []
    for _col_name, number_of_absent_values in absent_data_values.items():
        if number_of_absent_values == 0:
            columns_with_no_absent_values.append(_col_name)
        else:
            _md_text += f"\n1. **{_col_name}**: {number_of_absent_values}"

    _md_text = f"O número de valores ausentes por coluna são: {_md_text}"

    _md_text += "\n\nAs colunas abaixo não possuem valores ausentes: "
    for _col_name in columns_with_no_absent_values:
        _md_text += f"\n1. **{_col_name}**"

    mo.md(_md_text)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Remoção de valores ausentes
    """)
    return


@app.cell
def _(iris_dataset, mo):
    cleaned_iris_dataset = iris_dataset.dropna()

    original_shape = iris_dataset.shape
    cleaned_shape = cleaned_iris_dataset.shape

    _md_text = ""
    _row_change = original_shape[0] - cleaned_shape[0]
    _col_change = original_shape[1] - cleaned_shape[1]

    if _row_change == 0:
        _md_text += "\nNão houve alteração no número de linhas do dataset iris.\n"
    else:
        _percent_reduction = (_row_change) / original_shape[0] * 100
        _md_text += f"\nHouve uma redução de **{_percent_reduction:.2f}%** no número de linhas com a eliminação de **{_row_change}** linhas com valores ausentes.\n"

    if _col_change == 0:
        _md_text += "\n**Não houve alteração no número de colunas** do dataset iris.\n"
    else:
        _percent_reduction = (_col_change) / original_shape[1] * 100
        _md_text += f"\nHouve uma redução de **{_percent_reduction:.2f}%** no número de colunas com a eliminação de **{_col_change} ** colunas com valores ausentes.\n"

    mo.md(_md_text)
    return cleaned_iris_dataset, cleaned_shape


@app.cell
def _(cleaned_iris_dataset):
    cleaned_iris_dataset.head(25)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Identificação e remoção de linhas duplicadas
    """)
    return


@app.cell
def _(cleaned_iris_dataset, mo):
    duplicated_rows_mask = cleaned_iris_dataset.duplicated()
    number_of_duplicated_values = duplicated_rows_mask.sum()

    mo.md(f"As {number_of_duplicated_values} linhas listadas abaixo são duplicatas:")
    return (duplicated_rows_mask,)


@app.cell
def _(cleaned_iris_dataset, duplicated_rows_mask):
    cleaned_iris_dataset[duplicated_rows_mask]
    return


@app.cell
def _(cleaned_iris_dataset, cleaned_shape, mo):
    _md_text = ""
    no_duplicates_iris_dataset = cleaned_iris_dataset.drop_duplicates()

    no_duplicates_shape = no_duplicates_iris_dataset.shape

    _row_change = cleaned_shape[0] - no_duplicates_shape[0]
    _col_change = cleaned_shape[1] - no_duplicates_shape[1]

    if _row_change == 0:
        _md_text += "\nNão houve alteração no número de linhas do dataset iris.\n"
    else:
        _percent_reduction = (_row_change) / cleaned_shape[0] * 100
        _md_text += f"\nHouve uma redução de **{_percent_reduction:.2f}%** no número de linhas com a eliminação de **{_row_change}** linhas duplicadas.\n"

    if _col_change == 0:
        _md_text += "\n**Não houve alteração no número de colunas** do dataset iris.\n"
    else:
        _percent_reduction = (_col_change) / cleaned_shape[1] * 100
        _md_text += f"\nHouve uma redução de **{_percent_reduction:.2f}%** no número de colunas com a eliminação de **{_col_change} ** colunas duplicadas.\n"

    mo.md(_md_text)
    return


if __name__ == "__main__":
    app.run()
