from django.shortcuts import render
from registration.models import UserData

from django.contrib.auth.models import User
import os
from django.conf import settings


def home(request):
    return render(request, 'home.html')


def myProfile(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        profilepicture = request.FILES.get('profilepicture')
        certificatepicture = request.POST.get('certificatepicture')
        if first_name:
            UserData.objects.filter(id=request.user.id).update(firstname=first_name)
        if last_name:
            UserData.objects.filter(id=request.user.id).update(lastname=last_name)
        if password1 and password2 and password1 == password2:
            user = User.objects.get(username=request.user.username)
            user.set_password(password1)
            user.save()
        if profilepicture:
            user1 = UserData.objects.get(id=request.user.id)
            user1.pic = profilepicture
            user1.save()
        if certificatepicture:
            user2 = UserData.objects.get(id=request.user.id)
            user2.Certificate = certificatepicture
            user2.save()

    users = UserData.objects.filter(id=request.user.id)
    return render(request, 'myProfile.html', {'users': users})
