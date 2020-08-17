# DRF imports
from rest_framework import serializers

# App imports
from navedex_api.core.models import Naver, Project

class NaverListSerializer(serializers.ModelSerializer):
    """
    Browser listing serializer (used only to list the browsers in the
    project requirements).
    """
    class Meta:
        """
        Serializer meta class
            Defines the model of the serializer, the ordering of the list of
            browsers and the fields to be listed.
        """
        model = Naver
        ordering = ['name']
        fields = ['id', 'name', 'birthdate', 'job_role', 'admission_date',]


class ProjectSerializer(serializers.ModelSerializer):
    """
    Projects serializers
    """
    navers = NaverListSerializer(many=True, read_only=True)

    class Meta:
        """
        Serializer meta class
            Defines the model of the serializer, the ordering of the list of 
            projects, the fields that will be required and listed, and unnamed
            arguments.
        """
        ordering = ['name']
        model = Project
        fields = ['id', 'name', 'navers']
        extra_kwargs = {'navers': {'required': False}}
    
    def create(self, validated_data):
        """
        Project creation function
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
        Project update function
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
    Project listing serializer (used only to list projects in browser requests)
    """

    class Meta:
        """
        Serializer meta class
            Defines the model of the serializer, the ordering of the list of
            projects and the fields to be listed
        """
        ordering = ['name']
        model = Project
        fields = ['id', 'name',]


class NaverSerializer(serializers.ModelSerializer):
    """
    Navers serializer
    """
    projects = ProjectListSerializer(many=True, read_only=True)

    class Meta:
        """
        Serializer meta class
            Defines the model of the serializer, the ordering of the list of
            browsers, the fields that will be required and listed, and unnamed
            arguments.
        """
        ordering = ['name']
        model = Naver
        fields = ['id', 'name', 'birthdate', 'job_role', 'admission_date',
            'projects',]

    def create(self, validated_data):
        """
        Naver create function
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
        Naver update function
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