from django import forms
from django.forms import ModelForm
from .models import Request,CustomUser,Company,Employee
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404



CustomUser = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=(('employee', 'Employee'), ('company', 'Company')), required=True)



class RegisterEmployeeForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control','placeholder': 'Email'}))
    join_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date','placeholder': 'Ημερομηνία Πρόσληψης', 'id': 'join_date'}))
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'data-toggle': 'tooltip', 'placeholder': 'Κωδικός','title': 'Your password must contain at least 8 characters and cannot be too similar to your other personal information.'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'data-toggle': 'tooltip','placeholder': 'Επιβεβαίωση Κωδικού','title': 'Please enter the same password for verification.'})
    )
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Όνομα'}))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Επίθετο'}))
    
    
   

    class Meta:
        model = CustomUser
        fields = ['email', 'join_date', 'password1', 'password2', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email
        user.user_type = 'employee'
        if commit:
            user.save()
            employee=Employee.objects.create(
            user=user,#1 user is employee user
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            join_date=self.cleaned_data['join_date'],
            )
           

        return employee



class RequestForm(ModelForm):
    type = forms.ChoiceField(choices=Request.REQUEST_TYPES_CHOICES)

    class Meta:
        model = Request
        fields = ["type", "start", "end", "description"]  # Include all fields here
        widgets = {
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Περιγραφή Αιτήσεως",
                }
            ),
            "start": forms.DateInput(
                attrs={
                    'class': 'form-control datepicker',
                    'placeholder': 'Ημερομηνία Έναρξης',
                    'type': 'date'
                }
            ),
            "end": forms.DateInput(
                attrs={
                    'class': 'form-control datepicker',
                    'placeholder': 'Ημερομηνία Λήξης',
                    'type': 'date'
                }
            )
        }
      
