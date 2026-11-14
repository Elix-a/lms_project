from rest_framework import serializers

from .models import User, Payment


class PaymentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Payment."""

    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор пользователя.

    - payments: история платежей пользователя (доп. задание).
    """
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'city', 'avatar', 'payments']