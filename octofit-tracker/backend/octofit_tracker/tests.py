from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Team, CustomUser, Activity, Workout, Leaderboard

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='Test Team')
        self.user = CustomUser.objects.create_user(username='testuser', email='test@example.com', password='pass', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='desc', duration=10)
        self.activity = Activity.objects.create(user=self.user, type='run', duration=10, distance=1.0)
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=50)

    def test_api_root(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_list(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_teams_list(self):
        response = self.client.get('/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_activities_list(self):
        response = self.client.get('/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_workouts_list(self):
        response = self.client.get('/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_leaderboard_list(self):
        response = self.client.get('/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
