import re
import pickle
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
nltk.download('stopwords')
def stemming(content):
    stemmed_content = re.sub('[^a-zA-Z]',' ',content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [ps.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
    stemmed_content = ' '.join(stemmed_content)
    return stemmed_content
def getacc(df):
  ps = PorterStemmer()
  vectorizer = TfidfVectorizer()
  df = df.fillna(' ')
  df['content'] = df['author']+' '+df['title']
  df['content'] = df['content'].apply(stemming)
  xTrain = df.drop('label',axis=1)
  yTrain = df['label']
  xTrain = vectorizer.fit_transform(xTrain['content'])
  trainX, valX, trainY, valY = train_test_split(xTrain, yTrain, test_size=0.20, random_state=42)
  model = LogisticRegression()
  model.fit(trainX, trainY)
  predictions = model.predict(valX)
  print(accuracy_score(valY, predictions))
  
  

  
