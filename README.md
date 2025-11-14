🛒 Django Auction Commerce App

This is a backend-focused Auction Commerce Web Application built using Django.
It allows users to create listings, place bids, add items to their watchlist, and manage auction activity.
The project emphasizes Python, Django ORM, authentication, and backend logic with simple HTML and light JavaScript.

🔥 Core Features

User authentication (register, login, logout)

Create auction listings

Place bids on items

Add listings to a personal watchlist

Category filtering

Close auctions (for listing owners)

Django Admin integration

Clean backend logic and models using Django ORM

🧩 Technologies Used

Python (Django Framework)

HTML (basic templates)

CSS (minimal styling)

JavaScript (light interactions)

SQLite database

📁 Project Structure
commerce/
│── auctions/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── commerce/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── db.sqlite3
└── manage.py

⚙️ Installation & Setup

Follow these steps to run the project locally.

1. Clone the repository
git clone https://github.com/iree26/commerce.git
cd main


If this project is in a different repo, tell me the repo name and I will update it.

2. Create a virtual environment
py -m venv venv

3. Activate the virtual environment

Windows:

venv\Scripts\Activate


macOS/Linux:

source venv/bin/activate

4. Install dependencies
pip install -r requirements.txt

5. Apply migrations
py manage.py migrate

6. Start the Django development server
py manage.py runserver


Then open in your browser:

http://127.0.0.1:8000/
