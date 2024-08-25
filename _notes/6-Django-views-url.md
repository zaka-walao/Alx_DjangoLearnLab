## views Definition
Views: Control what a user sees. The view retrieves data from the appropriate model and passes it to a template.

## Django Views and URL Configuration
This concept page introduces the concept of views in Django and how they are used to handle HTTP requests and generate responses. 

It covers both `function-based views` and `class-based views`, as well as the `URL configuration` process for mapping URL patterns to corresponding views.

In a Django web application, views play a crucial role in`handling user requests and generating appropriate responses. 

## What are views 

Views are Python functions or classes that `receive HTTP requests`, process the data, and `return HTTP responses`. Django provides two types of views: `function-based views and class-based views`. 

Additionally, Django’s URL configuration system allows you to define URL patterns and map them to the corresponding views.

## My comment
In summary, what views does is simple:

- It processes http web requests(GET,POST,DELETE, UPDATE) and returns a response.
- Views response could be - HTML page, a redirect, JSON object or error message
- views contains logic that interacts with the database

## Concept Overview

### Topics
- Function-based Views
- Class-based Views
- URL Configuration


## Learning Objecives 
- Understand the purpose and structure of `function-based views`
- Learn about `class-based views` and their advantages
- Configure URL patterns and map them to corresponding views
- Utilize URL parameters and regular expressions in URL patterns
- Pass data between `views and templates`


## Function-based Views

Function-based views are the traditional way of defining views in Django. 

They are Python functions that take an `HTTP request` as the first argument and `return an HTTP response`. 

Function-based views are straightforward and easy to understand, making them a `good choice for simple views or when you need fine-grained control over the view logic.`

```python
from django.http import HttpResponse

def hello_view(request):
    """A basic function view returning a greeting message."""
    return HttpResponse("Hello, World!")
```

Here, the `hello_view` function takes an HTTP request `(request)` as input and returns an HTTP response containing the string `“Hello, World!”`.

```python
from django.shortcuts import render
from .models import Book

def book_list(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'book_list': books}  # Create a context dictionary with book list
      return render(request, 'books/book_list.html', context)

```

In this example, the `book_list` function retrieves all `Book` objects using the `Book.objects.all()` queryset. 

It then constructs a context dictionary named `context` that holds the list of books under the key `book_list`. Finally, it utilizes the `render` shortcut to render the `books/book_list.html` template, passing along the `context` dictionary to make the book list accessible within the template.


## Class-based Views
Class-based views are an alternative approach to defining views in Django. 

They are Python classes that inherit from Django’s built-in view classes and provide a more structured and reusable way of handling HTTP requests. 

Class-based views promote code reusability, support mixins for shared behavior, and offer better organization and separation of concerns.

```python
from django.views.generic import TemplateView

class HelloView(TemplateView):
    """A class-based view rendering a template named 'hello.html'."""
    template_name = 'hello.html'
```

Class-based views can inherit from various built-in view classes offered by Django, including `ListView`, `DetailView`, `CreateView`, and more. 

These classes provide a significant amount of functionality out of the box, minimizing the amount of code you need to write. Here, the `HelloView` inherits from Django’s  `TemplateView` class and specifies the template to render using the `template_name` attribute.

Here are more examples on class based views:

## Example 1
This example shows a `BookDetailView` that inherits from `DetailView` and displays details of a specific book. It overrides the `get_context_data` method to inject additional context data relevant to the book, such as its average rating (assuming a method `get_average_rating` exists on the `Book` model).

```py
from django.views.generic import DetailView
from .models import Book

class BookDetailView(DetailView):
  """A class-based view for displaying details of a specific book."""
  model = Book
  template_name = 'books/book_detail.html'

  def get_context_data(self, **kwargs):
    """Injects additional context data specific to the book."""
    context = super().get_context_data(**kwargs)  # Get default context data
    book = self.get_object()  # Retrieve the current book instance
    context['average_rating'] = book.get_average_rating() 

```
context = super().get_context_data(**kwargs): This line calls the get_context_data method of the parent DetailView class, which returns the default context data (like the Book instance itself).

`context['average_rating'] = book.get_average_rating():`

 This line adds a new key-value pair to the context dictionary. The key is `average_rating`, and the value is the result of calling the get_average_rating() method on the Book instance. This method would presumably calculate and return the average rating for the book.

## Example 2
This example shows a `BookUpdateView` that inherits from `UpdateView` and facilitates updating details of a book. 

It defines the editable fields (title, author, and description) and the template used for the update form `(book_update_form.html)`. 

It also sets the `success_url` to redirect the user to the book list view `(book_list)` after a successful update. Additionally, it overrides the `form_valid` method to potentially execute custom logic after the form is validated (e.g., sending notifications).


```python
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy
from .models import Book

class BookUpdateView(UpdateView):
  """A class-based view for updating details of a specific book."""
  model = Book
  fields = ['title', 'author', 'description']  # Specify fields to be editable
  template_name = 'books/book_update_form.html'
  success_url = reverse_lazy('book_list')  # URL to redirect after successful update

  def form_valid(self, form):
    """Executes custom logic after form validation."""
    response = super().form_valid(form)  # Call default form validation
    # Perform additional actions after successful update (e.g., send notifications)
    return response

```
## URL Configuration

Django’s URL configuration system allows you to define URL patterns and map them to corresponding views. URL patterns can include parameters and regular expressions to match complex URL structures. 

The `urls.pyfile` in your Django project and apps is where you define these URL patterns and associate them with the appropriate views.

```python

from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
    path('about/', views.AboutView.as_view(), name='about'),
]
```
In this example, the URL pattern `/hello/` is mapped to the `hello_view` function-based view, and the `/about/ `pattern is mapped to the `AboutView` class-based view.

https://docs.djangoproject.com/en/5.1/topics/http/views/#writing-views

https://docs.djangoproject.com/en/5.1/topics/class-based-views/

https://docs.djangoproject.com/en/5.1/topics/http/urls/