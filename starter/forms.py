from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
# from .forms import SignUpForm
from django.shortcuts import render, redirect
from .models import Profile

# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=100, help_text='Last Name')
#     last_name = forms.CharField(max_length=100, help_text='Last Name')
#     email = forms.EmailField(max_length=150, help_text='Email')
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name',
#                   'email', 'password1', 'password2',)
placeholders = {
    'username': forms.TextInput(attrs={'placeholder': 'username'}),
    'CompanyName': forms.TextInput(attrs={'placeholder': 'CompanyName'}),
    'location': forms.TextInput(attrs={'placeholder': 'location'}),
    'type_of_business': forms.TextInput(attrs={'placeholder': 'type_of_business'}),
    'Email': forms.TextInput(attrs={'placeholder': 'Email'}),
}
  
# creating a form  
class InputForm(forms.Form): 
  
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length = 100) 
    username = forms.CharField(max_length = 100) 
    location = forms.CharField(max_length = 200) 
    email = forms.EmailField()
    # password = forms.CharField(max_length = 100) 
    phone_number = forms.IntegerField( 
                     help_text = "Enter your phone number"
                     ) 
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)

# Individual
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='First Name', label='First Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name', label='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email', label='Email')


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', ]
        # widgets = placeholders


# Enterprise

class EnterpriseReg(forms.ModelForm):
    CompanyName = forms.CharField(max_length=100, help_text='Company Name')
    location = forms.CharField(max_length=100, help_text='Location')
    type_of_business = forms.CharField(max_length=150, help_text='Type of Business')
    email = forms.EmailField(max_length=150, help_text='Email')
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Profile
        fields = ['CompanyName', 'location', 'type_of_business',
                  'email', 'password']
        # widgets = placeholders

