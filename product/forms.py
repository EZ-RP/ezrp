from django import forms
from product.models import Item


class ProductForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('item_id', 'item_desc', 'units', 'product_category')

