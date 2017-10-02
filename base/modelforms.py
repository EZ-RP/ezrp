from django import forms
from base.models import Address
from base.models import SystemParameters


# Create the form class.
class AddressForm(forms.ModelForm):
     class Meta:
         model = Address
         fields = ('street', 'suburb', 'state', 'postcode', 'country')


class SysParamForm(forms.ModelForm):
     class Meta:
         model = SystemParameters
         fields = ('description', 'str_value')

