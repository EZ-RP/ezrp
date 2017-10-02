from django import forms

from .models import Inventory


class InvForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ('available_qty', 'reserved_qty', 'ordered_qty',)