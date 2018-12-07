from django.contrib.auth.models import BaseUserManager
from django.core.cache import cache
from django.db import models
from django.utils import timezone


class AccountsSettingsManager(models.Manager):
    def get(self):
        accounts_settings = cache.get('accounts_settings')
        if not accounts_settings:
            accounts_settings = super().get()
            cache.set('accounts_settings', accounts_settings)
        return accounts_settings


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, first_name, last_name, email, password, **extra_fields):
        email = email.strip().lower()
        user = self.model(first_name=first_name, last_name=last_name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, first_name, last_name, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        user = self._create_user(first_name, last_name, email, password, **extra_fields)
        return user

    def create_superuser(self, first_name, last_name, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('email_confirmed', timezone.now())
        user = self._create_user(first_name, last_name, email, password, **extra_fields)
        return user