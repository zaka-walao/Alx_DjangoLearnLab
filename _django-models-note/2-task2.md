## Implementing User Authentication in Django


**Objective:** Develop the ability to manage user authentication within a Django application. This task focuses on setting up user login, logout, and registration functionalities using Django’s built-in authentication system.

## Task Description:
Enhance your `relationship_app` by adding user authentication features. Implement views and templates for user login, logout, and registration to demonstrate how Django manages user sessions and permissions.

## Steps:
1. Setup User Authentication Views:

   - Utilize Django’s built-in views and forms for handling user authentication. You will need to create views for user login, logout, and registration.
2. Create Templates for Authentication:

    - Provide HTML templates for each authentication action (login, logout, and registration). Templates will be provided, allowing you to focus on backend integrations.
3. Configure URL Patterns:

    - Define URL patterns in relationship_app/urls.py to link to the authentication views.
4. Test Authentication Functionality:

    - Ensure that users can register, log in, and log out.

## Provided HTML Templates:
**Login Template (`login.html`):**

```python

<!-- login.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
    <h1>Login</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Login</button>
    </form>
    <a href="{% url 'register' %}">Register</a>
</body>
</html>

```
**Logout Template (`logout.html`):**
```python
<!-- logout.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Logout</title>
</head>
<body>
    <h1>You have been logged out</h1>
    <a href="{% url 'login' %}">Login again</a>
</body>
</html>


```
**Registration Template (register.html):**

```python
<!-- register.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Register</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
    <h1>Register</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Register</button>
    </form>
</body>
</html>


```
## Repo:

- GitHub repository: `Alx_DjangoLearnLab`
- Directory: `django-models`