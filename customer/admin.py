from django.contrib import admin
from models import Client, Address, ClientAddress

# Register your models here.

class ClientAddressAdmin(admin.ModelAdmin):
    list_display = ["client","address", "type"]

class ClientAddressInlineAdmin(admin.TabularInline):
    model = ClientAddress
    extra = 1

class ClientAdmin(admin.ModelAdmin):
    inlines = [ClientAddressInlineAdmin]

admin.site.register(Client, ClientAdmin)
admin.site.register(Address)
admin.site.register(ClientAddress, ClientAddressAdmin)
