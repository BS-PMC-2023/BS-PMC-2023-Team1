from django.shortcuts import render
from registration.models import UserData


def user_list(request):
    if request.method == 'POST':
        if request.POST.get('expert'):
            users = UserData.objects.filter(isexpert=True)
            return render(request, 'users.html', {'users': users})
        else:
            users = UserData.objects.filter(isexpert=False)
            return render(request, 'users.html', {'users': users})

    users = UserData.objects.all()
    return render(request, 'users.html', {'users': users})


