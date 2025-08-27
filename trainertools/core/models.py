from django.db import models
from django.contrib.auth.models import User


#Trainer will be the default user

class Client(models.Model):
    trainer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="clients")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Workout(models.Model):
    WORKOUT_TYPES = [
        ("cardio", "Cardio"),
        ("strength", "Strength Training"),
        ("flexibility", "Flexibility"),
        ("mobility", "Mobility"),
        ("other", "Other"),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="workouts")
    date = models.DateField()
    workout_type = models.CharField(max_length=20, choices=WORKOUT_TYPES)
    description = models.TextField()

    def __str__(self):
        return f"{self.client.name} - {self.get_workout_type_display()} on {self.date}"
