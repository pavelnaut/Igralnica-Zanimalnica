from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.core.validators import EmailValidator
from django.utils.translation import ugettext_lazy as _

from .models import User


class SignUpForm(UserCreationForm):
    '''
    Custom form is needed as we have written our own
    AbstractBaseUser that uses email field for login
    instead of username.
    '''
    choices = list(User.ACADEMIC_CHOICES)

    email = forms.EmailField(label='Поща', required=True,
                             validators=[EmailValidator(message="Не е валиден имейл.")],
                             widget=forms.EmailInput(
                                 attrs={
                                     'class': 'form-control'
                                 }
                             ))

    password1 = forms.CharField(label='Парола', required=True,
                                max_length=32,
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control'
                                    }
                                ))

    password2 = forms.CharField(label='Потвърди парола', required=True,
                                max_length=32,
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control'
                                    }
                                ))

    first_name = forms.CharField(label='Име', required=False, max_length=32,
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': 'form-control'
                                     }
                                 ))

    last_name = forms.CharField(label='Фамилия', required=False, max_length=32,
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control'
                                    }
                                ))


    #avatar = forms.ImageField() # <-- csrf problems?

    kind = forms.ChoiceField(label='Аз съм', required=False, choices=choices,
                             widget=forms.Select(
                                 attrs={
                                     'class': 'form-control'
                                 }
                             ))

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'kind')


class LogInForm(AuthenticationForm):
    '''
    Extends the password field only for the translation
    '''
    password = forms.CharField(
        label=_("Парола"),
        strip=False,
        widget=forms.PasswordInput,
    )

    error_messages = {
        'invalid_login': _(
            "Моля въведете правилна поща и парола."),
        'inactive': _("Този профил е блокиран."),
                      }