FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
ADD . /code/
RUN pip install -r /code/app/requirements.txt

ENV DJANGO_DB_NAME=sqlite3
ENV DJANGO_SU_NAME=cheetar
ENV DJANGO_SU_EMAIL=foo@bar.com
ENV DJANGO_SU_PASSWORD=qwertyqwerty
ENV DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': '/code/app/db.sqlite3',}}


RUN python3 -c "import django; django.setup(); \
   from django.contrib.auth.management.commands.createsuperuser import get_user_model; \
   get_user_model()._default_manager.db_manager('$DJANGO_DB_NAME').create_superuser( \
   username='$DJANGO_SU_NAME', \
   email='$DJANGO_SU_EMAIL', \
   password='$DJANGO_SU_PASSWORD')"
