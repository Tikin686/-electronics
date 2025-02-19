from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """
    API view для создания нового пользователя.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """
        Создаем нового пользователя с активным статусом и хешем пароля.
        """
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()