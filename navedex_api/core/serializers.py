# Importações DRF
from rest_framework import serializers

# Importações da app
from navedex_api.core.models import Naver, Project

class NaverListSerializer(serializers.ModelSerializer):
    """
    Serializer de listargem de Navers (usado apenas para listar os navers nas
    requisições de projeto).
    """
    class Meta:
        """
        Meta classe do serializer
            Define o model do serializer, a ordenação da listagem dos navers
            e os campos que serão listados.
        """
        model = Naver
        ordering = ['name']
        fields = ['id', 'name', 'birthdate', 'job_role', 'admission_date',]


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer dos projetos 
    """
    navers = NaverListSerializer(many=True, read_only=True)

    class Meta:
        """
        Meta classe do serializer
            Define o model do serializer, a ordenação da listagem dos projetos,
            os campos que serão requeridos e listados, e argumentos não
            nomeados.
        """
        ordering = ['name']
        model = Project
        fields = ['id', 'name', 'navers']
        extra_kwargs = {'navers': {'required': False}}
    
    def create(self, validated_data):
        """
        Função de criação do projeto
        """
        request = self.context.get('request')
        navers_data =  request.data.get('navers', [])
        navers = Naver.objects.filter(id__in=navers_data)
        project = Project.objects.create(**validated_data)

        for naver in navers:
            project.navers.add(naver)

        return project

    def update(self, instance, validated_data):
        """
        Função de atualização do projeto
        """
        request = self.context.get('request')
        instance.name = request.data.get('name', '')
        navers_data =  request.data.get('navers', [])
        navers = Naver.objects.filter(id__in=navers_data)
        instance.navers.clear()

        for naver in navers:
            instance.navers.add(naver)

        return instance


class ProjectListSerializer(serializers.ModelSerializer):
    """
    Serializer de listargem de Projeto (usado apenas para listar os projeto nas
        requisições de navers)
    """

    class Meta:
        """
        Meta classe do serializer
            Define o model do serializer, a ordenação da listagem dos proetos e
            os campos que serão listados
        """
        ordering = ['name']
        model = Project
        fields = ['id', 'name',]


class NaverSerializer(serializers.ModelSerializer):
    """
    Serializer dos navers 
    """
    projects = ProjectListSerializer(many=True, read_only=True)

    class Meta:
        """
        Meta classe do serializer
            Define o model do serializer, a ordenação da listagem dos navers,
            os campos que serão requeridos e listados, e argumentos não
            nomeados.
        """
        ordering = ['name']
        model = Naver
        fields = ['id', 'name', 'birthdate', 'job_role', 'admission_date',
            'projects',]

    def create(self, validated_data):
        """
        Função de criação do naver
        """
        request = self.context.get('request')
        projects_data =  request.data.get('projects', [])
        projects = Project.objects.filter(id__in=projects_data)
        naver = Naver.objects.create(**validated_data)

        for project in projects:
            project.navers.add(naver)

        return naver

    def update(self, instance, validated_data):
        """
        Função de atualização do naver
        """
        request = self.context.get('request')
        instance.name = request.data.get('name', '')
        instance.birthdate = request.data.get('birthdate', '')
        instance.job_role = request.data.get('job_role', '')
        instance.admission_date = request.data.get('admission_date', '')
        projects_data =  request.data.get('projects', [])
        new_projects = Project.objects.filter(id__in=projects_data)
        old_projects = Project.objects.filter(navers=instance)

        for project in old_projects:
            project.navers.remove(instance)

        for project in new_projects:
            project.navers.add(instance)

        return instance