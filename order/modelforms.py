from django import forms
from order.models import Order
from order.models import OrderLine
from order.models import Discounts
from party.models import *


class DateTimeInput(forms.SelectDateWidget):
    input_type = 'datetime'


# Create the form class.
class OrderForm(forms.ModelForm):

    class Meta:

        model = Order

        fields = ('account_number', 'address', 'delivery_date', 'order_status')  # 'order_number', 'order_status'
        widgets = {
            'delivery_date': forms.SelectDateWidget()
        }


class LineForm(forms.ModelForm):

    class Meta:
        model = OrderLine
        fields = ('item_id', 'quantity', 'price')  # , 'discount_price'


class DiscountForm(forms.ModelForm):

    class Meta:
        model = Discounts
        fields = ('account_number', 'product_category', 'item_id', 'quantity', 'start_date', 'end_date', 'value')
        widgets = {
            'start_date': forms.SelectDateWidget(),
            'end_date': forms.SelectDateWidget(),
        }

