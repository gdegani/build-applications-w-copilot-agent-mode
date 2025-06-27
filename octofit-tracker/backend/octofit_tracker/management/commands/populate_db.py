from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(
            host=settings.DATABASES['default']['CLIENT']['host'],
            port=int(settings.DATABASES['default']['CLIENT']['port'])
        )
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users

        # Create users
        users = [
            User(_id=ObjectId(), email='thundergod@mhigh.edu', name='Thunder God', team='Blue Team', is_active=True),
            User(_id=ObjectId(), email='metalgeek@mhigh.edu', name='Metal Geek', team='Blue Team', is_active=True),
            User(_id=ObjectId(), email='zerocool@mhigh.edu', name='Zero Cool', team='Blue Team', is_active=True),
            User(_id=ObjectId(), email='crashoverride@mhigh.edu', name='Crash Override', team='Gold Team', is_active=True),
            User(_id=ObjectId(), email='sleeptoken@mhigh.edu', name='Sleep Token', team='Gold Team', is_active=True),
        ]
        User.objects.bulk_create(users)

        # Create teams
        blue_team = Team(
            _id=ObjectId(),
            name='Blue Team',
            members=[
                {'_id': users[0]._id, 'email': users[0].email, 'name': users[0].name, 'team': users[0].team, 'is_active': users[0].is_active},
                {'_id': users[1]._id, 'email': users[1].email, 'name': users[1].name, 'team': users[1].team, 'is_active': users[1].is_active},
                {'_id': users[2]._id, 'email': users[2].email, 'name': users[2].name, 'team': users[2].team, 'is_active': users[2].is_active},
            ]
        )
        gold_team = Team(
            _id=ObjectId(),
            name='Gold Team',
            members=[
                {'_id': users[3]._id, 'email': users[3].email, 'name': users[3].name, 'team': users[3].team, 'is_active': users[3].is_active},
                {'_id': users[4]._id, 'email': users[4].email, 'name': users[4].name, 'team': users[4].team, 'is_active': users[4].is_active},
            ]
        )
        blue_team.save()
        gold_team.save()

        # Create activities
        from datetime import datetime
        activities = [
            Activity(_id=ObjectId(), user=users[0].email, activity_type='Cycling', duration=1.0, date=datetime(2025, 6, 1, 9, 0)),
            Activity(_id=ObjectId(), user=users[1].email, activity_type='Crossfit', duration=2.0, date=datetime(2025, 6, 2, 10, 0)),
            Activity(_id=ObjectId(), user=users[2].email, activity_type='Running', duration=1.5, date=datetime(2025, 6, 3, 8, 30)),
            Activity(_id=ObjectId(), user=users[3].email, activity_type='Strength', duration=0.5, date=datetime(2025, 6, 4, 7, 45)),
            Activity(_id=ObjectId(), user=users[4].email, activity_type='Swimming', duration=1.25, date=datetime(2025, 6, 5, 11, 15)),
        ]
        Activity.objects.bulk_create(activities)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), user=users[0].email, workout_type='Cycling', details={"goal": "Road cycling event"}, date=datetime(2025, 6, 1, 9, 0)),
            Workout(_id=ObjectId(), user=users[1].email, workout_type='Crossfit', details={"goal": "Crossfit competition"}, date=datetime(2025, 6, 2, 10, 0)),
            Workout(_id=ObjectId(), user=users[2].email, workout_type='Running', details={"goal": "Marathon"}, date=datetime(2025, 6, 3, 8, 30)),
            Workout(_id=ObjectId(), user=users[3].email, workout_type='Strength', details={"goal": "Strength training"}, date=datetime(2025, 6, 4, 7, 45)),
            Workout(_id=ObjectId(), user=users[4].email, workout_type='Swimming', details={"goal": "Swimming competition"}, date=datetime(2025, 6, 5, 11, 15)),
        ]
        Workout.objects.bulk_create(workouts)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), team='Blue Team', score=285, rank=1),
            Leaderboard(_id=ObjectId(), team='Gold Team', score=165, rank=2),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
