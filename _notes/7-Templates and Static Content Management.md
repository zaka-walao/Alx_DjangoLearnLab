
## Templates and Static Content Management

This concept page introduces Django templates and the management of static content within Django projects.

 It covers the creation and utilization of templates for rendering dynamic web pages, as well as the handling of static files such as CSS, JavaScript, and images.

## Concept Overview
## Topics
- Django Templates
- Template Language
- Template Inheritance
- Static Files Management


## Learning Objectives
- Understand the role of templates in generating dynamic web content
- Learn the syntax and features of Django’s template language
- Explore template inheritance and its benefits for code reuse and organization
- Master the management of static files in Django projects, including CSS, JavaScript, and images


## Django Templates
In Django, templates are `text files `that define the `structure and presentation of data` for web pages. 

They separate the presentation logic from the application logic, allowing developers to create reusable and maintainable code. Templates provide a way to `generate dynamic HTML` by interpolating data from the `application’s views and models.`


My comment - In short, templates get data from the app logic which is from the app views and app models.



## Template Language
Django’s template language provides a set of tags, filters, and variables for manipulating and displaying dynamic data within templates. 

Templates can access and display data passed from views using variable interpolation `({{ variable }})` and can execute loops and conditional statements using template tags `({% tag %})`.


Tags such as `{% for %}`, `{% if %}`, and `{% include %}` allow for control flow and template inclusion, while filters like `{{ value|date }}` and `{{ value|truncatechars:30 }}` modify the displayed data.


```python

<!-- book_list.html -->
<h1>Book List</h1>
<ul>
{% for book in book_list %}
  <li>{{ book.title }} by {{ book.author }}</li>
{% endfor %}
</ul>
```

## My code explanation

The `book_list.html` template you’ve provided is a simple Django template used to display a list of books. Let’s break down how it works:

### **Template Structure and Context**

- **`<h1>Book List</h1>`**: This is an HTML heading that will display "Book List" as the title of the page.
  
- **`<ul>`**: This tag creates an unordered list in HTML. Each book in the list will be represented as a list item (`<li>`).

- **`{% for book in book_list %}`**: This is a Django template tag that starts a for loop. It iterates over a list of books, which is expected to be passed to the template as a context variable named `book_list`.

- **`<li>{{ book.title }} by {{ book.author }}</li>`**: This line creates a list item (`<li>`) for each book. It displays the title of the book followed by the author's name. The double curly braces (`{{ }}`) are used to output the values of `book.title` and `book.author` in the HTML.

- **`{% endfor %}`**: This marks the end of the for loop.

### **How the Template is Rendered**

- **Context Data**: The view that renders this template should pass a context variable named `book_list`, which is a list or queryset of `Book` objects. Each `Book` object should have attributes like `title` and `author` that can be accessed within the loop.

### **Example of a View That Uses This Template**

Here’s how you might set up a Django view to render this template:

```python
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'books/book_list.html', {'book_list': books})
```

- **`Book.objects.all()`**: This retrieves all `Book` objects from the database.
- **`render(request, 'books/book_list.html', {'book_list': books})`**: This renders the `book_list.html` template, passing the list of books as the context variable `book_list`.

### **How It Works:**

- When a user navigates to the URL that maps to `book_list`, the view retrieves all books from the database and passes them to the `book_list.html` template.
- The template then iterates over each book in `book_list`, displaying the title and author of each one within an unordered list.

### **Resulting HTML:**

If you have two books in your database with the following details:

1. "The Great Gatsby" by F. Scott Fitzgerald
2. "1984" by George Orwell

The rendered HTML will look like this:

```html
<h1>Book List</h1>
<ul>
  <li>The Great Gatsby by F. Scott Fitzgerald</li>
  <li>1984 by George Orwell</li>
</ul>
```

This HTML will be sent to the user’s browser and displayed as a simple list of books.


## Template Inheritance
Template inheritance is a powerful feature in Django that allows you to create a base template with common elements and extend it with child templates for specific pages. This promotes code reuse and consistency across your web application.

```python
<!-- base.html -->
<html>
  <head>
    <title>{% block title %}My Site{% endblock %}</title>
  </head>
  <body>
    {% block content %}{% endblock %}
  </body>
</html>

<!-- book_list.html -->
{% extends 'base.html' %}
{% block title %}Book List{% endblock %}
{% block content %}
  <h1>Book List</h1>
  <ul>
    {% for book in book_list %}
      <li>{{ book.title }} by {{ book.author }}</li>
    {% endfor %}
    </ul>
{% endblock %}

```

## Template Tags and Filters
Django provides a rich set of built-in template tags and filters for common tasks like looping, conditional rendering, URL generation, and string formatting. You can also create custom template tags and filters to extend the fun.

`<a href="{% url 'book-detail' book.id %}">{{ book.title|truncatechars:30 }}</a>`


## Static Files Management
Django provides built-in tools for managing static files such as CSS, JavaScript, and images. Static files are typically stored in the `static` directory within Django apps and are served directly by the web server in production for improved performance.

```py
<!-- base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}My Site{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <!-- Content -->
    <script src="{% static 'js/script.js' %}"></script>
</body>
</html>


```

In this example, `{% static %}` template tag is used to include static files like CSS and JavaScript in the HTML template. These files are stored in the static directory of the app and are referenced using the `{% static %} tag`.

- Django Templates - https://docs.djangoproject.com/en/5.1/topics/templates/
- Template Syntax - https://docs.djangoproject.com/en/5.1/ref/templates/language/
- Template Inheritance - https://docs.djangoproject.com/en/5.1/ref/templates/language/#template-inheritance
- Built-in Template Tags and Filters - https://docs.djangoproject.com/en/5.1/ref/templates/builtins/

- Managing Static Files - https://docs.djangoproject.com/en/5.1/howto/static-files/