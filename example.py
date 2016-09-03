from PepipostAPIV10Lib.Controllers.Email import *
import json

Email = Email()

#data = ()
data = {
    'api_key' : 'yoursecretapikey',
    'recipients' : ['recipient1@example.com','recipient2@example.com'],
    'email_details' : {
        'fromname' : 'sender name',
        'subject' : 'test email subject sent using Pepipost SDK - Python',
        'from' : 'from@example.com',
        'content' : '<p>This is a test email sent using Pepipost JSON/Email Python SDK</p>'
    }
}

response = Email.send(data)

print response
