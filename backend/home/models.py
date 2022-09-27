from django.conf import settings
from django.db import models


class MyModel(models.Model):
    "Generated Model"
    intfield = models.BigIntegerField()
