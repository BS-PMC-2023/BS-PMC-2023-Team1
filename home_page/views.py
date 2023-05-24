from django.shortcuts import render
from registration.models import UserData
from articles.models import PredictionApproves, ArticleCache
from django.contrib.auth.models import User
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import os
from django.conf import settings


def generateGraph(request):
    plt.clf()

    Predictionapprovess = PredictionApproves.objects.filter(expertId=request.user.id)
    articles = ArticleCache.objects.all()
    name = request.user.username
    agree = 0
    disagree = 0
    for article in articles:
        if Predictionapprovess.filter(link=article.link).exists():
            if Predictionapprovess.get(link=article.link).approved:
                agree += 1
            else:
                disagree += 1
    ###############################################################
    x = ['agree', 'disagree']
    y = [agree, disagree]
    sns.barplot(x=x, y=y)
    plt.xlabel('agree or disagree')
    plt.ylabel('number of articles')
    plt.title('Expert ' + name + ' Agreement-Disagreement Ratio With Our Model')
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()

    # Pass the plot to the template context
    return image_base64

def home(request):
    return render(request, 'home.html')

def myarticle(request):

    articles = PredictionApproves.objects.filter(expertId=request.user.id)
    return render(request, 'myarticle.html' ,{'articles': articles, 'image': generateGraph(request)})


def expertArticleList(request, expertId):

    articles = PredictionApproves.objects.filter(expertId=expertId)
    return render(request, 'myarticle.html' ,{'articles': articles, 'image': generateGraph(request)})



def myProfile(request):
    if request.method == 'POST':
        if request.POST.get('useridd'):
            idd=request.POST.get('useridd')
            first_name = request.POST.get('firstname')
            last_name = request.POST.get('lastname')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            profilepicture = request.FILES.get('profilepicture')
            certificatepicture = request.POST.get('certificatepicture')
            if first_name:
                UserData.objects.filter(user_id=idd).update(firstname=first_name)
            if last_name:
                UserData.objects.filter(user_id=idd).update(lastname=last_name)
            if password1 and password2 and password1 == password2:
                user = User.objects.get(username=idd)
                user.set_password(password1)
                user.save()
            if profilepicture:
                user1 = UserData.objects.get(user_id=idd)
                user1.pic = profilepicture
                user1.save()
            if certificatepicture:
                user2 = UserData.objects.get(user_id=idd)
                user2.Certificate = certificatepicture
                user2.save()

            users = UserData.objects.filter(user_id=idd)
            return render(request, 'myProfile.html', {'users': users})


        else:
            first_name = request.POST.get('firstname')
            last_name = request.POST.get('lastname')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            profilepicture = request.FILES.get('profilepicture')
            certificatepicture = request.POST.get('certificatepicture')
            if first_name:
                UserData.objects.filter(user_id=request.user.id).update(firstname=first_name)
            if last_name:
                UserData.objects.filter(user_id=request.user.id).update(lastname=last_name)
            if password1 and password2 and password1 == password2:
                user = User.objects.get(username=request.user.id)
                user.set_password(password1)
                user.save()
            if profilepicture:
                user1 = UserData.objects.get(user_id=request.user.id)
                user1.pic = profilepicture
                user1.save()
            if certificatepicture:
                user2 = UserData.objects.get(user_id=request.user.id)
                user2.Certificate = certificatepicture
                user2.save()

    users = UserData.objects.filter(user_id=request.user.id)
    return render(request, 'myProfile.html', {'users': users})
