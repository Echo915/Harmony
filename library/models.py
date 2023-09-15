from django.db import models

# Create your models here.
class NewBook(models.Model):
    bookTitle = models.CharField(max_length=50)
    book = models.FileField(null=True) # FileField is used for file input