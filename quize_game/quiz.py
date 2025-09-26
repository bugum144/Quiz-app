import tkinter as tk
from tkinter import messagebox

quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "answer": "Blue Whale"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "JavaScript", "C++", "Java"],
        "answer": "JavaScript"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f4f7")
        self.root.resizable(True, True)

        self.score = 0
        self.question_index = 0
        self.selected_option = tk.StringVar()

        self.header = tk.Label(root, text="Welcome to the Quiz!", font=("Arial Rounded MT Bold", 20, "bold"),
                               bg="#4a90e2", fg="white", pady=10)
        self.header.pack(fill="x")

        self.content_frame = tk.Frame(root, bg="#f0f4f7")
        self.content_frame.pack(expand=True, fill="both", padx=30, pady=20)

        self.question_label = tk.Label(self.content_frame, text="", wraplength=500, font=("Arial", 16, "bold"),
                                       bg="#f0f4f7", fg="#333")
        self.question_label.pack(pady=(10, 20), anchor="w")

        self.options_frame = tk.Frame(self.content_frame, bg="#f0f4f7")
        self.options_frame.pack(anchor="w", pady=(0, 20))

        self.option_buttons = []
        for _ in range(4):
            btn = tk.Radiobutton(self.options_frame, text="", variable=self.selected_option, value="",
                                 font=("Arial", 13), bg="#eaf1fb", fg="#222", selectcolor="#d0e6fa",
                                 indicatoron=0, width=25, pady=8, bd=0, relief="ridge", cursor="hand2")
            btn.pack(anchor="w", pady=5, padx=10, fill="x")
            self.option_buttons.append(btn)

        self.next_button = tk.Button(self.content_frame, text="Next", command=self.next_question,
                                     font=("Arial Rounded MT Bold", 13), bg="#4a90e2", fg="white",
                                     activebackground="#357abd", activeforeground="white", padx=20, pady=8,
                                     bd=0, relief="ridge", cursor="hand2")
        self.next_button.pack(pady=10, anchor="e")

        self.status_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f4f7", fg="#4a90e2")
        self.status_label.pack(side="bottom", fill="x", pady=5)

        self.load_question()

        self.root.bind("<Configure>", self.on_resize)

    def load_question(self):
        self.selected_option.set(None)
        question_data = quiz_data[self.question_index]
        self.question_label.config(text=f"Q{self.question_index + 1}: {question_data['question']}")

        for i, option in enumerate(question_data["options"]):
            self.option_buttons[i].config(text=option, value=option)
        self.status_label.config(text=f"Question {self.question_index + 1} of {len(quiz_data)} | Score: {self.score}")

    def next_question(self):
        chosen = self.selected_option.get()
        if not chosen:
            messagebox.showwarning("Warning", "Please select an option before proceeding.")
            return

        if chosen == quiz_data[self.question_index]["answer"]:
            self.score += 1

        self.question_index += 1

        if self.question_index < len(quiz_data):
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"Your Score: {self.score}/{len(quiz_data)}")
        self.root.destroy()

    def on_resize(self, event):
        # Responsive font size based on window width
        width = event.width
        font_size = max(12, min(18, width // 40))
        self.question_label.config(font=("Arial", font_size, "bold"))
        for btn in self.option_buttons:
            btn.config(font=("Arial", font_size - 3))

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
