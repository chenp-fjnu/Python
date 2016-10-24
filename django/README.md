# Wiki
https://docs.djangoproject.com/en/1.10/intro/tutorial01/

# Command Notes:
django-admin startproject mysite
python manage.py startapp polls
python manage.py migrate
python manage.py makemigrations polls
python manage.py sqlmigrate polls 0001
python manage.py migrate


python manage.py runserver
python manage.py check
python manage.py shell
python manage.py createsuperuser
python manage.py test app
coverage run --source='.' manage.py test app

# Django Notes:
template: https://docs.djangoproject.com/en/1.10/ref/templates/language/
Avoiding race conditions:https://docs.djangoproject.com/en/1.10/ref/models/expressions/#avoiding-race-conditions-using-f
shortcut
Testing:
https://docs.djangoproject.com/en/1.10/topics/testing/
Testing tools:https://docs.djangoproject.com/en/1.10/topics/testing/tools/#django.test.LiveServerTestCase
//Django includes LiveServerTestCase to facilitate integration with tools like Selenium.
Test Coverage:
https://docs.djangoproject.com/en/1.10/topics/testing/advanced/#topics-testing-code-coverage

TODO:
https://docs.djangoproject.com/en/1.10/intro/tutorial06/