from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

client = Client("ACc0304e02373de6ce19ae6d5c3e9e2fa2", "dfef0a24cdb05d648c80cf67bf44cbd5")
client.messages.create(to="6269223460", from_="+13344588868", body="shut up")

resp = MessagingResponse()
resp.message("thanKs for replying!")