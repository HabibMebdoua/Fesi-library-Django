
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('books.urls')),
    path('students/' , include('students.urls')),
    path('users/' , include('users.urls'))
]
