

from django.urls import path
from . import views
app_name = 'course'

urlpatterns = [
  path("", views.index, name="index"),
  path("python/", views.course_detail, name="course_detail"),
]

