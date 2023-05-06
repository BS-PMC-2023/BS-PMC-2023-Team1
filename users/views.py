from django.shortcuts import render, redirect
from registration.models import UserData
from django.contrib.auth.models import User


def user_list(request):
    onlineuser = UserData.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        if request.POST.get('expert'):
            users = UserData.objects.filter(isexpert=True)
            return render(request, 'users.html', {'users': users , 'onlineuser':onlineuser})
        else:
            users = UserData.objects.filter(isexpert=False)
            return render(request, 'users.html', {'users': users , 'onlineuser':onlineuser})

    users = UserData.objects.all()
    return render(request, 'users.html', {'users': users , 'onlineuser':onlineuser})

def delete_user(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('users')

