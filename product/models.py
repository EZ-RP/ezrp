from django.db import models


"""Naming conventions:
    - Class names                           = CamelCase
    - Function or model field names         = lowercase_underscore"""


class Item(models.Model):
    FULFILMENT_TYPE = (
        ('P', 'Purchase'),
        ('M', 'Production')
    )
    item_number = models.IntegerField()
    name = models.CharField(max_length=30, help_text= "The name of the desired product")
    item_desc = models.CharField(verbose_name="Description", max_length=120, help_text="The description of the product")
    unit = models.CharField(max_length=10, help_text="The unit of measurement for the product")
    product_category = models.CharField(max_length=30, help_text="The category of the product")
    fulfilment_type = models.CharField(max_length=1, choices=FULFILMENT_TYPE, help_text="Whether the product is produced or purchased")

    class Meta:
        managed = True
        db_table = 'product_item'

    def __str__(self):
        return '%s %s' % (self.name, self.product_category)

    def get_next_id(self):
        last_item = Item.objects.all().order_by('-item_number').first()
        if last_item != None:
            return last_item.id + 1
        else:
            return 1
