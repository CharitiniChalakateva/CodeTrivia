# main.py
from quiz import Quiz

if __name__ == "__main__":
    from questions import questions
    quiz = Quiz(questions)
    quiz.start_quiz()
