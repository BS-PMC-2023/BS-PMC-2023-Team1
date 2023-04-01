from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    firstname = forms.CharField()
    age = forms.IntegerField()
    gender = forms.CharField()
    isexpert = forms.BooleanField()

    class Meta:
        model = User
        fields = ['username', 'firstname', 'email', 'age', 'gender', 'password1', 'password2', 'isexpert']
