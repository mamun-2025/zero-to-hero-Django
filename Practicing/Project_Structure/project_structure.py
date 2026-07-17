


# 1. Django Project Structure
"""
তুমি যখন Project তৈরি করো:
django-admin startproject config .

তখন Structure এমন হয়:
myproject/
│
├── manage.py
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
└── db.sqlite3   (migrate করার পর)


প্রতিটি File-এর কাজ
File	কাজ
manage.py	   Django Command Center
settings.py	   Project Configuration
urls.py	      URL Routing
wsgi.py	      WSGI Server Entry Point
asgi.py	      ASGI Server Entry Point
init.py	      Python Package হিসেবে চিনিয়ে দেয়



পুরো Request Flow

যখন Browser-এ লিখো:
http://127.0.0.1:8000/products/

তখন ভিতরে কী হয়?

Browser

↓

manage.py runserver

↓

Django Application

↓

settings.py

↓

urls.py

↓

views.py

↓

models.py

↓

Database

↓

HttpResponse

↓

Browser

এখন প্রতিটি File বুঝি।

"""


# 2. manage.py ⭐⭐⭐
"""
manage.py কী?
এটি Django Project-এর Command Center।
সব Django Command এখান থেকে চালানো হয়।

যেমন:
python manage.py runserver
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser

সব Command manage.py দিয়ে।



manage.py-এর Code:
#!/usr/bin/env python

import os
import sys

def main():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "config.settings"
    )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()



Line by Line
১
import os
Operating System-এর Environment Variable নিয়ে কাজ করে।


২
import sys
Command Line Argument পড়ে।

যেমন
python manage.py runserver
runserver এখানে sys.argv-এ থাকে।


৩
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings"
)

এটাই সবচেয়ে গুরুত্বপূর্ণ Line।
এটি Django-কে বলে:
"তোমার Configuration File হলো config.settings।"
তারপর Django settings.py Load করে।


৪
execute_from_command_line(
    sys.argv
)
এটি Command Execute করে।


যদি লিখো:
python manage.py migrate
তাহলে Django Migration চালাবে।


Flow
python manage.py runserver

↓

manage.py

↓

settings.py

↓

Run Server

"""


# 3. settings.py ⭐⭐⭐⭐⭐
"""
এটি Django Project-এর Brain।
সব Configuration এখানে থাকে।

যেমন
DEBUG = True
Development Mode।

ALLOWED_HOSTS = []
কোন Host থেকে Request আসবে।

INSTALLED_APPS
কোন App Install করা আছে।

MIDDLEWARE
Request-এর আগে এবং পরে কী কী কাজ হবে।

DATABASES
Database Connection।

TEMPLATES
Template কোথায় আছে।

STATIC_URL
Static File কোথায়।


settings.py Flow:
settings.py

│

├── Apps

├── Database

├── Templates

├── Static

├── Media

├── Middleware

└── Security


DATABASES:
DATABASES = {

"default": {

"ENGINE":
"django.db.backends.sqlite3",

"NAME":
BASE_DIR / "db.sqlite3",

}

}


Production-এ PostgreSQL হবে।


INSTALLED_APPS:
INSTALLED_APPS = [

'django.contrib.admin',

'django.contrib.auth',

'django.contrib.sessions',

]

এখানে নিজের App-ও যোগ করো।
'products',


"""


# 4. urls.py ⭐⭐⭐⭐⭐
"""
এটি Django-এর GPS।

কোন URL কোথায় যাবে সেটা বলে।
Example:
from django.urls import path
from . import views

urlpatterns = [
                path("", views.views.home),
            
]


Flow

User

/products/

↓

urls.py

↓

views.py

↓

Response

Multiple App:
path(
"products/",
include("products.urls")
)

এখানে include() অন্য App-এর URL যুক্ত করে।

"""


# 5. wsgi.py ⭐⭐⭐
"""
WSGI = Web Server Gateway Interface

Production Server-এর Entry Point।

Development

python manage.py runserver

Production

Nginx

↓

Gunicorn

↓

wsgi.py

↓

Django

Gunicorn wsgi.py ব্যবহার করে Django Application চালায়।

Flow

Client

↓

Nginx

↓

Gunicorn

↓

wsgi.py

↓

Django

"""



# 6. asgi.py ⭐⭐⭐
"""
ASGI = Asynchronous Server Gateway Interface

এটি Async Application-এর জন্য।

ব্যবহার হয়:

WebSocket
Chat Application
Live Notification
Async View
Streaming

Production

Client

↓

Nginx

↓

Uvicorn

↓

asgi.py

↓

Django



WSGI vs ASGI:
| WSGI             | ASGI             |
| ---------------- | ---------------- |
| Sync             | Sync + Async     |
| Gunicorn         | Uvicorn / Daphne |
| Traditional Web  | Web + WebSocket  |
| Request/Response | Real-time Apps   |


Real Production Architecture:
Browser

↓

Nginx

↓

Gunicorn

↓

wsgi.py

↓

Django

↓

PostgreSQL


Chat Application:
Browser

↓

WebSocket

↓

Uvicorn

↓

asgi.py

↓

Django

↓

Redis


সব File-এর সম্পর্ক:
manage.py
     │
     ▼
settings.py
     │
     ▼
urls.py
     │
     ▼
views.py
     │
     ▼
models.py
     │
     ▼
Database




"""