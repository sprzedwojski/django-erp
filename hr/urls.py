from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^jobs/$', views.jobs, name='jobs'),
    url(r'^job/(?P<job_id>[0-9]+)/$', views.job, name='job'),
    url(r'^applicants/$', views.applicants, name='applicants'),
    url(r'^applicant/(?P<app_id>[0-9]+)/$', views.applicant, name='applicant'),
    url(r'^employees/$', views.employees, name='employees'),
    url(r'^employee/(?P<emp_id>[0-9]+)/$', views.employee, name='employee'),
    url(r'^logout/$', views.logout_user, name='logout')
]
