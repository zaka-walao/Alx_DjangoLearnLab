## Models and Django ORM
This concept page aims to introduce the concept of models in Django, the Django Object-Relational Mapping (ORM) system, and how to configure the database for your Django project. 

It covers the purpose of models, their structure, how they interact with the database using the ORM, and the steps to set up a database connection in Django.

### **My personal Note**
In Django, models are Python classes that define the structure and behavior of the data in your application.

 They represent the database schema and are used to interact with the database. Each model corresponds to a single table in the database, and each attribute of the model represents a database field.


 Django models handle CRUD operations (Create, Read, Update, Delete) and offer an easy-to-use API to interact with the database.
## Concept Overview
### Topics


- **Models and Their Structure**
- **Django ORM: Object-Relational Mapping**
- **Database interaction with the Django ORM**
- **Configuring the Database**

## Learning Objectives
- Understand the purpose and structure of Django models
- Learn about the Django ORM and its benefits
- Create and manipulate models using the Django ORM
- Query the database using the Django ORM
- Configure a database connection in Django for MySQL and set up the required database driver for the MySQL database engine
- Apply database migrations to create or update tables based on model definitions


## Models and Their Structure
In Django, **models are defined as Python classes** that inherit from the `django.db.models.Model base class`.

Each attribute of the model represents a `database field`, and its type is defined using field classes provided by Django (e.g., CharField, IntegerField, DateField, etc.).

In the below example, the `Book` model has three fields: `title`, `author`, and `published_date`.

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

```

## Some of the most common fields are:
- **CharField:** This field is used to store text-based data with a limited number of characters. It takes a max_length parameter that specifies the maximum length of the string.

- **TextField:** This field is used to store large amounts of text data without any length restriction.

- **IntegerField:** This field is used to store integer values.

- **FloatField:** This field is used to store floating-point numbers.

- **DecimalField:** This field is used to store precise decimal values, often used for representing monetary values.

- **BooleanField:** This field is used to store boolean (True/False) values.

- **DateField:** This field is used to store date values.

- **EmailField:** This field is a subclass of CharField and is used to store email 
addresses. It provides basic validation for email formats.


These are just a few examples of the many field classes provided by Django. Each field class has its own set of options and validation rules that you can customize based on your requirements. 


Additionally, Django allows you to create custom field classes by subclassing the existing field classes or creating entirely new field classes to suit your specific needs.

## Django ORM: Object-Relational Mapping
The Django ORM (Object-Relational Mapping) provides an `abstraction layer` that allows `developers to interact with the database using Python code instead of writing raw SQL queries. `

It `automatically handles tasks` like creating database tables based on model definitions, performing database migrations, and executing CRUD (Create, Read, Update, Delete) operations.

## Benefits of using the Django ORM include:

**Database abstraction:** Developers can work with Python objects instead of writing SQL queries directly.

**Portability:** The ORM supports multiple database engines (e.g., SQLite, PostgreSQL, MySQL, Oracle) with minimal code changes.

**Database Schema:** Automatic handling of database schema changes through migrations.

**Powerful Queries:** Supports powerful querying capabilities with a Pythonic syntax.


## Database Interaction with the Django ORM
The Django ORM provides a rich query API that allows developers to retrieve, filter, and manipulate data in the database using Python code. 


It supports complex queries, including joins, aggregations, and annotations, making it a powerful tool for working with relational databases.

```python

## literrally the Book class and book objects
# Retrieving all books
books = Book.objects.all()

# Filtering books by author
books_by_author = Book.objects.filter(author='John Doe')

# Ordering books by published date
books_ordered = Book.objects.order_by('published_date')

# Creating a new book
new_book = Book(title='New Book', author='Jane Smith', published_date='2023-01-01')
new_book.save()

```

## Configuring the Database
By default, Django uses SQLite, a lightweight file-based database, for development environments. However, for production environments, 

it’s recommended to use a more robust database engine like PostgreSQL, MySQL, or Oracle. Django supports multiple database engines and provides a straightforward way to configure the database settings.

Configuring the database settings in Django involves modifying the DATABASES setting in the `settings.py file.` Here’s an example of how to configure a MySQL database:

```json
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

```
In this example, we’re configuring the `default` database connection with the following settings:

- `ENGINE:` The database engine to use (django.db.backends.mysql for MySQL).
- `NAME: `The name of the database (mydatabase).
- `USER:` The username to connect to the database (mydatabaseuser).
- `PASSWORD:` The password for the database user (mypassword).
- `HOST:` The hostname or IP address of the database server (localhost for a local server).
- `PORT:` The port number for the database server (3306 is the default for MySQL).

After configuring the database settings, you’ll need to install the appropriate database driver for MySQL. You can install the MySQL driver using pip:

`pip install mysqlclient`

Once the database is configured, Django will automatically create the necessary tables based on your model definitions when you run the `migrate` command:

`python manage.py migrate`


This command applies any pending database migrations, creating or updating tables and columns as needed based on your model changes.

Note: Make sure you have a MySQL server running and accessible, and that you have the necessary permissions to create a new database and user. The Django documentation provides more detailed instructions for setting up different database engines.'

https://docs.djangoproject.com/en/5.0/topics/db/models/

https://docs.djangoproject.com/en/5.0/topics/db/queries/

https://docs.djangoproject.com/en/5.0/intro/tutorial02/

https://docs.djangoproject.com/en/5.0/ref/databases/#database-drivers

