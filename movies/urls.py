# import path from django.urls to be able to use down
from django.urls import path
# import all function we create inside file view.py
from .views import home_page, create, edit, delete
# need to change parentheses from {} to [], if not will give you an error
urlpatterns = [
# path line should have ('url',name of function, name = 'name of function again')
    path('', home_page, name='home_page'),
    path('create/', create, name='create'),
    path('edit/<str:movie_id>', edit, name='edit'),
    path('delete/<str:movie_id>', delete, name='delete')
]
