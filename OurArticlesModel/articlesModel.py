from GoogleNews import GoogleNews as g
import pandas as pd
import newspaper
from django.db.models import Count
from articles.models import ArticleCache, PredictionApproves

import re
import pickle
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

from keras.preprocessing.text import one_hot
from keras.utils import pad_sequences
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout, Embedding


def initializeEngine(query: str = None, language: str = "en"):
    """ Given a query, initialize the engine for the article retrieval.

    :param query:           Search query.
    :param language:        The language of the articles.
    :return:                GoogleNews engine object.
    """

    # Find Articles
    gn = g(lang=language, period='1d')
    gn.search(query)

    return gn


def getPage(engine: g, page: int = 1):
    """ Given a query, find and return the relevant articles from Google News.

    :param engine:          A GoogleNews engine object, pre-initialized.
                            Call the function 'initializeEngine' before calling this function.
    :param page:            The page index.
    :return:                A dataframe of the articles, with the columns:
                            ['title', 'content', 'media', 'link', 'img', 'datetime']
    """

    def getContent(link):
        """ Given a link to a specific article, return the content of it (text) and the img path.
        Check if the article already cached before using the api.

        :param link:        The link for the article.
        :return:            Article's content and img path, as a list of strings.
        """
        articleObject = ArticleCache.objects.filter(link=link)
        if articleObject.exists():
            articleObject = articleObject.first()

            return [getattr(articleObject, 'content'), getattr(articleObject, 'img')]
        else:
            article = newspaper.Article(link)
            article.download()
            article.parse()

            ArticleCache.objects.create(
                link = link,
                content = article.text,
                img = article.top_img
            )

            return [article.text, article.top_img]

    # Find Articles
    df = pd.DataFrame(engine.page_at(page)).iloc[:6]

    # Check which articles are already cached in the database
    df[['content', 'img']] = df['link'].apply(lambda l: getContent(l)).to_list()

    # Get statistical data
    df['approves'] = df['link'].apply(lambda l: PredictionApproves.objects.filter(link=l, approved=True).aggregate(Count('expertId'))['expertId__count'])
    df['denials'] = df['link'].apply(lambda l: PredictionApproves.objects.filter(link=l, approved=False).aggregate(Count('expertId'))['expertId__count'])

    return df[['title', 'content', 'media', 'link', 'img', 'date', 'approves', 'denials']]


def getPrediction(data):
    """ Given a data, use the classifier to predict whether the article is FAKE or LEGIT. """
    def preprocessing(data):
        """ Preprocess the data. """
        nltk.download('stopwords')

