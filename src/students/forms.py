from django import forms
from .models import *
class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name' , 'family_name' , 'code' , 'branch']