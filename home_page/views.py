from django.shortcuts import render
from OurArticlesModel import articlesModel
from django.test import TestCase, Client
from django.urls import reverse


def home(request):
    df = articlesModel.findArticles("Sports")
    return render(request, 'home.html', {'data': df.iterrows()})



