This project is my third to build using Django


# Permissions

I have included permissions to the views can_create, delete, edit_book that restricts only users in authorized groups can access the views


# Advanced security features implemented

Ensured protection against CSRF, XSS, SQL injection by updating the settings file accordingly and updating the security measure like securing https and redirecting non-https to https  to avoid click-baiting.

Updated templates by adding CSRF token to protect against CSRF
Used ORM instead of text scripting to prevent XSS
Ensured form validation in the views