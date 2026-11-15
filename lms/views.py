from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer
from .permissions import IsModerator, IsOwner


# --- CRUD для курса через ViewSet (Задания 2 и 3) ---
class CourseViewSet(viewsets.ModelViewSet):
    """Полный CRUD для курса с разграничением прав."""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        """
        Настраиваем права в зависимости от действия (action).
        - create: только авторизованные, не модераторы.
        - destroy: только авторизованные, не модераторы, владельцы.
        - update/partial_update/retrieve: авторизованные, модераторы ИЛИ владельцы.
        - list: авторизованные.
        """
        if self.action == 'create':
            permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, ~IsModerator, IsOwner]
        elif self.action in ['update', 'partial_update', 'retrieve']:
            permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        else:  # list
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        """Модераторы видят все курсы, остальные — только свои (Задание 3)."""
        user = self.request.user
        if user.groups.filter(name='Модераторы').exists():
            return Course.objects.all()
        return Course.objects.filter(owner=user)

    def perform_create(self, serializer):
        """Привязываем курс к текущему пользователю при создании."""
        serializer.save(owner=self.request.user)


# --- CRUD для урока через Generic-классы ---
class LessonListCreateAPIView(generics.ListCreateAPIView):
    """Список уроков и создание нового."""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        """Создавать уроки могут все, кроме модераторов."""
        if self.request.method == 'POST':
            permission_classes = [IsAuthenticated, ~IsModerator]
        else:  # GET
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        """Модераторы видят все уроки, остальные — только свои."""
        user = self.request.user
        if user.groups.filter(name='Модераторы').exists():
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=user)

    def perform_create(self, serializer):
        """Привязываем урок к текущему пользователю при создании."""
        serializer.save(owner=self.request.user)


class LessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Получение одного урока, его обновление и удаление."""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        """
        Редактировать могут владельцы и модераторы.
        Удалять — только владельцы (и не модераторы).
        """
        if self.request.method == 'DELETE':
            permission_classes = [IsAuthenticated, ~IsModerator, IsOwner]
        elif self.request.method in ['PUT', 'PATCH']:
            permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        else:  # GET
            permission_classes = [IsAuthenticated, IsModerator | IsOwner]

        return [permission() for permission in permission_classes]