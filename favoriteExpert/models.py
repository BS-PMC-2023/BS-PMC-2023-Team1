from django.db import models


# Create your models here.
class favoriteExpert(models.Model):
    expertId = models.IntegerField()
    userId = models.IntegerField()


class favoriteArticle(models.Model):
    link = models.CharField(max_length=1000)
    userId = models.IntegerField()
