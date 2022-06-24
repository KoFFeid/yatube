from django import views
from django.urls import path
from . import views

app_name  = 'posts'

urlpatterns = [
    path('', views.index, name='main'),
    path('group/<slug:pk>/', views.group_posts, name='group')
]
