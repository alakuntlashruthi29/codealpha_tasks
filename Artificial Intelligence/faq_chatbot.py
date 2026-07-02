import tkinter as tk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# FAQ Data
faq_questions = [
    "What are your working hours?",
    "How can I contact support?",
    "Where are you located?",
    "What services do you provide?",
    "How can I reset my password?"
]

faq_answers = [
    "We are open from 9 AM to 6 PM.",
    "You can contact us at support@example.com.",
    "We are located in Hyderabad.",
    "We provide software and data analytics services.",
    "Click on 'Forgot Password' to reset your password."
]

# Function to get answer
def get_response():
    user_input = entry.get()

    corpus = faq_questions + [user_input]

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(corpus)

    similarity = cosine_similarity(vectors[-1], vectors[:-1])
    index = similarity.argmax()

    response_box.delete("1.0", tk.END)
    response_box.insert(tk.END, faq_answers[index])

# GUI
root = tk.Tk()
root.title("FAQ Chatbot")
root.geometry("600x400")

tk.Label(root,
         text="Ask a Question",
         font=("Arial", 14, "bold")).pack(pady=10)

entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack(pady=10)

tk.Button(root,
          text="Send",
          bg="blue",
          fg="white",
          command=get_response).pack(pady=10)

tk.Label(root,
         text="Bot Response",
         font=("Arial", 14, "bold")).pack(pady=10)

response_box = tk.Text(root, height=5, width=50)
response_box.pack()

root.mainloop()