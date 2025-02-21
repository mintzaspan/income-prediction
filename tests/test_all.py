import pandas as pd
from src.train_model import load_csv_to_df


def test_load_to_csv(test_csv):
    df = load_csv_to_df(test_csv)
    assert df is not None
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert list(df.columns) == ['col1', 'col2']