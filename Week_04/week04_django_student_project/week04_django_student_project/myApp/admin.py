from django.contrib import admin
from .models import Student, Module

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('firstName','lastName','age','email','enrolmentDate')
    search_fields = ('firstName','lastName','email')
    filter_horizontal = ('modules',)

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('code','name')
    search_fields = ('code','name')
