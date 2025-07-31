import os
import re
import markdown
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Course


# ✅ Helper to clean chapter titles from filenames
def clean_title(filename):
    name = re.sub(r"^\d+(\.\d+)?[_ ]*", "", filename)  # Remove leading digits, underscore or space
    name = name.replace(".md", "").replace("_", " ").strip()
    return name.capitalize()


# ✅ Get all chapter metadata from markdown files
def get_chapter_list():
    folder = os.path.join(settings.BASE_DIR, 'course', 'Dy_courses', 'Python')
    files = sorted([f for f in os.listdir(folder) if f.endswith('.md')])
    return [{"filename": f, "title": clean_title(f)} for f in files]


# ✅ Main view for the course
def index(request):
    chapters = get_chapter_list()
    chapter_param = request.GET.get('chapter')
    current = next((c for c in chapters if c["filename"] == chapter_param), chapters[0])
    current_index = chapters.index(current)

    filepath = os.path.join(settings.BASE_DIR, 'course', 'Dy_courses', 'Python', current["filename"])
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            md_text = f.read()
    except FileNotFoundError:
        return HttpResponse("Chapter not found.", status=404)

    # ✅ Convert Markdown to HTML
    html = markdown.markdown(md_text)

    # ✅ Determine previous and next chapters
    prev_chapter = chapters[current_index - 1] if current_index > 0 else None
    next_chapter = chapters[current_index + 1] if current_index < len(chapters) - 1 else None

    # ✅ Define course milestone triggers
    milestones = {
        "operator": 25,
        "list comprehension": 50,
        "join tuple": 75,
        "python dictionary": 100,
    }

    # ✅ Check if `?next=1` is present and current chapter is a milestone
    milestone_percent = 0
    if 'next' in request.GET:
        current_title = current["title"].lower()
        for keyword, percent in milestones.items():
            if keyword in current_title:
                milestone_percent = percent
                break

    # ✅ Render the course reading page
    return render(request, 'course/python.html', {
        "markdown_content": html,
        "chapters": chapters,
        "current_chapter": current["filename"],
        "prev_chapter": prev_chapter,
        "next_chapter": next_chapter,
        "milestone_percent": milestone_percent,
    })


# ✅ Show all available courses (if needed)
def course_detail(request):
    courses = Course.objects.all()
    return render(request, 'course/course_detail.html', {'courses': courses})


# ✅ Start a specific course/chapter manually (if needed)
def start_course(request, course_id, chapter):
    course = get_object_or_404(Course, course_id=course_id)
    return render(request, 'course/start.html', {
        'course': course,
        'chapter': chapter
    })
