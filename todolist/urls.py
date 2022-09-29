from django.urls import path
from .views import *
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import add_todolist
from todolist.views import deleted
from todolist.views import finished

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('create-task/', add_todolist, name='add_todolist'),
    path('logout/', logout_user, name='logout'),
    path('delete-task/<int:id>', deleted, name = 'deleted'),
    path('finished-task/<int:id>', finished, name = 'finished')
]