# 💻 My Library Project
A modern Django web application with a clean, organized structure.

## 📃 Overview

This project follows a custom structure:
- `src/`: Main code directory
  - `config/`: Project configuration
  - `library/`: Main application
  - `user/`: Users application
  - `analytics/`: Analytics application
- `venv/`: Virtual environment (not tracked in git)

## 🔍 Prior Requirements

-   Python >= 3.7
-   Any text editor

## 🔧 Instalation

Follow these steps to create a project using Django:

1.  **Clone this repository**

2.  **Create and activate virtual environment**

    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
    > If `.\venv\Scripts\activate` use this code first `Set-ExecutionPolicy Unrestricted -Scope Process`. This allows the use of scripts in the system.

3.  **Install dependencies**

    ```bash
    cd src
    pip install -r requirements.txt
    ```

4.  **Apply migrations**

    ```bash
    python manage.py migrate
    ```

4.  **Populate data**
    ```bash
    python manage.py populate_db
    ```
    
5.  **Create a superuser**

    ```bash
    python manage.py createsuperuser
    ```
    
## 🚀 Running the project
```bash
    cd src
    python manage.py runserver
```

Access the site at `http://127.0.0.1:8000/` and admin at `http://127.0.0.1:8000/admin/`

## 🛠 Development
- Add models to library/models.py
- Create views in library/views.py
- Add URL patterns in library/urls.py
- Create templates in library/templates/

## 👤 Autors
- Baltazar LLique Franklin Anderson
- García Castillejo Rafael
- Rodriguez Ordoñez Juan Daniel
  
##
Built with ❤️ using Django 5



 
