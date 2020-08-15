# Importações DRF
from rest_framework import serializers

# Importações da app
from navedex_api.usuario.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    """
    Serializer de usuário
    """
    class Meta:
        """
        Meta classe do serializer
        Define o model do serializer e os campos que serão usados.
        """
        model = User
        fields = ('email', 'password')

    def create(self, validated_data):
        """
        Função de criação do usuário
        """
        user = User(
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()

        return user