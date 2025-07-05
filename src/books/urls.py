from django.urls import path
from . import views
urlpatterns = [
    path('' , views.index , name='index'),
    path('add_book' , views.add_book , name='add_book'),
    path('books' , views.all_books , name='all_books'),
    path('books/delete_all' , views.delete_all_books , name='delete_all_books'),
    path('copies' , views.all_copies , name='copies'),
    path('copies/delete/<int:copy_id>' , views.delete_one_copy , name='delete_one_copy'),
    path('copies/delete/all' , views.delete_all_copies , name='delete_all_copies'),
    path('copies/edit/<int:copy_id>' , views.edit_copy , name='edit_copy'),
    path('add_copy' , views.books , name='books'),
    path('books/delete/<int:book_id>' , views.delete_one_book , name='delete_one_book'),
    path('edit-book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('add_copy/<int:id>' , views.add_copy , name='add_copy'),
    path('loaned_books' , views.loaned_books , name='loaned_books'),
    path('lend_book' , views.lend_book , name='lend_book'),
    path('lend_details/<int:id>' , views.lend_details , name='lend_details'),
    path('end_lend/<int:id>' , views.end_lend , name='end_lend'),
    path('lost_books' , views.lost_books , name='lost_books'),
    path('book_found/<int:id>' , views.book_found , name='book_found'),
]