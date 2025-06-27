# Views for OctoFit Tracker
from rest_framework import viewsets
from .models import User, Team, Activity, Workout, Leaderboard
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request, format=None):
    # Use both Codespace and localhost URLs for dev/test
    codespace_url = 'https://stunning-capybara-vpjj45qj5r2xg5-8000.app.github.dev/'
    localhost_url = 'http://localhost:8000/'
    return Response({
        'users': [codespace_url + 'api/users/', localhost_url + 'api/users/'],
        'teams': [codespace_url + 'api/teams/', localhost_url + 'api/teams/'],
        'activity': [codespace_url + 'api/activity/', localhost_url + 'api/activity/'],
        'workouts': [codespace_url + 'api/workouts/', localhost_url + 'api/workouts/'],
        'leaderboard': [codespace_url + 'api/leaderboard/', localhost_url + 'api/leaderboard/'],
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
