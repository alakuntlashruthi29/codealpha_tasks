from flask import Flask, request
import sqlite3

app = Flask(__name__)

# Create database and table
conn = sqlite3.connect('restaurant.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    item TEXT
)
''')

conn.commit()
conn.close()

# Home Page
@app.route('/')
def home():
    return '''
    <h1>Restaurant Management System</h1>

    <h3>Menu</h3>
    <ul>
        <li>Pizza</li>
        <li>Burger</li>
        <li>Pasta</li>
        <li>Sandwich</li>
    </ul>

    <h3>Place Order</h3>

    <form method="POST" action="/order">

        Name:<br>
        <input type="text" name="customer_name"><br><br>

        Select Item:<br>
        <select name="item">
            <option>Pizza</option>
            <option>Burger</option>
            <option>Pasta</option>
            <option>Sandwich</option>
        </select><br><br>

        <input type="submit" value="Place Order">

    </form>
    '''

# Order Route
@app.route('/order', methods=['POST'])
def order():

    customer_name = request.form['customer_name']
    item = request.form['item']

    conn = sqlite3.connect('restaurant.db')
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO orders (customer_name, item) VALUES (?, ?)",
        (customer_name, item)
    )

    conn.commit()
    conn.close()

    return f'''
    <h2>Order Placed Successfully!</h2>

    Customer Name: {customer_name}<br>
    Item Ordered: {item}<br><br>

    <a href="/">Back to Home</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)