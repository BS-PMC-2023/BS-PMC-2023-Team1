import pandas as pd
import articlesModel
from sklearn.metrics import accuracy_score


def getAccuracy():
    df = pd.read_csv('news data/test.csv')
    predictions = articlesModel.getPrediction(df)

    return accuracy_score(df['label'], predictions)


getAccuracy()