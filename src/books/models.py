from django.db import models
from students.models import * 



class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)   
    book_catigory=[
        ('Computer Science','Computer Science'),
        ('physics','physics'),
        ('Material science','Material science'),
        ('chemistry','chemistry'),
        ('mathematics','mathematics'),
    ]
    catigory = models.CharField(choices=book_catigory , max_length=255)
    book_type = [
        ('Graduation thesis','Graduation thesis'),
        ('Book','Book'),
        ('Dictionary','Dictionary')
    ]
    type = models.CharField(max_length=255 , choices=book_type , default='Book')
    copies = models.PositiveIntegerField(default=1)
    
    is_taken = models.BooleanField(default=False)
    
    def __str__(self) :
        return self.title
    
class Copy(models.Model):
    book = models.ForeignKey(Book , related_name='book_copy' , on_delete=models.CASCADE)
    serial_number = models.PositiveIntegerField()
    code = models.CharField(max_length=100 , help_text='code / Number ' , default='-----/000')
    is_taken = models.BooleanField(default=False)
    number = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.book.title}  {self.code}'

class LendBook(models.Model):
    copy = models.ForeignKey(Copy , related_name='lend_copy' , on_delete=models.CASCADE)
    student = models.ForeignKey(Student , related_name='lend_student' , on_delete=models.CASCADE)
    from_date = models.DateField(auto_now_add=True)
    to_date = models.DateField()

    def __str__(self) :
        return self.copy.book.title
    
class LostLend(models.Model):
    lend = models.ForeignKey(LendBook , related_name='lost_lend' , on_delete=models.CASCADE)


