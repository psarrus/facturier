from __future__ import unicode_literals

from django.db import models
from customer.models import Client
from catalog.models import Product

# Create your models here.
class Invoice(models.Model):
    ref = models.IntegerField()
    creation_date = models.DateField()
    client = models.ForeignKey(Client)
    payement_date = models.DateField(null=True,blank=True)

    def get_total(self):
        total = 0
        for line in self.invoiceline_set.all():
            total += line.get_total()
        return total

    def get_ht(self):
        ht = 0
        for line in self.invoiceline_set.all():
            ht += line.get_ht()
        return ht

    def get_tva(self):
        tva1 = tva2 = tva3 = 0
        for line in self.invoiceline_set.all():
            if line.product.vat == 0.055:
                tva1 += line.get_tva()
            elif line.product.vat ==    0.1:
                tva2 += line.get_tva()
            else:
                tva3 += line.get_tva()
        return (tva1, tva2, tva3)


    def __unicode__(self):
        return "%s %s %s %s" % (self.ref,self.creation_date,self.client.first_name,self.client.last_name)

class InvoiceLine(models.Model):
    invoice = models.ForeignKey(Invoice)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    unit_price = models.FloatField()

    def get_ht(self):
        return ((self.quantity * self.unit_price) / (self.product.vat+1))

    def get_tva(self):
        return ((self.quantity * self.unit_price) - ((self.quantity * self.unit_price)/(self.product.vat+1)))

    def get_total(self):
        return (self.quantity * self.unit_price)

    def __unicode__(self):
        return "%s %s %s %s" % (self.product.ref,self.product.name,self.quantity,self.unit_price)
