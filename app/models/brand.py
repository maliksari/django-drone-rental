from django.db import models

from .base import BaseModel


class Brand(BaseModel):
    name = models.CharField(max_length=150, blank=True, null=True)
    description = models.CharField(max_length=250, blank=False, null=False)

    class Meta:
        db_table = 'brand_products'

    def __str__(self):
        return self.name


class ProductModel(BaseModel):
    name = models.CharField(max_length=150, blank=True, null=True)
    description = models.CharField(max_length=250, blank=False, null=False)

    class Meta:
        db_table = 'product_models'

    def __str__(self):
        return self.name
