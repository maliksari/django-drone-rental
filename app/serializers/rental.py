from rest_framework import serializers

from app.models import RentalPeriod


class RentalPeriodSerializer(serializers.Serializer):
    rental_type= serializers.CharField()
    price = serializers.CharField()

    # class Meta:
    #     model = RentalPeriod
    #     fields = ('id', 'rental_type', 'price', 'product')
