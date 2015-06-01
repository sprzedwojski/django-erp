__author__ = 'tomasz'

from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from hr.models import JobApplicant, JobOffer, Employee
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, "hr/index.html")


@login_required
def jobs(request):
    job_list = JobOffer.objects.order_by('job_name', '-job_open_from', '-job_open_to')
    context = {'job_list': job_list}
    return render(request, "hr/job_list.html", context)


@login_required
def job(request, job_id):
    selected_job = get_object_or_404(JobOffer, pk=job_id)
    applicant_list = JobApplicant.objects.filter(appl_job=job_id)
    context = {'job': selected_job, 'applicants': applicant_list}
    return render(request, "hr/job.html", context)


@login_required
def applicants(request):
    applicant_list = JobApplicant.objects.order_by('-appl_submitted')
    context = {'applicant_list': applicant_list}
    return render(request, "hr/applicants.html", context)


@login_required
def applicant(request, app_id):
    selected_applicant = get_object_or_404(JobApplicant, pk=app_id)
    context = {'applicant': selected_applicant}
    return render(request, "hr/applicant.html", context)


@login_required
def employees(request):
    employee_list = Employee.objects.order_by('-emp_salary')
    context = {'employee_list': employee_list}
    return render(request, "hr/employees.html", context)


@login_required
def employee(request, emp_id):
    selected_employee = get_object_or_404(Employee, pk=emp_id)
    context = {'employee': selected_employee}
    return render(request, "hr/employee.html", context)


@login_required
def logout_user(request):
    logout(request)
    return render(request, "hr/logout.html")

