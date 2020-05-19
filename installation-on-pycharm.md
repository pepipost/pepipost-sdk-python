#### Defining environment variable
   
   * Python and PIP should be defined in your PATH. Verify the same using below commands:
   
     ```pip --version```   //This will display the version of PIP dependency manager installed.

     ```python --version```  //This will display the version of Python installed. This should be >=2.7.1, if you are using Python 2 else it can be >=3.4 if you are using Python 3.
     
     
   * Use the below command to navigate to the directory: 
      
     ```cd pepipost_python```
      
#### Quickstart- Using the SDK from GitHub repository 

   1. Run the below command to download the requirements:
         
      ```pip install -r requirements.txt```
      
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
