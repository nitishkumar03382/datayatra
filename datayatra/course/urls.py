from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'course'

urlpatterns = [ 
    path("python/", views.index, name="index"),
    path('', views.course_detail, name='course_list'),  # Main course list
    path('<str:course_id>/<int:chapter>/', views.start_course, name='start'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # ✅ also fixed: documents_root → document_root
