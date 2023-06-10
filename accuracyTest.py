import pandas as pd
from acc import getacc
import pandas as pd



def getAccuracy():
    df = pd.read_csv(r'train10.csv')
    print(getacc(df))
getAccuracy()



