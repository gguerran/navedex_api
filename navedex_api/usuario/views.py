# DRF imports
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

# App imports
from navedex_api.usuario.serializers import CreateUserSerializer
from navedex_api.usuario.models import User

class CreateUserView(generics.CreateAPIView):
    """
    API endpoint that allows Users to be viewed, created, edited and deleted.
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)