from django.urls import path

from . import views
app_name = 'practice'
urlpatterns = [
    path("run/<str:qid>/", views.run_code, name="run_code"),
    path("submit_code/<str:qid>/", views.submit_code, name="submit_code"),
    path("", views.index, name="index"),
    path("question_list/", views.question_list, name="question_list"),
    path("solve/<str:qid>/", views.solve, name="solve"),
    
]