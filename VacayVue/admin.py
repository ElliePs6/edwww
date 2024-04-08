from django.contrib import admin
from .models import Employee, Company, Request, CustomUser





admin.site.register(CustomUser)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'hr_name')
    ordering = ('name',)
    search_fields = ('name', 'hr_name')

admin.site.register(Company, CompanyAdmin)
    

@admin.register(Employee)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'join_date') 
    ordering = ('first_name',)


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'start', 'end', 'type', 'description')
    search_fields = ('type', 'user')
  