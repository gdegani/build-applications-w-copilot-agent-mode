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


        # Insert test data directly using pymongo
        from datetime import datetime
        # Users
        users = [
            {"_id": ObjectId(), "email": "thundergod@mhigh.edu", "name": "Thunder God", "team": "Blue Team", "is_active": True},
            {"_id": ObjectId(), "email": "metalgeek@mhigh.edu", "name": "Metal Geek", "team": "Blue Team", "is_active": True},
            {"_id": ObjectId(), "email": "zerocool@mhigh.edu", "name": "Zero Cool", "team": "Blue Team", "is_active": True},
            {"_id": ObjectId(), "email": "crashoverride@mhigh.edu", "name": "Crash Override", "team": "Gold Team", "is_active": True},
            {"_id": ObjectId(), "email": "sleeptoken@mhigh.edu", "name": "Sleep Token", "team": "Gold Team", "is_active": True},
        ]
        db.users.insert_many(users)

        # Teams
        blue_team = {
            "_id": ObjectId(),
            "name": "Blue Team",
            "members": users[:3],
        }
        gold_team = {
            "_id": ObjectId(),
            "name": "Gold Team",
            "members": users[3:],
        }
        db.teams.insert_many([blue_team, gold_team])

        # Activities
        activities = [
            {"_id": ObjectId(), "user": users[0]["email"], "activity_type": "Cycling", "duration": 1.0, "date": datetime(2025, 6, 1, 9, 0)},
            {"_id": ObjectId(), "user": users[1]["email"], "activity_type": "Crossfit", "duration": 2.0, "date": datetime(2025, 6, 2, 10, 0)},
            {"_id": ObjectId(), "user": users[2]["email"], "activity_type": "Running", "duration": 1.5, "date": datetime(2025, 6, 3, 8, 30)},
            {"_id": ObjectId(), "user": users[3]["email"], "activity_type": "Strength", "duration": 0.5, "date": datetime(2025, 6, 4, 7, 45)},
            {"_id": ObjectId(), "user": users[4]["email"], "activity_type": "Swimming", "duration": 1.25, "date": datetime(2025, 6, 5, 11, 15)},
        ]
        db.activity.insert_many(activities)

        # Workouts
        workouts = [
            {"_id": ObjectId(), "user": users[0]["email"], "workout_type": "Cycling", "details": {"goal": "Road cycling event"}, "date": datetime(2025, 6, 1, 9, 0)},
            {"_id": ObjectId(), "user": users[1]["email"], "workout_type": "Crossfit", "details": {"goal": "Crossfit competition"}, "date": datetime(2025, 6, 2, 10, 0)},
            {"_id": ObjectId(), "user": users[2]["email"], "workout_type": "Running", "details": {"goal": "Marathon"}, "date": datetime(2025, 6, 3, 8, 30)},
            {"_id": ObjectId(), "user": users[3]["email"], "workout_type": "Strength", "details": {"goal": "Strength training"}, "date": datetime(2025, 6, 4, 7, 45)},
            {"_id": ObjectId(), "user": users[4]["email"], "workout_type": "Swimming", "details": {"goal": "Swimming competition"}, "date": datetime(2025, 6, 5, 11, 15)},
        ]
        db.workouts.insert_many(workouts)

        # Leaderboard
        leaderboard_entries = [
            {"_id": ObjectId(), "team": "Blue Team", "score": 285, "rank": 1},
            {"_id": ObjectId(), "team": "Gold Team", "score": 165, "rank": 2},
        ]
        db.leaderboard.insert_many(leaderboard_entries)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
