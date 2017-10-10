from django.contrib import admin
from django.db import models
from django.contrib.admin import widgets


# Register your models here.
class StopAdmin(admin.ModelAdmin):
    formfield_overrides = {
       models.DateField: {'widget': widgets.AdminDateWidget}
    }

