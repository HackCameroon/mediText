from flask import Flask, url_for, render_template, request
import classes

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
        classes.add(name, bday, number)
    return render_template('doc.html')

@app.route('/prescribe', methods = ["POST", "GET"])
def prescribe():
    global current_patient
    if request.method == 'POST':
        name = request.form['name']
        bday = request.form['bday']
        if classes.patient_exist(name, bday) != False:
            current_patient = classes.patient_exist(name, bday)

    return render_template('prescribe.html')


if __name__ == "__main__":
    app.run(debug=True)