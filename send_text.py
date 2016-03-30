from twilio.rest import TwilioRestClient

account_sid = "AC890d0dbd96dd6bb1f21818fbb00460e3"
auth_token  = "edb6386da4fbe28365e0b4cb3273241c"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Jenny, Jenny who can I turn to? Please?! I love you <3",
    to="+15037841300",  
    from_="+17073371418")
print message.sid
