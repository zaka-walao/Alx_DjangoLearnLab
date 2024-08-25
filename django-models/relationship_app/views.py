from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

# Create your views here.
def list_books(request):
    """
    A function-based view to list all books with their titles and authors.
    """
    books = Book.objects.all()  ## Retrieve all book objects from the database
    context = {'books': books}  # # Pass the books to the template context
    return render(request, 'relationship_app/list_books.html', context)


from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    """
    A class-based view to display details of a specific library, including all books.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
