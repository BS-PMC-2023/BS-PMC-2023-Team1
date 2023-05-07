from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_list, name='users'),
    path('delete/<int:id>/', views.delete_user, name='delete_user'),
    path('approve/<int:id>/', views.approve, name='approve'),
]
