from django.contrib import admin

from .models import User, Department, Company, Employee, Employment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "__str__")


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "__str__")


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "__str__")


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "__str__")


@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin):
    list_display = ("id", "__str__")
