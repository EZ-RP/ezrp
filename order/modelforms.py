from django import forms
from order.models import Order
from order.models import OrderLine
from order.models import Discounts


# Create the form class.
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('order_number', 'account_number', 'address', 'order_status', 'delivery_date')


class LineForm(forms.ModelForm):
    class Meta:
        model = OrderLine
        fields = ('item_id', 'quantity', 'price')  # , 'discount_price'


class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discounts
        fields = ('account_number', 'product_category', 'item_id', 'quantity', 'start_date', 'end_date', 'value')


