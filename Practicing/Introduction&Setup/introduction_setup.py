


# 1. Django কী?
"""
Definition
Django হলো Python দিয়ে Web Application তৈরির একটি High-Level Web Framework।
এটি এমন অনেক কাজ আগে থেকেই তৈরি করে দেয়, যেগুলো না থাকলে তোমাকে নিজে লিখতে হতো।

যেমন:
URL Routing
Database Connection
Authentication
Admin Panel
Forms
Security
Session Management
ORM


"""

# 2. Framework কী?
"""
ধরো তুমি একটি বাড়ি বানাবে।

Framework ছাড়া
সবকিছু নিজে করতে হবে।

ইট কিনো
↓
বালি কিনো
↓
রড কিনো
↓
নিজে ডিজাইন করো
↓
বাড়ি বানাও

অনেক সময় লাগবে।


Framework দিয়ে
আগেই একটি শক্ত ভিত্তি তৈরি আছে।

Ready Structure

↓

তুমি শুধু নিজের প্রয়োজন অনুযায়ী কাজ করো
Django ঠিক এই Ready Structure-টাই দেয়।

Real Example
ধরো Facebook Login।

User:

Login

↓

Django Authentication

↓

Database

↓

Success

↓

Dashboard

এই পুরো Flow Django সহজ করে দেয়।

"""



# 3. Django-এর সুবিধা
"""
1. Fast Development
অনেক কাজ আগে থেকেই তৈরি।

2. Security
Built-in Protection:

CSRF
XSS
SQL Injection
Clickjacking

3. Scalable
ছোট Project থেকে বড় Production System পর্যন্ত ব্যবহার করা যায়।

4. ORM
Raw SQL কম লিখতে হয়।

User.objects.filter(is_active=True)

Django ভিতরে SQL বানায়।

5. Admin Panel
মাত্র কয়েক লাইনে Admin Dashboard।


Django Architecture (MVT)
Django MVC ব্যবহার করে না।
Django ব্যবহার করে:

MVT

Model

View

Template


পুরো Flow
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

Model

↓

View

↓

Template

↓

Browser
Model

Model Database-এর সাথে কাজ করে।

উদাহরণ:
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

এটি products Table তৈরি করবে।

View
View হলো Business Logic।

def home(request):
    return HttpResponse("Hello Django")


Template
HTML Page।

<h1>Hello Django</h1>


MVT Example
User Browser-এ গেল:

/products/

Flow:

URL

↓

Product View

↓

Product Model

↓

Database

↓

Product List

↓

Template

↓

Browser
MVC vs MVT
MVC	         Django MVT
Model	         Model
View (UI)	   Template
Controller	   View

Django-তে View অনেকটা Controller-এর কাজ করে।


Django Setup
Django শুরু করার আগে কী লাগে?

Python Install
pip
Virtual Environment
Django Install
Virtual Environment

"""



# 4. Virtual Environment কী?
"""
একটি Project-এর জন্য আলাদা Python Environment।

ধরো:

Project A
Django 5.2

Project B
Django 4.2

Virtual Environment না থাকলে Version Conflict হতে পারে।
Virtual Environment থাকলে প্রতিটি Project আলাদা Environment ব্যবহার করে।

Virtual Environment তৈরি
Windows:
python -m venv .venv

Linux / macOS:
python3 -m venv .venv


Activate

Windows:
.venv\Scripts\activate

Linux/macOS:
source .venv/bin/activate

Check:
python --version

Prompt-এর শুরুতে সাধারণত এমন দেখাবে:
(.venv)
মানে Environment Active।


Django Installation

Install:
pip install django

Version Check:
django-admin --version


First Django Project

নতুন Project তৈরি:
django-admin startproject config .
এখানে config হলো Project-এর নাম।
. মানে বর্তমান Folder-এই Project তৈরি হবে।

Run Server:
python manage.py runserver

Output:
Starting development server at

http://127.0.0.1:8000/
Browser-এ গেলে Django-এর Welcome Page দেখবে।

"""