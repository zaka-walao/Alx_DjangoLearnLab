from django.urls import path
from .views import book_list, LibraryDetailView,RegisterView, index
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('books/', book_list, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='bookshelf/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='bookshelf/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(template_name='bookshelf/register.html'), name='register'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('add_book/', views.create_book, name='add_book'),
    path('edit_book/', views.edit_book, name='edit_book'),
    path('delete_book/', views.delete_book, name='delete_book'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='bookshelf/login.html'), name='login'),
]