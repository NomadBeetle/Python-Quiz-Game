from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface


def create_question_bank(data: list[dict]) -> list[Question]:
    return [Question(q["question"], q["correct_answer"]) for q in data]


def main():
    question_bank = create_question_bank(question_data)
    quiz = QuizBrain(question_bank)
    QuizInterface(quiz)  # GUI handles mainloop and quiz progression

    # Final score display (optional for CLI fallback)
    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")


if __name__ == "__main__":
    main()
