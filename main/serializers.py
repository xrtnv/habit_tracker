from rest_framework import serializers

from main.models import Habit
from main.validators import HabitValidator


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [HabitValidator(
            pleasant='pleasant',
            related='related',
            award='award',
            run_time='run_time'
        )]

    def create(self, validated_data):
        new_habit = Habit.objects.create(**validated_data)
        new_habit.owner = self.context['request'].user
        if new_habit.pleasant == True:
            new_habit.period = None
        else:
            new_habit
        new_habit.save()
        return new_habit