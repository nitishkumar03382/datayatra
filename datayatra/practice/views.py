from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection
import json
import markdown
import os
from django.http import Http404
from .utils import markdown_to_html
from .utils import checktestcase
from .models import Question, Submisson
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

def index(request):
    """
    Render the index page of the practice app.
    """
    # get question by id from database
    # question = get_object_or_404(Question, pk="0002_some_patients")
    # # get markdown file path from question model
    # print(question.get_markdown_path())
    filepath = os.path.join("./practice/questions/0002_some_patients/question.md")
    print(f"Loading question from: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        md_text = f.read()
    question_description = markdown_to_html(md_text)
    context = {'question_description': question_description}
    return render(request, 'practice/index.html', context)

@login_required
def run_code(request, qid):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "User not authenticated"}, status=401)
    if request.method == "POST":
        p_error = False
        user_op = []
        tc_op = []
        result = []
        tc_result = []
        columns = []
        tc_columns = []
        p_status = {}
        status = {}
        user_input = request.POST.get("user_code")
        question = get_object_or_404(Question, qid=qid)
        testcase_path = question.get_testcase_path()
        print(f"Loading test cases from: {testcase_path}")
        is_ordered = False
        tc_filepath = question.get_testcase_path()
        with open(tc_filepath, 'r', encoding='utf-8') as f:
            test_cases = json.load(f)
        with connection.cursor() as cursor:
            #execute test case setup
            setup_qry = test_cases[0]['setup']
            print(f"Executing setup query: {setup_qry}")
            for qry in setup_qry:
                if not qry.strip():
                    continue

                cursor.execute(qry)

            # Execute user input query
            print(f"Executing user input query...")
            try:
                cursor.execute(user_input)
                result = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                user_op = [dict(zip(columns, row)) for row in result]
            except Exception as e:
                print(f"Error executing user query: {e}")
                p_error = True
                p_status = {"status": "error", "message": str(e), "code":400}
                p_context = {"status": p_status}
                
            # Test case query execution
            print("Executing test case query...")
            cursor.execute(test_cases[0]['query'])
            tc_result = cursor.fetchall()
            tc_columns = [desc[0] for desc in cursor.description]
            tc_op = [dict(zip(tc_columns, row)) for row in tc_result]
        
        print("Checking test case...")
        
        if user_op == tc_op and is_ordered == True:
            print("Test case passed.")
            status = {"status": "success", "message": "Test case passed."}
        elif sorted(result) == sorted(tc_result) and columns == tc_columns and is_ordered == False:
            print("Test case passed.")
            status = {"status": "success", "message": "Test case passed ✅", "code":200}
        else:
            print("Test case failed.")
            status = {"status": "error", "message": "Test case failed ❌", "code":400}
        if p_error:
            context = {"result": result, "columns": columns,
                   "tc_result": tc_result, "tc_columns": tc_columns,
                   "status": p_status}
        else:
            context = {"result": result, "columns": columns,
                    "tc_result": tc_result, "tc_columns": tc_columns,
                    "status": status}
        
        return JsonResponse(context)

def question_list(request):
    """
    Get all questions from the database.
    """
    questions = Question.objects.all()
    question_list = []
    for question in questions:
        question_list.append({
            'qid': question.qid,
            'title': question.title,
            'category': question.category,
            'difficulty': question.difficulty,
            'tags': question.tags,
            'created_at': question.created_at,
            'updated_at': question.updated_at
        })
    return render(request, 'practice/question_list.html', {'questions': question_list})
@csrf_exempt
def submit_code(request, qid):
    print("Received code submission")
    if request.method == "POST":
        data = json.loads(request.body)
        code = data.get("code")
        user = request.user
        question = get_object_or_404(Question, qid=qid)
        if not code:
            return JsonResponse({"error": "No code provided"}, status=400)
        # Save the submission
        submission = Submisson.objects.create(
            user=user,
            question=question,
            code=code
        )
        submission.save()
        return JsonResponse({"message": "Code submitted successfully", "submission_id": submission.id}, status=201)


def solve(request, qid):
    """
    Render the solve page for a specific question.
    """
    question = get_object_or_404(Question, qid=qid)
    filepath = question.get_markdown_path()
    if not os.path.exists(filepath):
        raise Http404("Question not found.")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        md_text = f.read()
    
    question_description = markdown_to_html(md_text)
    context = {'question': question, 'question_description': question_description}
    return render(request, 'practice/solve.html', context)