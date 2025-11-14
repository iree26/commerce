📬 Mail App – Django Project

This is a web application built with Django, featuring Python-based backend logic, light JavaScript for interactivity, and clean HTML/CSS templates.
It demonstrates core concepts such as authentication, routing, template rendering, and data handling with Django’s ORM.

🚀 Features

User authentication (login, logout, register)

Mail inbox page

Dynamic front-end behavior via JavaScript (inbox.js)

Clean HTML templates (layout.html, inbox.html, etc.)

Django ORM for database interactions

Custom views and URL routing

Static styling with CSS

📁 Project Structure
mail/
│── migrations/
│── static_mail/
│   └── styles.css
│── templates/mail/
│   ├── inbox.html
│   ├── layout.html
│   ├── login.html
│   └── register.html
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

🛠 Installation and Setup

Follow these steps to run the project locally:

1. Clone the repository
git clone https://github.com/iree26/mail.git

cd main

3. Create a virtual environment
py -m venv venv

4. Activate the virtual environment

Windows (PowerShell):

venv\Scripts\Activate


macOS/Linux:

source venv/bin/activate

4. Install requirements
pip install -r requirements.txt

5. Apply migrations
py manage.py migrate

6. Run the development server
py manage.py runserver


Then visit:

http://127.0.0.1:8000/
