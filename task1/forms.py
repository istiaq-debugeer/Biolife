from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailInput, PasswordInput,ModelForm

from task1.models import Contact,Register



class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

class RegisterForm(ModelForm):

    class Meta:
        model=Register
        fields='__all__'


class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields='__all__'