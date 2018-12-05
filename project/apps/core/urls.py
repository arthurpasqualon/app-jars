
from django.contrib import admin
from django.urls import path
from .views import Home, Contact

app_name='core'

urlpatterns = [
    path ('', Home, name='home'),
    path('contato/', Contact, name='contact'),
]