from django import forms

from .models import Subject

class NewSubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["name"]

class NewTopicForm(forms.ModelForm):
    class Meta:
        model = Subject
        subject = forms.ModelChoiceField(queryset=Subject.objects.all())
        fields = ["name",]