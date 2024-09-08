from django import forms
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email',)

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
