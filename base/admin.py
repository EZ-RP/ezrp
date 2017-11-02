from django.contrib import admin
from django.contrib.admin import widgets
from django.apps import apps
from base import models
from human_resources import models
from order import models
from party import models
from product import models
from stock import models



for model in apps.get_app_config('base').models.values():
    admin.site.register(model)

