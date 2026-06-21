import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

class DataPreprocessor:
    def run(self):
        df = pd.read_csv('data/sample.csv')
        X = df.iloc[:, :-1]
        y = df.iloc[:, -1]

        le = LabelEncoder()
        y = le.fit_transform(y)

        scaler = StandardScaler()
        X = scaler.fit_transform(X)

        return train_test_split(X, y, test_size=0.2)
