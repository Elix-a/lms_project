import django_filters

from .models import Payment


class PaymentFilter(django_filters.FilterSet):
    """
    Фильтр для модели Payment.

    Поддерживает:
    - ordering: сортировка по дате оплаты (?ordering=payment_date или ?ordering=-payment_date)
    - course: фильтр по ID курса (?course=2)
    - lesson: фильтр по ID урока (?lesson=2)
    - payment_method: фильтр по способу оплаты (?payment_method=cash)
    """
    ordering = django_filters.OrderingFilter(
        fields=(
            ('payment_date', 'payment_date'),
        ),
        field_labels={
            'payment_date': 'Дата оплаты',
        },
    )
    course = django_filters.NumberFilter(field_name='course__id')
    lesson = django_filters.NumberFilter(field_name='lesson__id')
    payment_method = django_filters.ChoiceFilter(choices=Payment.PAYMENT_METHOD_CHOICES)

    class Meta:
        model = Payment
        fields = ['course', 'lesson', 'payment_method']