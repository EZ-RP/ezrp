from django import forms
from order.models import Order
from order.models import OrderLine


# Create the form class.
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('order_number', 'account_number', 'address', 'order_status', 'delivery_date')



class LineForm(forms.ModelForm):
    class Meta:
        model = OrderLine
        fields = ('item_id', 'quantity', 'price', 'discount_price')


