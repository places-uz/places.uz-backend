from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from core.utils.files import delete_file
from core.utils.serializers import ValidatorSerializer
from users.models import User, Token


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')
        extra_kwargs = {'email': {'read_only': True}}


class SimpleUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')


class ChangePasswordValidator(ValidatorSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=8)

    def validate_old_password(self, password):
        if not self.context['request'].user.check_password(password):
            raise ValidationError('Incorrect old password.')
        return password


class RefreshTokenSerializer(ModelSerializer):
    access_token = serializers.CharField(max_length=100, write_only=True)

    def create(self, data):
        token = Token.objects.filter(key=data.get('access_token'))
        if not token.exists():
            raise ValidationError('Access Token is not true.')

        return Token.objects.create(user=self.context.get('user'))

    class Meta:
        model = Token
        fields = ('id', 'access_token', 'key', )
        extra_kwargs = {'key': {'read_only': True}}
