#password = kumar9110
#username=vicky911095
from django.shortcuts import render, redirect
from .models import Blog
from .form import BlogForm



def index(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/index.html', {'blogs': blogs})

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog:index')
    else:
        form = BlogForm()


    return render(request, 'blog/create_blog.html', {'form': form})

def view_all(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


# def view_all(request):
#     blogs = Blog.objects.all()
#     return render(request, 'blog/all_blogs.html', {'blogs': blogs})
