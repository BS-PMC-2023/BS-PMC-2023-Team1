from django.urls import path
from . import views

urlpatterns = [
   path('', views.favoriteExpert2, name='favoriteExpert'),
   path('favoriteExpert2', views.favoriteExpert2, name='favoriteExpert2'),
   path('filterex', views.filterex, name='filterex'),
   path('favoriteArticle', views.favoriteArticle1, name='favoriteArticle'),
   path('deleteArticle', views.deleteArticle, name='deleteArticle'),
      ]
