# quiz.py
import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions

    def start_quiz(self):
        score = 0
        random.shuffle(self.questions)
        for question in self.questions:
            print(question["question"])
            for i, option in enumerate(question["options"]):
                print(f"{i + 1}. {option}")
            user_answer = input("Enter the number of your answer: ")
            if user_answer == str(question["options"].index(question["correct_answer"]) + 1):
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer is {question['correct_answer']}\n")
        print(f"Quiz finished. Your score is {score}/{len(self.questions)}")

if __name__ == "__main__":
    from questions import questions
    quiz = Quiz(questions)
    quiz.start_quiz()
