import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['exact', 'icontains'],
            'author__name': ['exact', 'icontains'],  # Filtering by author's name
            'publication_year': ['exact', 'gte', 'lte'],  # Exact, ≥, ≤ filters
        }