from models import Author, Book, Library, Librarian

"""
 Implement Sample Queries:
    - Prepare a Python script `query_samples.py` in the `relationship_app` directory. This script should contain the query for each of the following of relationship:
       - Query all books by a specific author.
       - List all books in a library.
       - Retrieve the librarian for a library.
"""
## filter books by author
def query_books_by_author(author_name):
    
  try:
    author = Author.objects.get(name=author_name)
    # Filter books by the author object
    books = Book.objects.filter(author=author)

  except Author.DoesNotExist:
     print(f"No author found with the name: {author}")

def list_all_the_books(library_name):
     # Get the library object with the given name
    library = Library.objects.get(name=library_name)
     # Get all books in the library
    books = library.books.all()
def retrieve_librarian_from_a_lib(library_name):
     library = Library.objects.get(name=library_name)
     #librarian = Book.objects.filter()
     librarian = Librarian.objects.get(library=library)