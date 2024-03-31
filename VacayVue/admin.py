from django.contrib import admin
from .models import Employee, Company, Requests, CustomUser



@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'user_type')
    ordering = ('email',)
    search_fields = ('email',)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'hr_name')
    ordering = ('name',)
    search_fields = ('name', 'hr_name')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company', 'join_date','admin')
    ordering = ('company',)


@admin.register(Requests)
class RequestsAdmin(admin.ModelAdmin):
    fields = ('EmployID', ('StartDate', 'EndDate'), 'Status', 'Type')
    list_display = ('EmployID', 'StartDate', 'EndDate', 'Type', 'Status')
    search_fields = ('Type', 'Status')
    list_filter = ('StartDate', 'EndDate', 'Status')