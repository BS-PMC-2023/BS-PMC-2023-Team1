from django.shortcuts import render
from registration.models import UserData
from .models import favoriteExpert
from django.shortcuts import render, redirect


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
