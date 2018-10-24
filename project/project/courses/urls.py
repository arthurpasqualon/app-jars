from django.urls import path
from .views import index, details

app_name='courses'

urlpatterns = [
    path ('', index, name='index'),
    path ('<slug>', details, name='details' )
]
