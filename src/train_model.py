import pandas as pd
import json
# from sklearn.model_selection import train_test_split

# Add the necessary imports for the starter code.


# Add code to load in the data.
def load_csv_to_df(filepath, **kwargs):
    """Loads a CSV file into a Pandas DataFrame.

    Args:
        filepath (str): The path to the CSV file
        **kwargs: Additional keyword arguments to pass to pd.read_csv()

    Returns:
        pandas.DataFrame: a pandas.DataFrame or None if an error occurs
    """

    try:
        df = pd.read_csv(filepath, **kwargs)  # Use kwargs to pass options
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except pd.errors.ParserError:
        print(f"Error: Could not parse CSV at {filepath}. Check file format.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    # import env variables
    with open("config.json", "r") as f:
        config = json.load(f)

    # load data
    df = load_csv_to_df(filepath=config["clean_data"])

    # split to features and target
    X = df.drop(config["target"], axis=1)
    y = df[config["target"]]

    # # Optional enhancement, use K-fold cross validation
    # instead of a train-test split.
    # train, test = train_test_split(data, test_size=0.20)

    # cat_features = [
    #     "workclass",
    #     "education",
    #     "marital-status",
    #     "occupation",
    #     "relationship",
    #     "race",
    #     "sex",
    #     "native-country",
    # ]
    # X_train, y_train, encoder, lb = process_data(
    #     train, categorical_features=cat_features,
    # label="salary", training=True
    # )

    # # Proces the test data with the process_data function.

    # # Train and save a model.
