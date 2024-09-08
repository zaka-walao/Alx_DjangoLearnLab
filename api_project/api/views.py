from rest_framework import viewsets #generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Book  # Import your Book model
from .serializers import BookSerializer  # Import the serializer you just created
from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Write permissions are only allowed to the owner of the object.
        return obj.owner == request.user

#class BookList(generics.ListAPIView):
    #queryset = Book.objects.all()  # Define the queryset to return all Book instances
    #serializer_class = BookSerializer  # Use the BookSerializer to serialize the data

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser, IsOwnerOrReadOnly]

     # You can also override get_permissions method to dynamically set permissions
    def get_permissions(self):
        # Example of dynamically setting permissions
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes]