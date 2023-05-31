import pandas as pd
from sklearn.metrics import accuracy_score


def getAccuracy():
    df = pd.read_csv('news data/test.csv')
    predictions = getPrediction(df)

    return accuracy_score(df['label'], predictions)
