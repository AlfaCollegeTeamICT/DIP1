from flask import Flask, render_template, request, redirect, url_for
import sqlite3

def create_database():
    conn = sqlite3.connect("./database.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT)''')
    conn.commit()
    conn.close()

app = Flask(__name__)

naam = "Wouter"

@app.route('/')
def hello_world():
    return render_template('helloworld.html',naam = naam)

@app.route('/test')
def testPagina():
    return render_template('test.html')

@app.route('/demo')
def demo():
    return render_template('demo.html')

@app.route('/database')
def db():
    conn = sqlite3.connect("./database.db")
    c = conn.cursor()
    c.execute('SELECT * FROM tasks')
    tasks = c.fetchall()
    conn.close()
    return render_template('database.html', tasks = tasks)

@app.route('/add', methods=['POST'])
def add_data():
    task = request.form['task']
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
    conn.commit()
    conn.close()
    return redirect(url_for('db'))

create_database()
app.run(debug=True)