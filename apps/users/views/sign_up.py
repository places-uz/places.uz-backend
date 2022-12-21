from django.db import transaction
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.serializers.sign_up import SignUpSerializer


class SignUpView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SignUpSerializer

    @transaction.atomic
    def perform_create(self, serializer):
        serializer.save()
