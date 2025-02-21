import pytest
import pandas as pd

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