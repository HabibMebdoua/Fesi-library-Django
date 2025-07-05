import django_filters
from .models import *

class BooksFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Book
        fields = ['title','author','catigory','type']


class CopiesFilter(django_filters.FilterSet):
    class Meta:
        model = Copy
        fields = ['book','serial_number','code']

# class CopyFilter(django_filters.FilterSet):
#     class Meta:
#         model = Copy
#         fields = ['code']


class LoandBooksFilter(django_filters.FilterSet):
    class Meta:
        model = LendBook
        fields = ['copy','student']