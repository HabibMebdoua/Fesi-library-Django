from django import forms
from .models import *


# class LendBookForm(forms.ModelForm):
#     to_date = forms.DateField(widget=forms.DateInput,required=True)
#     class Meta:
#         model = LendBook
#         fields = ['book' , 'student' , 'to_date']


class AddBookFrom(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title' , 'author' ,'copies', 'catigory','type'] 

class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title' , 'author' ,'copies', 'catigory','type']
        
class AddCopyFrom(forms.ModelForm):
    class Meta:
        model = Copy
        fields = ['serial_number' , 'code'] 

