import pytest
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

@pytest.fixture(scope="function")
def test_csv(tmp_path):
    # Create a test CSV file
    test_csv_path = tmp_path / "test.csv"
    data = {
        "col1": [1, 2],
        "col2": [3,4]
    }
    df = pd.DataFrame(data)
    df.to_csv(test_csv_path, index=False)
    return test_csv_path

@pytest.fixture(scope="function")
def synthetic_data():
    np.random.seed(42)
    X = pd.DataFrame({
        'numeric_feature1': np.random.rand(100),
        'numeric_feature2': np.random.rand(100),
        'categorical_feature': np.random.choice(['A', 'B', 'C'], size=100)
    })
    y = pd.Series(data=np.random.choice([0, 1], size=100), name="salary")
    return train_test_split(X, y, test_size=0.2, random_state=42)