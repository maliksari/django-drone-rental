import logging
from rest_framework.viewsets import ModelViewSet



from app.models import Brand,ProductModel
from app.serializers.brand import BrandSerializer, ProductModelSerializer
from app.views.base import Auth 


# Get an instance of a logger
logger = logging.getLogger(__name__)


class BrandView(Auth,ModelViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
  


class ProductModelView(Auth,ModelViewSet):
    serializer_class = ProductModelSerializer
    queryset = ProductModel.objects.all()
   

