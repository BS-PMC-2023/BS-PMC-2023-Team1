import pandas as pd
from acc import getacc

def getAccuracy():
    df = pd.read_csv(r'test.csv')
    print(getacc(df))
getAccuracy()
