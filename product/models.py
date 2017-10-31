from django.db import models


"""Naming conventions:
    - Class names                           = CamelCase
    - Function or model field names         = lowercase_underscore"""


class Item(models.Model):
    FULFILMENT_TYPE = (
        ('P', 'Purchase'),
        ('M', 'Production')
    )
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    item_desc = models.CharField(verbose_name="Description", max_length=120)
    units = models.CharField(max_length=30)
    product_category = models.CharField(max_length=30)
    fulfilment_type = models.CharField(max_length=1, choices=FULFILMENT_TYPE)

    def __str__(self):
        return '%s %s' % (self.name, self.product_category)



