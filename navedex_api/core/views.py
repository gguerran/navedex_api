# DRF imports
from rest_framework import viewsets
from rest_framework import permissions

# App imports
from navedex_api.core.models import  Naver, Project
from navedex_api.core.serializers import NaverSerializer, ProjectSerializer


class NaverViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Navers to be viewed, created, edited and deleted.
    """
    queryset = Naver.objects.all()
    serializer_class = NaverSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ('__all__')

    def perform_create(self, serializer):
        """
        API endpoint function that configures the authenticated user as the
        creator of the object
        """
        serializer.save(created_by=self.request.user)
    
    def get_queryset(self):
        """
        API endpoint function that sets up searches for only objects created by
        the authenticated user
        """
        return Naver.objects.filter(created_by=self.request.user)


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Projects to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ('__all__')

    def perform_create(self, serializer):
        """
        API endpoint function that configures the authenticated user as the
        creator of the object.
        """
        serializer.save(created_by=self.request.user)
    
    def get_queryset(self):
        """
        API endpoint function that sets up searches for only objects created by
        the authenticated user
        """
        return Project.objects.filter(created_by=self.request.user)