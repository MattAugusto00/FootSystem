from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Transfer

# register/create a user

class CreateUserForm(UserCreationForm):

  class Meta:

    model = User
    fields = ['username', 'password1', 'password2']


# login a user

class LoginForm(AuthenticationForm):

  username = forms.CharField(widget=TextInput())
  password = forms.CharField(widget=PasswordInput())


# create a record
class CreateTransferForm(forms.ModelForm):
  class Meta:

    model = Transfer
    fields = ['player', 'origin_club', 'destiny_club', 'value']


# update a record
class UpdateTransferForm(forms.ModelForm):
  class Meta:

    model = Transfer
    fields = ['player', 'origin_club', 'destiny_club', 'value']
 