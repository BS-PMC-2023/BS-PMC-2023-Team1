import pandas as pd
from acc import getacc
import pandas as pd



def getAccuracy():
    df = pd.read_csv(r'OurArticlesModel/news data/train.csv')
    print(getacc(df))
getAccuracy()



