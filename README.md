# Django_Models
A Brief Definition of Django
A Django model is a built-in feature that Django uses to create tables, fields, and various constraints. Django models simplify the tasks and organize tables into models. 
 Task- Django Models
 Create a new virtual environment in a folder named .env and install Django in it.
Create a new Django project. Using your Zuriboard Student ID as the name of the project.
Create a new application using the Django startapp command. The app should be called blog.
Add the blog app to the main_projects INSTALLED_APPS.
Create a new model in the blog app called Post. It should have the following fields:
Post

--------

* Title : A string of maxlength 200, use Django’s models.`CharField`
* Text : Any amount of text, use Django’s TextField
* Author : A Foreign Key to the current user model. Make use of Django’s `get_user_model` function.
* Created_date : A date-time column, use Django’s models.DateTimeField. 
* Published_date : A date-time column, use Django’s models.DateTimeField.
Create migrations for your new model using the makemigrations Django command.
Run all migrations using the migrate Django command.
