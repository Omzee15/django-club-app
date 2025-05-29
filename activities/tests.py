from django.test import TestCase
from .models import Activity, Enrollment
from django.contrib.auth.models import User

class ActivityModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.activity = Activity.objects.create(name='Yoga Class', description='A relaxing yoga class.')

    def test_activity_creation(self):
        self.assertEqual(self.activity.name, 'Yoga Class')
        self.assertEqual(self.activity.description, 'A relaxing yoga class.')

class EnrollmentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.activity = Activity.objects.create(name='Yoga Class', description='A relaxing yoga class.')
        self.enrollment = Enrollment.objects.create(user=self.user, activity=self.activity)

    def test_enrollment_creation(self):
        self.assertEqual(self.enrollment.user, self.user)
        self.assertEqual(self.enrollment.activity, self.activity)

    def test_user_enrollment_in_activity(self):
        self.assertIn(self.enrollment, self.user.enrollment_set.all())