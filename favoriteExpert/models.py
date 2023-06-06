from django.db import models


# Create your models here.
class favoriteExpert(models.Model):
    expertId = models.IntegerField()
    userId = models.IntegerField()
