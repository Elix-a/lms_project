from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from .filters import PaymentFilter
from .models import User, Payment
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    UserSerializer,
    UserPublicSerializer,
    PaymentSerializer,
    UserRegistrationSerializer
)


class UserRegistrationAPIView(generics.CreateAPIView):
    """
    Регистрация нового пользователя.
    Доступна без токена (AllowAny), так как пользователь еще не авторизован.
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


class UserViewSet(viewsets.ModelViewSet):
    """
    CRUD для пользователей (дополнительное задание).
    - Просматривать можно любой профиль (только авторизованным).
    - Редактировать можно только свой профиль (через IsOwnerOrReadOnly).
    - Свои платежи видны, чужие — скрыты (через get_serializer_class).
    """
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        """Динамический выбор сериализатора в зависимости от того, чей профиль запрашивают."""
        if self.action in ['retrieve', 'update', 'partial_update']:
            # Получаем объект пользователя, к которому идет запрос
            obj = self.get_object()
            # Если пользователь смотрит/редактирует СВОЙ профиль — показываем платежи
            if obj == self.request.user:
                return UserSerializer
            # Если ЧУЖОЙ профиль — скрываем платежи
            return UserPublicSerializer

        # Для списка (list) и других действий используем полный сериализатор
        return UserSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    """
    CRUD для платежей с фильтрацией и сортировкой (Задание 4 из прошлой ДЗ).
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PaymentFilter