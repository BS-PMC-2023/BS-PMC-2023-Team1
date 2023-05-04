from GoogleNews import GoogleNews as g
import pandas as pd
import newspaper
from articles.models import ArticleCache


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
    df = pd.DataFrame(engine.page_at(page)).iloc[:9]

    # Check which articles are already cached in the database
    df[['content', 'img']] = df['link'].apply(lambda l: getContent(l)).to_list()

    return df[['title', 'content', 'media', 'link', 'img', 'date']]
