from django.forms import ModelForm, modelform_factory, TextInput, Select
from django.forms.models import inlineformset_factory
from models import Product

# Create the form class.
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'ref' : TextInput(attrs={'placeholder':'Reference','size':35}),
            'designation' : TextInput(attrs={'placeholder':'Designation','size':35}),
            'unit_price' : TextInput(attrs={'placeholder':'Prix Unitaire TTC','size':35}),
            'vat' : TextInput(attrs={'placeholder':'TVA','size':35}),
        }
