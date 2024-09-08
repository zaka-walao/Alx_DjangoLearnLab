from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)

# List all books in a library
library = Library.objects.get(name=library_name)
books = books.all()

# Retrieve the librarian for a library
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)