from django.urls import path
from . import views
from django.contrib.auth import views as aut_views
urlpatterns = [
    path('register/' , views.register , name='register'),
    path('logout/' , aut_views.LogoutView.as_view(), name='logout'),
    path('login/' , aut_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('retrive_users/' , views.base, name='base'),
]