from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz_brain = quiz
        self.window = Tk()
        self.window.title("Python Quiz Game")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Score label
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 15))
        self.score_label.grid(row=0, column=1)

        # Question canvas
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="",
            font=("Arial", 16, "italic"),
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.true_button_pressed)
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.false_button_pressed)
        self.true_button.grid(row=3, column=0)
        self.false_button.grid(row=3, column=1)

        # Load the first question
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.reset_canvas_color()
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)

    def true_button_pressed(self):
        self.give_feedback(self.quiz_brain.check_answer("True"))

    def false_button_pressed(self):
        self.give_feedback(self.quiz_brain.check_answer("False"))

    def give_feedback(self, is_correct: bool):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def reset_canvas_color(self):
        self.canvas.config(bg="white")
