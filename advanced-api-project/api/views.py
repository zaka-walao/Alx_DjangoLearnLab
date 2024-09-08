from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
#from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework import filters
from rest_framework.filters import SearchFilter, OrderingFilter


# List all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [IsAuthenticatedOrReadOnly]
    #filter_backends = [filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']

# Retrieve book based on its ID
class BookDetailView(generics.RetrieveApiView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

# Adding a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [IsAuthenticated]

# Updating a book based on its ID
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.ojects.all()
    serializer_class = BookSerializer
    permission_class = [IsAuthenticated]

# Deleting a book based on its ID
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [IsAuthenticated]


