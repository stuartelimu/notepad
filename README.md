# Notepad
A simple notepad application made with django.

## Goal
The goal of this application is to learn how to use django's generic class based views to create a simple application using the DRY principle.


### Prerequisites
This application assumes you have some knowledge with the following
- Django
- Bulma CSS

### Installation & Setup
Clone or download this repository to your local machine. 

`git clone https://github.com/stuartelimu/notepad`

Change into this directory, create and activate a virtual environment. Here I'm using `virtualenv`.
```
cd notepad
virtualenv env && source env/bin/activate
```

Install the packages from the `requirements.txt` file

`pip install -r requirements.txt`

Make migrations to create & populate your database

`python manage.py makemigrations && python manage.py migrate`

Start the development server

`python manage.py runserver`

Visit `http://127.0.0.1:8000/` to see the project in your browser.

### Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Bulma](https://bulma.io/) - The CSS framework used





