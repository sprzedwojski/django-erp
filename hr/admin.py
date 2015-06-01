from datetime import datetime
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils import timezone

from hr.models import *


# Register your models here.


class JobApplicantAdmin(admin.ModelAdmin):
    list_display = ('appl_name', 'appl_surname', 'appl_email', 'appl_birthdate', 'appl_submitted')

    def response_add(self, request, obj, post_url_continue=None):
        """This makes the response after adding go to another apps changelist for some model"""
        return HttpResponseRedirect(reverse("hr:applicant", args=[obj.id]))

    def response_change(self, request, obj):
        if obj.appl_status.stat_order == RecruitmentStatus.get_max_id():
            employee = Employee()
            employee.emp_applicant = obj
            employee.emp_position = ""
            employee.emp_salary = 0
            employee.save()
            return HttpResponseRedirect(reverse("admin:hr_employee_change", args=[employee.id]))
        return HttpResponseRedirect(reverse("hr:applicant", args=[obj.id]))


class JobOfferAdmin(admin.ModelAdmin):
    list_display = ('job_name', 'job_open_from', 'job_open_to')

    def response_add(self, request, obj, post_url_continue=None):
        """This makes the response after adding go to another apps changelist for some model"""
        return HttpResponseRedirect(reverse("hr:job", args=[obj.id]))


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_applicant', 'emp_salary', 'emp_position')

    def response_change(self, request, obj):
        dt_now = timezone.now()
        day = 1
        if dt_now.month == 12:
            month = 1
            year = dt_now.year + 1
        else:
            month = dt_now.month + 1
            year = dt_now.year

        employees = SalaryHistory.objects.filter(shi_employee__id=obj.id, shi_month=datetime(year, month, day))

        if employees.count() == 1:
            history = employees[0]
            history.shi_salary = obj.emp_salary
            history.save()
        else:
            salary_history = SalaryHistory()
            salary_history.shi_employee = obj
            salary_history.shi_salary = obj.emp_salary

            salary_history.shi_month = datetime(year, month, day)
            salary_history.save()
        return HttpResponseRedirect(reverse("hr:employee", args=[obj.id]))

    def response_add(self, request, obj, post_url_continue=None):
        """This makes the response after adding go to another apps changelist for some model"""
        return HttpResponseRedirect(reverse("hr:employee", args=[obj.id]))


class RecruitmentAdmin(admin.ModelAdmin):
    list_display = ('stat_name', 'stat_order')


class SalaryHistoryAdmin(admin.ModelAdmin):
    list_display = ('shi_employee', 'shi_salary', 'shi_month')


admin.site.register(JobApplicant, JobApplicantAdmin)
admin.site.register(JobOffer, JobOfferAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(RecruitmentStatus, RecruitmentAdmin)
admin.site.register(SalaryHistory, SalaryHistoryAdmin)