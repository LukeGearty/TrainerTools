from django import forms
from .models import Client, Workout, TrainerProfile
from django.contrib.auth.models import User



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

class TrainerRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    manager = forms.ModelChoiceField(
        queryset=TrainerProfile.objects.filter(user__is_superuser=True),
        required=False
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            # Create the TrainerProfile with manager
            TrainerProfile.objects.create(
                user=user,
                manager=self.cleaned_data['manager']
            )
        return user
