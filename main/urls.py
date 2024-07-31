from django.urls import path

from main.apps import MainConfig
from main.views import HabitCreateAPIView, HabitListAPIView, HabitUpdateAPIView, HabitDeleteAPIView, HabitDetailAPIView

app_name = MainConfig.name

urlpatterns = [
    path('create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('list/', HabitListAPIView.as_view(), name='habit_list'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('detail/<int:pk>/', HabitDetailAPIView.as_view(), name='habit_detail'),
    path('delete/<int:pk>/', HabitDeleteAPIView.as_view(), name='habit_delete'),
]