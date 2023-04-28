from django.shortcuts import render
from OurArticlesModel import articlesModel
from django.test import TestCase, Client
from django.urls import reverse


def home(request):
    try:
        df = articlesModel.findArticles("news")
        return render(request, 'home.html', {'data': df.iterrows()})
    except:
        return render(request, 'home.html')


