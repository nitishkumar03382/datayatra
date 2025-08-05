from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name="index"),
]


