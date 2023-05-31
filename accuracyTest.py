import pandas as pd
from sklearn.metrics import accuracy_score


df = pd.read_csv(r'test.csv')
predictions = getPrediction(df)

print( accuracy_score(df['label'], predictions))
