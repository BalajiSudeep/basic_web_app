from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('output.html')  # Show the form

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']  # Extract form data
    return render_template('result.html', name=name)  # Show result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
