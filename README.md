# Blog App

A Django-based blogging platform where users can create, update, view, and manage posts and drafts. The app supports published posts, draft management, and user authentication.

## Features

User authentication (login required for creating or editing posts)

Create, update, and delete posts

Manage drafts (unpublished posts)

View published posts

Class-based views for clean and maintainable code

Form validation for post creation and updates

## Technologies Used

Backend: Django 5.2.5, Python 3.11

Frontend: HTML, CSS, Django Templates

Database: SQLite (default for development)

Other Tools: Django’s generic class-based views, LoginRequiredMixin for access control

## Setup Instructions

Clone the repository:

git clone https://github.com/yourusername/blog-app.git
cd blog-app


Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Apply migrations:

python manage.py migrate


Run the development server:

python manage.py runserver


Access the app in your browser:

http://127.0.0.1:8000/