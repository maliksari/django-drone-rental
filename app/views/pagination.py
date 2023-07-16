from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    page_size = 20


class RentalPaging(PageNumberPagination):
    page_size = 20
