from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *
from .filters import *

def all_students(request):
    students = Student.objects.all()

    #Filter Part
    filter = StudentsFilter(request.GET , queryset=students)
    students = filter.qs

    context = {
        'students':students,
        'filter':filter
    }
    return render(request , 'students/all_students.html' , context)

def add_student(request):
    form = AddStudentForm()
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request , 'Student added')
            redirect('add_student')
        else:
            messages.warning(request , 'Invalid informations')
    else:
        form = AddStudentForm()
        
       

    context={
        'form':form,
    }
    return render(request , 'students/add_student.html',context)


def delete_student(request , id):
    student = Student.objects.get(id=id)
    student.delete()
    messages.info(request , 'Student deleted')
    return redirect('all_students')


def delete_all_students(request):
    students = Student.objects.all()
    students.delete()
    messages.info(request , 'All students deleted successfuly')
    return redirect('all_students')

def edit_student(request , student_id):
    student = get_object_or_404(Student , id=student_id)
    if request.method == 'POST':
        student.first_name = request.POST.get('first_name')
        student.family_name = request.POST.get('family_name')
        student.branch = request.POST.get('branch')
        student.code = request.POST.get('code')
        student.save()
        messages.success(request, "Student updated successfully!")
        return redirect('all_students')  # Redirect to students page after update
    
    context = {
        'student' : student,
    }

    return render(request ,'students/all_students.html' , context)