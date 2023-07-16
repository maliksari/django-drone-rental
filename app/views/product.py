from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser


from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from app.models import Product
from .pagination import ProductPagination


from app.models import Product
from app.serializers.product import ProductCreateSerializer, ProductSerializer, ProductListSerializer


class ProductView(APIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # parser_classes = (FormParser, MultiPartParser)

    # @swagger_auto_schema(operation_description="Product list", tags=['Product'])
    # def get(self, request):
    #     queryset = Product.objects.filter(is_active=True)
    #     serializer = ProductSerializer(queryset, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_description="Product create", request_body=ProductCreateSerializer, tags=['Product'])
    def post(self, request):
        serializer = ProductCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({
                "data": serializer.data
            })
        else:
            return Response({
                "errors": serializer.errors
            })


class ProductDetailView(APIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # parser_classes = (FormParser, MultiPartParser)

    @swagger_auto_schema(operation_description="Product detail", tags=['Product'])
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(operation_description="Product delete", tags=['Product'])
    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return Response({"message": "Success"}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(operation_description="Product update", request_body=ProductSerializer, tags=['Product'])
    def put(self, request, pk):
        product = get_object_or_404(Product.objects.all(), pk=pk)
        data = request.data
        serializer = ProductSerializer(
            instance=product, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"message": "Product updated successfully"}, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_description="Product patch", request_body=ProductSerializer, tags=['Product'])
    def patch(self, request, pk):
        product = get_object_or_404(Product.objects.all(), pk=pk)
        data = request.data
        serializer = ProductSerializer(
            instance=product, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"message": "Product updated successfully"}, status=status.HTTP_200_OK)


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'categories__category_code': ['exact'],
        'brand__name': ['exact'],
        'model__name': ['exact'],
        'rental_periods__price': ['exact'],
    }
