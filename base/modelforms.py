from django import forms
from base.models import Address, PayDetails, SystemParameters


# Create the form class.
class AddressForm(forms.ModelForm):
     class Meta:
         model = Address
         fields = ('street', 'suburb', 'state', 'postcode', 'country')


class PayDetailsForm(forms.ModelForm):
    class Meta:
        model = PayDetails
        fields = ('account_name', 'bsb_number', 'account_number')


class SysParamForm(forms.ModelForm):
     class Meta:
         model = SystemParameters
         fields = ('description', 'str_value')

