from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.contrib.auth import login





def list_books(request):
      books = Book.objects.all()  # Fetch all book instances from the database
      return render(request, 'relationship_app/list_books.html', {'books': books})
    
  

  
class LibraryDetailView(ListView):
    model = Book
    template_name = 'relationship_app/library_detail.html'  # Use the library_detail.html template for this view
    context_object_name = 'books'  # Context variable name to be used in the template

    def get_queryset(self):
        library_id = self.kwargs['library_id']  # Retrieve the library_id from the URL
        return Book.objects.filter(library__id=library_id)  

def register(request):
    form = UserCreationForm()
    template_name = 'relationship_app/register.html'
    return render(request, "register.html", {"form":form})


class UserLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

class UserloginView(LoginView):
     template_name ='relationship_app/login.html'

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Meta


@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        form = Meta(request.POSt)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    
@permission_required('relationship_app.can_change_book')
def change_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = Meta(request.POST, instance=book)
        if form.is_valid():
            form.save()
            
        
@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()

    