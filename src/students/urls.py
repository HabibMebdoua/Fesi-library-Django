from django.urls import path
from . import views
urlpatterns = [
    path('' , views.all_students , name='all_students'),
    path('add_student' , views.add_student , name='add_student'),
    path('delete_student/<int:id>' , views.delete_student , name='delete_student'),
    path('delete_all_students' , views.delete_all_students , name='delete_all_students'),
    path('edit_student/<int:student_id>' , views.edit_student, name='edit_student'),
]