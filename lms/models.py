from django.conf import settings
from django.db import models


class Course(models.Model):
    """Модель курса."""
    title = models.CharField('Название', max_length=255)
    preview = models.ImageField('Превью', upload_to='courses/', blank=True, null=True)
    description = models.TextField('Описание', blank=True, null=True)

    # Владелец (пользователь, создавший курс) - пригодится позже
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name='Владелец'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    """Модель урока."""
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lessons',
        verbose_name='Курс'
    )
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', blank=True, null=True)
    preview = models.ImageField('Превью', upload_to='lessons/', blank=True, null=True)
    video_link = models.URLField('Ссылка на видео', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
