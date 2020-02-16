from flask import Flask, url_for, render_template, request, redirect
import classes

app = Flask(__name__)
current_patient = ''

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register', methods = ["POST", "GET"])
def register():
    if request.method == 'POST':
        name = request.form['name']
        bday = request.form['bday']
        number = request.form['number']
        classes.add(name, bday, number)
    return render_template('doc.html')

@app.route('/prescribe', methods = ["POST", "GET"])
def pres():
    global current_patient
    if request.method == 'POST':
        name = request.form['name']
        bday = request.form['bday']
        if classes.patient_exist(name, bday) != False:
            current_patient = classes.patient_exist(name, bday)
            return redirect(url_for('prescribing'))

    return render_template('prescribe.html')

@app.route('/prescribing', methods = ["POST", "GET"])
def prescribing():
    if request.method == 'POST':
        drug = request.form['drug']
        dosage = request.form['dosage']
        comments = request.form['comments']
        strict = request.form['strict']
        
        new_doctor = classes.Doctor("John Smith","John", "Smith", "5555555555")
        classes.prescribe(new_doctor, current_patient, drug, comments)
        if strict:
            current_patient.drug.change_strict()
        return redirect(url_for('success'))
    return render_template('prescribing.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(debug=True)