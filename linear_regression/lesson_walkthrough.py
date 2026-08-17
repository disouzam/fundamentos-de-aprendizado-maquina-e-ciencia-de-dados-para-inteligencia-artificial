import marimo

__generated_with = "0.23.13"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import numpy as np
    import plotly.graph_objects as go
    import math
    from scipy.stats import pearsonr

    return go, math, np, pearsonr


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Regressão linear simples
    """)
    return


@app.cell
def _(np):
    x_values = list(range(0, 10))
    x_array = np.array(x_values)

    y_values = [1, 3, 2, 5, 7, 8, 8, 9, 10, 12]
    y_array = np.array(y_values)
    return x_array, y_array


@app.cell
def _(go, x_array, y_array):
    fig = go.Figure(
        data=go.Scatter(x=x_array, y=y_array, mode="markers", marker=dict(size=12))
    )
    fig.update_layout(
        title="Scatter Plot",
        xaxis_title="X",
        yaxis_title="Y",
        xaxis=dict(rangemode="tozero"),
        yaxis=dict(rangemode="tozero"),
    )
    fig
    return


@app.cell
def _(go, np):
    def coefficient_estimation(x, y):
        number_of_data_points = np.size(x)

        mean_x = np.mean(x)
        mean_y = np.mean(y)

        Sxx = 0
        Sxy = 0

        for i in range(0, number_of_data_points):
            delta_x = x[i] - mean_x
            delta_y = y[i] - mean_y
            Sxx += delta_x**2
            Sxy += delta_x * delta_y

        beta_1 = Sxy / Sxx
        beta_0 = mean_y - beta_1 * mean_x

        return beta_0, beta_1

    def plot_regression_line(x, y, b):
        fig = go.Figure(
            data=go.Scatter(x=x, y=y, mode="markers", marker=dict(size=12), name="Data")
        )
        fig.update_layout(
            title="Scatter Plot",
            xaxis_title="X",
            yaxis_title="Y",
            xaxis=dict(rangemode="tozero"),
            yaxis=dict(rangemode="tozero"),
            width=900,
            height=600,
        )

        y_pred = b[0] + b[1] * x
        fig.add_trace(go.Scatter(x=x, y=y_pred, mode="lines", name="Regression Line"))

        return fig

    return coefficient_estimation, plot_regression_line


@app.cell
def _(coefficient_estimation, x_array, y_array):
    betas = coefficient_estimation(x_array, y_array)

    assert abs(betas[0] - 1.236) < 0.001
    assert abs(betas[1] - 1.170) < 0.001

    print(f"Estimated coefficients:\nb_0 = {betas[0]:.3f}  \nb_1 = {betas[1]:.3f}")
    return (betas,)


@app.cell
def _(betas, plot_regression_line, x_array, y_array):
    plot_regression_line(x_array, y_array, betas)
    return


@app.cell
def _(betas, math, np, x_array, y_array):
    def residual_standard_error(x, y, b):
        number_of_data_points = np.size(x)
        rse = 0
        for i in range(0, number_of_data_points):
            y_pred = b[0] + x[i] * b[1]
            rse += (y[i] - y_pred) ** 2

        rse = math.sqrt(rse / (number_of_data_points - 2))

        return rse

    rse = residual_standard_error(x_array, y_array, betas)

    assert abs(rse - 0.8384) < 0.0001

    print(f"RSE = {rse:.3f}")
    return


@app.cell
def _(betas, np, x_array, y_array):
    def r_squared(x, y, b):
        number_of_data_points = np.size(x)
        c1 = 0
        c2 = 0

        mean_y = np.mean(y)

        for i in range(0, number_of_data_points):
            y_pred = b[0] + b[1] * x[i]
            c1 += (y[i] - y_pred) ** 2
            c2 += (y[i] - mean_y) ** 2

        rsquared = 1 - c1 / c2

        return rsquared

    r_squared_raw_calculation = r_squared(x_array, y_array, betas)
    print(f"R2 = {r_squared_raw_calculation:.3f}")
    return (r_squared_raw_calculation,)


@app.cell
def _(pearsonr, r_squared_raw_calculation, x_array, y_array):
    r_squared_from_scipy = pearsonr(x_array, y_array)[0] ** 2

    print(f"Pearson ao quadrado: {r_squared_from_scipy:.3f}")

    assert abs(r_squared_raw_calculation - r_squared_from_scipy) < 0.0001
    return


if __name__ == "__main__":
    app.run()
