from django.contrib import admin

# Register your models here.
# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from DjangoERP.models import Employee


class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'


# Define a new User admin
class DjangoUserAdmin(UserAdmin):
    inlines = [EmployeeInline]

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, DjangoUserAdmin)