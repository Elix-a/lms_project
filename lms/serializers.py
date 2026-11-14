from rest_framework import serializers

from .models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Lesson."""

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'preview', 'video_link', 'course']


class CourseSerializer(serializers.ModelSerializer):
    """
    Сериализатор для курса.

    - lesson_count: количество уроков (SerializerMethodField, Задание 1).
    - lessons: вложенный список уроков (LessonSerializer, Задание 3).
    """
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, obj):
        """Возвращает количество уроков, связанных с курсом."""
        return obj.lessons.count()