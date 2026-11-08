from rest_framework import generics, viewsets

from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer


# --- CRUD для курса через ViewSet ---
class CourseViewSet(viewsets.ModelViewSet):
    """Полный CRUD для курса."""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# --- CRUD для урока через Generic-классы ---
class LessonListCreateAPIView(generics.ListCreateAPIView):
    """Получение списка уроков и создание нового."""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Получение одного урока, его обновление и удаление."""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer