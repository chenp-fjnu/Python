# Wiki

https://docs.djangoproject.com/en/1.10/intro/tutorial01/

# Command Notes:

```python
django-admin startproject mysite
python manage.py startapp polls
python manage.py migrate
python manage.py makemigrations polls
python manage.py sqlmigrate polls
python manage.py migrate

python manage.py runserver
python manage.py check
python manage.py shell
python manage.py createsuperuser
python manage.py test app
coverage run --source='.' manage.py test app

python -c "import django; print(django.__path__)"

pip install --user django-polls/dist/django-polls-0.1.zip
pip uninstall django-polls
```
# Django Notes:

template: https://docs.djangoproject.com/en/1.10/ref/templates/language/

Avoiding race conditions:https://docs.djangoproject.com/en/1.10/ref/models/expressions/#avoiding-race-conditions-using-f

shortcut

Testing:https://docs.djangoproject.com/en/1.10/topics/testing/

Testing tools:https://docs.djangoproject.com/en/1.10/topics/testing/tools/#django.test.LiveServerTestCase

//Django includes LiveServerTestCase to facilitate integration with tools like Selenium.

Test Coverage:https://docs.djangoproject.com/en/1.10/topics/testing/advanced/#topics-testing-code-coverage

ModelAdmin:https://docs.djangoproject.com/en/1.10/ref/contrib/admin/

Reuseable apps: https://docs.djangoproject.com/en/1.10/intro/reusable-apps/
# TODO:
https://docs.djangoproject.com/en/1.10/intro/tutorial06/