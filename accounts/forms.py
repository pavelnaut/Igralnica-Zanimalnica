from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import EmailValidator

from .models import User


class SignUpForm(UserCreationForm):
    choices = list(User.ACADEMIC_CHOICES)

    email = forms.EmailField(required=True,
                             validators=[EmailValidator(message="Не е валиден имейл.")],
                             widget=forms.EmailInput(
                                 attrs={
                                     'class': 'form-control'
                                 }
                             ))

    password1 = forms.CharField(required=True,
                                max_length=32,
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control'
                                    }
                                ))

    password2 = forms.CharField(required=True,
                                max_length=32,
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control'
                                    }
                                ))

    first_name = forms.CharField(max_length=32,
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': 'form-control'
                                     }
                                 ))

    last_name = forms.CharField(max_length=32,
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control'
                                    }
                                ))


    #avatar = forms.ImageField() # <-- csrf problems?

    kind = forms.ChoiceField(choices=choices,
                             widget=forms.Select(
                                 attrs={
                                     'class': 'form-control'
                                 }
                             ))

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'kind')

