from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import ExampleForm
from django.contrib.auth import login
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required, user_passes_test
from django.http import HttpResponseForbidden
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from .forms import CustomUserCreationForm


# Helper function to check user's role
def role_check(user, role):
    return user.is_authenticated and user.userprofile.role == role

# Admin view
@user_passes_test(lambda u: role_check(u, 'Admin'))
def admin_view(request):
    return render(request, 'bookshelf/admin_view.html')

# Librarian view
@user_passes_test(lambda u: role_check(u, 'Librarian'))
def librarian_view(request):
    return render(request, 'bookshelf/librarian_view.html')

# Member view
@user_passes_test(lambda u: role_check(u, 'Member'))
def member_view(request):
    return render(request, 'bookshelf/member_view.html')

# View to add a new book
@permission_required('bookshelf.can_create_book', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

# View to edit an existing book
@permission_required('bookshelf.can_edit_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = ExampleForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = ExampleForm(instance=book)
    return render(request, 'bookshelf/edit_book.html', {'form': form})

# View to delete a book
@permission_required('bookshelf.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/delete_book.html', {'book': book})

# Create more views here.

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'bookshelf/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')
    
class LoginView(LoginView):
    template_name = 'bookshelf/login.html'
    
    def get_success_url(self):
        user = self.request.user

        # Check the user's role and return the appropriate URL
        if user.role == 'admin':
            return reverse_lazy('admin')  # replace with your admin view name
        elif user.role == 'librarian':
            return reverse_lazy('librarian')  # replace with your librarian view name
        elif user.role == 'member':
            return reverse_lazy('member')  # replace with your member view name
        else:
            return reverse_lazy('home')  # a fallback view
    

class LogoutView(LogoutView):
    template_name = 'bookshelf/logout.html'
    success_url = reverse_lazy('login')

def book_list(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'bookshelf/book_list.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'bookshelf/library_detail.html'
    context_object_name = 'library'
    
def index(request):
    libraries = Library.objects.all()
    return render(request, 'bookshelf/index.html', {'libraries': libraries})

def profile(request):
    return render(request, 'bookshelf/profile.html')