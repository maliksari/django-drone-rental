from rest_framework import serializers

from app.models import Product, Category, RentalPeriod
from app.serializers.rental import RentalPeriodSerializer


class ProductCreateSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Category.objects.all())
    rental_periods = RentalPeriodSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'brand','model','weight','product_code', 'description',
                  'categories', 'rental_periods')
        

    # @classmethod
    # def create_rental_period(cls,data):
    #     data = RentalPeriodSerializer(data=data)
    #     craate_rental_period = RentalPeriod.objects.create(**data)
    #     craate_rental_period.save()
    #     return craate_rental_period

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        rental_periods_data = validated_data.pop('rental_periods')
        product = Product.objects.create(**validated_data)

        for category in categories_data:
            product.categories.add(category)

        for rental_period_data in rental_periods_data:
            rental_period = RentalPeriod.objects.create(**rental_period_data)
            product.rental_periods.add(rental_period)
        return product

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['categories'] = instance.categories.values_list('id', flat=True)
        ret['rental_periods'] = RentalPeriodSerializer(instance.rental_periods.all(), many=True).data
        return ret


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'product_code',
                  'description')




class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'category_code']


class RentalPeriodListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalPeriod
        fields = ['id', 'rental_type', 'price']


class ProductListSerializer(serializers.ModelSerializer):
    categories = CategoryListSerializer(many=True)
    rental_periods = RentalPeriodListSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'product_code', 'description', 'categories', 'rental_periods']