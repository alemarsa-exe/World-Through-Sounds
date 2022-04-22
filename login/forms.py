from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    #email = forms.EmailField(required=True)
    #username = forms.CharField(max_length=50, required=True)
    #password = forms.CharField(max_length=10, required=True)

    '''def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields.pop('password2')'''
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2') 