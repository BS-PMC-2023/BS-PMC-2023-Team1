from django.shortcuts import render, redirect
from OurArticlesModel import articlesModel


def home(request):
    df = articlesModel.findArticles("Sports")
    return render(request, 'home.html', {'data': df.iterrows()})
