from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailInput, PasswordInput,ModelForm
#
from task1.models import Register,Comment,CommentAttachment,Contact
#
#
#
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

class CommentForm(ModelForm):
        class Meta:
            model=Comment
            fields=['textcomment']


class AttachmentForm(ModelForm):
    class Meta:
        model=CommentAttachment
        fields=['attachment']



