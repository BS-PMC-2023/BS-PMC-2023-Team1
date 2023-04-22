from django.shortcuts import render
from registration.models import UserData


def user_list(request):
    users = UserData.objects.all()
    return render(request, 'users.html', {'users': users})
