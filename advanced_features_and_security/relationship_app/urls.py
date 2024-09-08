from django.urls import path
from .import views
from .views import  register, LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from .views import list_books



urlpatterns = [

    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView, name='library_detail'),
    # path("register", register, name="register"),
    # path("login", LoginView.as_view, name="login"),
    # path("logout", LogoutView.as_view, name="logout"),

]

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    
]


from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    # Other URL patterns...
]

urlpatterns = [
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),

]