from django import forms
from product.models import *

class ProductForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('item_id','name','item_desc', 'units', 'product_category')