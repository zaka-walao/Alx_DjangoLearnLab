##  Implementing Advanced Model Relationships in Django

**Objective:** Master Django’s ORM capabilities by creating a set of models that demonstrate the use of `ForeignKey`, `ManyToMany`, and `OneToOne` relationships. 

This task will help you understand how to model complex data relationships in a Django project effectively.

## Task Description:
Duplicate the previous project directory `Introduction_ to_ Django`, rename it to `django-models` and add a new app named `relationship_app` where you’ll define models that showcase complex relationships between entities using `ForeignKey`, `ManyToMany`, and `OneToOne` fields.

## Steps:
1. **Create the `relationship_app` App:**

    - Within your Django project directory, generate a new app: python manage.py startapp relationship_app.

2. **Define Complex Models in `relationship_app/models.py:`**

    - Author Model:
      - `name:` CharField.
    - Book Model:
       - `title:` CharField.
       - `author:` ForeignKey to `Author`.
    - Library Model:
       - `name:` CharField.
       - `books:` ManyToManyField to `Book`.
    - Librarian Model:
       - `name:` CharField.
       - `library:` OneToOneField to `Library.`
3.  **Apply Database Migrations:**

    - Run migrations to create your model tables: `python manage.py makemigrations relationship_app` followed by `python manage.py migrate.`
 4. Implement Sample Queries:
    - Prepare a Python script `query_samples.py` in the `relationship_app` directory. This script should contain the query for each of the following of relationship:
       - Query all books by a specific author.
       - List all books in a library.
       - Retrieve the librarian for a library.

## Repo:

- GitHub repository: `Alx_DjangoLearnLab`
- Directory: `django-models`
- File: `models.py`, `query_samples.py`