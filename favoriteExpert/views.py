from django.shortcuts import render
from registration.models import UserData
from .models import favoriteExpert, favoriteArticle
from django.shortcuts import render, redirect
from articles.models import PredictionApproves, ArticleCache


# Create your views here.
def favoriteExpert2(request):
    exprts = UserData.objects.filter(isexpert=True, Pending=False)
    if request.method == 'POST':
        if request.POST.get('likeBtn.x'):
            if not favoriteExpert.objects.filter(expertId=request.POST.get('expid'), userId=request.user.id).exists():
                favoriteExpert.objects.create(expertId=request.POST.get('expid'), userId=request.user.id)
    return render(request, 'favoriteExpert.html', {'exprts': exprts})


# Create your views here.
def filterex(request):
    exprts = None
    if request.method == 'POST':
        exprts = UserData.objects.filter(isexpert=True, Pending=False)
        if request.POST.get('radio'):
            if request.POST.get('radio') == 'all':
                exprts = UserData.objects.filter(isexpert=True, Pending=False)
            if request.POST.get('radio') == 'My favorite':
                temp = favoriteExpert.objects.filter(userId=request.user.id)
                exprts = UserData.objects.filter(user_id__in=temp.values('expertId'))
                return render(request, 'favoriteExpert.html', {'exprts': exprts})
            return render(request, 'favoriteExpert.html', {'exprts': exprts})
    return render(request, 'favoriteExpert.html', {'exprts': exprts})


def favoriteArticle1(request):
    temp = favoriteArticle.objects.filter(userId=request.user.id)
    exprts = ArticleCache.objects.filter(link__in=temp.values('link'))
    return render(request, 'favoriteArticle.html', {'exprts': exprts})


def deleteArticle(request):
    if request.method == 'POST':
        if request.POST.get('delete'):
            favoriteArticle.objects.filter(link=request.POST.get('delete'), userId=request.user.id).delete()
            return redirect('/favoriteExpert/favoriteArticle')
    return redirect('/favoriteExpert/favoriteArticle')
