from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="UserTest@mail.ru",
            first_name="User",
            last_name="Test",
            password="134USTest132"
        )
        self.habit = Habit.objects.create(
            owner=self.user,
            place="Home",
            time="11:10",
            action="Хорошая работа",
            pleasant_habit=False,
            period=3,
            reward="good",
            time_to_complete=115,
            published=False,
            created_at="2025-01-08"
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_habit_create(self):
        url = reverse("habits:list-habits-public")
        data = {
            "owner": self.user.pk,
            "place": "Home",
            "time": "11:10",
            "action": "Хорошая работа",
            "pleasant_habit": False,
            "period": 3,
            "reward": "good",
            "time_to_complete": 115,
            "published": False,
            "created_at": "2025-01-08"
        }

        response = self.client.post(url, data)

        self.assertEquals(
            response.status_code, status.HTTP_201_CREATED
        )

        self.assertEquals(
            Habit.objects.get(place="Home"), "Home"
        )

    def test_habit_update(self):
        url = reverse("habits:view-habit", args=(self.habit.pk,))
        data = {
            "published": True,
        }

        response = self.client.patch(url, data)

        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("published"), True
        )

    def test_habit_delete(self):
        url = reverse("habits:list-habits", args=(self.habit.pk,))

        response = self.client.delete(url)

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Habit.objects.filter(adction=""), ""
        )
