from flask import Flask, request
import sqlite3

app = Flask(__name__)

# Create database and table
conn = sqlite3.connect('events.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS registrations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    event TEXT
)
''')

conn.commit()
conn.close()

# Home Page
@app.route('/')
def home():
    return '''
    <h1>Event Registration System</h1>

    <h3>Available Events</h3>
    <ul>
        <li>Python Workshop</li>
        <li>Data Science Seminar</li>
        <li>Web Development Bootcamp</li>
    </ul>

    <h3>Register</h3>

    <form method="POST" action="/register">
        Name:<br>
        <input type="text" name="name"><br><br>

        Email:<br>
        <input type="email" name="email"><br><br>

        Event:<br>
        <select name="event">
            <option>Python Workshop</option>
            <option>Data Science Seminar</option>
            <option>Web Development Bootcamp</option>
        </select><br><br>

        <input type="submit" value="Register">
    </form>
    '''

# Registration Route
@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    event = request.form['event']

    conn = sqlite3.connect('events.db')
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO registrations (name, email, event) VALUES (?, ?, ?)",
        (name, email, event)
    )

    conn.commit()
    conn.close()

    return f'''
    <h2>Registration Successful!</h2>

    Name: {name}<br>
    Email: {email}<br>
    Event: {event}<br><br>

    <a href="/">Back to Home</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)