from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def index(request):
    context = {'title':"Это главная страница проекта Yatube"}
    return render(request, 'posts/index.html', context)


def group_posts(request, pk):
    context = {'title':"Здесь будет информация о группах проекта Yatube"}
    return render(request, 'posts/group_list.html', context)