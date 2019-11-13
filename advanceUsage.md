#### Example of Advance Usage

```python
# -*- coding: utf-8 -*-
from pepipost.pepipost_client import PepipostClient
from pepipost.models.email_body import EmailBody
from pepipost.models.personalizations import Personalizations
from pepipost.models.attachments import Attachments
from pepipost.models.mfrom import From
from pepipost.models.email_body_attachments import EmailBodyAttachments
from pepipost.models.settings import Settings
from pepipost.exceptions.api_exception import APIException
from pepipost.models.attributes import Attributes
from pepipost.models.xheaders import Xheaders
import jsonpickle

client = PepipostClient()
email_controller = client.email
body = EmailBody()
body.personalizations = []

api_key = 'pass api-key here' 
body.personalizations.append(Personalizations())

body.personalizations[0].recipient = 'my-email-id@domain.com'
body.personalizations[0].x_apiheader_cc = 'x api header cc content'
body.personalizations[0].x_apiheader = 'xapi header for emails'
body.personalizations[0].attributes = Attributes('{"name":"pepi","love":"Emails"}').get_attributes()
body.personalizations[0].attachments = []
body.personalizations[0].attachments.append(Attachments()) 
body.personalizations[0].attachments[0].file_content = '"SGVsbG8sIHRoaXMgZmlsZSBpcyBhbiBpbmZvcm1hdGlvbmFsIGZpbGU6OiBTZW5kaW5nIGVtYWlscyB0byB0aGUgaW5ib3ggaXMgd2hhdCB3ZSBkbywgYnV0IHRoYXTigJlzIG5vdCB0aGUgb25seSByZWFzb24gd2h5IGRldmVsb3BlcnMgYW5kIGVudGVycHJpc2VzIGxvdmUgdXMuIFdlIGFyZSB0aGUgb25seSBFU1AgdGhhdCBkb2VzbuKAmXQgY2hhcmdlIGZvciBlbWFpbHMgb3BlbmVkLg=="'
body.personalizations[0].attachments[0].file_name = 'pepipost.txt'
body.personalizations[0].recipient_cc = ['my-cc-emailid@gmail.com']
body.personalizations[0].recipient_bcc = ['my-email-bcc-id@domain.com']
body.personalizations[0].x_headers = Xheaders('{"custom_key1":"custom_value1","custom_key2":"custom_value2"}').get_xheaders()

body.tags = 'tagsPython'
body.mfrom = From()

body.mfrom.from_email = 'pepi@net.xyz'
body.mfrom.from_name = 'i am pepi'
body.subject = 'Pepipost mail through php sdk'
body.content = '<html><body>Hello, Welcome to Pepipost Family.<br>My name is [% name %].<br>my love is sending [% love %]</body> <br></html>'
body.ampcontent = '<!doctype html><html ⚡4email><head><meta charset="utf-8"><script async src="https://cdn.ampproject.org/v0.js"></script><style amp4email-boilerplate>body{visibility:hidden}</style></head><body>  Hello, AMP4EMAIL world.</body></html>'

body.attachments = []
body.attachments.append(EmailBodyAttachments())
body.attachments[0].file_content = '"SGVsbG8sIHRoaXMgZmlsZSBpcyBhbiBpbmZvcm1hdGlvbmFsIGZpbGU6OiBTZW5kaW5nIGVtYWlscyB0byB0aGUgaW5ib3ggaXMgd2hhdCB3ZSBkbywgYnV0IHRoYXTigJlzIG5vdCB0aGUgb25seSByZWFzb24gd2h5IGRldmVsb3BlcnMgYW5kIGVudGVycHJpc2VzIGxvdmUgdXMuIFdlIGFyZSB0aGUgb25seSBFU1AgdGhhdCBkb2VzbuKAmXQgY2hhcmdlIGZvciBlbWFpbHMgb3BlbmVkLg=="'
body.attachments[0].file_name = 'pepipost_1.txt'

body.settings = Settings()

body.settings.footer = 1
body.settings.clicktrack = 1
body.settings.opentrack = 1
body.settings.unsubscribe = 1
body.settings.bcc = 'my-email-bcc-id@domain.com'
body.reply_to_id = 'replyto@gmail.com'
body.template_id = 11344

URL = "https://<api-endpoint>";

try:
    result = email_controller.create_send_email(api_key, body, URL)
    if not (result.error_info is None):
        print("Reason :: " + str(result.error_info.error_message) + "\n" + "Message :: " + str(result.message))
    else:
        print("Message :: " + result.message)
except APIException as e:
    print(e)

```