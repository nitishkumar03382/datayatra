from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    comment = models.TextField(null=True,blank=True)
    github_link = models.URLField(max_length=500, null=True, blank=True)
    author =  models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title
