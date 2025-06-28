

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_blog, name='create_blog'),
]
