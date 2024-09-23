from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Item

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    username = forms.CharField(label='username',widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1 = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'placeholder':'Re-Type Password'}))
    email = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder':'Email'}))


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['name', 'image']
