from tkinter import *
from quiz_brain import QuizBrain

FONT = ("Arial", 20, "italic")
LABEL_FONT = ("Aria", 12, "bold")
THEME_COLOR = "#375362"

def dummy():
    pass


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(self.window, text="Score: 0", fg="white", bg=THEME_COLOR, font=LABEL_FONT)
        self.score_label.grid(row=0, column=1)

        self.question_display = Canvas(width=300, height=250, bg="white")
        self.question_text = self.question_display.create_text(150, 125, text="Some Question?", fill=THEME_COLOR, font=FONT, width=270)
        self.question_display.grid(row=1, column=0, columnspan=2, pady=50)

        right = PhotoImage(file="images/true.png")
        wrong = PhotoImage(file="images/false.png")

        self.right_button = Button(image=right, command=self.true_pressed, highlightthickness=0)
        self.right_button.grid(row=2, column=0)

        self.wrong_button = Button(image=wrong, command=self.false_pressed, highlightthickness=0)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_display.config(bg="white")
        if self.quiz.question_number < 10:
            q_text = self.quiz.next_question()
            self.question_display.itemconfig(self.question_text, text=q_text)
        else:
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
            self.question_display.itemconfig(self.question_text, text="You've reached the end of the quiz.")

    def true_pressed(self):
        if self.quiz.check_answer("True"):
            self.question_display.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.question_display.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def false_pressed(self):
        if self.quiz.check_answer("False"):
            self.question_display.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.question_display.config(bg="red")
        self.window.after(1000, self.get_next_question)



