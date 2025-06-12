from django.shortcuts import render
from django.http import HttpResponse
import markdown
# Create your views here.


def index(request):
    return   render(request, 'course/index.html', {})

def course_detail(request):
    # read md file from a dir
    filepath = "./course/Dy_courses/Python/introduction_to_python.md"
    with open(filepath, 'r', encoding='utf-8') as f:
        md_text = f.read()
    # convert md to html
    md = markdown.Markdown()
    html_text = md.convert(md_text)
    context = {'course_content': html_text}
    return render(request, 'course/course_detail.html', context)
    