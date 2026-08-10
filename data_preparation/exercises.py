import marimo

__generated_with = "0.23.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import MinMaxScaler, StandardScaler
    import matplotlib.pyplot as plt
    from sklearn.preprocessing import Binarizer

    return Binarizer, MinMaxScaler, StandardScaler, mo, np, pd, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # URLs dos datasets no GitHub
    """)
    return


@app.cell
def _():
    iris_with_errors_url = r"https://raw.githubusercontent.com/disouzam/fundamentos-de-aprendizado-maquina-e-ciencia-de-dados-para-inteligencia-artificial/refs/heads/data-preparation-exercises/data-versioned/iris-with-errors.csv"

    iris_url = r"https://raw.githubusercontent.com/disouzam/fundamentos-de-aprendizado-maquina-e-ciencia-de-dados-para-inteligencia-artificial/refs/heads/data-preparation-exercises/data-versioned/iris.csv"

    vehicle_url = r"https://raw.githubusercontent.com/disouzam/fundamentos-de-aprendizado-maquina-e-ciencia-de-dados-para-inteligencia-artificial/refs/heads/data-preparation-exercises/data-versioned/Vehicle.csv"

    boston_housing_url = r"https://raw.githubusercontent.com/disouzam/fundamentos-de-aprendizado-maquina-e-ciencia-de-dados-para-inteligencia-artificial/refs/heads/data-preparation-exercises/data-versioned/BostonHousing.csv"
    return boston_housing_url, iris_url, iris_with_errors_url, vehicle_url


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Leitura de uma base de dados com problemas artificialmente introduzidos
    """)
    return


@app.cell
def _(iris_with_errors_url, read_csv_with_diagnostics):
    iris_dataset = read_csv_with_diagnostics(iris_with_errors_url)
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
def _(get_markdown_about_df_columns, iris_dataset, mo):
    _md_text = get_markdown_about_df_columns(iris_dataset)
    mo.md(_md_text)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Tipos de dados das colunas
    """)
    return


@app.cell
def _(get_markdown_about_df_datatypes, iris_dataset, mo):
    _md_text = get_markdown_about_df_datatypes(iris_dataset)
    mo.md(_md_text)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Valores ausentes
    """)
    return


@app.cell
def _(get_markdown_about_absent_values, iris_dataset, mo):
    _md_text = get_markdown_about_absent_values(iris_dataset)
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
def _(iris_with_errors_url, read_csv_with_diagnostics):
    iris_dataset_2 = read_csv_with_diagnostics(iris_with_errors_url)
    return (iris_dataset_2,)


@app.cell
def _(iris_dataset_2):
    iris_dataset_2
    return


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
def _(iris_with_errors_url, np, read_csv_with_diagnostics):
    iris_dataset_4 = read_csv_with_diagnostics(iris_with_errors_url)
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
def _(iris_with_errors_url, np, read_csv_with_diagnostics):
    iris_dataset_6 = read_csv_with_diagnostics(iris_with_errors_url)
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
def _(iris_url, read_csv_with_diagnostics):
    full_iris_dataset = read_csv_with_diagnostics(iris_url)
    return (full_iris_dataset,)


@app.cell
def _(full_iris_dataset):
    full_iris_dataset.head()
    return


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
    return (normalized_columns,)


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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Comparação visual
    """)
    return


@app.cell
def _(
    full_iris_dataset,
    full_iris_dataset_numeric_columns,
    normalized_columns,
    np,
    plt,
    standardized_columns,
):
    for coluna in range(full_iris_dataset_numeric_columns.shape[1]):
        nome_coluna = full_iris_dataset.columns[coluna]
        cor_coluna = np.random.rand(
            3,
        )

        plt.figure(figsize=(6, 3))
        plt.hist(
            full_iris_dataset_numeric_columns[:, coluna],
            bins=15,
            alpha=0.8,
            color=cor_coluna,
        )
        plt.title(f"Dados originais — {nome_coluna}")
        plt.xlabel(nome_coluna)
        plt.ylabel("Frequência")
        plt.show()

        plt.figure(figsize=(6, 3))
        plt.hist(
            normalized_columns[:, coluna],
            bins=15,
            alpha=0.8,
            color=cor_coluna,
        )
        plt.title(f"Dados normalizados — {nome_coluna}")
        plt.xlabel(nome_coluna)
        plt.ylabel("Frequência")
        plt.show()

        plt.figure(figsize=(6, 3))
        plt.hist(
            standardized_columns[:, coluna],
            bins=15,
            alpha=0.8,
            color=cor_coluna,
        )
        plt.title(f"Dados padronizados — {nome_coluna}")
        plt.xlabel(nome_coluna)
        plt.ylabel("Frequência")
        plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Binarização
    """)
    return


@app.cell
def _(Binarizer, MinMaxScaler, full_iris_dataset_numeric_columns):
    T = 0.1
    print("Limiar:", T)
    print("---------------------")

    normalizer = MinMaxScaler(feature_range=(0, 1))
    normalized_array = normalizer.fit_transform(full_iris_dataset_numeric_columns)

    binarizer = Binarizer(threshold=T)
    binarized_array = binarizer.fit_transform(normalized_array)

    for _i in range(10):
        print("Antes:", normalized_array[_i])
        print("Depois:", binarized_array[_i])
        print("---------------------")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Lidando com variáveis categóricas

    ## Codificação como inteiros
    """)
    return


@app.cell
def _(iris_url, read_csv_with_diagnostics):
    iris_dataset_8 = read_csv_with_diagnostics(iris_url)

    print("Coluna original com as classes:")
    print(iris_dataset_8[iris_dataset_8.columns[-1]].head(10))
    return (iris_dataset_8,)


@app.cell
def _(iris_dataset_8, np):
    classes = np.unique(iris_dataset_8[iris_dataset_8.columns[-1]])
    class_mapping = {iris_class: number for number, iris_class in enumerate(classes)}
    print("Mapeamento usado:", class_mapping)
    return (class_mapping,)


@app.cell
def _(class_mapping, iris_dataset_8):
    iris_dataset_8_codified = iris_dataset_8.copy()

    iris_dataset_8_codified[iris_dataset_8.columns[-1]] = iris_dataset_8_codified[
        iris_dataset_8.columns[-1]
    ].map(class_mapping)

    iris_dataset_8_codified
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## One-hot enconding
    """)
    return


@app.cell
def _(pd):
    dummies_df = pd.DataFrame({"categoria": ["a", "b", "a", "c", "a", "b"]})

    dummies_df
    return (dummies_df,)


@app.cell
def _(dummies_df, pd):
    dummies_df_onehot = pd.get_dummies(dummies_df, drop_first=True)
    dummies_df_onehot
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Identificação de variáveis correlacionadas
    """)
    return


@app.cell
def _(boston_housing_url, read_csv_with_diagnostics):
    boston_housing = read_csv_with_diagnostics(boston_housing_url)
    return (boston_housing,)


@app.cell
def _(boston_housing):
    boston_housing.head(10)
    return


@app.cell
def _(boston_housing, plt):
    corr = boston_housing.corr(numeric_only=True)

    plt.figure(figsize=(8, 8))
    plt.imshow(corr, cmap="Blues", interpolation="none", aspect="auto")
    plt.colorbar()
    plt.xticks(range(len(corr)), corr.columns, rotation="vertical")
    plt.yticks(range(len(corr)), corr.columns)
    plt.title("Matriz de correlação entre variáveis", fontsize=14, fontweight="bold")
    plt.grid(False)
    plt.show()
    return (corr,)


@app.cell
def _(corr):
    p = 0.75
    pares_correlacionados = []

    # Percorre apenas metade da matriz para evitar repetir pares.
    for _i, col_i in enumerate(corr.columns):
        for j, col_j in enumerate(corr.columns):
            if j > _i and abs(corr.loc[col_i, col_j]) > p:
                pares_correlacionados.append((col_i, col_j, corr.loc[col_i, col_j]))

    print(f"Pares com correlação absoluta maior que {p}:")
    for col_i, col_j, valor in pares_correlacionados:
        print(f"{col_i} -- {col_j}: correlação = {valor:.3f}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Dados desbalanceados
    """)
    return


@app.cell
def _(read_csv_with_diagnostics, vehicle_url):
    vehicle_dataset = read_csv_with_diagnostics(vehicle_url)
    return (vehicle_dataset,)


@app.cell
def _(vehicle_dataset):
    vehicle_dataset.head(10)
    return


@app.cell
def _(vehicle_dataset):
    vehicle_classes = vehicle_dataset[vehicle_dataset.columns[-1]]

    print("Primeiros valores da coluna de classe:")
    print(vehicle_classes.head())

    print("\nNúmero de elementos por classe:")
    print(vehicle_classes.value_counts())
    return (vehicle_classes,)


@app.cell
def _(plt, vehicle_classes):
    contagem_classes = vehicle_classes.value_counts().sort_index()

    plt.figure(figsize=(7, 4))
    plt.bar(contagem_classes.index, contagem_classes.values, alpha=0.75)
    plt.title("Número de elementos em cada classe")
    plt.xlabel("Classe")
    plt.ylabel("Número de elementos")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Subamostragem simples
    """)
    return


@app.cell
def _(np, vehicle_dataset):
    N = 5

    X = np.array(vehicle_dataset)
    cls = np.array(vehicle_dataset[vehicle_dataset.columns[-1]])
    classes_unicas = np.unique(cls)

    amostras = []
    for classe in classes_unicas:
        indices_classe = np.argwhere(cls == classe).ravel()
        indices_sorteados = np.random.choice(indices_classe, N, replace=False)
        amostras.append(X[indices_sorteados, :])

    X_balanceado = np.vstack(amostras)

    print("Dados obtidos a partir da amostragem:")
    print(X_balanceado)
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
def _(pd):
    def get_markdown_about_df_columns(df: pd.DataFrame):
        cols = list(df.columns)

        md_text = ""
        for col in cols:
            md_text += f"\n1. **{col}**"

        md_text = f"As colunas que existem no dataset são: {md_text}"
        return md_text

    return (get_markdown_about_df_columns,)


@app.cell
def _(pd):
    def get_markdown_about_df_datatypes(df: pd.DataFrame):
        data_types = df.dtypes

        md_text = ""

        for col_name, col_type in data_types.items():
            md_text += f"\n1. **{col_name}**: {col_type}"

        md_text = f"Os tipos de dados de cada coluna estão listados abaixo: {md_text}"
        return md_text

    return (get_markdown_about_df_datatypes,)


@app.cell
def _(pd):
    def get_markdown_about_absent_values(df: pd.DataFrame):
        absent_data_values = df.isna().sum()

        md_text = ""

        columns_with_no_absent_values = []
        for col_name, number_of_absent_values in absent_data_values.items():
            if number_of_absent_values == 0:
                columns_with_no_absent_values.append(col_name)
            else:
                md_text += f"\n1. **{col_name}**: {number_of_absent_values}"

        md_text = f"O número de valores ausentes por coluna são: {md_text}"

        md_text += "\n\nAs colunas abaixo não possuem valores ausentes: "
        for col_name in columns_with_no_absent_values:
            md_text += f"\n1. **{col_name}**"

        return md_text

    return (get_markdown_about_absent_values,)


if __name__ == "__main__":
    app.run()
