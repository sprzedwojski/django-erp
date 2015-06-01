from django.contrib import admin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import Client, Product

# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    def response_add(self, request, obj, post_url_continue=None):
        """This makes the response after adding go to another apps changelist for some model"""
        return HttpResponseRedirect(reverse("sales:clients"))

    def response_change(self, request, obj):
        return HttpResponseRedirect(reverse("sales:clients"))

    def response_delete(self, request, obj_display, obj_id):
        return HttpResponseRedirect(reverse("sales:clients"))


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'client', 'price', 'delivery_date')

    def response_add(self, request, obj, post_url_continue=None):
        """This makes the response after adding go to another apps changelist for some model"""
        return HttpResponseRedirect(reverse("sales:products"))

    def response_change(self, request, obj):
        return HttpResponseRedirect(reverse("sales:product_detail", args=[obj.id]))

    def response_delete(self, request, obj_display, obj_id):
        return HttpResponseRedirect(reverse("sales:products"))

admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)