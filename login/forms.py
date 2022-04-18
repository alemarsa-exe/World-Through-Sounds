from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    userId = forms.IntegerField()
    name = forms.CharField(max_length=50)
    role = forms.CharField(max_length=10)
    
    class Meta:
        model = User
        fields = ('userId', 'role', 'name', 'password1', 'password2') 