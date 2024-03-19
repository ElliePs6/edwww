from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import  LoginForm, CustomUserCreationForm
from django.contrib.auth.models import User
from  VacayVue.models import CustomUser  # Import the CustomUser model

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_type = form.cleaned_data['user_type']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if user.user_type == 'employee':  # Access user_type attribute of CustomUser
                    return redirect('employee_home')
                elif user.user_type == 'company':  # Access user_type attribute of CustomUser
                    return redirect('company_home')
            else:
                messages.error(request, 'Invalid username or password.')
                return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'authenticate/login.html', {'form': form})


def employee_home(request):
    return render(request, 'authenticate/login_employee.html')

def company_home(request):
    return render(request, 'authenticate/login_company.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'Είσαι Αποσυνδεμένος')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'company'  # Set user type to 'company'
            user.save()
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'authenticate/register_user.html', {'form': form})

def user_view(request):
    return render(request, 'authenticate/user_view.html')
