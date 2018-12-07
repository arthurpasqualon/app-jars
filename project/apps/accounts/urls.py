from django.urls import path

from . import views

app_name = 'apps_accounts'

urlpatterns = [
    path('minha/', views.MyAccountView.as_view(), name='my_account'),
    path('minha/foto/', views.MyAccountProfilePictureView.as_view(), name='my_account_profile_picture'),
]
