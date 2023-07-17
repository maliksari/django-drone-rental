from django_filters import rest_framework as filters

from app.models import Rental


class RentalFilter(filters.FilterSet):
    start_date = filters.DateTimeFilter(
        field_name='start_date', lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name='end_date', lookup_expr='lte')
    product_code = filters.CharFilter(field_name='product__product_code')
    username = filters.CharFilter(field_name='renter__username')

    class Meta:
        model = Rental
        fields = ['start_date', 'end_date', 'product_code', 'username']
