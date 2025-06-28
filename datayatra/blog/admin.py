
from django.contrib import admin
from .models import Blog
# Register your models here.
#admin.site.register(Blog)
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
        list_display = ('title','date_created','likes')

