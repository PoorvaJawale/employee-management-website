# Flask Employee Management CRUD Web App

A secure and stylish web application to manage employee records using Python's Flask framework. Includes user registration, login authentication (with bcrypt), and full CRUD (Create, Read, Update, Delete) functionality.

## Features
-User Registration & Login with hashed passwords using bcrypt <br>
-Session-based user authentication <br>
-Add, Edit, Delete employee records <br>
-SQLite3 as the backend database <br>
-Modular code with separate `models.py` and `templates` <br>
-Clean and responsive UI with Bootstrap <br>
-Flash messages for user feedback <br>

## Tech Stack

|  LAYER         |  Technology              |
| ---------------|--------------------------|
|  Backend       |  Python, Flask           |
|  Frontend      |  HTML, Bootstrap         |
|  Database      |  SQLite3                 |
|  Auth & Hash   |  Flask Sessions, Bcrypt  |
|  ORM           |  Flask SQLAlchemy        |

## Getting Started

###1. Clone the repository

``bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name ``

###2. Create virtual environment 

``bash
python -m venv venv
source venv/bin/activate ``

###3. Install dependencies

``bash
pip install -r requirements.txt `` <br>

if requirements.txt is not available, then manually install: <br>

``bash
pip install flask flask_sqlalchemy flask_bcrypt ``

###4. Run the application

``bash
python app.py `` <br>

Open your browser and go to http://127.0.0.1:5000/login

## Folder Structure

project/ <br>
│ <br>
├── app.py               # Main Flask application <br>
├── models.py            # SQLAlchemy models (User, Data) <br>
├── templates/ <br>
│   ├── base.html        # Layout <br>
│   ├── header.html      # Optional header <br>
│   ├── index.html       # Dashboard with CRUD <br>
│   ├── login.html       # Login page <br>
│   └── register.html    # Registration page <br>
├── static/              # Optional for custom CSS/JS <br>
└── database.db <br>


