from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    firstname = forms.CharField()
    lastname = forms.CharField()
    isexpert = forms.BooleanField(required=False)
    pic = forms.ImageField(required=False)
    isAdmin = forms.BooleanField(required=False)
    Certificate = forms.ImageField(required=False)
    Pending = forms.BooleanField(required=False)
    class Meta:
        model = User
        fields = ['username', 'firstname', 'email', 'lastname', 'password1', 'password2', 'isexpert', 'pic',
                  'isAdmin', 'Certificate','Pending']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email