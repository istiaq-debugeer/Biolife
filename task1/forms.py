from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from task1.models import Comment,CommentAttachment,Contact
#
#
#
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

class RegisterForm(forms.ModelForm):

    class Meta:
        model=User
        fields=('first_name','last_name','email','username','password')

class Loginform(forms.Form):

    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=30)
    # class Meta:
    #     model=User
    #     fields=('username','password')
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'

class CommentForm(forms.ModelForm):
        class Meta:
            model=Comment
            fields=['textcomment']


class AttachmentForm(forms.ModelForm):
    class Meta:
        model=CommentAttachment
        fields=['attachment']



