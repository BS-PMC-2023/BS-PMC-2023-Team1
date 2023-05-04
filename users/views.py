from django.shortcuts import render, redirect
from registration.models import UserData
from django.contrib.auth.models import User


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

def delete_user(request, id):
    print(id)
    user = User.objects.get(id=id)
    user.delete()
    return redirect('users')


