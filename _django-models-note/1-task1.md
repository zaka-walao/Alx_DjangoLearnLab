##  Django Views and URL Configuration

**Objective:** Develop proficiency in creating both function-based and class-based views in Django, and configuring URL patterns to handle web requests effectively. 

This task will help you understand different ways to define views and manage URL routing in Django.

## Task Description:
In your existing Django project, enhance the `relationship_app` by adding new views that display information about books and libraries. 

Implement both function-based and class-based views to handle these displays and configure the URL patterns to route these views correctly.

## Steps:
1. Implement Function-based View:

    - Create a function-based view in `relationship_app/views.py` that lists all books stored in the database.
    - This view should render a simple text list of book titles and their authors.
2. Implement Class-based View:

   - Create a class-based view in `relationship_app/views.py` that displays details for a specific library, listing all books available in that library.
   - Utilize Django’s ListView or DetailView to structure this class-based view.
3. Configure URL Patterns:

   - Edit `relationship_app/urls.py` to include URL patterns that route to the newly created views. Make sure to link both the function-based and class-based views.
4. Create Templates (Optional for Display):

   - For a more structured output, using the code below as templates for each view to render the information in HTML format instead of plain text.


## Template for Listing Books (list_books.html):
This template will be used by the function-based view to display a list of all books.

```python
<!-- list_books.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>List of Books</title>
</head>
<body>
    <h1>Books Available:</h1>
    <ul>
        {% for book in books %}
        <li>{{ book.title }} by {{ book.author.name }}</li>
        {% endfor %}
    </ul>
</body>
</html>

```
## Template for Displaying Library Details (library_detail.html):

This template will be used by the class-based view to show details of a specific library, including all books available in that library.

```python
<!-- library_detail.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Library Detail</title>
</head>
<body>
    <h1>Library: {{ library.name }}</h1>
    <h2>Books in Library:</h2>
    <ul>
        {% for book in library.books.all %}
        <li>{{ book.title }} by {{ book.author.name }} (Published {{ book.publication_year }})</li>
        {% endfor %}
    </ul>
</body>
</html>

```

## Repo:

- GitHub repository: Alx_DjangoLearnLab
- Directory: django-models



## Solution

To achieve the objective of developing proficiency in creating both function-based and class-based views in Django and configuring URL patterns effectively, follow the detailed steps below:

### 1. **Implement Function-Based View (FBV)**

A function-based view (FBV) in Django is a Python function that takes a web request and returns a web response. To create an FBV that lists all books, you will render a simple text list of book titles and their authors.

#### Steps to Create the Function-Based View

1. **Open** `relationship_app/views.py`.

2. **Add** the function-based view to list all books:

   ```python
   from django.shortcuts import render
   from .models import Book

   def book_list_view(request):
       """
       A function-based view to list all books with their titles and authors.
       """
       books = Book.objects.all()  # Retrieve all book objects from the database
       context = {'books': books}  # Pass the books to the template context
       return render(request, 'relationship_app/book_list.html', context)
   ```

3. **Create a Template** `book_list.html` in `relationship_app/templates/relationship_app/`:

   ```html
   <!-- book_list.html -->
   <h1>Book List</h1>
   <ul>
   {% for book in books %}
       <li>{{ book.title }} by {{ book.author.name }}</li>
   {% endfor %}
   </ul>
   ```

### 2. **Implement Class-Based View (CBV)**

A class-based view (CBV) in Django allows more functionality with less code by using object-oriented programming principles. Here, we will use Django's `DetailView` to display details for a specific library, including a list of all books available in that library.

#### Steps to Create the Class-Based View

1. **Open** `relationship_app/views.py`.

2. **Add** the class-based view for library details:

   ```python
   from django.views.generic import DetailView
   from .models import Library

   class LibraryDetailView(DetailView):
       """
       A class-based view to display details of a specific library, including all books.
       """
       model = Library
       template_name = 'relationship_app/library_detail.html'
       context_object_name = 'library'
   ```

3. **Create a Template** `library_detail.html` in `relationship_app/templates/relationship_app/`:

   ```html
   <!-- library_detail.html -->
   <h1>{{ library.name }}</h1>
   <h2>Books available in this library:</h2>
   <ul>
   {% for book in library.books.all %}
       <li>{{ book.title }} by {{ book.author.name }}</li>
   {% endfor %}
   </ul>
   ```

### 3. **Configure URL Patterns**

To link these views to URLs, you'll need to configure the URL patterns in `relationship_app/urls.py`.

#### Steps to Configure URL Patterns

1. **Open** `relationship_app/urls.py`.

2. **Edit** the file to include the URL patterns for both views:

   ```python
   from django.urls import path
   from .views import book_list_view, LibraryDetailView

   urlpatterns = [
       path('books/', book_list_view, name='book-list'),  # URL pattern for the function-based view
       path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),  # URL pattern for the class-based view
   ]
   ```

### **Summary of What We Did**

- **Function-Based View** (`book_list_view`): This view lists all books and their authors. We used `Book.objects.all()` to fetch all books from the database and passed them to a template that renders each book’s title and author.

- **Class-Based View** (`LibraryDetailView`): This view displays details for a specific library, including all books available in that library. We used Django's `DetailView` to automatically handle retrieving a single `Library` instance and passed it to a template that lists the library's books.

- **URL Configuration**: We set up URL patterns in `urls.py` to map specific URLs to our views. The pattern for `book_list_view` uses a fixed path (`books/`), while the pattern for `LibraryDetailView` uses a dynamic segment (`<int:pk>/`) to capture the primary key of the library.

By following these steps, you have implemented both function-based and class-based views and configured URL patterns to handle web requests effectively in Django.