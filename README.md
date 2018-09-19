![pepipostlogo](https://pepipost.com/assets/img/pepipost-footLogo.png)

[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.txt)
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
## Installation 
   
There are two ways of installing this Pepipost library. You can use either of the below: 
   
```pip install pepipost``` 

Once Pepipost is install, use the sample example to test.
   
**OR**
   
```git clone https://github.com/pepipost/pepipost-sdk-python.git pepipost_python``` 
   
 
#### Prerequisites
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
   
   
#### Defining environment variable
   
   * Python and PIP should be defined in your PATH. Verify the same using below commands:
   
     ```pip --version```   //This will display the version of PIP dependency manager installed.

     ```python --version```  //This will display the version of Python installed. This should be >=2.7.1, if you are using Python 2 else it can be >=3.4 if you are using Python 3.
     
     
   * Use the below command to navigate to the directory: 
      
     ```cd pepipost_python```
      
#### Quickstart- Using the SDK from GitHub repository 

   1. Run the below command to download the requirements:
         
      ```pip install -r requirement.txt```
      
      ![Building SDK - Step 1](https://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=pepipost-Python)

   2. Open project in an IDE. Here we have used PyCharm IDE. 
      The basic workflow presented here is also applicable if you prefer using a different editor or IDE.
      
      ![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=pyCharm)
      
      Click on ```Open``` in PyCharm to browse to your generated SDK directory and then
      
      Click ```OK```

      ![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=openProject0&workspaceFolder=pepipost-Python)     

      The project files will be displayed in the side bar as follows:

      ![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=openProject1&workspaceFolder=pepipost-Python&projectName=pepipost)     

   3. Add a new "Test Project"

      Create a new directory by right clicking on the solution name as shown below:

      ![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=pepipost-Python&projectName=pepipost)

      Name the directory as "test"

      ![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=nameDirectory)
   
      Add a python file to this project with the name "testsdk"

      ![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=createFile&workspaceFolder=pepipost-Python&projectName=pepipost)

      Name it "testsdk"

      ![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=nameFile)

   4. Importing files from python library

      In order to import file you need to just copy the [sample file from here](#sample). 

      ![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=pepipost-Python&libraryName=pepipost.pepipost_client&projectName=pepipost&className=PepipostClient)

   5. Get your API key and Sending Domain from your Pepipost account. 
  
      * **apikey** will be available under Login to Pepipost -> Settings -> Integration  
      * **Sending Domain** will be available under Login to Pepiost -> Settings -> Sending Domains 

```
  *Note :: Domains showing with Active status on Sending Domain dashboard are only allowed to send any sort of emails.* In case there are no Sending Domain added under your account, then first add the domain, get the DNS (SPF/DKIM) settings done and get it reviewed by our compliance team for approval. Once the domain is approved, it will be in ACTIVE status and will be ready to send any sort of emails. 
```
      
   6. Run the Test Project 
      
      ```Ctrl+F5```
      
      **OR** 
      
      Right click on your Python file inside your Test project and click on ```Run```

      ![Run Test Project - Step 1](https://apidocs.io/illustration/python?step=runProject&workspaceFolder=pepipost-Python&libraryName=pepipost.pepipost_client&projectName=pepipost&className=PepipostClient)

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
    if not (result.error_info.error_message is None):
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
pepipost-php-sdk library is guided and supported by the [Pepipost Developer Experience Team](https://github.com/orgs/pepipost/teams/pepis/members) .
This pepipost-php-sdk library is maintained and funded by Pepipost Ltd. The names and logos for pepipost-php-sdk are trademarks of Pepipost Ltd.

<a name="license"></a>
## License
This code library was semi-automatically generated by APIMATIC v2.0 and licensed under The MIT License (MIT). 
