from django.db import models

# Author model
class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# Book model having a one to many relationship with the Author model
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self) -> str:
        return self.title