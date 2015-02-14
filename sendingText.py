__author__ = 'MR028042'

import twilio
print(twilio.__version__)

from twilio.rest import TwilioRestClient

account_sid = "AC80e88ac5e0be33b8c35b26866e0a0fce"
auth_token = "9d15d342b3e94e41d4e9a2dcd5425c51"
client = TwilioRestClient(account_sid, auth_token)


message = client.sms.messages.create(
    body="Sending SMS from python code... Mrunal!!!",
    to="+13522261091",
    from_="+13524159287")
print message.sid


