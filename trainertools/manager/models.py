from django.db import models
from django.contrib.auth.models import User
from core.models import Client


class TrainerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="trainer_profile")
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="supervised_trainers")

    def __str__(self):
        return self.user.username
