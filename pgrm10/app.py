
# pyrefly: ignore [missing-import]
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/style.css')
def style():
    return app.send_static_file('style.css')

@app.route('/submit', methods = ['POST'])
def submit():
    name = request.form['name']
    course = request.form['course']

    return render_template('result.html', name = name, course = course)

if __name__== '__main__':
    app.run(debug = True)
