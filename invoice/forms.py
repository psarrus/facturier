from django.forms import ModelForm, modelform_factory
from django.forms.models import inlineformset_factory

from models import Invoice, InvoiceLine


# class InvoiceForm(ModelForm):
#     class Meta:
#         model = Invoice
#         fields = '__all__'

InvoiceLineFormSet = inlineformset_factory(Invoice,InvoiceLine,
                                            fields='__all__',
                                            extra=0,
                                            min_num=1,
                                            can_delete=True)
