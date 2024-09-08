# The code is expected to create an instance of a book with the attribute values assigned i.e 1984, George Orwell, 1949,
q = Book(title="1984", author="George Orwell", publication_year=1949)
q.save()
# OR
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)