from pathlib import Path

import pandas as pd


def save_dataframe(
    df: pd.DataFrame,
    file_path: str,
) -> None:
    """
    Save a DataFrame to CSV.

    Creates the parent directory if it doesn't exist.
    """

    path = Path(file_path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_csv(
        path,
        index=True,
    )