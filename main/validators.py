from rest_framework.serializers import ValidationError


class HabitValidator:

    def __init__(self, pleasant, related, award, run_time):
        self.pleasant = pleasant
        self.related = related
        self.award = award
        self.run_time = run_time

    def __call__(self, value):
        pleasant = dict(value).get(self.pleasant)
        related = dict(value).get(self.related)
        award = dict(value).get(self.award)
        run_time = dict(value).get(self.run_time)

        if run_time is None:
            run_time = 0

        if pleasant == True and (related or award):
            raise ValidationError(
                'У приятной привычки не может быть вознаграждения'
            )
        elif related and award:
            raise ValidationError(
                'С полезной привычкой может быть связано либо приятная привычка, либо отдельное вознаграждение'
            )
        elif run_time < 0 or run_time > 120:
            raise ValidationError(
                'Время выполнения должно быть больше 0 и меньше 120 сек.'
            )
        elif pleasant == True and run_time is None:
            raise ValidationError({
                'run_time': 'Время выполнения должно быть больше 0 и меньше 120 сек.'
            })