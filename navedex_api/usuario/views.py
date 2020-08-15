# Importações DRF
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

# Importações da app
from navedex_api.usuario.serializers import CreateUserSerializer
from navedex_api.usuario.models import User

class CreateUserView(generics.CreateAPIView):
    """
    Endpoint da API que permite que os Usuários sejam visualizados, criados,
    editados e excluídos.
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)