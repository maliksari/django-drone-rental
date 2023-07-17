from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# rest
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from django.contrib import admin

schema_view = get_schema_view(
    openapi.Info(
        title="Django ile İHA Kiralama Projesi",
        default_version='v0.0.1',
        description="API Dökümantasyonu",
        terms_of_service="",
        contact=openapi.Contact(email="malik.sari06@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('api/', include('app.urls')),
    path('', include('pages.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
