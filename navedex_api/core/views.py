# Importações DRF
from rest_framework import viewsets
from rest_framework import permissions

# Importações da app
from navedex_api.core.models import  Naver, Project
from navedex_api.core.serializers import NaverSerializer, ProjectSerializer


class NaverViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os Navers sejam visualizados, criados,
    editados e excluídos.
    """
    queryset = Naver.objects.all()
    serializer_class = NaverSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ('__all__')

    def perform_create(self, serializer):
        """
        Função do endpoint da API que configura o usuário autenticado como
        criador do objeto
        """
        serializer.save(created_by=self.request.user)
    
    def get_queryset(self):
        """
        Função do endpoint da API que configura as buscas para somente os
        objetos criados pelo usuário autenticado
        """
        return Naver.objects.filter(created_by=self.request.user)


class ProjectViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os Projetos sejam visualizados ou editados.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ('__all__')

    def perform_create(self, serializer):
        """
        Função do endpoint da API que configura o usuário autenticado como
        criador do objeto
        """
        serializer.save(created_by=self.request.user)
    
    def get_queryset(self):
        """
        Função do endpoint da API que configura as buscas para somente os
        objetos criados pelo usuário autenticado
        """
        return Project.objects.filter(created_by=self.request.user)