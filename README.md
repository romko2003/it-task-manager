IT Task Manager

A portfolio web application built with Django for managing tasks inside an IT team.
The system allows developers, designers, QA engineers, and project managers to create, assign, and track tasks throughout the development process.

This project demonstrates practical skills in:

Django architecture

custom user models

relational database design

CRUD interfaces

filtering and search

Bootstrap-based UI

Demo Features
Task Management

Create, update, and delete tasks

Assign tasks to multiple workers

Set priority and deadlines

Mark tasks as completed or reopen them

View detailed task information

Task Organization

Task types (e.g. Bug, Feature, Refactor)

Tags (Many-to-Many relationship)

Filtering:

by status (done / todo)

by task type

by priority

by assignee

Text search by task name and description

Worker Management

Custom user model: Worker

Position assigned to each worker

Worker list page

Worker detail page with:

active tasks

completed tasks

Reference Data CRUD

Positions

Task types

Tags

Tech Stack

Backend: Django, Python

Database: SQLite

Frontend: Django Templates, Bootstrap

Version control: Git, GitHub (feature branch workflow)

Database Structure

The project uses a relational schema with the following main entities:

Worker (custom user model)

Position

Task

TaskType

Tag

See the database diagram:

db_diagram.png
Installation
1. Clone the repository
git clone https://github.com/<your-username>/it-task-manager.git
cd it-task-manager
2. Create virtual environment
python -m venv venv

Activate it:

macOS/Linux

source venv/bin/activate

Windows

venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Apply migrations
python manage.py migrate
5. Create superuser
python manage.py createsuperuser
6. Run the server
python manage.py runserver

Open in browser:

http://127.0.0.1:8000/
Project Structure
it-task-manager/
│
├── it_task_manager/   # Django project settings
├── tasks/             # Main application
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── templates/         # HTML templates
├── static/            # CSS and static files
├── screens/           # Screenshots for PR
├── db_diagram.png     # Database diagram
├── requirements.txt
├── manage.py
└── README.md
Screenshots

All interface screenshots are available in the screens/ directory.

Key Concepts Demonstrated

Custom Django user model

Class-based views (CBV)

Many-to-many relationships

Query optimization with select_related and prefetch_related

Filtering and search

Clean project structure

Feature-branch Git workflow

Author

Portfolio project created as part of the Mate Academy Django course.
