from django.contrib import admin
from .models import Course, Program, Event, Module
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'institution', 'from_date', 'to_date']
    search_fields = ['name', 'institution']
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Course, CourseAdmin)

admin.site.register(Program)
admin.site.register(Module)
admin.site.register(Event)