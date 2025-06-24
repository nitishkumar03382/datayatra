from django.shortcuts import render
from django.http import HttpResponse
from course.models import Course, Chapter   
import markdown, markdown2

# from datayatra import course
# Create your views here.


def index(request):
    data = Course.objects.all()
    return   render(request, 'course/index.html', {'data': data})

def course_detail(request, course_id, chapter_order=0):
    # read md file from a dir
    print(course_id, chapter_order)
    
    # het course object with course_id and chapter_order
    course = Course.objects.get(course_id=course_id)
    # get the chapter object with chapter_order
    chapter = course.chapter_set.filter(chapter_order=chapter_order).first()
    if not chapter:
        return HttpResponse("Chapter not found", status=404)
    chapters = Chapter.objects.filter(course_id=course_id).order_by('chapter_order')
    chapter_name = chapter.chapter_name
    filepath = f"./course/Dy_courses/{course_id}/{chapter_name}.md"
    print(f"filepath: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        md_text = f.read()
    # convert md to html
    # md = markdown.Markdown()
    # html_text = md.convert(md_text)
    html_text = markdown2.markdown(md_text, extras=['fenced-code-blocks', 'tables', 'code-friendly', 'toc', 'cuddled-lists', 'strike', 'task_list', 'pyshell', 'highlightjs-lang'])
    context = {'course_content': html_text, 
               'course_id': course_id, 
               'chapter_order': chapter_order,
               'chapters': chapters,
               }
    return render(request, 'course/course_detail.html', context)
    