from django.db import models


class Address(models.Model):

    street = models.CharField(max_length=150)
    suburb = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
