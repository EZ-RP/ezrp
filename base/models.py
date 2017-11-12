from django.db import models


"""Naming conventions:
    - Class names                           = CamelCase
    - Function or model field names         = lowercase_underscore"""


class Address(models.Model):
    street = models.CharField(max_length=150, help_text="A Street Address.")
    suburb = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=50, default="Australia")

    def __str__(self):
        return '%s %s %s %s' % (self.street, self.suburb, self.state, self.postcode)


class PayDetails(models.Model):
    account_number = models.CharField(max_length=10)
    bsb_number = models.CharField(max_length=10)
    account_name = models.CharField(max_length=20)


# DS: SystemParameters Table
class SystemParameters (models.Model):
    description = models.CharField(max_length=200)
    str_value = models.CharField(max_length=150)


