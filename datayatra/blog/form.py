from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 3,
                'class': 'form-control',
                'placeholder': 'Write your blog content here...'
            }
        )
    )

    class Meta:
        model = Blog
        fields = ('title', 'content', 'github_link')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Blog title'
            }),
            'github_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://github.com/your-repo'
            }),
        }
