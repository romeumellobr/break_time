from twilio import TwilioRestException
from twilio.rest import TwilioRestClient

account_sid = "" # Your Account SID from www.twilio.com/console
auth_token  = ""  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

try:
    message = client.messages.create(
        body="Hello from Python!",
        to="+99367009981701",    # Replace with your phone number
        from_="+99367009981701") # Replace with your Twilio number
except TwilioRestException as e:
    print(e)
