from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from main.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(
            email='base@mail.ru',
            password='2344'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        """Create habit"""
        data = {
            "action": "Bad action",
            "pleasant": True,
            "run_time": 120,
            "public": True
        }
        response = self.client.post(
            reverse('main:habit_create'),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_habit(self):
        """Test list"""
        response = self.client.get(
            reverse('main:habit_list'),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_habit(self):
        """Test update"""
        habit = Habit.objects.create(
            owner=self.user,
            action='Bad action',
            pleasant=True,
            run_time=120,
            public=True,
            pk=2
        )

        data = {'public': False}

        response = self.client.patch(
            reverse('main:habit_update', kwargs={'pk': habit.pk}),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_habit(self):
        """Test Delete"""
        habit = Habit.objects.create(
            owner=self.user,
            action='Bad action',
            pleasant=True,
            run_time=120,
            public=True,
            pk=2
        )
        response = self.client.delete(
            reverse('main:habit_delete', kwargs={'pk': habit.pk})
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )