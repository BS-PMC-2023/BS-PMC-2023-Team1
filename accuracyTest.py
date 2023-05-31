import pandas as pd


def getAccuracy():
    df = pd.read_csv(r'test.csv')
    print(df)
getAccuracy()
