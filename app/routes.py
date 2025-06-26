from flask import render_template
from app import app
from app.db import get_db_connection

@app.route('/')
def home():
    conn = get_db_connection()
    db_version = "Could not connect to database."
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT version();")
                db_version = cur.fetchone()[0]
            conn.close()
        except Exception as e:
            db_version = f"Error: {e}"
    return render_template('home.html', db_version=db_version)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
