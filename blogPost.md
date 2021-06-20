
FastAPI is a relatively new Python framework that allows you to create applications very quickly. In my opinion, FastAPI is the NodeJS of the Python world. This framework allows you to read API request data seamlessly with built in modules, and doesn't require the bulky setup as seen in Django or the multiple packages needed to run Flask. 

You can create re-usable data models, handle file uploads, generate API docs, and setup authentication within your application using built in OAuth and JWT support. On top of that, you can use any database you want. 

If you don't want the complexity of Django, and would like more features than Flask, this is the framework for you. In this article, we will go over the features of FastAPI, setup a basic API, and show you how simple it is to get started.

### Pre-Requisites

Before we get started building with FastAPI, we need to have the following installed:

* Python 3 
* pip
* virtualenv 

Once those software packages and libraries are installed, we can begin creating a new FastAPI application. To begin, create a new directory to devlop within. Via the command line, change directories into that folder, and create a new virtual environment using the following command `virtualenv fast-env`. After creating the virtual environment, you need to change directory into that environment folder and activate it, which can be done by typing `source bin/activate`.

Now that we have a virtual environment, we can install all the packages needed to develop an application with FastAPI. To begin, we need to install the FastAPI library and a webserver to run it. Assuming that you have Python 3 installed, you should run  `pip3 install fastapi` in your terminal to install the FastAPI library, and once that is complete, run `pip3 install uvicorn[standard]` to install the web server.

In order to incorporate authentication, we need to install the Authlib library in order to handle Json Web Tokens (JWT) required to use Auth0's library. To install, run `pip3 install Authlib` in the command line.

### First Steps

With all the libraries installed, we can go back to the application root (fastAPI) and create a `main.py` file, where our server code will live. The contents of the `main.py` will look like this:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

```
Lets break this down. To start, we are importing the FastAPI library, and creating out app by calliung the `FastAPI()` function. From there, we are defining a route to handle get requests on the base URL by decorating it with `@app.get`. Under the decorator, we are creating a route handler, which is a function that will run each time that base route is called. Here, we are returning an object with the key of "message" and value of "Hello World".

To get the server up and running, type `uvicorn main:app --reload` in the terminal. From there, you can visit the API via the web browser by going to the URL shown in the CLI (most likely http://127.0.0.1:8000), and in doing so, you will be greeted with `{"message": "Hello World"}` on the homepage. Congrats, you have just created your first FastAPI application!


### Adding Routes

Now that a base application is setp, we will add routes and some structure to the application. The best way to do that would be to add a `routes` folder to contain all of the application paths. In the root directory, create a routes folder and within it, create a `messages.py` file. This file will contain the following code:

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/public/")
async def get_public():
    return { "message": "The API doesn't require an access token to share this message."}


@router.get("/protected")
async def get_protected():
    return {"message": "The API successfully recognized you as an admin."}


@router.get("/admin")
async def get_admin():
    return {"message": "Hello World"}

```

In this file, we are calling the APIRouter functionality of FastAPI in order to define routes outside of the main application. We have three routes, each accepting a `GET` request, and returning a different message depending upon the endpoint.

All of these endpoints are public, meaning they are not protected at all. In order to protect the endpoints against unauthorized users, we would need to add an authorization aspect to these routes, which is where Auth0 comes in.

### Adding Authorization


