import pandas as pd
import json
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, TargetEncoder
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
import os
import pickle
from sklearn.metrics import f1_score


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


def split_data(X, y, test_size=0.2, random_state=42, stratification=True):
    """Splits data into training and test sets.

    Args:
        X : features data
        y : target data
        test_size : proportion of data to be used for testing
        random_state : reproducibility seed
        stratify : option for stratifying using target variable

    Returns:
        X_train : train features data
        X_test : test features data
        y_train : train target data
        y_test : test target data
    """

    if stratification:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state, stratify=y
        )
    else:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )

    return (X_train, X_test, y_train, y_test)


def train_model(X_train, y_train, algo="random_forest"):
    """Trains a binary classification model.

    Args:
        X_train : (pd.DataFrame) features data to train the algorithm
        y_train : (pd.DataFrame or pd.Series) target data to
        train the algorithm
        algo : type of model to be trained "random_forest" (default)
         or "gradient_boosting"

    Returns:
        pipe : trained model with preprocesing steps
    """

    numeric_features = X_train.select_dtypes(include="number").columns.tolist()
    numeric_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="mean")),
            ("scaler", StandardScaler()),
        ]
    )

    categorical_features = X_train.select_dtypes(
        include=["object", "category"],
        exclude=["datetime", "timedelta", "datetimetz"],
    ).columns.tolist()
    categorical_transformer = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="constant", fill_value="unknown"),
            ),
            ("encoder", TargetEncoder(target_type="binary", random_state=42)),
            ("scaler", StandardScaler()),
        ]
    )
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )

    classifiers = {
        "random_forest": RandomForestClassifier(n_jobs=-1),
        "gradient_boosting": GradientBoostingClassifier(),
    }

    classifier = classifiers[algo]

    pipe = Pipeline(
        steps=[("preprocessor", preprocessor), ("classifier", classifier)]
    )

    features_list = numeric_features + categorical_features
    features = X_train[features_list]

    target = y_train

    pipe.fit(features, target)

    return pipe


def save_model(model, output_path):
    """Saves a trained sklearn classifier to the specified path

    Args:
        model : trained sklearn model or pipeline that can be pickled
        output_path : path to save .pkl object

    Returns:
        None
    """
    if not os.path.exists(os.path.dirname(output_path)):
        os.mkdir(os.path.dirname(output_path))

    with open(output_path, "wb") as f:
        pickle.dump(model, f)
    print(f"Model saved in {output_path}")


def evaluate_slice(data, target, model):
    """
    Computes evaluation metrics for slices in categorical variables.
    Saves output to 'outputs/slice_output.txt'

    Args:
        data : pandas.DataFrame
        target : label column name
        model : trained model

    Returns:
        None
    """

    categorical_features = data.select_dtypes(
        include=["object", "category"],
        exclude=["datetime", "timedelta", "datetimetz"],
    ).columns.tolist()

    if target in categorical_features:
        categorical_features.remove(target)

    scores = pd.DataFrame(columns=["variable", "slice", "f1_score"])

    for i in categorical_features:
        slice_values = data[i].unique().tolist()
        for slice_value in slice_values:
            df = data[data[i] == slice_value]
            X = df.drop(target, axis=1)
            y = df[target].values
            y_pred = model.predict(X)
            f1 = f1_score(y_true=y, y_pred=y_pred, pos_label=">50K")
            scores.loc[len(scores)] = [i, slice_value, f1]

    outputs_path = "outputs/slice_output.txt"
    if not os.path.exists(os.path.dirname(outputs_path)):
        os.mkdir(os.path.dirname(outputs_path))

    with open(outputs_path, "w") as f:
        f.write(scores.to_string(header=False, index=False))


if __name__ == "__main__":
    # import env variables
    with open("config.json", "r") as f:
        config = json.load(f)

    # load data
    df = load_csv_to_df(filepath=config["clean_data"])

    # split to features and target
    X = df.drop(config["target"], axis=1)
    y = df[config["target"]]

    # split data to train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    # train model
    model = train_model(X_train, y_train)

    # save model
    save_model(model, config["model_output_path"])

    # evaluate fairness
    evaluate_slice(df, "salary", model)
