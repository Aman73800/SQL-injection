# SQL Injection Demo with Flask and SQLite

This project demonstrates how SQL Injection vulnerabilities work in a simple login system built with Flask and SQLite, and how to secure it using parameterized queries.

---

## 📁 Project Structure

```
├── app.py           # Vulnerable login system (SQL injection demo)
├── init_db.py       # Creates SQLite database and inserts test user
├── templates/
│   └── login.html   # Frontend login form with SQLi tip
├── users.db         # SQLite database file
```

---

## ✅ Requirements

* Python 3.x
* Flask

Install Flask:

```bash
pip install flask
```

---

## 🛠️ Step-by-Step Guide

### Step 1: Clone or Download This Project

```bash
git clone https://github.com/your-username/sql-injection-flask-demo.git
cd sql-injection-flask-demo
```

### Step 2: Initialize the Database

This creates a `users` table and inserts a test user (`admin` / `admin123`).

```bash
python init_db.py
```

You should see:

```
✅ Database initialized.
```

### Step 3: Run the Vulnerable App

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

### Step 4: Try a Normal Login

Use these credentials:

* **Username:** `admin`
* **Password:** `admin123`

You should see ✅ `Login successful`.

---

### 🚨 Step 5: Exploit SQL Injection (For Demo Only)

Try logging in with:

* **Username:** `admin' --`
* **Password:** *(anything)*

You'll bypass the password check! This simulates a real-world SQL Injection attack.

---

## 🔐 How to Secure It

To prevent this, you must use **parameterized queries** instead of string interpolation:

```python
# Insecure (used in app.py):
cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")

# Secure (recommended):
cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
```

You can replace `app.py` with a secure version once you're done experimenting.

---

## 📸 Screenshots (for reference)

* Login form UI
* SQL injection tip on UI
* SQLi working with `admin' --`
* DB setup (`init_db.py`)
* Terminal output
* App running demo

---

## 🙋‍♂️ Author

**Aman Yadav**
Feel free to connect with me on [LinkedIn](https://linkedin.com/in/your-profile)!

---

## 📄 License

This project is for educational purposes only. Do not use this technique on any live system.

---
