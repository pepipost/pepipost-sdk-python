![pepipostlogo](https://pepipost.com/wp-content/uploads/2017/07/P_LOGO.png)

[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.txt)
[![Open Source Helpers](https://www.codetriage.com/pepipost/pepipost-sdk-python/badges/users.svg)](https://www.codetriage.com/pepipost/pepipost-sdk-python)
[![Twitter Follow](https://img.shields.io/twitter/follow/pepi_post.svg?style=social&label=Follow)](https://twitter.com/pepi_post)

# Python SDK Client library :snake: for [Pepipost](https://pepipost.com)

This SDK contain methods for easily interacting with the Pepipost Email Sending API to send emails within few seconds.

We are trying to make our libraries a Community Driven. To help us building right things in proper order we would request you to help us by sharing comments, creating new [issues](https://github.com/pepipost/pepipost-sdk-python/issues) or [pull requests](https://github.com/pepipost/pepipost-sdk-python/pulls). We welcome any sort of contribution to this library.

The latest 5.0 version of this library provides is fully compatible with the latest Pepipost v5 API.
For any update of this library check [Releases](https://github.com/pepipost/pepipost-sdk-python/releases)

## Table of Content
* [Installation](#installation)
* [Sample Example](#sample)
* [Announcements](#announcements)
* [Roadmap](#roadmap)
* [About](#about)
* [License](#license)

<a name="installation"></a>
Installation 
============

Prerequisites
-------------
   * Python (2 >=2.7.9 or 3 >= 3.4)
   * Python IDE (we are using [Pycharm](https://www.jetbrains.com/pycharm/download/) )
   * Python packages  
      * nose
      * jsonpickle
      * requests
      * cachecontrol
      * python-dateutil
     
   * Installation of PIP can be done from [here](https://pip.pypa.io/en/stable/installing/). 
   * We recommend using PIP Dependency manager in order to install all the dependencies which we had mentioned in ```requirements.txt``` files that comes in SDK.

Install Package
---------------
   
#### Install directly from GitHub
You can install the library directly from GitHub also using the below command:
   
    git clone https://github.com/pepipost/pepipost-sdk-python.git pepipost_python

Note: If you are installing directly from GitHub, then you need to install the dependecies separately which are mentioned in our requirements.txt file.

#### For IDE based installation
Refer [this](https://github.com/pepipost/pepipost-sdk-python/blob/master/pyCharm.md) link to install and use this SDK in a IDE environment.   

<a name="sample"></a>
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

<a name="announcements"></a>
# Announcements

v5.0 has been released! Please see the [release notes](https://github.com/pepipost/pepipost-sdk-python/releases/) for details.

All updates to this library are documented in our [releases](https://github.com/pepipost/pepipost-sdk-python/releases). For any queries, feel free to reach out us at dx@pepipost.com

<a name="roadmap"></a>
## Roadmap

If you are interested in the future direction of this project, please take a look at our open [issues](https://github.com/pepipost/pepipost-sdk-python/issues) and [pull requests](https://github.com/pepipost/pepipost-sdk-python/pulls). We would love to hear your feedback.

<a name="about"></a>
## About
pepipost-sdk-python library is guided and supported by the [Pepipost Developer Experience Team](https://github.com/orgs/pepipost/teams/pepis/members) .
This pepipost-sdk-python library is maintained and funded by Pepipost Ltd. The names and logos for pepipost-php-sdk are trademarks of Pepipost Ltd.

<a name="license"></a>
## License
This code library was semi-automatically generated by APIMATIC v2.0 and licensed under The MIT License (MIT). 
