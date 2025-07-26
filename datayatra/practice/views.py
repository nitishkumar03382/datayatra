from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, StreamingHttpResponse
from django.http import JsonResponse
from django.db import connection, connections
import sqlite3
import json
import markdown
import os
from django.http import Http404
from .utils import markdown_to_html
from .utils import checktestcase
from .models import Question, Submisson, CaseStudy
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import time



def checktestcase(user_code, query, setup, i):
    """
    Check User code against test cases.
    """
    columns, result, user_op = [], [], []
    conn = sqlite3.connect(':memory:')  # Use in-memory SQLite database for testing
    connection = conn
    with connections['sandbox'].cursor() as cursor:
        # run setup queries
        for qry in setup:
            if not qry.strip():
                continue
            cursor.execute(qry)
        # run user code
        try:
            cursor.execute(user_code)
            result = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            user_op = [dict(zip(columns, row)) for row in result]
        except Exception as e:
            print(f"Error executing user query: {e}")
            return {"status": "error", "message": f"Error in Testcase {i}" + str(e), "code": 400}
    # run test case query
    with connections['sandbox'].cursor() as cursor:
        cursor.execute(query)
        tc_result = cursor.fetchall()
        tc_columns = [desc[0] for desc in cursor.description]
        tc_op = [dict(zip(tc_columns, row)) for row in tc_result]
    # check if user output matches test case output
    is_ordered = False  # Set to True if order matters
    if user_op == tc_op and is_ordered:
        return {"status": "success", "message": f"Test case {i} passed ✅", "code": 200}
    elif sorted(result) == sorted(tc_result) and columns == tc_columns and not is_ordered:
        return {"status": "success", "message": f"Test case {i} passed ✅", "code": 200}
    else:
        return {"status": "error", "message": f"Test case {i} failed ❌", "code": 400}
    


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
        
        with connections['sandbox'].cursor() as cursor:
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
@csrf_exempt
@login_required
def submit_code(request, qid):
    if request.user.is_authenticated:
        user = request.user
    else:
        return JsonResponse({"error": "User not authenticated"}, status=401)
    
    if request.method == 'POST':
        user_code = request.POST.get('user_code', '')
        if not user_code:
            return JsonResponse({"error": "No code provided"}, status=400)
        print(f"Received code for question {qid}: {user_code[:50]}...")  # Log first 50 characters for brevity
        question = get_object_or_404(Question, qid=qid)
        tc_filepath = question.get_testcase_path()  
        print(f"Loading test cases from: {tc_filepath}")
        with open(tc_filepath, 'r', encoding='utf-8') as f:
            test_cases = json.load(f)
        test_case_results = []
        i = 1
        is_success = True
        for test_case in test_cases:
            check_result = checktestcase(user_code, test_case['query'], test_case['setup'], i)
            print(f"Test case {i} result: {check_result}")
            if check_result['status'] == 'error':
                is_success = False
                # return JsonResponse(check_result)
            test_case_results.append(check_result)
            i += 1
        context = {
            'test_case_results': test_case_results
        }
        # Save submission to the database
        submission = Submisson( 
            user=user,
            question=question,
            code=user_code,
            status='Solved' if is_success else 'Attempted',
            is_passed=is_success
        )
        submission.save()
    return JsonResponse(context)


def get_question_status(user, question_id, submission_map=None):
    """
    Returns the status of a question for a user: 'Solved', 'Attempted', or 'Unsolved'.
    If user is not authenticated, returns empty string.
    
    Optionally pass a submission_map {question_id: [submissions]} for performance.
    """
    if not user.is_authenticated:
        return ""

    if submission_map is None:
        from .models import Submisson
        submissions = Submisson.objects.filter(user=user, question_id=question_id)
    else:
        submissions = submission_map.get(question_id, [])

    if any(sub.is_passed for sub in submissions):
        return "Solved"
    elif submissions:
        return "Attempted"
    else:
        return "Unsolved"
def question_list(request):
    user = request.user
    questions = Question.objects.all()
    question_list = []

    # Build submission_map for efficiency
    if user.is_authenticated:
        user_submissions = Submisson.objects.filter(user=user)
        submission_map = {}
        for sub in user_submissions:
            submission_map.setdefault(sub.question_id, []).append(sub)
    else:
        submission_map = {}

    for question in questions:
        status = get_question_status(user, question.qid, submission_map)
        question_list.append({
            'qid': question.qid,
            'title': question.title,
            'category': question.category,
            'difficulty': question.difficulty,
            'tags': question.tags,
            'created_at': question.created_at,
            'updated_at': question.updated_at,
            'status': status,
        })

    return render(request, 'practice/question_list.html', {'questions': question_list})


def solve(request, qid):
    """
    Render the solve page for a specific question.
    """
    if request.user.is_authenticated:
        user = request.user
        submissons = Submisson.objects.filter(user=user, question__qid=qid)
        if submissons.exists():
            latest_submissons = submissons.order_by('-submitted_at').first()
            passed_submissions = submissons.filter(is_passed=True)
            if passed_submissions.exists():
                status = 'Solved'
            else:
                status = 'Attempted'
        else:
            status = 'Unsolved'
    else:
        user = None
        status = None
    
    question = get_object_or_404(Question, qid=qid)
    filepath = question.get_markdown_path()
    if not os.path.exists(filepath):
        raise Http404("Question not found.")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        md_text = f.read()
    
    question_description = markdown_to_html(md_text)
    context = {'question': question, 'question_description': question_description, 'status': status, 'user': user}
    return render(request, 'practice/solve.html', context)

def case_study(request):
    case_studies = CaseStudy.objects.all()
    return render(request, 'practice/case_study.html', {'case_studies': case_studies})
def case_study_questions(request, case_study_id):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "User not authenticated"}, status=401)
    
    case_study = get_object_or_404(CaseStudy, id=case_study_id)
    questions = Question.objects.filter(case_study=case_study)

    # Calculate progress
    progress = get_case_study_progress(request.user, case_study.id)
    print(f"Progress for case study {case_study.title}: {progress}%")

    # Fetch all submissions once for efficiency
    if request.user.is_authenticated:
        user_submissions = Submisson.objects.filter(user=request.user, question__in=questions)
        submission_map = {}
        for sub in user_submissions:
            submission_map.setdefault(sub.question_id, []).append(sub)
    else:
        submission_map = {}

    # Add status per question
    question_list = []
    for q in questions:
        status = get_question_status(request.user, q.qid, submission_map)
        question_list.append({
            'qid': q.qid,
            'title': q.title,
            'category': q.category,
            'difficulty': q.difficulty,
            'tags': q.tags,
            'created_at': q.created_at,
            'updated_at': q.updated_at,
            'status': status,
        })

    return render(request, 'practice/case_study_questions.html', {
        'case_study': case_study,
        'questions': question_list,
        'progress': progress
    })

def get_case_study_progress(user, case_study_id):
    case_study = CaseStudy.objects.get(id=case_study_id)
    
    # Total questions in case study
    total_questions = Question.objects.filter(case_study=case_study).count()
    
    # Solved questions by user (only the ones passed)
    solved_question_ids = Submisson.objects.filter(
        user=user,
        question__case_study=case_study,
        is_passed=True
    ).values_list('question_id', flat=True).distinct()
    
    solved_count = solved_question_ids.count()

    progress = (solved_count / total_questions) * 100 if total_questions > 0 else 0
    return round(progress, 2)