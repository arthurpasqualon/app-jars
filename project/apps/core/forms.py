from django import forms
from django.contrib.auth import password_validation
from material import Layout, Row

from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, UserChangeForm

from apps.accounts.models import User


class UpdateProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def clean_password(self):
        return self.clean_password