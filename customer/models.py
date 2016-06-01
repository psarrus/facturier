from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models as geomodels
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    web = models.CharField(max_length=500)

    def __unicode__(self):
        return "%s %s" % (self.first_name,self.last_name)

class Address(models.Model):
    street = models.CharField(max_length=500)
    zipcode = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
    tel = models.CharField(max_length=10)
    fax = models.CharField(max_length=10)

    point = geomodels.PointField(null=True,blank=True)

    def __unicode__(self):
        return "%s %s %s" % (self.street,self.zipcode,self.city)

class ClientAddress(models.Model):

    type_address_choices = (
    ('1', 'facturation'),
    ('2', 'livraison'),
    )

    client = models.ForeignKey(Client)
    type = models.CharField(max_length=1,
                              choices=type_address_choices,)
    address = models.ForeignKey(Address)

    def __unicode__(self):
        return "%s %s %s %s %s" % (self.client.first_name,self.client.last_name,self.get_type_display(),self.address.zipcode,self.address.city)

from geopy.geocoders import Nominatim
from django.contrib.gis.geos import fromstr

@receiver(pre_save, sender=Address)
def address_geocoding(sender, instance, **kwargs):
    geolocator = Nominatim()
    location = geolocator.geocode("%s %s" % (instance.street,instance.city))
    print((location.latitude, location.longitude))
    instance.point = fromstr('POINT(%s %s)' % (location.longitude, location.latitude))
