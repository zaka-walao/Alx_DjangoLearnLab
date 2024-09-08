from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a superuser and user for permissions testing purposes
        self.superuser = User.objects.create_superuser(username='admin', password='adminpassword')
        self.suser = User.objects.create_superuser(username='test', password='testpassword')
        
        # Set up API client and log in as the superuser
        self.client = APIClient()
        self.client.login(username='admin', password='adminpassword')  # Session-based login
        #self.client.login(username='test', password='testpassword')  # Session-based login

        # Create initial data
        self.book1 = Book.objects.create(title='Book One', author='Author A', publication_year=2020)
        self.book2 = Book.objects.create(title='Book Two', author='Author B', publication_year=2021)

    def test_create_book_as_superuser(self):
        url = reverse('book-create')
        data = {'title': 'Book Three', 'author': 'Author C', 'publication_year': 2022}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(title='Book Three').author, 'Author C')

    def test_create_book_as_anonymous_user(self):
        # Log out the superuser to simulate an anonymous request
        self.client.logout()  # Logout to remove session-based authentication
        
        url = reverse('book-create')
        data = {'title': 'Book Four', 'author': 'Author D', 'publication_year': 2023}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Ensure unauthenticated access is forbidden

    def test_get_books(self):
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_book_as_superuser(self):
        url = reverse('book-update', kwargs={'pk': self.book1.pk})
        data = {'title': 'Updated Book One', 'author': 'Author A', 'publication_year': 2020}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book One')

    def test_update_book_as_anonymous_user(self):
        # Log out the superuser to simulate an anonymous request
        self.client.logout()
        
        url = reverse('book-update', kwargs={'pk': self.book1.pk})
        data = {'title': 'Updated Book One', 'author': 'Author A', 'publication_year': 2020}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Unauthenticated users should be forbidden

    def test_delete_book_as_superuser(self):
        url = reverse('book-delete', kwargs={'pk': self.book1.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_delete_book_as_anonymous_user(self):
        # Log out the superuser to simulate an anonymous request
        self.client.logout()
        
        url = reverse('book-delete', kwargs={'pk': self.book1.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Unauthenticated users should be forbidden

    def test_filter_books(self):
        url = reverse('book-list') + '?author=Author A'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Author A')

    def test_search_books(self):
        url = reverse('book-list') + '?search=Book'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_order_books(self):
        url = reverse('book-list') + '?ordering=-publication_year'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book Two')  # Should be the most recent publication

    def test_permissions(self):
        # Log out the user to test permissions
        self.client.logout()  # Remove authentication credentials
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Assuming permissions are required which is not the case for the book-list view
