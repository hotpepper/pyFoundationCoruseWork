from twilio import rest
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC60bd7b39268433022559ebe2a30edb6e"
auth_token  = "53e210bd6d8361e0d3c629767362587f"
client = rest.TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(
    body="Seth's first code generated TXT",
    to="+19172021095",    # Replace with your phone number
    from_="+12014845286") # Replace with your Twilio number
print message.sid


#(201) 484-5286
