from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    family_name = models.CharField(max_length=255)
    code = models.PositiveIntegerField()
    student_branch=[
        ('Computer Science','Computer Science'),
        ('physics','physics'),
        ('Material science','Material science'),
        ('chemistry','chemistry'),
        ('mathematics','mathematics'),
    ]
    branch = models.CharField(max_length=255 , choices=student_branch)
    date = models.DateField(auto_now_add=True)

    def __str__(self) :
        return f'{self.first_name}   {self.family_name}   {self.code}'

