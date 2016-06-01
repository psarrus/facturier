from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):

    code_vat_choices  = (
    (0,'0%'),
    (0.055, '5.5%'),
    (0.1, '10%'),
    (0.2, '20%'),
    )

    ref = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    unit_price = models.FloatField()
    vat = models.FloatField(choices=code_vat_choices,)

    def __unicode__(self):
        return "%s" % self.name
