from django.shortcuts import render
from django.test import TestCase, Client
from django.urls import reverse


def home(request):
    return render(request, 'home.html')
