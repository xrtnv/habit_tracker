from rest_framework.permissions import BasePermission

from main.models import Habit


class IsOwner(BasePermission):
    message = 'Вы не создалеть привычки'

    def has_permission(self, request, view):
        habit = Habit.objects.get(pk=view.kwargs['pk'])
        if request.user == habit.owner:
            return True