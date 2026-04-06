from django.test import TestCase
from .models import User, Team, Workout, Activity, Leaderboard

class BasicModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name="Test Team")
        self.assertEqual(str(team), "Test Team")

    def test_user_creation(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create(username="testuser", email="test@example.com", team=team)
        self.assertEqual(user.email, "test@example.com")

    def test_workout_creation(self):
        workout = Workout.objects.create(name="Pushups", description="Pushups workout")
        self.assertEqual(str(workout), "Pushups")

    def test_activity_creation(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create(username="testuser", email="test@example.com", team=team)
        workout = Workout.objects.create(name="Pushups", description="Pushups workout")
        activity = Activity.objects.create(user=user, workout=workout, duration=30)
        self.assertEqual(activity.duration, 30)

    def test_leaderboard_creation(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create(username="testuser", email="test@example.com", team=team)
        leaderboard = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(leaderboard.points, 100)
