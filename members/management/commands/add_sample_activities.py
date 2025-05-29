from django.core.management.base import BaseCommand
from members.models import Activity

class Command(BaseCommand):
    help = 'Add sample activities to the database'

    def handle(self, *args, **kwargs):
        # List of sample sports activities
        activities = [
            {'name': 'Chess', 'description': 'Strategic board game sessions and tournaments.'},
            {'name': 'Cricket', 'description': 'Cricket coaching and practice matches.'},
            {'name': 'Football', 'description': 'Football training and team play.'},
            {'name': 'Pool', 'description': 'Pool and billiards sessions for all skill levels.'},
            {'name': 'Gym', 'description': 'Access to gym facilities with professional trainers.'},
            {'name': 'Swimming', 'description': 'Swimming lessons and practice sessions.'},
            {'name': 'Basketball', 'description': 'Indoor/outdoor basketball sessions.'},
            {'name': 'Tennis', 'description': 'Tennis coaching and friendly matches.'},
            {'name': 'Yoga', 'description': 'Relaxing yoga sessions for all levels.'},
            {'name': 'Badminton', 'description': 'Badminton training and matches.'},
        ]

        # Create activities if they don't already exist
        for activity_data in activities:
            activity, created = Activity.objects.get_or_create(
                name=activity_data['name'],
                defaults={'description': activity_data['description']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created activity: {activity.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Activity already exists: {activity.name}'))

        self.stdout.write(self.style.SUCCESS('Sample activities have been added successfully!'))
