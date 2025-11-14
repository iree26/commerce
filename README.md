Mail App – Django Project

This is a web application built with Django, featuring Python-based backend logic, light JavaScript for interactivity, and simple HTML/CSS templates.
The project demonstrates core concepts such as authentication, routing, template rendering, and data handling with Django.

Features
User authentication (login, logout, register)
Mail inbox page
Dynamic front-end behavior via JavaScript (inbox.js)
Simple and clean HTML templates
Django ORM for database interactions
Custom views and URL routing
Static styling with CSS

mail/
│── migrations/
│── static_mail/
│    └── styles.css
│── templates/mail/
│    ├── inbox.html
│    ├── layout.html
│    ├── login.html
│    └── register.html
│── admin.py
│── apps.py
│── models.py
│── tests.py
│── views.py
│── urls.py
│── inbox.js
project3/
│── settings.py
│── urls.py
│── wsgi.py
│── asgi.py
manage.py
db.sqlite3

INSTALLATION AND SETUP
git clone https://github.com/iree26/main.git
cd main
py -m venv venv
venv\Scripts\Activate
source venv/bin/activate
py manage.py migrate
py manage.py runserver
