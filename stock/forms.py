from django import forms

from .models import Inventory


class InvForm(forms.ModelForm):
    """
    denotes what is shown in the edit form for Inventory
    """
    class Meta:
        model = Inventory
        fields = ('available_qty', 'reserved_qty', 'ordered_qty',)
