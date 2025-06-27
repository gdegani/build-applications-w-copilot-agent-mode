# Tests for OctoFit Tracker
from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='test@example.com', name='Test User')
        self.assertEqual(user.email, 'test@example.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Team A')
        self.assertEqual(team.name, 'Team A')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user='test@example.com', activity_type='run', duration=30, date='2025-01-01T00:00:00Z')
        self.assertEqual(activity.activity_type, 'run')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(user='test@example.com', workout_type='cardio', details={}, date='2025-01-01T00:00:00Z')
        self.assertEqual(workout.workout_type, 'cardio')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team='Team A', score=100, rank=1)
        self.assertEqual(leaderboard.rank, 1)
