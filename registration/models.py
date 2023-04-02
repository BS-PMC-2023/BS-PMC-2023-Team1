from django.contrib.auth.models import User
from django.db import models


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20, default='SOME STRING')
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20)
    isexpert = models.BooleanField(default=True)
    pic = models.ImageField(upload_to='media/', null=True)

  # if your using 'title' as the attribute to identify your objects
