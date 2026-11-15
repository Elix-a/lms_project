from rest_framework import serializers

from .models import User, Payment


class PaymentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Payment."""
    class Meta:
        model = Payment
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации новых пользователей."""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'phone', 'city', 'avatar']

    def validate_email(self, value):
        """Проверка, что пользователь с таким email еще не зарегистрирован."""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Пользователь с таким email уже существует.")
        return value

    def create(self, validated_data):
        """Создаем пользователя с хэшированием пароля."""
        user = User.objects.create_user(**validated_data)
        return user


class UserSerializer(serializers.ModelSerializer):
    """
    Полный сериализатор пользователя (для своего профиля).
    Включает историю платежей.
    """
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'city', 'avatar', 'payments']


class UserPublicSerializer(serializers.ModelSerializer):
    """
    Сериализатор для просмотра чужого профиля (доп. задание).
    Скрывает историю платежей и лишние данные.
    """
    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'city', 'avatar']