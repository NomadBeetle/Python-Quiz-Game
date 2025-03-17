from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Creating a list of Question objects
question_bank = [Question(q["question"], q["correct_answer"]) for q in question_data]

# Initializing the quiz
quiz_1 = QuizBrain(question_bank)

# Running the quiz until no questions remain
while quiz_1.still_has_questions():
    quiz_1.next_question()

# Display final score
print("You have completed the quiz!")
print(f"Your total score is: {quiz_1.score}/{quiz_1.question_no}")
