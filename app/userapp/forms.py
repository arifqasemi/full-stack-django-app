from django import forms
from userapp.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.ModelForm):
    email = forms.CharField(max_length=254, error_messages={'required': 'email is required'})
    password = forms.CharField(widget=forms.PasswordInput(), error_messages={'required': 'Password is required'})

    class Meta:
        model = User
        fields = ("email", "password")
        
        
        
class RegisterForm(UserCreationForm):
    username=forms.CharField(required=False)
    email=forms.EmailField(required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email','password1','password2']