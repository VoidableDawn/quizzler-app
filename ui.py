from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg = THEME_COLOR, padx = 20, pady = 20)

        self.score = Label(text = "Score: 0",
                           font = ("Arial", 10, "normal"),
                           fg = "white", bg = THEME_COLOR)
        self.score.grid(column = 1, row = 0)

        true_image = PhotoImage(file = "images/true.png")
        false_image = PhotoImage(file = "images/false.png")

        self.canvas = Canvas(width = 300, height = 250, bg = "white")
        self.question_text = self.canvas.create_text(150, 125, text = "Sample Text",
                                                     width = 280,
                                                     font = FONT, fill = THEME_COLOR)
        self.canvas.grid(column = 0, row = 1, columnspan = 2, pady = 50)

        self.true_button = Button(image = true_image, bg = THEME_COLOR,
                                  borderwidth = 0, command = self.check_true)
        self.true_button.grid(column = 0, row = 2)

        self.false_button = Button(image = false_image, bg = THEME_COLOR,
                                   borderwidth = 0, command = self.check_false)
        self.false_button.grid(column = 1, row = 2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg = "white")
        if self.quiz.still_has_questions():
            self.score.config(text = f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text = "You have reached the end of the quiz")
            self.true_button.config(state = "disabled")
            self.false_button.config(state = "disabled")


    def check_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def check_false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")
        self.window.after(1000, func = self.get_next_question)
