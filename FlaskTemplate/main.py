from flask import Flask, render_template

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

app.run(debug=True)