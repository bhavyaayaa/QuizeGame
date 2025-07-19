import tkinter as tk
from tkinter import messagebox
import sqlite3
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QuizMaster GunGun")
        self.root.geometry("700x500")
        self.username = ""
        self.score = 0
        self.question_index = 0
        self.selected_difficulty = ""
        self.current_question = None

        self.show_welcome_screen()

    def show_welcome_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Welcome to \n Fun Time It's Quize Time \U0001F4DA", font=("Helvetica", 20)).pack(pady=20)

        tk.Label(self.root, text="Enter your name:").pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=5)

        tk.Button(self.root, text="Start Quiz", command=self.select_difficulty).pack(pady=20)

    def select_difficulty(self):
        self.username = self.name_entry.get().strip()
        if not self.username:
            messagebox.showwarning("Input Error", "Please enter your name.")
            return

        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"Hi {self.username}! Choose Difficulty:", font=("Helvetica", 16)).pack(pady=20)
        for level in ["Easy", "Medium", "Hard"]:
            tk.Button(self.root, text=level, font=("Helvetica", 14), width=20,
                      command=lambda l=level: self.start_quiz(l)).pack(pady=5)

    def start_quiz(self, difficulty):
        self.selected_difficulty = difficulty.lower()
        self.score = 0
        self.question_index = 0

        conn = sqlite3.connect("quiz.db")
        cursor = conn.cursor()
        cursor.execute("SELECT question, option1, option2, option3, option4, answer FROM questions WHERE difficulty = ?", (self.selected_difficulty,))
        self.questions = cursor.fetchall()
        conn.close()

        if not self.questions:
            messagebox.showerror("Error", f"No questions found for difficulty: {difficulty}")
            self.show_welcome_screen()
            return

        random.shuffle(self.questions)
        self.show_question()

    def show_question(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.current_question = self.questions[self.question_index]

        question_text = self.current_question[0]
        options = self.current_question[1:5]

        tk.Label(self.root, text=f"Question {self.question_index + 1} of {len(self.questions)}", font=("Helvetica", 14)).pack(pady=10)
        tk.Label(self.root, text=question_text, wraplength=600, font=("Helvetica", 16)).pack(pady=20)

        self.selected_option = tk.StringVar()
        for opt in options:
            tk.Radiobutton(self.root, text=opt, variable=self.selected_option, value=opt, font=("Helvetica", 14)).pack(anchor="w", padx=100)

        tk.Button(self.root, text="Next", command=self.next_question).pack(pady=20)

    def next_question(self):
        selected = self.selected_option.get()
        if selected == self.current_question[5]:
            self.score += 1

        self.question_index += 1
        if self.question_index < len(self.questions):
            self.show_question()
        else:
            self.show_result()
            
    def show_result(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"Quiz Completed, {self.username}!", font=("Helvetica", 18)).pack(pady=20)
        tk.Label(self.root, text=f"Your Score: {self.score} out of {len(self.questions)}", font=("Helvetica", 16)).pack(pady=10)

        #Motivation line based on performance
        percentage = self.score / len(self.questions)

        if percentage == 1.0:
            message = "🌟 Perfect score! You're a Quize Master!"
        elif percentage >= 0.8:
            message = "🔥 Great job! You're doing amazing Dude!"
        elif percentage >= 0.5:
            message = "👍 Good effort! Keep practicing Dude!"
        else:
            message = "💡 Don't give up! Practice makes perfect... Dude!"

        tk.Label(self.root, text=message, font=("Helvetica", 14), fg="blue").pack(pady=10)

        tk.Button(self.root, text="Play Again", command=self.show_welcome_screen).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

