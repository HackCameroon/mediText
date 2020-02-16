from flask import Flask, url_for, render_template, request, redirect
import classes
import pillSMS as ps
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from multiprocessing import Process



new_doctor = classes.Doctor("John Smith","John", "Smith", "5555555555")
app = Flask(__name__)
current_patient = ""
current_doctor = "SELF"

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
        try:
            strict = request.form['strict']
        except:
            strict = False
        
        t = classes.prescribe(current_doctor, current_patient, drug, comments)
            
        if (t and strict):
            current_patient.drug.change_strict()
            ps.send_message(current_patient)
            return redirect(url_for('success'))
        elif(t == False):
            return redirect(url_for('incorrect_input'))
        else:
            ps.send_message(current_patient)
            return redirect(url_for('success'))

    return render_template('prescribing.html')

@app.route('/success')
def success():
    global current_doctor
    current_doctor = "SELF"
    return render_template('success.html')

@app.route('/incorrect_input')
def incorrect_input():
    global current_doctor
    current_doctor = "SELF"
    return render_template('incorrect_input.html')

@app.route('/login', methods = ["POST", "GET"])
def login():
    global current_doctor
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['pass']
        if classes.doctor_login(username, password) != False:
            current_doctor = classes.doctor_login(username, password)
            return redirect(url_for('doctor_home'))
        else:
            return redirect(url_for('incorrect_input'))
    return render_template('doctor_login.html')

@app.route('/doctor_home')
def doctor_home():
    return render_template('doctor_home.html')

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    patient = current_patient
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body.lower() == 'yes':
        resp.message("Thank you for telling us! We will notify you when your next dose is.")
    elif body.lower() == 'miss':
        if (type(patient) == classes.Patient and patient.drug.strict_dosage):
            resp.message("{} has a strict dosage so please try not to miss your next dosage.".format(patient.drug.name.upper()))
        elif(type(patient) == classes.Patient):
            resp.message("Because {} does not have a strict dosage please take the missed dosage and try not to miss your next scheduled dosage.".format(patient.drug.name.upper()))
        else:
            resp.message("You are not subscribed to any drugs")
    else:
        resp.message("Invalid response")
    return str(resp)
   

if __name__ == "__main__":
    app.run(debug=True)