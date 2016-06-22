from django.forms import ModelForm, modelform_factory, TextInput, Select
from django.forms.models import inlineformset_factory

from models import Address, Client

# Create the form class.
class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['last_name','first_name','email','mobile','web']
        widgets = {
            'last_name' : TextInput(attrs={'placeholder':'Nom','size':100}),
            'first_name' : TextInput(attrs={'placeholder':'Prenom','size':100}),
            'email' : TextInput(attrs={'placeholder':'Email','size':100}),
            'mobile' : TextInput(attrs={'placeholder':'mobile','size':100}),
            'web' : TextInput(attrs={'placeholder':'web','size':100}),
        }

AddressLineFormSet = inlineformset_factory(Client, Address,
                            fields = '__all__',
                            widgets = {
                                'type': Select(attrs={'placeholder':'Type'}),
                                'street' : TextInput(attrs={'placeholder':'Street','size':35}),
                                'zipcode' : TextInput(attrs={'placeholder':'Code Postal','size':35}),
                                'city' : TextInput(attrs={'placeholder':'Ville','size':35}),
                                'tel' : TextInput(attrs={'placeholder':'Tel','size':35}),
                                'fax' : TextInput(attrs={'placeholder':'Fax','size':35}),
                            },
                            extra=0,
                            min_num=1,
                            can_delete=True)
