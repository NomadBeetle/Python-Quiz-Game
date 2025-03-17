class QuizBrain:
    def __init__(self, question_list):
        """Initializes the quiz with a list of questions."""
        self.question_no = 0  # Tracks the current question number
        self.score = 0  # Stores the user's score
        self.question_list = question_list  # Stores the list of questions

    def still_has_questions(self):
        """Checks if there are remaining questions in the quiz."""
        return self.question_no < len(self.question_list)

    def check_answer(self, answer, correct_a):
        """Compares user's answer with the correct answer and updates score."""
        if answer.lower() == "exit":
            self.question_no = len(self.question_list)  # Ends the quiz immediately
        elif answer.lower() == correct_a.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's Wrong")
        print(f"The correct answer was: {correct_a}")
        print(f"Your current score is {self.score}/{self.question_no}")
        print("\n")

    def next_question(self):
        """Displays the next question and gets user input."""
        question = self.question_list[self.question_no]
        ans = input(f"Q{self.question_no + 1}: {question.text} (True/False)? : ")

        if ans.lower() == "exit":
            print("Exiting the quiz...")
            self.question_no = len(self.question_list)  # Ensures loop breaks
            return

        self.question_no += 1
        self.check_answer(ans, question.answer)
