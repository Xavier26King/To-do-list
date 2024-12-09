# To-do-list


## How to Set Up and Run the Project

### Prerequisites
Ensure you have the following installed on your system:

- Python (>=3.6)
- pip (Python package manager)
- Virtualenv (recommended for creating isolated environments)

### Steps to Set Up and Run the Project

#### 1. Clone the Repository
Download or clone the repository to your local machine.
```bash
git clone <repository_url>
cd django_todo
```

#### 2. Create a Virtual Environment
Set up a virtual environment to manage dependencies.
```bash
python -m venv env
source env/bin/activate  # For Linux/Mac
env\Scripts\activate   # For Windows
```

#### 3. Install Dependencies
Install the required Python packages.
```bash
pip install django
```

#### 4. Create a Django Project
Initialize the Django project.
```bash
django-admin startproject todo_project .
```

#### 5. Create the To-Do App
Create a Django app to handle tasks.
```bash
python manage.py startapp todo
```

#### 6. Configure the App
- Add the app to the `INSTALLED_APPS` section in `todo_project/settings.py`:

  ```python
  INSTALLED_APPS = [
      ...,
      'todo',
  ]
  ```

- Create the database migrations:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

#### 7. Run the Development Server
Start the Django development server to test the application.
```bash
python manage.py runserver
```

#### 8. Access the Application
Open your browser and navigate to:

- **View tasks:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Add a task:** [http://127.0.0.1:8000/add/](http://127.0.0.1:8000/add/)

