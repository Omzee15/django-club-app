from django.db import models
from django.contrib.auth.models import User

class Membership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_member = models.BooleanField(default=False)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Member: {self.is_member}"

class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(Membership, related_name='activities')

    def __str__(self):
        return self.name