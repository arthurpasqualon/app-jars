from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

# from project.core.admin import BaseModelAdmin

from .models import Institution, User


# admin.site.register(Profile)
admin.site.register(Institution)
admin.site.register(User)
