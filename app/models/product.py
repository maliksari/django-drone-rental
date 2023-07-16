from django.db import models

from .base import BaseModel
from .brand import Brand, ProductModel


class Product(BaseModel):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE,related_name="brand_products")
    model = models.ForeignKey('ProductModel', on_delete=models.CASCADE,related_name="product_models")
    weight = models.IntegerField(blank=True, null=True)
    product_code = models.CharField(
        max_length=50, unique=True, db_index=True)
    categories = models.ManyToManyField(
        'Category', related_name='products_category')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="products", default='')
    rental_periods = models.ManyToManyField(
        'RentalPeriod', related_name='products_period')

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name
