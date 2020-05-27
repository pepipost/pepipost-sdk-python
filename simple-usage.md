### Sample Example

```python
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

mail_send_controller = client.mail_send
body = Send()
body.reply_to = 'you-reply-to-id-address@mydomain.name'
body.mfrom = From()
body.mfrom.email = 'hello@your-register-domain-with-pepipost'
body.mfrom.name = 'Example Pepi'
body.subject = 'Emailing with Pepipost is easy'
body.content = []

body.content.append(Content())
body.content[0].mtype = TypeEnum.HTML
body.content[0].value = '<html><body>Hey,<br><br>Do you know integration is even simpler in Pepipost, <br>with Python <br> Happy Mailing ! <br><br>Pepipost </body></html>'

body.personalizations = []

body.personalizations.append(Personalizations())
body.personalizations[0].to = []

body.personalizations[0].to.append(EmailStruct())
body.personalizations[0].to[0].name = 'random'
body.personalizations[0].to[0].email = 'random@mydomain.name'

body.tags = ['Campaign']

try:
    result = mail_send_controller.create_generatethemailsendrequest(body)
    print(result)
except APIException as e: 
    print(e)

```