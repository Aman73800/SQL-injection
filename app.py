from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)

        user = cursor.fetchone()
        conn.close()

        if user:
            message = "✅ Login successful"
        else:
            message = "❌ Invalid credentials"

    return render_template('login.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
