from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField


class Register_User(UserCreationForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'type strong password'}))
    password2 = forms.CharField(
        label='Password(again)', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'confirm password'}))

    class Meta:
        model = User
        fields = ['username',  'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name',
                  'last_name': 'Last Name', 'email': 'Email', }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'type   valid email'}), }


class Login_Form(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-input', 'placeholder': 'username'}))
    password = forms.CharField(label='Password', strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'password'}))
