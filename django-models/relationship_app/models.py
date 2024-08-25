from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
  
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    ## which means each book is associated with a single author.
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
   ## related_name: It allows you to access all books by an author using `author.books.all()`.
# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')
# Create your models here.
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return self.name