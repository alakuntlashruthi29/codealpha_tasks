import tkinter as tk

# Main window
root = tk.Tk()
root.title("LearnHub")
root.geometry("500x700")
root.configure(bg="#F5F7FA")

# Header
header = tk.Label(
    root,
    text="LearnHub",
    bg="#4A90E2",
    fg="white",
    font=("Arial", 24, "bold"),
    pady=15
)
header.pack(fill="x")

# Welcome text
welcome = tk.Label(
    root,
    text="Welcome Back!",
    bg="#F5F7FA",
    fg="#333333",
    font=("Arial", 18, "bold")
)
welcome.pack(pady=20)

# Search box
search = tk.Entry(root, width=30, font=("Arial", 12))
search.insert(0, "Search Courses")
search.pack(pady=10)

# Course Card 1
frame1 = tk.Frame(root, bg="white", bd=2, relief="solid")
frame1.pack(padx=20, pady=15, fill="x")

tk.Label(
    frame1,
    text="Python Programming",
    bg="white",
    font=("Arial", 14, "bold")
).pack(pady=10)

tk.Button(
    frame1,
    text="Start Learning",
    bg="#4A90E2",
    fg="white",
    width=15
).pack(pady=10)

# Course Card 2
frame2 = tk.Frame(root, bg="white", bd=2, relief="solid")
frame2.pack(padx=20, pady=15, fill="x")

tk.Label(
    frame2,
    text="Web Development",
    bg="white",
    font=("Arial", 14, "bold")
).pack(pady=10)

tk.Button(
    frame2,
    text="Start Learning",
    bg="#50C878",
    fg="white",
    width=15
).pack(pady=10)

# Profile button
profile_btn = tk.Button(
    root,
    text="Profile",
    bg="#FF914D",
    fg="white",
    font=("Arial", 12, "bold"),
    width=15
)
profile_btn.pack(pady=40)

root.mainloop()