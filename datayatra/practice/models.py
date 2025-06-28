from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    QUESTION_TYPES = [
        ('SQL', 'SQL'),
        ('Pandas', 'Pandas'),
        ('Spark', 'Spark'),
        ('Python', 'Python'),
    ]
    DIFFICULTY_LEVELS = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]
    
    qid = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=QUESTION_TYPES)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_LEVELS)
    tags = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_markdown_path(self):
        return f"./practice/questions/{self.qid}/question.md"
    def get_testcase_path(self):
        return f"./practice/questions/{self.qid}/testcases.json"
    def __str__(self):
        return f"{self.title} [{self.category}]"  # Display title and category in admin panel

class Submisson(models.Model):
    STATUS_CHOICES = [
        ('Solved', 'Solved'),
        ('Unsolved', 'Unsolved'),
        ('Attempted', 'Attempted')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    code = models.TextField()
    status = models.CharField(max_length=20, default='Unsolved', choices=STATUS_CHOICES)
    is_passed = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.question.title} ({self.submitted_at})"