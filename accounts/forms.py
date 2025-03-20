from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'password1', 'password2']
