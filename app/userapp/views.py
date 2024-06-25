from django.shortcuts import render,HttpResponse,redirect
from django.views import View
# Create your views here.
from userapp.forms import LoginForm,RegisterForm;
from userapp.models import User
from django.contrib.auth import authenticate,login
class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request,"userapp/login.html",{'form':form})
    
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request,username=email,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                error_message = "Invalid username or password. Please try again."

        else:
            error_message = "Form validation failed. Please check your input."
        return render(request,"userapp/login.html",{'form':form,'error_message':error_message})
    
    
    
    
class RegisterView(View):
    def get(self,request):
        form = RegisterForm
        return render(request,'userapp/register.html',{'form':form})
    
    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User()
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('login')
        else:
            form = RegisterForm
        return render(request,'userapp/register.html',{'form':form})
        
        
        
class HomeView(View):
    def get(self,request):
        return HttpResponse('this home')