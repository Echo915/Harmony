from django import forms
from .models import PasswordOperator, Schedule


class PasswordForm(forms.ModelForm):
    class Meta:
        model = PasswordOperator
        fields = ["password", "time", "label"]
        widgets = {
            # Provides a password input widget for the specified fields
            "password":forms.PasswordInput(attrs={"class": "form-control", "type": "password", "placeholder": "password"}),
            "time": forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}),
            "label": forms.TextInput(attrs={"class": "form-control", "placeholder": "Lock Label. e.g. 'Anime'... "})   
        }

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ["schedule", "time"]
        widgets = {
           "time": forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}),
           "schedule":forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter New Task"})
        }