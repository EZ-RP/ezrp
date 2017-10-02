from django import forms
from party.models import *

class PartyForm(forms.ModelForm):


    class Meta:
        model = Party
        fields = ('party_name', 'account_number', 'business_number')

