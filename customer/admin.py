from django.contrib import admin
from models import Client, Address

# Register your models here.
class AddressInlineAdmin(admin.TabularInline):
    model = Address
    extra = 1

class ClientAdmin(admin.ModelAdmin):
    list_display = ["last_name","first_name","email", "mobile", "web"]
    inlines = [AddressInlineAdmin]

class AddressAdmin(admin.ModelAdmin):
    list_display = ["client","type","street", "zipcode", "city", "tel", "fax",]

admin.site.register(Client, ClientAdmin)
admin.site.register(Address, AddressAdmin)
