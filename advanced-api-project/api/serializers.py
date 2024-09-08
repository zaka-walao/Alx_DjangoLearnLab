from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# Book serializer to serialize all fields of the book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    # Validating publication year to acertain that it's not in the future
    def validate_book(self, data):
        publication_year = data.get('publication_year')
        current_year = datetime.now().year

        # Checking validity of the publication_year data
        if publication_year > current_year:
            raise serializers.ValidationError({
                'publication_year': 'Publication year cannot be in the future.'
            })

        return data

# Author serializer to serialize the name of the author, and to dynamically serialize the related comments 
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ["name", "books"]
