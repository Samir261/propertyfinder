# from django.shortcuts import render
# from .models import User
# from django.http import HttpResponse
# from django.views.generic import CreateView
# from .forms import UserRegisterForm
# from django.contrib.auth import login
# from django.contrib.auth.views import LoginView
# # from django.urls import reverse_lazy
# # from django.views.generic import TemplateView



# # Create your views here.
# # def addUser(request):
    
# #     form = UserRegisterForm()
# #     if request.method == "POST":
# #         form = UserRegisterForm(request.POST or None)
# #         if form.is_valid():
# #             form.save()
# #         return HttpResponse("User registered")  
            
        
#     # return render(request,'user/adduser.html',{'form':form})

# class UserregisterView(CreateView):
#     model=User
#     form_class=UserRegisterForm
#     template_name='user/user_register.html'
#     success_url='/'


# class Userloginview(LoginView):
#     template_name='user/login.html'
#     success_url='/'

#     def get_redirect_url(self):
#         if self.request.user.is_authenticated:
#             if self.request.user:
#                 return '/owner/'
#             else:
#                 return '/customer/'
        
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from .forms import *
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.views import View
from django.views.generic import ListView
from .models import *

# Create your views here.
class User_Registraion_View(CreateView):
     model = User
     form_class = User_Registraion_Form
     template_name = 'userregister.html'
     success_url = '/user/login/'
    
    
    
     def form_valid(self,form):
        #email = form.cleaned_data.get('email')
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)
     
     
class Buyer_Registraion_View(CreateView):
    model = User
    form_class = Buyer_Registraion_Form
    template_name = 'login.html'
    success_url = '/login/'
    
   
    def form_valid(self,form):
        #email = form.cleaned_data.get('email')
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)
    
   

class UserLoginView(LoginView):
    template_name = 'login.html'
    success_url = "/"
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user:
                return "/"
            else:
                return "/"


class UserLoginView1(LoginView):
    template_name = 'login1.html'
    success_url = "/property/create_project/"
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user:
                return  "/property/create_project/"
            else:
                return "/"

def home(request):
    return render(request, 'index.html')
