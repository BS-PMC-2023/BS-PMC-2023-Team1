from django.db import models
from registration.models import UserData


# Create your models here.
class ArticleCache(models.Model):
    link = models.CharField(max_length=200, default="unknown", primary_key=True)
    content = models.CharField(max_length=300, default="")
    img = models.CharField(max_length=200, default="")
    isFake = models.BooleanField(default=False)


class PredictionApproves(models.Model):
    link = models.CharField(max_length=200, default="unknown")
    expertId = models.ForeignKey(UserData, on_delete=models.CASCADE)
    approved = models.BooleanField(default=True) # True for like, False for dislike
