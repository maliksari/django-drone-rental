from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404



from app.models import RentalPeriod
from app.serializers.rental import RentalPeriodSerializer


class RentaPeriodView(APIView):
    queryset = RentalPeriod.objects.all()
    serializer_class = RentalPeriodSerializer

    @swagger_auto_schema(operation_description="Rental list", tags=['RentalPeriod'])
    def get(self, request):
        queryset = RentalPeriod.objects.filter(is_active=True)
        serializer = RentalPeriodSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_description="RentalPeriod create", request_body=RentalPeriodSerializer, tags=['RentalPeriod'])
    def post(self, request):
        serializer = RentalPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data": serializer.data
            })
        else:
            return Response({
                "errors": serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)


# class RentalPeriodDetailView(APIView):
#     queryset = RentalPeriod.objects.all()
#     serializer_class = RentalPeriodSerializer

#     @swagger_auto_schema(operation_description="RentalPeriod detail", tags=['RentalPeriod'])
#     def get(self, request, pk):
#         try:
#             product = RentalPeriod.objects.get(pk=pk)
#             serializer = RentalPeriodSerializer(product)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except RentalPeriod.DoesNotExist:
#             return Response({"message": "RentalPeriod not found"}, status=status.HTTP_404_NOT_FOUND)

#     @swagger_auto_schema(operation_description="RentalPeriod delete", tags=['RentalPeriod'])
#     def delete(self, request, pk):
#         try:
#             product = RentalPeriod.objects.get(pk=pk)
#             product.delete()
#             return Response({"message": "Success"}, status=status.HTTP_200_OK)
#         except RentalPeriod.DoesNotExist:
#             return Response({"message": "RentalPeriod not found"}, status=status.HTTP_404_NOT_FOUND)

#     @swagger_auto_schema(operation_description="RentalPeriod update", request_body=RentalPeriodSerializer, tags=['RentalPeriod'])
#     def put(self, request, pk):
#         rental = get_object_or_404(RentalPeriod.objects.all(), pk=pk)
#         data = request.data
#         serializer = RentalPeriodSerializer(
#             instance=rental, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#         return Response({"message": "RentalPeriod updated successfully"}, status=status.HTTP_200_OK)

#     @swagger_auto_schema(operation_description="RentalPeriod patch", request_body=RentalPeriodSerializer, tags=['RentalPeriod'])
#     def patch(self, request, pk):
#         rental = get_object_or_404(RentalPeriod.objects.all(), pk=pk)
#         data = request.data
#         serializer = RentalPeriodSerializer(
#             instance=rental, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#         return Response({"message": "RentalPeriod updated successfully"}, status=status.HTTP_200_OK)
