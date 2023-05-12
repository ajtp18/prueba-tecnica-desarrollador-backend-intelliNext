from django.db import models

# Create your models here.

class Book(models.Model):
    isbn = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    yearOfPublication = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Book: {self.title}, {self.author}"