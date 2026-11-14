from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .filters import PaymentFilter
from .models import User, Payment
from .serializers import UserSerializer, PaymentSerializer


class UserViewSet(viewsets.ModelViewSet):
    """CRUD для пользователей (дополнительное задание)."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    """
    CRUD для платежей с фильтрацией и сортировкой (Задание 4).

    Поддерживает query-параметры:
    - ?ordering=payment_date / ?ordering=-payment_date
    - ?course=<id>
    - ?lesson=<id>
    - ?payment_method=cash|transfer
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PaymentFilter