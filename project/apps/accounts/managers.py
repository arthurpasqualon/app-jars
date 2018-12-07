from django.contrib.auth.models import BaseUserManager
from django.core.cache import cache
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    use_in_migrations = True

    # def dashboards_active(self, user):
    #     from project.apps.bime.models import BimeDashboard
    #     removed = user.company.companydashboardremoved_set.filter(user=user).values_list('dashboard_id', flat=True)
    #     dashboard_ids = user.company.companydashboard_set.filter(is_active=True).exclude(dashboard_id__in=removed).values_list('dashboard_id', flat=True)
    #     return BimeDashboard.objects.filter(id__in=dashboard_ids, is_activated=True, is_published=True)
    
    # def dashboards_inactive(self, user):
    #     from project.apps.bime.models import BimeDashboard
    #     removed = user.company.companydashboardremoved_set.filter(user=user).values_list('dashboard_id', flat=True)
    #     dashboard_ids = user.company.companydashboard_set.filter(is_active=True).exclude(dashboard_id__in=removed).values_list('dashboard_id', flat=True)
    #     return BimeDashboard.objects.filter(is_activated=True, is_published=True).exclude(id__in=dashboard_ids)

