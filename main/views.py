from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from main.models import Habit
from main.paginators import HabitPaginator
from main.permissions import IsOwner
from main.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """Habit Create"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]


class HabitListAPIView(generics.ListAPIView):
    """Habit List"""
    serializer_class = HabitSerializer
    permission_classes = [AllowAny]
    pagination_class = HabitPaginator

    def get_queryset(self):
        user = self.request.user.pk
        user_habits = Habit.objects.filter(owner=user)
        public_habits = Habit.objects.filter(public=True)

        queryset = user_habits | public_habits
        return queryset.distinct()


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Habit Update"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDetailAPIView(generics.RetrieveAPIView):
    """Habit Detail"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDeleteAPIView(generics.DestroyAPIView):
    """Habit Delete"""
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]