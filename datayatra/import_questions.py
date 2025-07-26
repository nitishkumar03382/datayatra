import os
import json
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "datayatra.settings")
django.setup()

from practice.models import Question  # Adjust if your model path is different

# Root directory for all questions
QUESTIONS_DIR = "./practice/questions"

def import_questions():
    for folder in os.listdir(QUESTIONS_DIR):
        folder_path = os.path.join(QUESTIONS_DIR, folder)

        question_id = folder
        print(f"Processing Question ID: {question_id}")
        
        if Question.objects.filter(qid=question_id).exists():
            print(f"  Question {question_id} already exists. Skipping.")
            continue
        title = question_id.replace('_', ' ')[5:].title()
        category = 'SQL'
        difficulty = 'Easy'
        tags = ['SQL', 'Database']
    
        # Create and save the Question object
        question = Question(
            qid=question_id,
            title=title,
            category=category,
            difficulty=difficulty,
            tags=tags
        )
        question.save()

if __name__ == "__main__":
    import_questions()
    print("Question import completed.")