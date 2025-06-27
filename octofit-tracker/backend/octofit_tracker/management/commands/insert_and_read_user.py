from django.core.management.base import BaseCommand
from octofit_tracker.models import User
from bson import ObjectId

class Command(BaseCommand):
    help = 'Insert a test user and read it back from the database.'

    def handle(self, *args, **kwargs):
        # Insert a user
        test_email = 'debuguser@example.com'
        User.objects.create(_id=ObjectId(), email=test_email, name='Debug User', team='Debug Team', is_active=True)
        # Read it back
        user = User.objects.filter(email=test_email).first()
        if user:
            self.stdout.write(self.style.SUCCESS(f'User found: {user.email}, {user.name}, {user.team}, {user.is_active}'))
        else:
            self.stdout.write(self.style.ERROR('User not found.'))
