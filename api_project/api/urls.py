from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BookViewSet
from django.urls import path
from .views import BookList
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

 


