from django.contrib import admin
from .models import Movie

admin.site.register(Movie)

# go to terminal to create  the user name by typing manage.py createsuperuser
# it will ask you to provide the user name >>type admin or any name you want
#  it will ask you to provide the email >>type admin@gmail.com or your email
# it will ask you to provide the password >>type 123 or password you want

