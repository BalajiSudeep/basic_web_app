# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

# Home route that displays a simple form
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = f"Hello, {name}! Thank you for submitting the form."
    return render_template('result.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)

