from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    course_id = models.CharField(max_length=100, primary_key=True)
    course_name = models.CharField(max_length=255)
    course_desc = models.TextField(null= True, blank=True)
    publisher_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Chapter(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    chapter_name = models.CharField(max_length=255)
    chapter_order = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    