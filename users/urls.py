"""Определяем схемы url для пользователей"""

from django.contrib import admin
from django.urls import path, include
from users.views import *
app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),

]
