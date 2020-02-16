import classes
from flask import Flask, request, redirect
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

current_patient = ""

def send_message(patient):
    global current_patient
    current_patient = patient
    client = Client("ACc0304e02373de6ce19ae6d5c3e9e2fa2", "dfef0a24cdb05d648c80cf67bf44cbd5")
    client.messages.create(to=patient.phone, from_="+13344588868", body=("Hi {}. This is a message to confirm that you are enrolled by {} to recieve reminders to take {}.").format((patient.firstname +" "+ patient.lastname).upper(),classes.prescribed[patient.firstname + " " + patient.lastname], patient.drug.name.upper()))

def send(patient):
    client = Client("ACc0304e02373de6ce19ae6d5c3e9e2fa2", "dfef0a24cdb05d648c80cf67bf44cbd5")
    client.messages.create(to=patient.phone, from_="+13344588868", body=("Hi {}. This is a message to remind you to take {}. Please reply if you 'YES' if you have taken the drug. Included doctor message: {}").format((patient.firstname + " " +patient.lastname).upper(), patient.drug.name.upper(), patient.drug.message))

def second(patient):
    client = Client("ACc0304e02373de6ce19ae6d5c3e9e2fa2", "dfef0a24cdb05d648c80cf67bf44cbd5")
    client.messages.create(to=patient.phone, from_="+13344588868", body=("Hi {}. This is a second message to remind you to take {}. Please reply if you 'YES' if you have taken the drug or 'MISS' 10 minutes have passed since your first text reminder.").format(patient.firstname +" "+ patient.lastname, patient.drug.name.upper()))

# app = Flask(__name__)

# @app.route("/sms", methods=['GET', 'POST'])
# def incoming_sms():
#     patient = current_patient
#     """Send a dynamic reply to an incoming text message"""
#     # Get the message the user sent our Twilio number
#     body = request.values.get('Body', None)

#     # Start our TwiML response
#     resp = MessagingResponse()

#     # Determine the right reply for this message
#     if body.lower() == 'yes':
#         resp.message("Thank you for telling us! We will notify you when your next dose is.")
#     elif body.lower == 'miss':
#         if (patient.drug.strict_dosage):
#             resp.message("{} has a strict dosage so please try not to miss your next dosage.".format(patient.drug.name.upper()))
#         else:
#             resp.message("Because {} does not have a strict dosage please take the missed dosage and try not to miss your next scheduled dosage.".format(patient.drug.name.upper()))
#     else:
#         resp.message("Invalid response")
#     return str(resp)

if __name__ == "__main__":
    pass