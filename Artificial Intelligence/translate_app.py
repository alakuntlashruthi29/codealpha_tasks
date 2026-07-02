import tkinter as tk
from tkinter import ttk
from googletrans import Translator

translator = Translator()

# Function to translate text
def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    src_lang = source_lang.get()
    dest_lang = target_lang.get()

    if text:
        translated = translator.translate(text, src=src_lang, dest=dest_lang)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated.text)

# Main window
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("600x500")

# Input Label
tk.Label(root, text="Enter Text", font=("Arial", 12, "bold")).pack()

# Input Text Box
input_text = tk.Text(root, height=5, width=50)
input_text.pack(pady=10)

# Language Selection
frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Source Language").grid(row=0, column=0)
source_lang = ttk.Combobox(frame, values=["en", "hi", "te", "fr", "es"])
source_lang.set("en")
source_lang.grid(row=1, column=0, padx=10)

tk.Label(frame, text="Target Language").grid(row=0, column=1)
target_lang = ttk.Combobox(frame, values=["en", "hi", "te", "fr", "es"])
target_lang.set("te")
target_lang.grid(row=1, column=1, padx=10)

# Translate Button
tk.Button(root,
          text="Translate",
          bg="blue",
          fg="white",
          command=translate_text).pack(pady=20)

# Output Label
tk.Label(root, text="Translated Text", font=("Arial", 12, "bold")).pack()

# Output Text Box
output_text = tk.Text(root, height=5, width=50)
output_text.pack(pady=10)

root.mainloop()