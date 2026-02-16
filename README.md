IT Task Manager

A portfolio Django web application for managing tasks inside an IT team.

The system allows workers to create tasks, assign them to team members, track progress, and organize work using task types, priorities, and tags.

Features Core functionality

Custom user model Worker (based on AbstractUser)

Worker position support

Task management:

Create, update, delete tasks

Assign multiple workers

Set priority and deadline

Mark tasks as done/undone

Task organization

Task types (e.g. Bug, Feature, Refactor)

Tags (Many-to-Many)

Filtering:

by status

by type

by priority

by assignee

Search by task name and description

Workers

Workers list page

Worker detail page

Tasks separated into:

Todo

Completed

Technologies

Python

Django

SQLite

Bootstrap

Database Structure

See db_diagram.png in the repository.

Installation

Clone the repository git clone https://github.com/<your-username>/it-task-manager.git cd it-task-manager
Create virtual environment python -m venv venv source venv/bin/activate # macOS/Linux venv\Scripts\activate # Windows
Install dependencies pip install -r requirements.txt
Apply migrations python manage.py migrate
Create superuser python manage.py createsuperuser
Run server python manage.py runserver
Open in browser:

http://127.0.0.1:8000/ Project Structure it_task_manager/ │ ├── it_task_manager/ # Django project settings ├── tasks/ # Main application ├── templates/ # HTML templates ├── static/ # CSS and static files ├── screens/ # Screenshots for PR ├── db_diagram.png # Database diagram ├── manage.py └── README.md Screenshots

See the screens/ folder.

Author

Portfolio project created as part of Mate Academy Django module.
