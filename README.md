# Coffee taster
https://capstonesaad.herokuapp.com/
## Getting Started

### About the project 

This api allows you to add coffee shops to visit with there rating and thier recommended product.
and you can check the once that you visited already

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/capstonesaad` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `/capstonesaad` directory.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=app.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

### Auth

auth.py
Auth0 is set up and running. The following configurations:

The Auth0 Domain Name = fsnd-saad.us.auth0.com
The JWT code signing secret = RS256
The Auth0 Client ID = place The JWT token contains the permissions for the 'Visitor' and 'admin' roles.
visitor "permissions": [
    "get:name",
    "get:visited",
    "post:visited"
  ]

admin   "permissions": [
    "delete:name",
    "get:name",
    "get:visited",
    "patch:name",
    "post:name",
    "post:visited"
  ]
  
  ### Endpoints
  
  app.py



'/coffeeshops' {get}

Fetches a dictionary of array coffeeshop
Request Arguments: None
Return: An array of object coffeeshops which contains id: integer key, name: String represent the name of the coffee shop, rate: String represent the rating of the coffee shop, and recommended: String represent a recommended product for the coffee shop
{ coffeeshop:[ { id:1, name: "BlueBottle", rate: "5", recommended: "cortado" }... ] }

'/coffeeshops' {post}

Fetches A dictionary
Request Arguments: name: String, rate: String and recommended: String
Return: A dictionary with one key "done" if "yes" so the coffeeshop has been added
{ "done": "yes" }

'/coffeeshops/id:integer' {patch}

Fetches A dictionary
Request Arguments: name: String, rate: String, recommended: String and URL argument id: Integer
Return: A dictionary with one key "done" if "yes" so the coffee shop has been modified
{ "done": "yes" }

'/coffeeshops/id:integer' {delete}

Fetches A dictionary
Request Arguments: URL argument id: Integer
Return: A dictionary with one key "done" if "yes" so the coffeeshop has been deleted
{ "done": "yes" }

'/visited' {get}

Fetches a dictionary of array visitedar
Request Arguments: None
Return: An array of object coffeeshop which contains id: integer key, name: String represent the name of the coffee shop, and recommended: String represent a recommended product of the coffee shop
{ visitedar:[ { id:1, name: "blue bottle", recommended: "flat white" }... ] }

'/visited' {post}

Fetches A dictionary
Request Arguments: name: String, recommended: String
Return: A dictionary with one key "done" if "yes" so the coffeeshop have been added
{ "done": "yes" }

Testing

to run the tests, you can by running the command
-python test.py

