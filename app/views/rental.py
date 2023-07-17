from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.views import APIView

from app.models import Rental
from app.serializers.rental import RentalSerializer,RentalListSerializer
from .pagination import RentalPaging
from .filter import RentalFilter


class RentalView(APIView):
    serializer = RentalSerializer

    @swagger_auto_schema(operation_description="Kiralama İşlemleri", request_body=RentalSerializer, tags=['Rental'])
    def post(self, request):
        serializer = RentalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        product = data.get('product', None)
        start_date = data.get('start_date', None)
        end_date = data.get('end_date', None)
        renter = request.user

        if start_date >= end_date:
            return Response({"message": "'Başlangıç tarihi bitiş tarihine büyük veya eşit olamaz !!!'"}, status=status.HTTP_400_BAD_REQUEST)

        # İHA bu tarihler arasında kiralikmı
        rental_exists = Rental.objects.filter(
            product_id=product,
            start_date__lte=start_date,
            end_date__gte=end_date,
            is_completed=True,
            is_approved=True
        ).exists()

        if rental_exists:
            return Response({"message": "Seçili İHA bu tarihler arasında kiralik başka bir tarih aralğı seçiniz"}, status=status.HTTP_409_CONFLICT)
        if serializer.is_valid():
            serializer.save(created_by=renter, renter=renter)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class RentalListView(generics.ListAPIView):
#     queryset = Rental.objects.all()
#     serializer_class = RentalListSerializer
#     filterset_class = RentalFilter
#     pagination_class = RentalPaging 

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class RentalListView(generics.ListAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalListSerializer
    filterset_class = RentalFilter
    pagination_class = RentalPaging 

    def get_queryset(self):
        queryset = Rental.objects.all()
        filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return filterset.qs

    @swagger_auto_schema(operation_description="Kiralama taleplerini listler",tags=['Rental'],
        manual_parameters=[
            openapi.Parameter('start_date', openapi.IN_QUERY, description='Start date filter', type=openapi.TYPE_STRING),
            openapi.Parameter('end_date', openapi.IN_QUERY, description='End date filter', type=openapi.TYPE_STRING),
            openapi.Parameter('product_code', openapi.IN_QUERY, description='Product code filter', type=openapi.TYPE_STRING),
            openapi.Parameter('username', openapi.IN_QUERY, description='Username filter', type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)