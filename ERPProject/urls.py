from django.conf.urls import patterns, include, url
from django.contrib import admin
from login import views, urls

urlpatterns = patterns('',
    url(r'^admin/login/', views.get_user),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.get_user),
    url(r'^login/', views.get_user),
    url(r'^sales/', include('sales.urls', namespace="sales")),
    url(r'^hr/', include('hr.urls', namespace="hr")),
    url(r'^finance/', include('finance.urls', namespace="finance")),
)
