from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import *
from .filters import *
from students.models import *
from .forms import *
import datetime
from django.core.paginator import Paginator
import random
def index(request):
    books = Copy.objects.all().order_by('id')[0:3]
    context = {
        'books':books
    }
    return render(request , 'books/index.html',context)

def add_book(request):
    form = AddBookFrom()
    if request.method == 'POST':
        form = AddBookFrom(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request , 'Book added')
            redirect('add_student')
        else:
            messages.warning(request , 'Invalid informations')
    else:
        form = AddBookFrom()
        
    context={
        'form':form,
    }
    return render(request , 'books/add_book.html',context)

def books(request):
    books = Book.objects.all()
    filter = BooksFilter(request.GET , queryset=books)
    books = filter.qs
    context = {
        'books':books,
        'filter':filter
    }
    return render(request , 'books/books.html',context)


def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.catigory = request.POST.get('catigory')
        book.type = request.POST.get('type')
        book.copies = request.POST.get('copies')
        book.save()
        messages.success(request, "Book updated successfully!")
        return redirect('books')  # Redirect to books page after update
    context = {
        'book':book
    }
    return render(request, 'books/books.html', context)


def add_copy(request , id):
    add_copy_form = AddCopyFrom()
    book = get_object_or_404(Book , id = id)
    # getting nubmer of copies 
    copies_number = Copy.objects.filter(book=book).count()
    if copies_number == None:
        copies_number = 1
    else:
        copies_number +=1

    if request.method == 'POST':
        add_copy_form = AddCopyFrom(request.POST)
        if add_copy_form.is_valid():
            if copies_number <= book.copies:
                copy = add_copy_form.save(commit=False)
                copy.book = book
                copy.number = copies_number
                add_copy_form.save()
                messages.success(request , 'Copy added')
            else:
                messages.warning(request , 'Copies are full')
    else:
        add_copy_form = AddCopyFrom()

    context = {
        'form':add_copy_form
    }
    return render(request , 'books/add_copy.html' , context)


def all_books(request):
    books = Copy.objects.all()

    if request.method == 'GET':
        title = None
        author = None
        type = None
        catigory = None
        if 'title' or 'author' or 'catigory' or 'type' in request.GET:
            title = request.GET.get('title')
            author = request.GET.get('author')
            type = request.GET.get('type')
            catigory = request.GET.get('catigory')

            #creating a  dynamic filter
            # Create an empty filter dictionary
            filter_conditions = {}
            if title:
                filter_conditions['book__title__icontains'] = title
            if catigory:
                filter_conditions['book__catigory'] = catigory
            if type:
                filter_conditions['book__type'] = type
            if author:
                filter_conditions['book__author'] = author

            books = Copy.objects.filter(**filter_conditions)
               

    # Paginator Part
    paginator = Paginator(books, 40)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    
    context = {
        'books':page_obj,
        'filter':filter
    }
   
    return render(request , 'books/all_books.html',context)


def delete_all_books(request):
    books = Book.objects.all()
    books.delete()   
    messages.info(request , 'All books deleted successfuly')
    return redirect('books')


def delete_one_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    messages.info(request , 'Book Deleted')
    return redirect('books')


def all_copies(request):
    copies = Copy.objects.all()
    filter = CopiesFilter(request.GET , queryset=copies)
    copies = filter.qs


    context = {
        'copies':copies,
        'filter':filter,
    }
    return render(request , 'books/all_copies.html',context)

def delete_one_copy(request , copy_id):
    copy = get_object_or_404(Copy , id=copy_id)
    copy.delete()
    messages.info(request , 'Copy has been deleted successfuly')
    return redirect('copies')

def delete_all_copies(request):
    copies = Copy.objects.all()
    copies.delete()
    messages.info(request , 'All copies has been deleted successfuly')
    return redirect('copies')


def edit_copy(request , copy_id):
    copy = get_object_or_404(Copy , id=copy_id)
    if request.method == 'POST':
        copy.serial_number = request.POST.get('number')
        copy.code = request.POST.get('code')
        copy.save()
        messages.success(request , 'Copy updated successfuly!')
        return redirect('copies')
    context = {
        'copy':copy,
    }
    return render(request , 'books/all_copies.html',context)


def lend_book(request):
    # for the auto complete
    all_copies = Copy.objects.all()
    all_students = Student.objects.all()

    if request.method == 'POST':
        # getting data from template
        student_code = request.POST['student-code']
        copy_code = request.POST['copy-code']
        to_date = request.POST['to-date'] 
        try:
            #getting student 
            student = Student.objects.get(code=student_code)
            print('='*100)
            # getting copy
            copy = Copy.objects.get(code=copy_code)
            #chek the number of book copies (it must be greater than 1)
            if copy.book.copies > 1 and copy.is_taken == False:
                #creating a new object in the model (Lend a book)
                loan = LendBook.objects.create(
                copy = copy,
                student = student,
                to_date = to_date, 
                )  
                #decrese book copies
                copy.book.copies -= 1 
                copy.book.save()
                # copie is taken
                copy.is_taken = True
                copy.save()
                messages.success(request , 'Loan added')   
            else:
                if copy.is_taken == True:
                    messages.warning(request , 'This book is already taken')
                else:
                    messages.warning(request , 'Can not lend this book it has only one copie')
        except:
            messages.warning(request , 'Invalid informations')

        return redirect('lend_book')
    
    context = {
        'copies':all_copies,
        'students':all_students
    }
    return render(request , 'books/lend_book.html',context)


def lend_details(request , id):
    lend = get_object_or_404(LendBook , id=id)
    context = {
        'lend':lend
    }
    return render(request , 'books/lend_details.html',context)

def end_lend(request , id):
    lend = LendBook.objects.get(id=id)
    #increase book copies by one
    lend.copy.book.copies +=1
    lend.copy.book.save()
    # disable is taken
    lend.copy.is_taken = False
    lend.copy.save()

    lend.delete()
    messages.info(request , 'Lend inded')
    return redirect('loaned_books')
    
def loaned_books(request):
    books = LendBook.objects.all()
    #Filter Part
    filter = LoandBooksFilter(request.GET , queryset=books)
    books = filter.qs

    context = {
        'books':books,
        'filter':filter
    }
    return render(request , 'books/loaned_books.html', context)




def lost_books(request):
   
    overdue_lends = LendBook.objects.filter(to_date__lt=datetime.date.today())
    
    for lend in overdue_lends:
        if not LostLend.objects.filter(lend=lend).exists():
            LostLend.objects.create(lend=lend)
    
    # Get all lost lends
    lost_lends = LostLend.objects.all()

    context = {
        'lost_lends': lost_lends,
    }
    return render(request, 'books/lost_books.html', context)


def book_found(request , id):
    lost_lend = LostLend.objects.get(id=id)
    lost_lend.delete()
    messages.info(request , 'Done')
    return redirect('lost_books')
