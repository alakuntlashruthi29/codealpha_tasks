import tkinter as tk
from tkinter import messagebox

# Initial flashcards
flashcards = [
    {"question": "What is Python?", "answer": "A programming language"},
    {"question": "Capital of India?", "answer": "New Delhi"},
    {"question": "2 + 2 ?", "answer": "4"}
]

current_index = 0
showing_answer = False


def display_card():
    global showing_answer
    showing_answer = False
    question_label.config(text=flashcards[current_index]["question"])
    answer_label.config(text="")


def show_answer():
    answer_label.config(text=flashcards[current_index]["answer"])


def next_card():
    global current_index
    if current_index < len(flashcards) - 1:
        current_index += 1
        display_card()


def previous_card():
    global current_index
    if current_index > 0:
        current_index -= 1
        display_card()


def add_card():
    q = question_entry.get()
    a = answer_entry.get()

    if q and a:
        flashcards.append({"question": q, "answer": a})
        question_entry.delete(0, tk.END)
        answer_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Flashcard Added!")
    else:
        messagebox.showwarning("Warning", "Enter both question and answer")


def edit_card():
    q = question_entry.get()
    a = answer_entry.get()

    if q and a:
        flashcards[current_index]["question"] = q
        flashcards[current_index]["answer"] = a
        display_card()
        messagebox.showinfo("Success", "Flashcard Updated!")


def delete_card():
    global current_index

    if len(flashcards) > 1:
        flashcards.pop(current_index)
        current_index = 0
        display_card()
        messagebox.showinfo("Deleted", "Flashcard Deleted!")
    else:
        messagebox.showwarning("Warning", "Cannot delete last card")


root = tk.Tk()
root.title("Flashcard Quiz App")
root.geometry("500x400")

question_label = tk.Label(root, text="", font=("Arial", 16))
question_label.pack(pady=20)

answer_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
answer_label.pack()

tk.Button(root, text="Show Answer", command=show_answer).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Previous", command=previous_card).grid(row=0, column=0, padx=10)
tk.Button(frame, text="Next", command=next_card).grid(row=0, column=1, padx=10)

tk.Label(root, text="Question").pack()
question_entry = tk.Entry(root, width=40)
question_entry.pack()

tk.Label(root, text="Answer").pack()
answer_entry = tk.Entry(root, width=40)
answer_entry.pack()

tk.Button(root, text="Add Card", command=add_card).pack(pady=5)
tk.Button(root, text="Edit Card", command=edit_card).pack(pady=5)
tk.Button(root, text="Delete Card", command=delete_card).pack(pady=5)

display_card()

root.mainloop()