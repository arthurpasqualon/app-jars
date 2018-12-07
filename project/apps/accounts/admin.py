from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

# from project.core.admin import BaseModelAdmin

from .forms import UserAdminForm
from .models import (
    AccountsSettings, User
)


@admin.register(AccountsSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

    def has_add_permission(self, request):
        return not AccountsSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'email_confirmed', 'is_active', 'is_volunteer', 'is_superuser')
    list_filter = ('email_confirmed', 'is_active', 'is_volunteer', 'is_superuser')
    search_fields = ('email', 'full_name')
    readonly_fields = ('full_name', 'uuid')
    ordering = ('full_name',)
    form = UserAdminForm

    fieldsets = (
        ("Usuário", {
            'fields': ('first_name', 'last_name', 'email', 'email_confirmed',
                       'is_active', 'is_volunteer', 'is_superuser', 'uuid', 'profile_image', 'profile_picture', 'password_reset', )
        }),
#         ("Empresa", {
#             'fields': ('company', 'is_company_admin','send_invite')
#         }),
    )
    


