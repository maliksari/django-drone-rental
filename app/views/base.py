from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class Auth(object):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)
