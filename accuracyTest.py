import pandas as pd
from acc import getacc
import pandas as pd
from articlesModel import getPrediction
from sklearn.metrics import accuracy_score



def getAccuracy():
    df = pd.read_csv(r'test.csv')
    print(getacc(df))
getAccuracy()



def getAccuracy2():
    df = pd.read_csv(r'test.csv')
    predictions = getPrediction(df)

    return accuracy_score(df['label'], predictions)
print(getAccuracy2())
