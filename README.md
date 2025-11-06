# Leave Management System - Django DRF 

---

## Project Overview

This Leave Management System allows employees to apply for leaves( edit or delete those existing ), managers to approve/reject them, and view notifications about the leaves of their direct juniors. It is built using Django REST Framework.

---

## Features

* Apply, update, and cancel leaves
* **Role-Based Access Control** — Different access for employees on their position.

* **Smart Leave Handling** — Auto-detects weekends, supports monthly leave limits

* Senior approval/rejection of leave requests

* **Notification System** — Tracks leave events (apply, approve, reject)

* **Error Handling** — Clean, descriptive responses for all API interactions
* **Leave Carry Forward** — Automatically carries forward unused leave monthly

---

## Tech Stack

* **Backend:** Django, Django REST Framework
* **Database:** PostgreSQL
* **Tools:** Postman (for API testing), Python 3.8+

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