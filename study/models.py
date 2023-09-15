from django.db import models

from django.urls import reverse

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False,)
    
    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=50, null=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name

class Flashcard(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=False)
    question = models.CharField(max_length=500, null=False)
    answer = models.TextField(null=False)

    # Displays the question of a particular model to the user
    def __str__(self):
        return self.question
    