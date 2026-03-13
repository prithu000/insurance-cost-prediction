import pandas as pd

def preprocess_data(path):
    df = pd.read_csv(path)
    df = pd.get_dummies(df, drop_first=True)

    X = df.drop("charges", axis=1)
    y = df["charges"]

    return X, y