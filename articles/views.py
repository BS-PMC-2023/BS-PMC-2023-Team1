from django.shortcuts import render
from OurArticlesModel import articlesModel


# Create your views here.
def catalog(request):
    try:
        df = articlesModel.findArticles("Sports")
        return render(request, 'articles/article.html', {'data': df.iterrows()})
    except:
        return render(request, 'articles/article.html')




