from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic
from .forms import TopicForm
def index(request):
    return render(request, 'learning_logs/index.html')
def topics(request):
    """Выводит список тем"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
def topic(request, topic_id):
    """Выводит одну темуу и все ее записи"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Определяет новую тему"""
    if request.method != 'POST':
        #Данные не отправлялись; создается пустая форма
        form = TopicForm()
    else:
        #Отправлены данные POST; обратотать данные
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
