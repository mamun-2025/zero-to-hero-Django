

# admin panel
"""
username: mamun
email : beparimamun708@gmail.com
password: password12345
"""

### Django-তে নতুন App তৈরি করার সম্পূর্ণ Standard Workflow।
"""
Step 1: App তৈরি
python manage.py startapp products


Step 2: settings.py
INSTALLED_APPS = [
    ...
    "products",
]


Step 3: Model লিখো

products/models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()



Step 4: Admin Register

products/admin.py

from django.contrib import admin
from .models import Product

admin.site.register(Product)



Step 5: View লিখো

products/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("Products App Working!")


   
✅ Step 6: App-এর urls.py তৈরি করো

এটা অনেকেই প্রথমে ভুলে যায়।

products/urls.py

from django.urls import path
from .views import home

urlpatterns = [
    path("", home, name="home"),
]



✅ Step 7: Project urls.py-তে Include করো

config/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/", include("products.urls")),
]

এখানে:

products/

মানে Browser-এ এই URL ব্যবহার করবে।



✅ Step 8: Migration তৈরি করো

Model লিখার পরে:

python manage.py makemigrations



✅ Step 9: Database Update
python manage.py migrate



✅ Step 10: Superuser তৈরি করো
python manage.py createsuperuser

তারপর

Username
Email
Password

দাও।



✅ Step 11: Server Run
python manage.py runserver

Output হবে:

Starting development server at http://127.0.0.1:8000/



✅ Step 12: Browser-এ Check

যাও:

http://127.0.0.1:8000/products/

দেখবে:

Products App Working!



✅ Step 13: Admin Check

যাও:

http://127.0.0.1:8000/admin/

Login করো।

তারপর দেখবে:

Products

নামে Model এসেছে।

নতুন Product Add করতে পারবে।



Django Request Flow
Browser
      │
      ▼
127.0.0.1:8000/products/
      │
      ▼
config/urls.py
      │
      ▼
products/urls.py
      │
      ▼
views.home()
      │
      ▼
HttpResponse
      │
      ▼
Browser
Django শেখার সময় প্রতিটি App বানানোর Checklist

প্রতিবার এই Checklist অনুসরণ করো:

✅ startapp
✅ INSTALLED_APPS
✅ models.py
✅ admin.py
✅ views.py
✅ app/urls.py
✅ project/urls.py (include)
✅ makemigrations
✅ migrate
✅ createsuperuser
✅ runserver
✅ Browser-এ URL Test
✅ Admin Panel Test

এটাই Django-তে নতুন App তৈরি করার সম্পূর্ণ Standard Workflow।

"""









# 1. App Structure
"""
Project এবং App কি এক জিনিস?

❌ না।

অনেকেই শুরুতে এই ভুলটা করে।

Project কী?

Project হলো পুরো Website।

যেমন:

E-commerce Website

এর মধ্যে থাকতে পারে:

User Management
Products
Orders
Payments
Reviews
Cart
Wishlist

এই পুরো জিনিসটাই Project।

App কী?

App হলো Project-এর একটি নির্দিষ্ট Feature বা Module।

উদাহরণ:

E-commerce Project

│

├── users

├── products

├── orders

├── cart

├── payments

├── reviews

প্রতিটি Folder একটি App।

কেন App ব্যবহার করা হয়?

ধরো সব Code এক জায়গায় লিখলে—

views.py

10000+ Lines

models.py

5000+ Lines

Maintain করা খুব কঠিন হবে।

তাই Django Feature অনুযায়ী App ভাগ করে।

Real Production Example

Amazon-এর মতো একটি Project:

Amazon

│

├── Authentication App

├── Product App

├── Order App

├── Cart App

├── Payment App

├── Notification App

├── Review App

প্রতিটি Team আলাদা App নিয়ে কাজ করতে পারে।

এটাই Modular Design।

Project vs App
Project	App
পুরো Website	একটি Feature
একটি Project	অনেক App
Global Settings	Feature Logic

"""


# 2. Creating App
"""
নতুন App তৈরি:

python manage.py startapp products

এখন Structure হবে:

products/

│

├── admin.py

├── apps.py

├── migrations/

├── models.py

├── tests.py

├── views.py

└── __init__.py
App তৈরি করার পর কী করতে হবে?

সবচেয়ে গুরুত্বপূর্ণ Step:

settings.py

INSTALLED_APPS = [

...

'products',

]
কেন?

কারণ Django-কে বলতে হবে—

"এই App-টিও Project-এর অংশ।"

না হলে:

Model Load হবে না
Migration হবে না
Admin-এ দেখা যাবে না

"""


# 3. apps.py ⭐⭐⭐
"""
অনেকে কখনো এই File খোলে না।

কিন্তু Interview-তে প্রশ্ন আসে।

Code

from django.apps import AppConfig

class ProductsConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'

    name = 'products'
AppConfig কী?

Django প্রতিটি App-এর জন্য একটি Configuration Object তৈরি করে।

name

name = "products"

মানে এই App-এর নাম।

default_auto_field

BigAutoField

Primary Key-এর Default Type।

অর্থাৎ:

id

Automatic হবে।

apps.py কখন কাজে লাগে?

যখন App Start হওয়ার সময় কিছু কাজ করতে হবে।

যেমন:

Signals Register
Cache Initialize
Custom Startup Logic

Example

class ProductsConfig(AppConfig):

    def ready(self):

        print("Products App Started")

Project Start হলে ready() একবার Execute হবে।

"""


# 4. admin.py ⭐⭐⭐⭐⭐
"""
Django-এর সবচেয়ে Powerful Feature।

Admin Panel কী?

Browser থেকেই Database Manage করা যায়।

URL

/admin/

Model

class Product(models.Model):

    name = models.CharField(max_length=100)

    price = models.IntegerField()

Register

from django.contrib import admin

from .models import Product

admin.site.register(Product)

এখন Browser-এ:

/admin/

থেকে Product Add/Edit/Delete করা যাবে।

Flow

Browser

↓

Admin Panel

↓

Model

↓

Database

Production-এ Admin ব্যবহার হয়:

Product Add
User Manage
Orders দেখার জন্য
Reports

"""


# 5. models.py ⭐⭐⭐⭐⭐
"""
সবচেয়ে গুরুত্বপূর্ণ File।

কারণ Database এখানেই Define হয়।

Example

from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=100)

    price = models.IntegerField()

    stock = models.IntegerField()

এটি Database Table হবে।

Product

id

name

price

stock

Model-এর কাজ

Python Class

↓

ORM

↓

SQL

↓

Database Table

Example

Product.objects.create(
    name="Laptop",
    price=80000
)

ORM ভিতরে SQL বানাবে:

INSERT INTO product
(name,price)

VALUES
('Laptop',80000);

"""


# 6. views.py ⭐⭐⭐⭐⭐
"""
View হলো Business Logic।

User গেল:

/products/

↓

View

↓

Database

↓

Response

Example

from django.http import HttpResponse

def home(request):

    return HttpResponse("Hello Django")

আরও Example

from .models import Product

from django.shortcuts import render

def products(request):

    items = Product.objects.all()

    return render(
        request,
        "products.html",
        {
            "products": items
        }
    )

Flow

Browser

↓

URL

↓

View

↓

Model

↓

Database

↓

Template

↓

Browser
App-এর ভিতরের Flow
URL

↓

View

↓

Model

↓

Database

↓

View

↓

Template

↓

Response
Project + App Architecture
config/

│

├── settings.py

├── urls.py

│

products/

│

├── models.py

├── views.py

├── admin.py

├── apps.py

│

users/

│

├── models.py

├── views.py

│

orders/

│

├── models.py

├── views.py
বাস্তব Backend Example

ধরো User Browser-এ গেল:

/products/

তারপর—

Browser

↓

config/urls.py

↓

products/views.py

↓

products/models.py

↓

PostgreSQL

↓

products/views.py

↓

Template

↓

Browser

"""



