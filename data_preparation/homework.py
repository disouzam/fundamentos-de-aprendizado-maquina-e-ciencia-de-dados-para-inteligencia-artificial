import marimo

__generated_with = "0.23.13"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import MinMaxScaler, StandardScaler
    import matplotlib.pyplot as plt

    return MinMaxScaler, StandardScaler, mo, np, pd, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## URLs dos datasets
    """)
    return


@app.cell
def _():
    iris_with_errors_url = r"https://raw.githubusercontent.com/disouzam/fundamentos-de-aprendizado-maquina-e-ciencia-de-dados-para-inteligencia-artificial/refs/heads/main/data-versioned/iris-with-errors.csv"

    iris_url = r"https://raw.githubusercontent.com/disouzam/fundamentos-de-aprendizado-maquina-e-ciencia-de-dados-para-inteligencia-artificial/refs/heads/main/data-versioned/iris.csv"
    return iris_url, iris_with_errors_url


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 1. Leia novamente a base `iris-with-errors.csv`, faça a limpeza dos dados e remova as duas últimas colunas.
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
    # 2. Leia novamente a base `iris-with-errors.csv` e substitua os valores ausentes pela **mediana** de cada atributo.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Leitura do dataset
    """)
    return


@app.cell
def _(iris_with_errors_url, read_csv_with_diagnostics):
    iris_dataset_with_errors2 = read_csv_with_diagnostics(iris_with_errors_url)
    return (iris_dataset_with_errors2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Substituição dos '?' por nan
    """)
    return


@app.cell
def _(iris_dataset_with_errors2, np):
    iris_dataset_with_errors2_mod1 = iris_dataset_with_errors2.replace("?", np.nan)
    return (iris_dataset_with_errors2_mod1,)


@app.cell
def _(iris_dataset_with_errors2_mod1):
    iris_dataset_with_errors2_mod1.head(5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Cálculo das medianas
    """)
    return


@app.cell
def _(iris_dataset_with_errors2_mod1):
    columns = iris_dataset_with_errors2_mod1.columns[:-1]
    iris_dataset_with_errors2_mod1[columns] = iris_dataset_with_errors2_mod1[
        columns
    ].astype(float)

    iris_dataset_with_errors2_median = iris_dataset_with_errors2_mod1[columns].median()
    iris_dataset_with_errors2_median
    return columns, iris_dataset_with_errors2_median


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Preenchimento / inputação de dados
    """)
    return


@app.cell
def _(
    columns,
    iris_dataset_with_errors2_median,
    iris_dataset_with_errors2_mod1,
):
    iris_dataset_with_errors2_mod2 = iris_dataset_with_errors2_mod1.copy()
    iris_dataset_with_errors2_mod2[columns] = iris_dataset_with_errors2_mod2[
        columns
    ].fillna(iris_dataset_with_errors2_median)
    return (iris_dataset_with_errors2_mod2,)


@app.cell
def _(iris_dataset_with_errors2_mod2):
    iris_dataset_with_errors2_mod2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 3. Considere a base `iris.csv`. Mostre o histograma de cada variável antes e depois da normalização.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Leitura do dataset
    """)
    return


@app.cell
def _(iris_url, read_csv_with_diagnostics):
    iris_dataset = read_csv_with_diagnostics(iris_url)
    return (iris_dataset,)


@app.cell
def _(iris_dataset):
    iris_dataset.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Normalização do dataset
    """)
    return


@app.cell
def _(iris_dataset, np):
    columns_iris = list(iris_dataset.columns)[:-1]

    iris_dataset_array = np.array(iris_dataset[columns_iris], dtype=float)
    iris_dataset_array.shape
    return columns_iris, iris_dataset_array


@app.cell
def _(MinMaxScaler, iris_dataset_array):
    scaler_minmax = MinMaxScaler(feature_range=(0, 1))
    iris_dataset_array_norm = scaler_minmax.fit_transform(iris_dataset_array)
    iris_dataset_array_norm.shape
    return (iris_dataset_array_norm,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Geração dos histogramas
    """)
    return


@app.cell
def _(columns_iris, iris_dataset_array, iris_dataset_array_norm, np, plt):
    for idx_col, column in enumerate(columns_iris):
        nome_coluna = columns_iris[idx_col]

        fig, axes = plt.subplots(1, 2, figsize=(12, 3))

        cor_coluna = np.random.rand(
            3,
        )

        axes[0].hist(
            iris_dataset_array[:, idx_col],
            bins=15,
            alpha=0.8,
            density=True,
            color=cor_coluna,
        )
        axes[0].set_title(f"Dados originais — {nome_coluna}")
        axes[0].set_xlabel(nome_coluna)
        axes[0].set_ylabel("Frequência")

        axes[1].hist(
            iris_dataset_array_norm[:, idx_col],
            bins=15,
            alpha=0.8,
            density=True,
            color=cor_coluna,
        )
        axes[1].set_title(f"Dados normalizados — {nome_coluna}")
        axes[1].set_xlabel(nome_coluna)
        axes[1].set_ylabel("Frequência")

        plt.tight_layout()
        plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 4. Considere a base `iris.csv`. Mostre o histograma de cada variável antes e depois da padronização.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Padronização
    """)
    return


@app.cell
def _(StandardScaler, iris_dataset_array):
    scaler_standard = StandardScaler()
    iris_dataset_array_standardized = scaler_standard.fit_transform(iris_dataset_array)
    iris_dataset_array_standardized.shape
    return (iris_dataset_array_standardized,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Geração dos histogramas
    """)
    return


@app.cell
def _(
    columns_iris,
    iris_dataset_array,
    iris_dataset_array_standardized,
    np,
    plt,
):
    for idx_col_2, column2 in enumerate(columns_iris):
        nome_coluna_2 = columns_iris[idx_col_2]

        fig2, axes2 = plt.subplots(1, 2, figsize=(12, 3))

        cor_coluna2 = np.random.rand(
            3,
        )

        axes2[0].hist(
            iris_dataset_array[:, idx_col_2],
            bins=15,
            alpha=0.8,
            density=True,
            color=cor_coluna2,
        )
        axes2[0].set_title(f"Dados originais — {nome_coluna_2}")
        axes2[0].set_xlabel(nome_coluna_2)
        axes2[0].set_ylabel("Frequência")

        axes2[1].hist(
            iris_dataset_array_standardized[:, idx_col_2],
            bins=15,
            alpha=0.8,
            density=True,
            color=cor_coluna2,
        )
        axes2[1].set_title(f"Dados padronizados — {nome_coluna_2}")
        axes2[1].set_xlabel(nome_coluna_2)
        axes2[1].set_ylabel("Frequência")

        plt.tight_layout()
        plt.show()
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
