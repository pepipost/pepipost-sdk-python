![pepipostlogo](https://pepipost.com/wp-content/uploads/2017/07/P_LOGO.png)

[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.txt)
[![Open Source Helpers](https://www.codetriage.com/pepipost/pepipost-sdk-python/badges/users.svg)](https://www.codetriage.com/pepipost/pepipost-sdk-python)
[![Twitter Follow](https://img.shields.io/twitter/follow/pepi_post.svg?style=social&label=Follow)](https://twitter.com/pepi_post)

# Official Python library :snake: for [Pepipost](https://pepipost.com)

This SDK contain methods for easily interacting with the Pepipost Email Sending API to send emails within few seconds.

We are trying to make our libraries a Community Driven. To help us building right things in proper order we would request you to help us by sharing comments, creating new [issues](https://github.com/pepipost/pepipost-sdk-python/issues) or [pull requests](https://github.com/pepipost/pepipost-sdk-python/pulls). We welcome any sort of contribution to this library.

The latest 2.5.0 version of this library provides is fully compatible with the latest Pepipost v2.0 API.
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

#### PIP based installation
   
    pip install pepipost

Once Pepipost is installed successfully, use the below sample [example](#sample-example) to test.
   
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
from pepipost.models.email_body import EmailBody
from pepipost.models.personalizations import Personalizations
from pepipost.models.attachments import Attachments
from pepipost.models.mfrom import From
from pepipost.models.email_body_attachments import EmailBodyAttachments
from pepipost.models.settings import Settings
from pepipost.exceptions.api_exception import APIException
import jsonpickle

client = PepipostClient()
email_controller = client.email
body = EmailBody()
body.personalizations = []

api_key = 'api_key here '
body.personalizations.append(Personalizations())
body.personalizations[0].recipient = 'recipient@your-mail.com'

body.tags = 'tagsPython'
body.mfrom = From()

body.mfrom.from_email = 'example@your-verified-domain'
body.mfrom.from_name = 'Example Pepi'
body.subject = 'Emailing with Pepipost is easy'
body.content = '<html><body>Hey,<br><br>Do you know integration is even simpler in Pepipost, <br>with Python <br> Happy Mailing ! <br><br>Pepipost </body></html>'
body.settings = Settings()

body.settings.footer = 1
body.settings.clicktrack = 1
body.settings.opentrack = 1
body.settings.unsubscribe = 1

try:
    result = email_controller.create_send_email(api_key, body)
    if not (result.error_info is None):
        print("Reason :: " + str(result.error_info.error_message) + "\n" + "Message :: " + str(result.message))
    else:
        print("Message :: " + result.message)
except APIException as e:
    print(e)

```

<a name="announcements"></a>
# Announcements

v2.5.0 has been released! Please see the [release notes](https://github.com/pepipost/pepipost-sdk-python/releases/) for details.

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
