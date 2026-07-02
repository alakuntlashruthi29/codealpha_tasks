import tkinter as tk

root = tk.Tk()
root.title("Online Learning Platform - Wireframe")
root.geometry("400x600")

# Header
header = tk.Label(root, text="Online Learning Platform",
                  font=("Arial", 16, "bold"))
header.pack(pady=10)

# Search Bar
search_box = tk.Entry(root, width=30)
search_box.insert(0, "Search Courses")
search_box.pack(pady=10)

# Course Buttons
course1 = tk.Button(root, text="Python Programming", width=25)
course1.pack(pady=10)

course2 = tk.Button(root, text="Web Development", width=25)
course2.pack(pady=10)

course3 = tk.Button(root, text="Data Science", width=25)
course3.pack(pady=10)

# Profile Button
profile = tk.Button(root, text="Profile", width=20)
profile.pack(side="bottom", pady=20)

root.mainloop()