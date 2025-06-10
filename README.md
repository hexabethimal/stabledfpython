# stabledfpython
This is DIY instructions to set up Runpod serverless with Python for generating images

**This project has an MIT LICENSE. Read the license for more information.**

# Description
If you can code a little Python, then you can get up and running quickly and cheaply with a private AI image generator server running Stable Diffusion. It's not free, but it is low cost at about 50 images for 30 cents (your results will vary).

**These instructions assume you are using a Windows computer. The instructions for Mac and Linux are not much different though.**

## Table of Contents
- [Create Runpod Account](https://github.com/hexabethimal/stabledfpython/#create-runpod-account)
- [Setup Your Cloud Server](https://github.com/hexabethimal/stabledfpython/#setup-your-cloud-server)
- [Obtain Server Endpoint](https://github.com/hexabethimal/stabledfpython/#obtain-server-endpoint)
- [Create Server API Key](https://github.com/hexabethimal/stabledfpython/#create-server-api-key)
- [Install Python](https://github.com/hexabethimal/stabledfpython/#install-python)
- [Create Python Virtual Environment](https://github.com/hexabethimal/stabledfpython/#create-python-virtual-environment)
- [Install Python Library Dependency](https://github.com/hexabethimal/stabledfpython/#install-python-library-dependency)
- [Editing Python Script](https://github.com/hexabethimal/stabledfpython/#editing-python-script)
- [Running Python Script](https://github.com/hexabethimal/stabledfpython/#running-python-script)
- [Seeing Results](https://github.com/hexabethimal/stabledfpython/#seeing-results)

## Create Runpod Account
1. Go to [Runpod.io website](https://www.runpod.io)
2. Create an account
3. Go to Billing under Account on the left sidebar
4. Add credit to your account, like $10 (you don't need much for a lot of images)

## Setup Your Cloud Server
1. On Runpod, under Manage on the left sidebar, click Serverless
2. Under Quick Deploy, select Image to see quick deploy options
3. Click 'Configure' button for one of the SD or Stable Diffusion options that looks good to you (You can change your mind a do a different one later)

## Obtain Server Endpoint
1. Once your server has finished deploying and shows 'Ready' in green, click on the Requests tab
2. Copy the POST address without the /run at the end. This is your Server Endpoint. You will need this later.

## Create Server API Key
1. Inside Runpod, go to Settings under Account in the left sidebar
2. Scroll down and click 'API Keys' dropdown
3. Click the button '+ Create API Key'
4. Copy the API Key value. You will need this later. (This authenticates you as an authorized user to access your server and prevents other people from using your server costing you money.)

## Install Python
Python is a programming language that helps people write instructions for computers in a way that’s easy to read and understand.
1. Download and install the latest version of Python [Python download](https://www.python.org/downloads/)
2. Install Python following the normal installation process

## Create Python Virtual Environment
Python is safe for your computer, but not everything that you could possibly do with Python is safe for your computer. While my instructions are completely safe for your computer, it's a good idea to get into the habit of only running Python through a Python virtual environment. This step teaches you how to set up a virtual environment for your image generator program.
1. Create a folder for your Python projects. Easiest to just put this folder at the root of your main drive (typically C: drive). Name it 1 word for ease, like `pythontest`
2. Open up a Command Prompt terminal in Windows and go to the folder from Step 1
  - Go to your Start Menu and search for Command Prompt and select it
  - This will automatically put you into a directory (folder) that you don't want to use for this, so you need to navigate to the directory you created in step 1.
  - Type `cd/.` and press Enter
  - If you put your Python projects folder in the C: Drive, then you're there now if you see `C:\>`
  - Navigate to your Python projects folder. If you followed step 1 exactly, then type  `cd pythontest`
3. Create and activate Python venv
  - Type `python -m venv mytestproject` where *mytestproject* is the name you want for your Python program. Wait a few seconds for it to create.
  - Type `mytestproject\Scripts\activate` where *mytestproject* is the name you chose for your Python program 

## Install Python Library Dependency
Python comes with many useful libraries (capabilities) during the normal installation, but there are many more libraries that you can add to Python to get it to do more stuff. In order to run this Python program, you need a very popular library called Requests
See here for information about the Requests library [Requests library](https://pypi.org/project/requests/)
1. Inside your Python Virtual Environment, enter `pip install requests`
You'll see some stuff happening inside your terminal. This is perfectly normal.
You may see a notice that *a new release of pip is available*. You can disregard this.

## Editing Python Script

## Running Python Script

## Seeing Results

