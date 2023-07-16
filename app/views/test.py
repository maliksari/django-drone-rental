
from rest_framework import serializers
from rest_framework import generics
from django_filters import rest_framework as filters
from drf_yasg.utils import swagger_auto_schema

from app.models import Rental
from .pagination import RentalPaging


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ('id', 'product', 'renter','rental_period','start_date', 'end_date')



class RentalFilter(filters.FilterSet):
    start_date = filters.DateTimeFilter(field_name='start_date', lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name='end_date', lookup_expr='lte')
    product_code = filters.CharFilter(field_name='product__product_code')
    username = filters.CharFilter(field_name='renter__username')

    class Meta:
        model = Rental
        fields = ['start_date', 'end_date', 'product_code', 'username']


class RentalListView(generics.ListAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    filterset_class = RentalFilter
    pagination_class = RentalPaging 


class RentalDetailView(generics.RetrieveAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class RentalCreateView(APIView):
    serializer_class = RentalSerializer

    @swagger_auto_schema(operation_description="RentalSerializer", request_body=RentalSerializer, tags=['Rental'])
    def post(self, request, format=None):
        serializer = RentalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
