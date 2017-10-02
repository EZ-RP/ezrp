from django import forms
from order.models import Order


# Create the form class.
class OrderForm(forms.ModelForm):
     class Meta:
         model = Order
         fields = ('order_number', 'account_number', 'address', 'order_status', 'delivery_date')


