import keras
from GoogleNews import GoogleNews as g
import newspaper
from django.db.models import Count
from articles.models import ArticleCache, PredictionApproves

import re
import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from keras.preprocessing.text import one_hot
from keras.utils import pad_sequences


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

    # Get predictions from classifier
    df['predict'] = df.apply(lambda x: getPrediction(x['title']), axis=1)

    return df[['title', 'content', 'media', 'link', 'img', 'date', 'approves', 'denials', 'predict']]


def getPrediction(data):
    """ Given a data, use the classifier to predict whether the article is FAKE or LEGIT.
    Return the preprocessed data.
    """
    def preprocessing(rawData):
        """ Preprocess the data. """
        nltk.download('stopwords')
        ps = PorterStemmer()
        voc_size = 5000
        sent_length = 20

        # Tokenization and stop words
        rawData = re.sub('[^a-zA-Z]', ' ', rawData).lower().split()
        rawData = [ps.stem(word) for word in rawData if word not in stopwords.words('english')]
        rawData = ' '.join(rawData)

        # One-Hot Representation
        rawData = [one_hot(word, voc_size) for word in rawData]

        # Embedding Representation
        rawData = pad_sequences(rawData, padding='pre', maxlen=sent_length)

        return np.array(rawData)

    processedData = preprocessing(data)
    model = keras.models.load_model('OurArticlesModel/Fake News Classifier.h5')

    prediction = (model.predict(processedData) > 0.5).astype("int32")

    return prediction