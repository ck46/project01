# DigestAI Backend
This is the backend for the DigestAI web application

## Requiments
1. Python 3.8+
2. MongoDD


## Installation
1. Clone the repo
2. CD into directory
3. Create a python virtual environment using the venv module and activate it.
4. Install requirements using pip

## Usage
This is a django application and thus will need to do migrations for the database models.
```
$python manage.py migrate
$python manage.py makemigrations
```

Then run the application using:
```
$python manage.py runserver
```

### API documentation
Once the server is running using the command above, the api documentation can be found here `http://localhost:8000/docs`


## To do
 - Move setup to docker