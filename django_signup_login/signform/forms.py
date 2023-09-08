from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    
    username = forms.CharField(label='',required=True, widget=forms.TextInput(attrs={'class':'input','placeholder':'Username'}))
    email = forms.EmailField(label='',required=True, widget=forms.EmailInput(attrs={'class':'input','placeholder':'Email'}))
    password1 = forms.CharField(label='',required=True, widget=forms.PasswordInput(attrs={'class':'input','placeholder':'Password'}))
    password2 = forms.CharField(label='',required=True, widget=forms.PasswordInput(attrs={'class':'input','placeholder':'Confirm Password'}))

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )