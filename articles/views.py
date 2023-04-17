from django.shortcuts import render
from OurArticlesModel import articlesModel


# Create your views here.
def main(request):
    df = articlesModel.findArticles("Sports")

    return render(request, 'articles/main.html', {'data': df.iterrows()})
