from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

# from project.core.admin import BaseModelAdmin

from .models import Institution, User


# admin.site.register(Profile)
admin.site.register(Institution)


class UserAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'password', 'date_of_birth', 
            'graduation', 'gender',  'profile_picture', 'institution', 
            'is_volunteer', 'is_principal', 'is_active')
    search_fields = ['first_name', 'last_name', 'institution']
    
admin.site.register(User, UserAdmin)
