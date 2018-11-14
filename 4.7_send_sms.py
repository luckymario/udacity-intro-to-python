from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC772441ad6c8bf0995af4fa26cf91028c"
# Your Auth Token from twilio.com/console
auth_token  = "724266ffbb4f6e79eb27bd71a309ca0b"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="My name is Mario?",
    to="+48660952307",    # Replace with your phone number
    from_="+48668280321") # Replace with your Twilio number
    
print(message.sid)
