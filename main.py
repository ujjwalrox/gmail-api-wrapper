from email_sender import send_message

# Add your processing code here




# We are using a dict to store mail info
mail = {}

mail['sender'] = 'youremail'
mail['reciever'] = 'recipient'
mail['subject'] = 'demo-subject'
mail['body'] = 'demo-body'

# call send_mail function and pass the dict
send_mail(mail)