import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


DEFAULT_BINS = 50


def plot_histogram(
    df: pd.DataFrame,
    column: str,
    bins: int = DEFAULT_BINS,
) -> None:
    """
    Plot a histogram for a dataframe column.
    """

    plt.figure(figsize=(8, 5))

    sns.histplot(df[column], bins=bins)

    plt.title(f"Distribution of {column}")

    plt.tight_layout()

    plt.show()


def plot_boxplot(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
) -> None:
    """
    Plot a boxplot.
    """

    plt.figure(figsize=(8, 5))

    sns.boxplot(
        data=df,
        x=x_col,
        y=y_col,
    )

    plt.tight_layout()

    plt.show()