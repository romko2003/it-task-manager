## IT Task Manager

A portfolio Django web application for managing tasks inside an IT team.

The system allows workers to create tasks, assign them to team members, track progress, and organize work using task types, priorities, and tags.

### Features

#### Core functionality

- **Custom user model**: `Worker` (based on `AbstractUser`)
- **Worker positions**: separate model for worker positions
- **Task management**:
  - Create, update, delete tasks
  - Assign multiple workers
  - Set priority and deadline
  - Mark tasks as done/undone
- **Task organization**:
  - Task types (e.g. Bug, Feature, Refactor)
  - Tags (Many-to-Many)
- **Filtering**:
  - by status
  - by type
  - by priority
  - by assignee
- **Search** by task name and description

#### Workers

- **Workers list page**
- **Worker detail page**
- Tasks separated into:
  - Todo
  - Completed

### Technologies

- **Python**
- **Django**
- **SQLite**
- **Bootstrap**

### Database Structure

See `db_diagram.png` in the repository.

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/<your-username>/it-task-manager.git
cd it-task-manager
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set environment variables**

Create a `.env` file (or export variables in your shell) and set at least:

```bash
export DJANGO_SECRET_KEY="your-production-secret-key"
```

5. **Apply migrations**

```bash
python manage.py migrate
```

6. **Create superuser**

```bash
python manage.py createsuperuser
```

7. **Run development server**

```bash
python manage.py runserver
```

Then open in browser: `http://127.0.0.1:8000/`

### Project Structure

```text
it_task_manager/
│
├── it_task_manager/   # Django project settings
├── tasks/             # Main application
├── templates/         # HTML templates
├── static/            # CSS and static files
├── screens/           # Screenshots for PR
├── db_diagram.png     # Database diagram
├── manage.py
└── README.md
```

### Screenshots

See the `screens/` folder.

### Author

Portfolio project created as part of the Mate Academy Django module.

bb