import os

print(os.getcwd())
print(os.path.abspath(__file__))
print(os.path.dirname(__file__))
print(os.path.basename(__file__))

print("\n")

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
print("PROJECT_ROOT: " + PROJECT_ROOT)

print("\n")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR: " + BASE_DIR)

print("\n")

print("os.getcwd: " + os.getcwd())

print("\n")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print("BASE_DIR: " + BASE_DIR)

print("\n")

STATICFILES_DIRS = os.path.join(BASE_DIR, 'static')
print("STATICFILES_DIRS: " + STATICFILES_DIRS)

print("\n")
print(os.environ)

"""
sixtymill [0]
|-- requirement.txt
|-- sixty_mill [1](project?)
|	|-- manage.py
|	|-- mysite.log
|	|-- Procfile
|	|-- requirements.txt
|	|-- runtime


|	|-- sixty_mill [2]
|	|--	|--	__init__.py
|	|--	|--	settings.py
|	|--	|--	test_dirnames.py
|	|--	|--	urls.py
|	|--	|--	wsgi.py

|	|--	|--	__pycache__ 
|	|--	|--	|-- (many files, ignored by git for prod)

|	|--	|--	admin 
|	|--	|--	|-- (files for basic admin site css/html/js)

|	|--	|--	static
|	|--	|--	|--- css
|	|--	|--	|--- fonts
|	|--	|--	|--- js
|	|--	|--	|--- sixty_mill



|	|-- splash_page [2] (app)
|	|--	|-- __init__.py
|	|--	|-- admin.py
|	|--	|-- apps.py
|	|--	|-- forms.py
|	|--	|-- models.py
|	|--	|-- tests.py
|	|--	|-- urls.py
|	|--	|-- views.py
|	|--	|-- __pycache__
|	|--	|--	|-- (many files, should not be used for prod)
|	|--	|--	Migrations
|	|--	|--	|-- (for database migrations)
|	|--	|--	Templates
|	|--	|--	|-- base.html
|	|--	|--	|-- home.html



|	|-- venv (virtual environment)
|	|--	|-- (many files, should use sixtymill_env)

|-- sixtymill_env [1]


Questions -
1. What is going to be the top level repository root?
2. 

Repository root will be a [1] and will include
- configuration_root
- django_project_root
- readme
- manage.py
- .gitignore
- requirements.txt

"""

