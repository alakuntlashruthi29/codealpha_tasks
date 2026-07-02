import tkinter as tk
import random

quotes = [
    ("Success is not final, failure is not fatal.", "Winston Churchill"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("Stay hungry, stay foolish.", "Steve Jobs"),
    ("Dream big and dare to fail.", "Norman Vaughan"),
    ("The best way to predict the future is to create it.", "Peter Drucker")
]


def new_quote():
    quote, author = random.choice(quotes)
    quote_label.config(text=f'"{quote}"')
    author_label.config(text=f"- {author}")


root = tk.Tk()
root.title("Random Quote Generator")
root.geometry("500x300")

quote_label = tk.Label(
    root,
    text="",
    wraplength=400,
    font=("Arial", 14),
    justify="center"
)
quote_label.pack(pady=40)

author_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    fg="blue"
)
author_label.pack()

tk.Button(root, text="New Quote", command=new_quote).pack(pady=20)

new_quote()

root.mainloop()