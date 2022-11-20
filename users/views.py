from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponse
# Create your views here.

def register(request):
    """Регистрируем нового пользователя"""
    if request.method != 'POST':
        #Выводит пустую форму регистрации
        form = UserCreationForm
    else:
        #Обработка заполненной формы
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #Выполнение входа и перенаправление на домашнюю страницу
            login(request, new_user)
            return redirect('Home')
    #Вывести пустую или неработающую форму
    context = {'form': form}
    return render(request, 'users/register.html', context)
