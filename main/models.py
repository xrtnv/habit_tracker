from rest_framework.exceptions import ValidationError
from django.conf import settings
from django.db import models

periods = (
    ('daily', 'Ежеднево'),
    ('weekly', 'Еженедельно'),
)

NULLABLE = {
    'null': True,
    'blank': True
}


class Habit(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='создатель', **NULLABLE)
    place = models.CharField(max_length=100, verbose_name='место', **NULLABLE)
    time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='время', **NULLABLE)
    action = models.CharField(max_length=255, verbose_name='действие', **NULLABLE)
    pleasant = models.BooleanField(verbose_name='приятная')
    related = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='связанная привычка', **NULLABLE)
    period = models.CharField(max_length=15, choices=periods, default='daily', verbose_name='период', **NULLABLE)
    award = models.CharField(max_length=255, verbose_name='награда', **NULLABLE)
    run_time = models.IntegerField(default=0, verbose_name='время выполнения')
    public = models.BooleanField(default=True, verbose_name='опубликовано')

    def __str__(self):
        return f'Привычка: {self.owner}'

    def clean(self):
        if self.period not in dict(periods).keys():
            raise ValidationError(
                {'period': 'Пожалуйста, выберите один из доступных периодов: daily, weekly'}
            )

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
