from django import forms
from .models import Client, Workout


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["first_name", "last_name","email", "notes"]


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ["date", "workout_type", "description"]
        widgets = {
            "date" : forms.DateInput(attrs={"type":"date"}),
            "description": forms.Textarea(attrs={"rows":4}),
        }