# Models for OctoFit Tracker
from djongo import models

class User(models.Model):
    _id = models.ObjectIdField()
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.email

class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100, unique=True)
    members = models.ArrayField(model_container=User, blank=True, null=True)
    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = models.ObjectIdField()
    user = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration = models.FloatField()
    date = models.DateTimeField()
    def __str__(self):
        return f"{self.user} - {self.activity_type}"

class Workout(models.Model):
    _id = models.ObjectIdField()
    user = models.CharField(max_length=100)
    workout_type = models.CharField(max_length=100)
    details = models.JSONField()
    date = models.DateTimeField()
    def __str__(self):
        return f"{self.user} - {self.workout_type}"

class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    team = models.CharField(max_length=100)
    score = models.FloatField()
    rank = models.IntegerField()
    def __str__(self):
        return f"{self.team} - {self.rank}"
