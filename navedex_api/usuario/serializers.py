# DRF imports
from rest_framework import serializers

# App imports
from navedex_api.usuario.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    """
    User serializer
    """
    class Meta:
        """
        Serializer meta class
        Defines the model of the serializer and the fields to be used.
        """
        model = User
        fields = ('email', 'password')

    def create(self, validated_data):
        """ User creation function. """
        user = User(
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()

        return user