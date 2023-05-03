from django.shortcuts import render
from OurArticlesModel import articlesModel


# Create your views here.
def catalog(request):
    try:
        engine = articlesModel.initializeEngine("Sports")
        df = articlesModel.getPage(engine, 1)
        return render(request, 'articles/article.html', {'data': df.iterrows()})
    except:
        return render(request, 'articles/article.html')




