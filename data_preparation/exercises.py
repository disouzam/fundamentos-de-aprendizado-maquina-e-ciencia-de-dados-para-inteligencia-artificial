import marimo

__generated_with = "0.23.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import MinMaxScaler, StandardScaler

    return MinMaxScaler, StandardScaler, mo, np, pd


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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Tratamento de valores faltantes

    ## _Alternativas para cenários complexos_

    Valores faltantes podem aparecer como:

    - ?
    - -
    - NA
    - None

    além do clássico caso de **NaN** tratado acima
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Nova leitura do dataset iris
    """)
    return


@app.cell
def _(pd):
    iris_dataset_2 = pd.read_csv("data/iris-with-errors.csv", header=0)
    iris_dataset_2
    return (iris_dataset_2,)


@app.cell
def _(iris_dataset_2, np):
    iris_dataset_2_cleaned = iris_dataset_2.replace("?", np.nan)

    print("Valores ausentes por coluna após substituir '?':")
    print(iris_dataset_2_cleaned.isna().sum())

    iris_dataset_2_cleaned.head(25)
    return (iris_dataset_2_cleaned,)


@app.cell
def _(iris_dataset_2_cleaned):
    iris_dataset_2_after_drops = iris_dataset_2_cleaned.dropna().drop_duplicates()

    print("Dimensão original:", iris_dataset_2_cleaned.shape)
    print("Dimensão após limpeza:", iris_dataset_2_after_drops.shape)

    iris_dataset_2_after_drops.head(25)
    return (iris_dataset_2_after_drops,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Remoção de linhas e colunas específicas
    """)
    return


@app.cell
def _(iris_dataset_2_after_drops):
    iris_dataset_3 = iris_dataset_2_after_drops.copy()

    print("Atributos atuais:", list(iris_dataset_3.columns))
    print("Colunas que serão removidas:", list(iris_dataset_3.columns[[1, 3]]))

    iris_dataset_3 = iris_dataset_3.drop(iris_dataset_3.columns[[1, 3]], axis=1)
    iris_dataset_3.head(25)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Remoção de linhas
    """)
    return


@app.cell
def _(iris_dataset_2_after_drops):
    iris_dataset_2_after_drop_rows = iris_dataset_2_after_drops.copy()

    removed_index = iris_dataset_2_after_drop_rows.index[[0, 2, 5]]
    print("Índices que serão removidos:", list(removed_index))

    iris_dataset_2_after_drop_rows = iris_dataset_2_after_drop_rows.drop(
        removed_index, axis=0
    )
    iris_dataset_2_after_drop_rows.head(25)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Substituição de valores ausentes
    """)
    return


@app.cell
def _(np, pd):
    iris_dataset_4 = pd.read_csv("data/iris-with-errors.csv", header=0)
    iris_dataset_4 = iris_dataset_4.replace("?", np.nan)

    print("Dimensão da base:", iris_dataset_4.shape)
    iris_dataset_4.head(25)
    return (iris_dataset_4,)


@app.cell
def _(iris_dataset_4, np):
    array = np.array(iris_dataset_4[iris_dataset_4.columns[:-1]], dtype=float)
    array
    return (array,)


@app.cell
def _(array, np):
    column_means = np.nanmean(array, axis=0)
    column_means
    return (column_means,)


@app.cell
def _(array, column_means, np):
    filled_array = array.copy()

    for _row in range(filled_array.shape[0]):
        for _col in range(filled_array.shape[1]):
            if np.isnan(filled_array[_row, _col]):
                filled_array[_row, _col] = column_means[_col]

    print("Matriz após a substituição dos valores ausentes por médias das colunas:")
    print(filled_array)
    return (filled_array,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Reconstrução do dataframe a partir do array multidimensional preenchido:
    """)
    return


@app.cell
def _(filled_array, iris_dataset_4, pd):
    iris_dataset_5 = pd.DataFrame(
        filled_array, columns=list(iris_dataset_4.columns[:-1])
    )
    iris_dataset_5
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Substituição usando a função `fillna()`:
    """)
    return


@app.cell
def _(np, pd):
    iris_dataset_6 = pd.read_csv("data/iris-with-errors.csv", header=0)
    iris_dataset_6 = iris_dataset_6.replace("?", np.nan)

    _columns = iris_dataset_6.columns[:-1]

    iris_dataset_6[_columns] = iris_dataset_6[_columns].astype(float)

    iris_dataset_7 = iris_dataset_6.copy()
    iris_dataset_7[_columns] = iris_dataset_7[_columns].fillna(
        iris_dataset_7[_columns].mean()
    )

    iris_dataset_7
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Normalização e padronização
    """)
    return


@app.cell
def _(pd):
    full_iris_dataset = pd.read_csv("data/iris.csv", header=0)

    print("Número de linhas e colunas:", full_iris_dataset.shape)
    full_iris_dataset.head()
    return (full_iris_dataset,)


@app.cell
def _(full_iris_dataset, np):
    full_iris_dataset_numeric_columns = np.array(
        full_iris_dataset[full_iris_dataset.columns[:-1]], dtype=float
    )
    categoric_column = full_iris_dataset[full_iris_dataset.columns[-1]]

    print("Dimensão da matriz de atributos:", full_iris_dataset_numeric_columns.shape)
    print("Classes:", np.unique(categoric_column))
    return (full_iris_dataset_numeric_columns,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Normalização
    """)
    return


@app.cell
def _(MinMaxScaler, full_iris_dataset_numeric_columns):
    for i in range(full_iris_dataset_numeric_columns.shape[1]):
        print(
            f"Coluna {i}: mínimo = {full_iris_dataset_numeric_columns[:, i].min():.2f}, máximo = {full_iris_dataset_numeric_columns[:, i].max():.2f}"
        )

    scaler_minmax = MinMaxScaler(feature_range=(0, 1))
    normalized_columns = scaler_minmax.fit_transform(full_iris_dataset_numeric_columns)

    print("\nDados normalizados:")
    print(normalized_columns[:10])
    print()

    for i in range(normalized_columns.shape[1]):
        print(
            f"Coluna {i}: mínimo = {normalized_columns[:, i].min():.2f}, máximo = {normalized_columns[:, i].max():.2f}"
        )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Padronização
    """)
    return


@app.cell
def _(StandardScaler, full_iris_dataset_numeric_columns):
    scaler_standard = StandardScaler()
    standardized_columns = scaler_standard.fit_transform(
        full_iris_dataset_numeric_columns
    )

    print("Dados padronizados:")
    print(standardized_columns[:10])
    return (standardized_columns,)


@app.cell
def _(np, standardized_columns):
    for _i in range(standardized_columns.shape[1]):
        print(f"Coluna {_i}: média = {np.mean(standardized_columns[:, _i]):.4f}")
        print(
            f"Coluna {_i}: desvio padrão = {np.std(standardized_columns[:, _i]):.4f}\n"
        )
    return


if __name__ == "__main__":
    app.run()
