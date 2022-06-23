from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def index(request):
    return render(request, 'posts/index.html')


def group_posts(request, slug):
    return render(request, 'posts/group_list.html')