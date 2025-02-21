import pandas as pd
import numpy as np
from src.train_model import load_csv_to_df, split_data, train_model
from sklearn.pipeline import Pipeline


def test_load_to_csv(test_csv):
    df = load_csv_to_df(test_csv)
    assert df is not None
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert list(df.columns) == ["col1", "col2"]


def test_split_data_stratified():
    # dummy data
    X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
    y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])

    X_train, X_test, y_train, y_test = split_data(
        X, y, test_size=0.2, stratification=True
    )

    # chekc sizes
    assert len(X_train) == 8
    assert len(X_test) == 2

    # check stratify
    assert (y_train == 0).sum() == 4
    assert (y_train == 1).sum() == 4
    assert (y_test == 0).sum() == 1
    assert (y_test == 1).sum() == 1


def test_pipeline(synthetic_data):
    X_train, X_test, y_train, y_test = synthetic_data

    model = train_model(X_train, y_train, algo="random_forest")

    assert isinstance(model, Pipeline)
    assert len(model.steps) == 2
