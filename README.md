# CodeTrivia in Python

This is a simple quiz application implemented in Python. It allows you to play a quiz game with a set of questions and multiple-choice answers. You can customize the questions by editing the `questions.py` file.

## How to Run

Follow these steps to run the quiz app:

1. Clone the repository to your local machine: 
 git clone (example : this repository)

2. Navigate to the project directory:
cd this repository

3. Start the quiz by running the `main.py` file:
python main.py

4. The quiz will start, and you will be asked a series of questions. Choose your answers by entering the corresponding number.

5. At the end of the quiz, your score will be displayed.

## Customizing Questions

You can customize the quiz questions by editing the `questions.py` file. Each question is represented as a dictionary with the following format:

```python
{
{
        "question": "What is the role of the CPU in a computer?",
        "options": [
            "Executes programming commands.",
            "Performs calculations and data processing.",
            "Manages computer memory.",
            "Handles networking operations."
        ],
        "correct_answer": "Performs calculations and data processing."
    },
    {
        "question": "What does HTML stand for?",
        "options": [
            "Hypertext Markup Language",
            "High-Level Text Markup Language",
            "Hyperlink and Text Markup Language",
            "Home Tool Markup Language"
        ],
        "correct_answer": "Hypertext Markup Language"
    },
    {
        "question": "What programming language is known for its readability and is commonly used for web development?",
        "options": ["Java", "Python", "C++", "Ruby"],
        "correct_answer": "Python"
    },
    {
        "question": "What is a database management system (DBMS)?",
        "options": [
            "A type of computer hardware.",
            "Software for managing computer files.",
            "A system for tracking physical items in a warehouse.",
            "Software for managing and interacting with databases."
        ],
        "correct_answer": "Software for managing and interacting with databases."
    },
    {
        "question": "What is an algorithm?",
        "options": [
            "A type of computer virus.",
            "A step-by-step procedure for solving a problem.",
            "A computer's physical components.",
            "A type of computer programming language."
        ],
        "correct_answer": "A step-by-step procedure for solving a problem."
    },
    {
        "question": "What is object-oriented programming (OOP)?",
        "options": [
            "A type of computer network architecture.",
            "A software development methodology.",
            "A type of computer memory.",
            "A way to format text in a word processor."
        ],
        "correct_answer": "A software development methodology."
    }
}