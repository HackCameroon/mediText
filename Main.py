from flask import Flask, url_for, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/register', methods = ["POST", "GET"])
def register():
    if request.method == 'POST':
        name = request.form['name']
        bday = request.form['bday']
        number = request.form['number']
        print(name, bday, number)
    return render_template('doc.html')

@app.route('/prescribe', methods = ["POST", "GET"])
def prescribe():
    if request.method == 'POST':
        name = request.form['name']
        bday = request.form['bday']
        print(name, bday)
    return render_template('prescribe.html')


if __name__ == "__main__":
    app.run(debug=True)