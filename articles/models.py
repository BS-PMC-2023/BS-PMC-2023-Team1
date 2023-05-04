from django.db import models


# Create your models here.
class ArticleCache(models.Model):
    link = models.CharField(max_length=200, default="unknown", primary_key=True)
    content = models.CharField(max_length=300, default="")
    img = models.CharField(max_length=200, default="")
    isFake = models.BooleanField(default=False)
