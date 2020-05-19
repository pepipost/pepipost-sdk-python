#### Example of Advance Usage

```python
# -*- coding: utf-8 -*-
from pepipost.pepipost_client import PepipostClient
from pepipost.configuration import Configuration
from pepipost.models.send import Send
from pepipost.models.mfrom import From
from pepipost.models.content import Content
from pepipost.models.type_enum import TypeEnum
from pepipost.models.attachments import Attachments
from pepipost.models.personalizations import Personalizations
from pepipost.models.email_struct import EmailStruct
from pepipost.models.settings import Settings
from pepipost.exceptions.api_exception import APIException
import jsonpickle

api_key = 'your api_key here'

client = PepipostClient(api_key)


send_controller = client.send
body = Send()
body.reply_to = 'you-reply-to-id-address@mydomain.name'
body.mfrom = From()
body.mfrom.email = 'hello@your-register-domain-with-pepipost'
body.mfrom.name = 'Example Pepi'
body.subject = 'Emailing with Pepipost is easy with [%NAME%]'
body.template_id = 0
body.content = []

body.content.append(Content())
body.content[0].mtype = TypeEnum.HTML
body.content[0].value = '<html><body>Hey,<br><br>Do you know integration is even simpler in Pepipost, <br>with Python <br> Happy Mailing ! <br><br>Pepipost [%NAME%]</body></html>'

body.content.append(Content())
body.content[1].mtype = TypeEnum.AMP
body.content[1].value = '<html><body>Hey,<br><br>Do you know integration is even simpler in Pepipost, <br>with Python <br> Happy Mailing ! <br><br>Pepipost </body></html>'

body.attachments = []

body.attachments.append(Attachments())
body.attachments[0].content = 'SGVsbG8gd2VsY29tZSB0byBQRVBJIHY1IEFQSQ=='
body.attachments[0].name = 'global-text-file.txt'

body.personalizations = []

body.personalizations.append(Personalizations())
body.personalizations[0].attributes = jsonpickle.decode('{"NAME":"TEAM"}')
body.personalizations[0].headers = jsonpickle.decode('{"key":"value"}')
body.personalizations[0].attachments = []

body.personalizations[0].attachments.append(Attachments())
body.personalizations[0].attachments[0].content = 'SGVsbG8gd2VsY29tZSB0byBQRVBJIHY1IEFQSQ=='
body.personalizations[0].attachments[0].name = 'personalized-test-file.txt'

body.personalizations[0].to = []

body.personalizations[0].to.append(EmailStruct())
body.personalizations[0].to[0].name = 'random-1'
body.personalizations[0].to[0].email = 'random-1@mydomain.name'

body.personalizations[0].to.append(EmailStruct())
body.personalizations[0].to[1].name = 'random-2'
body.personalizations[0].to[1].email = 'random-2@mydomain.name'

body.personalizations[0].cc = []

body.personalizations[0].cc.append(EmailStruct())
body.personalizations[0].cc[0].name = 'random-cc'
body.personalizations[0].cc[0].email = 'random-cc@mydomain.name'

body.personalizations[0].bcc = []

body.personalizations[0].bcc.append(EmailStruct())
body.personalizations[0].bcc[0].name = 'random-bcc'
body.personalizations[0].bcc[0].email = 'random-bcc@mydomain.name'

body.personalizations[0].token_to = '"{\"Arg1\":\"Value1\"}"'
body.personalizations[0].token_cc = '"{\"Arg1\":\"Value1\"}"'
body.personalizations[0].token_bcc = '"{\"Arg1\":\"Value1\"}"'

body.personalizations.append(Personalizations())
body.personalizations[1].attributes = jsonpickle.decode('{"NAME":"TEAM"}')
body.personalizations[1].headers = jsonpickle.decode('{"key":"value"}')
body.personalizations[1].attachments = []

body.personalizations[1].attachments.append(Attachments())
body.personalizations[1].attachments[0].content = 'SGVsbG8gd2VsY29tZSB0byBQRVBJIHY1IEFQSQ=='
body.personalizations[1].attachments[0].name = 'personalized-test-file.txt'

body.personalizations[1].to = []

body.personalizations[1].to.append(EmailStruct())
body.personalizations[1].to[0].name = 'random-1'
body.personalizations[1].to[0].email = 'random-1@mydomain.name'

body.personalizations[1].cc = []

body.personalizations[1].cc.append(EmailStruct())
body.personalizations[1].cc[0].name = 'random-cc'
body.personalizations[1].cc[0].email = 'random-cc@mydomain.name'

body.personalizations[1].bcc = []

body.personalizations[1].bcc.append(EmailStruct())
body.personalizations[1].bcc[0].name = 'random-bcc'
body.personalizations[1].bcc[0].email = 'random-bcc@mydomain.name'

body.personalizations[1].token_to = '"{\"Arg1\":\"Value1\"}"'
body.personalizations[1].token_cc = '"{\"Arg1\":\"Value1\"}"'
body.personalizations[1].token_bcc = '"{\"Arg1\":\"Value1\"}"'

body.settings = Settings()
body.settings.footer = True
body.settings.click_track = True
body.settings.open_track = True
body.settings.unsubscribe_track = True
body.settings.hepf = True
body.tags = ['Campaign']
body.schedule = 0
body.bcc = []

body.bcc.append(EmailStruct())
body.bcc[0].name = 'random-bcc'
body.bcc[0].email = 'random-bcc@mydomain.name'

try:
    result = send_controller.create_generate_the_mail_send_request(body)
    print(result)
except APIException as e: 
    print(e)
```