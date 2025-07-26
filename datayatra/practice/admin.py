from django.contrib import admin
from .models import Question, Submisson, CaseStudy
# Register your models here.
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('qid', 'title', 'category', 'difficulty', 'case_study', 'created_at', 'updated_at')

@admin.register(Submisson)
class SubmissonAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'is_passed', 'submitted_at')
@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')