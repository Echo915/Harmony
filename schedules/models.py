from django.db import models

# Create your models here.

class PasswordOperator(models.Model):
    password = models.CharField(max_length=10, null=False)
    time = models.DateTimeField(null=False)
    label = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.label

class Schedule(models.Model):
    schedule = models.CharField(null=False, max_length=100)
    time = models.DateTimeField(null=False)

    def __str__(self):
        return self.schedule 