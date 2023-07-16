from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from app.models import BaseModel, Product


class RentalPeriodChoices(models.TextChoices):
    DAILY = 'daily', 'Daily'
    WEEKLY = 'weekly', 'Weekly'
    MONTHLY = 'monthly', 'Monthly'
    YEARLY = 'yearly', 'Yearly'


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

    def __str__(self):
        return f"Renter: {self.renter.username} - Product: {self.product.name}"

    def clean(self):
        # Ürünün kiralanabilirliğini kontrol et
        if self.is_completed:
            raise ValidationError('Product is already rented.')

        # Başlangıç tarihinin bitiş tarihinden önce olduğunu kontrol et
        if self.start_date >= self.end_date:
            raise ValidationError('Start date must be before end date.')

    def save(self, *args, **kwargs):
        self.full_clean()  # Özel doğrulama kontrollerini gerçekleştir
        super().save(*args, **kwargs)

    def approve_rental(self):
        if self.is_completed:
            raise ValidationError('Rental is already completed.')
        self.is_completed = True
        self.save()
