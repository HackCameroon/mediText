from flask import Flask, url_for, render_template, request, redirect
import classes
import pillSMS as ps

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
        else:
            return redirect(url_for('incorrect_input'))
    return render_template('prescribe.html')

@app.route('/prescribing', methods = ["POST", "GET"])
def prescribing():
    if request.method == 'POST':
        drug = request.form['drug']
        dosage = request.form['dosage']
        comments = request.form['comments']
        strict = request.form['strict']
        
        new_doctor = classes.Doctor("John Smith","John", "Smith", "5555555555")
        t = classes.prescribe(new_doctor, current_patient, drug, comments)
            
        if (t and strict):
            current_patient.drug.change_strict()
            ps.send_message(current_patient)
            return redirect(url_for('success'))
        elif(t == False):
            return redirect(url_for('incorrect_input'))

    return render_template('prescribing.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/incorrect_input')
def incorrect_input():
    return render_template('incorrect_input.html')

@app.route('/login', methods = ["POST", "GET"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['pass']
        if classes.doctor_login(username, password) != False:
            return redirect(url_for('doctor_home'))
        else:
            return redirect(url_for('incorrect_input'))
    return render_template('doctor_login.html')

@app.route('/doctor_home')
def doctor_home():
    return render_template('doctor_home.html')

if __name__ == "__main__":
    app.run(debug=True)