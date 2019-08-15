from django.db import models


class Shoe(models.Model):
    name = models.CharField()
    brand_name = models.CharField()
    category = models.CharField()
    size = models.CharField()
    retail_price = models.DecimalField()
    regular_price = models.DecimalField()
    