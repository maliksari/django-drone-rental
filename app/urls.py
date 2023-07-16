from django.urls import path
from rest_framework import routers

from .views import register, category, product, brand,test


router = routers.DefaultRouter()

router.register(r'category', category.CategoryView, basename='category')
router.register(r'brand', brand.BrandView, basename='brand')
router.register(r'product/model', brand.ProductModelView,
                basename='product_model')

urlpatterns = [
    path('register/', register.CreateUserView.as_view(),
         name="register"),

    path('products/', product.ProductView.as_view(),
         name='product'),
    path('products/<int:pk>/', product.ProductDetailView.as_view(),
         name='product-detail'),

    path('products/list', product.ProductListView.as_view(),
         name='product-list'),
    path('test/rental', test.RentalCreateView.as_view(),
         name='rental-list'),



]

urlpatterns += router.urls
