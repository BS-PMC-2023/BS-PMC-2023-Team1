from django.shortcuts import render
from OurArticlesModel import articlesModel


def home(request):
    # df = articlesModel.findArticles("Sports")
    # return render(request, 'home.html', {'data': df.iterrows()})
    return render(request, 'home.html')