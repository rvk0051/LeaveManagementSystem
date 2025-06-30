# Leave Management System - Django DRF 

---

## Project Overview

This Leave Management System allows employees to apply for leaves( edit or delete those existing ), managers to approve/reject them, and view notifications about the leaves of their direct juniors. It is built using Django REST Framework.

---

## Features

* Authentication and Authorization

* Apply, update, and cancel leaves

* Automatic leave balance tracking

* Senior approval/rejection of leave requests

* Notification system for leave actions

* Automatic carry forward of unused leaves

* Intelligent Holiday Handling: Saturdays and Sundays are automatically recognized as non-working days; if included in a leave request, they won't be counted towards the leave balance.

* Robust Error Handling: Comprehensive exception handling to provide meaningful error messages for invalid inputs or unexpected issues, enhancing API reliability.

---

## Tech Stack

* Backend: Django, Django REST Framework
* Authentication: JWT (djangorestframework-simplejwt)
* Database: PostgreSQL
* Tools: Postman (for testing), Python 3.8+

---

## Installation Guide

#### Clone the repo:

* git clone <repo-url>
* cd project_root

#### Create virtual environment & activate:

* python -m venv venv
* venv\Scripts\activate

#### Install requirements:

* pip install -r requirements.txt

#### Set up .env (if applicable) or configure settings.py.

#### Run migrations:

* python manage.py makemigrations
* python manage.py migrate

#### Create superuser:

* python manage.py createsuperuser

#### Run server:

* python manage.py runserver

---

#### Authentication APIS

* Login: /api/auth/login/

* Register: /api/auth/register/

* User Data: /api/auth/users/user_data/

* Junior's Data: /api/auth/user_juniors/

---

#### Leave Management APIs

* View user's leave: GET /api/leaves/user/

* View junior's leave: GET /ap/leaves/juniors/

* Apply Leave: POST /api/leaves/

* Update Leave: PUT /api/leaves/<id>/

* Cancel Leave: DELETE /api/leaves/<id>/

* Approve/Reject: POST /api/leaves/<id>/approve/ or /reject/

* Leave Limits: 4 working days/month (auto tracked)

---

## Notification APIs

* View notifications: GET /api/notifications/

* Mark one as read: POST /api/notifications/<id>/mark-read/

* Mark all as read: POST /api/notifications/mark-all-read/

---