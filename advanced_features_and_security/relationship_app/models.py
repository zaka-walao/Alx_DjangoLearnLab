from django.db import models
from django.contrib.auth.models import User
 

 

class Author(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    class Meta(models.Model):
        permissions = [
            ('Can add book', 'can_add_book')
            ('Can change book', 'can_change_book')
            ('can delete book', 'can_delete_book')
        ]

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return self.name
# Create your models here.

class UserProfile(models.Model):
    CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choice= CHOICES)

    def __str__(self):
        return self.user.username
