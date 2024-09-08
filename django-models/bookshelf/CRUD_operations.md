# Create an instance of a Book object
>>> q = Book(title="1984", author="George Orwell", publication_year=1949)
>>> q.save()
>>> Book.objects.all()
<QuerySet [<Book: 1984>]>

# Retrieve and display the created book from database
>>> books = Book.objects.all()
>>> for book in books:
...     print(book.title, book.author, book.publication_year)
... 
1984 George Orwell 1949

# Retrieve and update object id=1
>>> book = Book.objects.get(id=1)
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> books = Book.objects.all()
>>> for book in books:
...     print(book.title, book.author, book.publication_year)

# Delete the Book instance id=1
>>> book = Book.objects.get(id=1)
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> books = Book.objects.all()
>>> for book in books:
...     print(book.title, book.author, book.publication_year)
... 