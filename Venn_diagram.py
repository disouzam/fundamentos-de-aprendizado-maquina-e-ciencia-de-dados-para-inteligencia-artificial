import marimo

__generated_with = "0.23.13"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    # From https://python-graph-gallery.com/venn-diagram/

    import matplotlib.pyplot as plt
    from matplotlib_venn import venn2

    # Use the venn2 function
    venn2(subsets=(10, 5, 2), set_labels=("Group A", "Group B"))
    plt.show()
    return


if __name__ == "__main__":
    app.run()
