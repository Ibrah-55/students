from django import forms
from django.core import validators
def check_size(value):
    if len(value) < 6:
        raise forms.ValidationError("The Password is too short")
class Signup(forms.Form):
    first_name=forms.CharField(initial='First Name', max_length=255, required=True)
    last_name=forms.CharField(initial='Last Name', max_length=255)
    email=forms.EmailField(help_text='Write your email here')
    address=forms.CharField(required=False)
    age=forms.IntegerField(required=True, max_value=150)
    password=forms.CharField(widget=forms.PasswordInput, validators=[check_size,])
    re_password=forms.CharField(help_text="Re-enter your password", widget=forms.PasswordInput)

    