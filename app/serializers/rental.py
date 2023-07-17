from rest_framework import serializers

from app.models import Rental, Product, RentalPeriod
from app.models.rental import RentalPeriodChoices


class RentalPeriodSerializer(serializers.Serializer):
    rental_type = serializers.CharField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)

    def validate_rental_type(self, value):
        value = str(value)
        if value not in dict(RentalPeriodChoices.choices).keys():
            raise serializers.ValidationError(
                {"rental_type": "Invalid rental period type."})
        return value

    def to_representation(self, instance):
        return {
            "rental_type": instance.get_rental_type_display(),
            "price": instance.price,
        }


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ('id', 'product', 'rental_period', 'start_date', 'end_date')


class RentalListPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalPeriod
        fields = ['id', 'rental_type', 'price']


class ProductRentalSerializer(serializers.ModelSerializer):
    rental_period = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'product_code', 'rental_period']

    def get_rental_period(self, obj):
        rental_period = obj.rental_periods.first()
        if rental_period:
            return RentalPeriodSerializer(rental_period).data
        return None


class RentalListSerializer(serializers.ModelSerializer):
    product = ProductRentalSerializer()
    renter_fullname = serializers.SerializerMethodField()

    class Meta:
        model = Rental
        fields = ['id', 'renter_id', 'renter_fullname',
                  'product', 'rental_period', 'start_date', 'end_date']

    def get_renter_fullname(self, obj):
        renter = obj.renter
        if renter is not None:
            full_name = renter.get_full_name()
            if full_name:
                return full_name
        return "Belirtilmemiş"
