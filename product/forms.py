from django import forms
from product.models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('product_category', 'name', 'item_desc', 'unit', 'fulfilment_type')


