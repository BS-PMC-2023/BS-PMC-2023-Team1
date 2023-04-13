from GoogleNews import GoogleNews as g
import pandas as pd
import newspaper


def findArticles(query: str = None, language: str = "en"):
    """ Given a query, find and return the relevant articles from Google News.

    :param language:        The language of the articles.
    :param query:           Search query.
    :return:                A dataframe of the articles, with the columns:
                            ['title', 'media', 'date', 'datetime', 'desc', 'link', 'img']
    """

    def getContent(link):
        """ Given a link to a specific article, return the content of it (text).

        :param link:        The link for the article.
        :return:            Article's content, as text.
        """

        article = newspaper.Article(link)
        article.download()
        article.parse()

        return [article.text, article.top_img]

    # Find Articles
    gn = g(lang=language, period='1d')
    gn.search(query)
    df = pd.DataFrame(gn.page_at(1)).iloc[:8]

    # Merge content
    df[['content', 'img']] = df['link'].apply(lambda l: getContent(l)).to_list()

    # Clear GoogleNews engine
    gn.clear()

    return df[['title', 'desc', 'content', 'media', 'link', 'img', 'date', 'datetime']]
