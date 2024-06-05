from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Record

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


#----------------------------------------------------------------------------------
# - register/create a user

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')




#----------------------------------------------------------------------------------
# - login a user


class LoginForm(forms.Form):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())




#----------------------------------------------------------------------------------
#Create record form

class AddRecordForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country')




#----------------------------------------------------------------------------------
#Update record form

class UpdateRecordForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country')