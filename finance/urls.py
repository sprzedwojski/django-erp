from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^results/$', views.results, name='results'),
    # url(r'^outcome/$', views.outcome, name='outcome'),
    # url(r'^logout/$', views.logout_view, name='logout')
]
