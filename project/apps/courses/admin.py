from django.contrib import admin
from .models import Course, Program, Event, Module, CourseParticipation, EventParticipation



class CourseParticipationInline(admin.TabularInline):
    model = CourseParticipation

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'institution', 'from_date', 'to_date']
    search_fields = ['name', 'institution']
    prepopulated_fields = {'slug' : ('name',)}
    inlines = [CourseParticipationInline]
    # actions = ["export_as_csv"]

admin.site.register(Course, CourseAdmin)


class EventParticipationInline(admin.TabularInline):
    model = EventParticipation

class EventAdmin(admin.ModelAdmin):
    search_fields = ['name', 'institution']
    inlines = [EventParticipationInline]

admin.site.register(Event, EventAdmin)


class ModuleInline(admin.StackedInline):
    model = Module

class ProgramAdmin(admin.ModelAdmin):
    inlines = [ModuleInline]

admin.site.register(Program, ProgramAdmin)