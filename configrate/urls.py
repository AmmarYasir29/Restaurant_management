
from django.urls import path
from configrate.views import get_users

urlpatterns = [
    path('users/', get_users, name='users')
]
