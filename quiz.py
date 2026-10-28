"""Quiz Application with Score Tracking Using Python.

A menu-driven console quiz: asks MCQs, checks answers instantly,
shows score, percentage and grade, and saves results to scores.txt.
"""

from datetime import date

SCORE_FILE = "scores.txt"

# Each question: (question text, [options], number of the correct option)
QUESTIONS = [
    ("Which keyword is used to define a function in Python?",
     ["func", "def", "function", "define"], 2),
    ("Which symbol is used for comments in Python?",
     ["//", "/*", "#", "--"], 3),
    ("Which data type stores True or False?",
     ["int", "str", "float", "bool"], 4),
    ("What does HTML stand for?",
     ["HyperText Markup Language", "High Text Machine Language",
      "Hyper Tool Markup Language", "Home Text Markup Language"], 1),
    ("Which function prints output in Python?",
     ["show()", "print()", "display()", "echo()"], 2),
    ("Which of these is a database?",
     ["Python", "Chrome", "SQLite", "Notepad"], 3),
]


def ask_question(number, question):
    text, options, answer = question
    print(f"\nQ{number}. {text}")
    for i, opt in enumerate(options, 1):
        print(f"   {i}. {opt}")
    while True:
        choice = input("Your answer (1-4): ")
        if choice in ("1", "2", "3", "4"):
            break
        print("Invalid input. Please enter a number from 1 to 4.")
    if int(choice) == answer:
        print("Correct!")
        return 1
    print(f"Wrong! Correct answer: {options[answer - 1]}")
    return 0


def get_grade(percent):
    if percent >= 80:
        return "Excellent"
    elif percent >= 50:
        return "Good"
    return "Needs Practice"


def save_score(name, score, total):
    with open(SCORE_FILE, "a") as f:
        f.write(f"{name.replace(',', ' ')},{score},{total},{date.today()}\n")


def start_quiz():
    name = input("Enter your name: ")
    score = 0
    for number, question in enumerate(QUESTIONS, 1):
        score += ask_question(number, question)
    total = len(QUESTIONS)
    percent = score / total * 100
    print("\n----- RESULT -----")
    print(f"Name   : {name}")
    print(f"Score  : {score} / {total}")
    print(f"Percent: {percent:.1f}%")
    print(f"Grade  : {get_grade(percent)}")
    save_score(name, score, total)


def view_scores():
    try:
        with open(SCORE_FILE) as f:
            records = [line.strip().split(",") for line in f if line.strip()]
    except FileNotFoundError:
        print("No scores saved yet.")
        return
    records.sort(key=lambda r: int(r[1]), reverse=True)
    print("\nRank | Name         | Score | Date")
    print("-" * 42)
    for rank, r in enumerate(records[:5], 1):
        print(f"{rank:<4} | {r[0]:<12} | {r[1]}/{r[2]:<3} | {r[3]}")


def main():
    while True:
        print("\n===== QUIZ APPLICATION =====")
        print("1. Start Quiz")
        print("2. View High Scores")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            start_quiz()
        elif choice == "2":
            view_scores()
        elif choice == "3":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
