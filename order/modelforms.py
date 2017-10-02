from django.forms import ModelForm
from order.models import Order


# Create the form class.
class OrderForm(ModelForm):
     class Meta:
         model = Order
         fields = ['order_number', 'account_number', 'address', 'order_status']


# Creating a form to add an article.
form = OrderForm()

# Creating a form to change an existing article.
article = Order.objects.get(pk=1)
form = OrderForm(instance=article)
