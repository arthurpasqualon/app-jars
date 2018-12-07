
from django.contrib import admin
from django.urls import path
from .views import HomeView, Contact

app_name='core'

urlpatterns = [
    path ('', HomeView.as_view(), name='home'),
    path('contato/', Contact, name='contact'),
]