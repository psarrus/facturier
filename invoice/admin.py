from django.contrib import admin
from models import Invoice, InvoiceLine

# Register your models here.

class InvoiceInlineAdmin(admin.TabularInline):
    model = InvoiceLine
    extra = 1

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ["ref","creation_date", "client","payement_date"]
    inlines = [InvoiceInlineAdmin]

class InvoiceLineAdmin(admin.ModelAdmin):
    list_display = ["invoice","product","quantity", "unit_price"]


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceLine, InvoiceLineAdmin)
