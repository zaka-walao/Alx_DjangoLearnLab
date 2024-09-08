# Code reads all instances of a book stored in the database and displays them in the order stipulated i.e title,author,pub year
books = Book.objects.all()
for book in books:
    print(book.title, book.author, book.publication_year)

# OR

# Get the book details by title
Book.objects.get(title="1984")