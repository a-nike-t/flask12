# flask12
##DECSRIPTION-
This is the basic flask app use to create, read, update and delete the user info,
Flask is a basic web framework that provides tools, libraries and technologies that allow you to build a web application.
The dependencies of flask are->
•	Werkzeug a WSGI utility library
•	jinja2 which is its template engine
###Modules Used—
>Bcrypt
>Flask
>Flask-Bcrypt
>Flask-SQLAlchemy
>Flask-WTF
>jinja2
>SQLAlchemy
>Werkzeug
>WTForms


##BASIC STRUCTURE

>F:.
>│   run.py   // the main file that contain the instance of the create_app that is to be run
>│
>└───f // the main module that contains the database as well as app details
>   │   config.py // configuration file containing class config having database URI 
>   │   models.py//the model to create database containing User class to create user and save it into the database
>   │   site.db // database file
>   │   __init__.py // the main initialisation file of “f” module containing the create_app function and blueprints
>   │
>   ├───main //the main module that will contain the main functions that will be common but not used here
>   │   │   forms.py // just given for future work
>   │   │   routes.py //--------------------------------
>   │   │   __init__.py //---------------------------------
>   │ 
>   ├───templates// the template folder containing different pages
>   │          |      account.html // the template to account page of different user 
>   │          |     layout.html // the basic layout to create the other templates – account, login, register (containing bootstrap)
>   │          |      login.html// the login template containing the form section for login
>   │          |      register.html // the register template containing the form section for register
>   │
>   ├───users // the main module containing all the functions about the users
>   │   │   forms.py // contain registration form, login form, update form with their validation function
>   │   │   routes.py // contain routes to login, logout, register, account and delete
>   │   │   __init__.py// the initialization file for user module
>   │   │
>   │   └───__pycache_
>   │
>   └───__pycache



