"""Определяем схемы url для пользователей"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from users.views import *
urlpatterns = [
    path('login/', login, name='Login'),
]
