from django.db import models


# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.client_name


class Product(models.Model):
    client = models.ForeignKey(Client)
    product_name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    delivery_date = models.DateField('date delivered')

    def __unicode__(self):
        return self.product_name