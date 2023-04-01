from django.contrib.auth.models import User
from django.shortcuts import render
import string
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UserRegisterForm
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.urls import reverse
##################################################################
####################index#######################################
from django.shortcuts import render
from django.utils.dateparse import parse_datetime
# Create your views here.
from .forms import UserRegisterForm
from .models import UserData
from django.contrib.auth.models import User


@csrf_exempt
def register_user(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            firstname = form.cleaned_data.get('firstname')
            age = form.cleaned_data.get('age')
            gender = form.cleaned_data.get('gender')
            isexpert = form.cleaned_data.get('isexpert')
            user = User.objects.get(username=username)
            user_data = UserData.objects.create(user=user, age=age, gender=gender, firstname=firstname,
                                                isexpert=isexpert)
            user_data.save()
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


###################################################################################
################login forms###################################################

def Login(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('neww')
        else:
            messages.info(request, f'account does not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form, 'title': 'log in'})