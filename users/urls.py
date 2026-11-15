from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, PaymentViewSet, UserRegistrationAPIView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'payments', PaymentViewSet, basename='payment')

urlpatterns = [
    # Эндпоинт регистрации (должен быть отдельно от роутера)
    path('users/register/', UserRegistrationAPIView.as_view(), name='user-register'),
    # Остальные маршруты из роутера
    path('', include(router.urls)),
]