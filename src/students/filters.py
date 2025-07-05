import django_filters
from .models import *

class StudentsFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['code','branch']