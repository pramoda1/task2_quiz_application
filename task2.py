import random

def display_categories():
    print("Quiz Categories:")
    print("1. General Knowledge")
    print("2. Science")
    print("3. Python Programming")
    print("4. Sports")
    print("5. Exit")



def load_questions(category):
    if category == "1":
        return general_knowledge_questions
    elif category == "2":
        return science_questions
    elif category == "3":
        return python_questions
    elif category == "4":
        return sports_questions
    elif category == "5":
        return None

def select_category():
    category = input("Select a category (1-5): ")
    return category


def shuffle_options(options):
    random.shuffle(options)
    return options

def display_question(question, options):
    print("\nQuestion: " + question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

def get_user_answer():
    user_answer = input("Enter the number of your answer: ")
    return user_answer

def evaluate_answer(user_answer, correct_answer, score):
    if user_answer == str(correct_answer):
        print("Correct!")
        return score + 1
    else:
        print(f"Wrong! The correct answer is {correct_answer}.")
        return score

def display_result(score, total_questions):
    print(f"\nYour Score: {score}/{total_questions}")
    percentage = (score / total_questions) * 100
    print(f"Percentage: {percentage}%")
    if percentage >= 70:
        print("Great job! You passed.")
    else:
        print("Try again. You didn't pass this time.")

# Questions and Answers
general_knowledge_questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "Berlin", "Madrid", "Rome"], "correct_answer": 1},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Venus", "Jupiter"], "correct_answer": 2},
    # Add more general knowledge questions here
]

science_questions = [
    {"question": "What is the chemical symbol for water?", "options": ["H2O", "CO2", "O2", "CH4"], "correct_answer": 1},
    {"question": "Who developed the theory of relativity?", "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"], "correct_answer": 2},
    # Add more science questions here
]

python_questions = [
    {"question": "What is the purpose of 'if __name__ == '__main__': in Python?", "options": ["Define a function", "Execute a block of code only if the script is run directly", "Import a module", "Declare a variable"], "correct_answer": 2},
    {"question": "What is a list comprehension in Python?", "options": ["A way to create lists", "A condition in an if statement", "A loop that iterates over a range", "A method to remove elements from a list"], "correct_answer": 1},
    # Add more Python programming questions here
]

sports_questions = [
    {"question": "Which sport is played at Wimbledon?", "options": ["Tennis", "Golf", "Soccer", "Cricket"], "correct_answer": 1},
    {"question": "Who is known as 'The Greatest' in boxing?", "options": ["Mike Tyson", "Muhammad Ali", "Floyd Mayweather", "Manny Pacquiao"], "correct_answer": 2},
    # Add more sports questions here
]

# Main Quiz Application
def main():
    score = 0
    total_questions = 5  # You can adjust this based on the number of questions you have per category

    while True:
        display_categories()
        category = select_category()

        if category == "5":
            print("Exiting the quiz. Goodbye!")
            break

        questions = load_questions(category)

        if questions is not None:
            random.shuffle(questions)
            for i in range(total_questions):
                current_question = questions[i]["question"]
                current_options = shuffle_options(questions[i]["options"])
                correct_answer = questions[i]["correct_answer"]

                display_question(current_question, current_options)
                user_answer = get_user_answer()
                score = evaluate_answer(user_answer, correct_answer, score)

            display_result(score, total_questions)
            score = 0  # Reset score for the next round

if __name__ == "__main__":
    main()
