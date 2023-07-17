from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from app.models import BaseModel, Product


class RentalPeriodChoices(models.TextChoices):
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'
    YEARLY = 'yearly'


class RentalPeriod(BaseModel):
    rental_type = models.CharField(
        max_length=100, choices=RentalPeriodChoices.choices)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.get_rental_type_display()


class Rental(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    renter = models.ForeignKey(User, on_delete=models.CASCADE)
    rental_period = models.ForeignKey(RentalPeriod, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Renter: {self.renter.username} - Product: {self.product.name}"

    def approve_rental(self):
        """ Müşteri tarfındaki onay """
        if self.is_completed:
            raise ValidationError('İşlem daha önce onaylandı')
        self.is_completed = True
        self.save()

    def approved(self):
        """Kiralık talebini onayla"""
        if self.is_approved:
            raise ValidationError('İşlem daha önce onaylandı')
