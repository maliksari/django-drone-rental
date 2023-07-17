import logging

from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, FormParser


from app.models import Category
from app.serializers.category import CategorySerializer
from app.views.base import Auth 


logger = logging.getLogger(__name__)


class CategoryView(Auth,ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    parser_classes = (FormParser, MultiPartParser)
   

    @swagger_auto_schema(operation_description="Category list", tags=['Category'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Category cerate", request_body=CategorySerializer, tags=['Category'])
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
       

    @swagger_auto_schema(operation_description="Category delete", tags=['Category'])
    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return response

    @swagger_auto_schema(operation_description="Category patch", tags=['Category'])
    def partial_update(self, request, *args, **kwargs):
        category = Category.objects.get(id=kwargs.get('pk'))
        category.modified_by=request.user
        category.save()
        response = super().partial_update(request, *args, **kwargs)
        return response

    @swagger_auto_schema(operation_description="Category get", tags=['Category'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Category put", tags=['Category'])
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        category_instance = Category.objects.get(id=response.data.get('id'))
        category_instance.modified_by=request.user
        category_instance.save()
        return response
