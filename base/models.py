from django.db import models


class Address(models.Model):

    street = models.CharField(max_length=150)
    suburb = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=50)

class Pay_details(models.Model):
    account_number = models.CharField(max_length=10)
    bsb_number = models.CharField(max_length=10)
    account_name = models.CharField(max_length=20)



# DS: Base Attribute Type Table
class AttributeType (models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)


# DS: Base Attribute Value Table
class AttributeValue (models.Model):
    value = models.CharField(max_length=50)
    attributetype = models.ForeignKey(AttributeType)


