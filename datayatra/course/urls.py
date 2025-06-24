

from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'course'

urlpatterns = [
  path("", views.index, name="index"),
  path("course/<str:course_id>/<str:chapter_order>", views.course_detail, name="course_detail"),
]

urlpatterns += static(settings.MEDIA_URL, documents_root = settings.MEDIA_ROOT)
