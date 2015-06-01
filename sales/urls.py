from django.conf.urls import url
from . import views
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^clients/$', views.clients, name='clients'),
    url(r'^products/$', views.products, name='products'),
    url(r'^specifics/(?P<product_id>[0-9]+)/$', views.detail, name='product_detail'),
    url(r'^logout/$', views.logout_view, name='logout')


    # url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^specifics/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='product_detail'),
]
