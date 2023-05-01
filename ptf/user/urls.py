from django.contrib import admin
from django.urls import path,include
from user.views import  User_Registraion_View, UserLoginView,UserLoginView1
from user import views
from django.contrib.auth.views import LogoutView



urlpatterns = [

   path('adduser/',User_Registraion_View.as_view(),name='userregister'),
   path('login/',UserLoginView.as_view(),name='login'),
   path('login1/',UserLoginView1.as_view(),name='login'),
   
]