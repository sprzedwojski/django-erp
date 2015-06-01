from django.conf.urls import patterns, include, url
from django.contrib import admin
from login import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ERPProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.get_user),
    url(r'^login', views.get_user),
    # url(r'^login/error', views.login_error)
)
