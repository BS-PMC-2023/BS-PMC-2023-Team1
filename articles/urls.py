from django.urls import path

from . import views

urlpatterns = [
    path('', views.catalog),
    path('<str:ctro>', views.catalog2 , name='catalog2'),
]
