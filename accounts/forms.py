from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from django.core.validators import EmailValidator, MinLengthValidator, MaxLengthValidator

from .models import User


class SignUpForm(UserCreationForm):
    '''
    Custom form is needed as we have written our own
    AbstractBaseUser that uses email field for login
    instead of username.
    '''
    choices = list(User.ACADEMIC_CHOICES)

    email = forms.EmailField(label='Поща', required=True,
                             validators=[EmailValidator, MaxLengthValidator(50)],
                             widget=forms.EmailInput(
                                 attrs={
                                     'class': 'form-control'
                                 }
                             ))

    password1 = forms.CharField(label='Парола', required=True, validators=[MinLengthValidator(6)],
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

    first_name = forms.CharField(label='Име', required=False, validators=[MaxLengthValidator(40)],
                                 max_length=32,
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': 'form-control'
                                     }
                                 ))

    last_name = forms.CharField(label='Фамилия', required=False, validators=[MaxLengthValidator(40)],
                                max_length=32,
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control'
                                    }
                                ))

    avatar = forms.ImageField(label='Аватар', required=False,
                              widget=forms.FileInput(
                                  attrs={
                                      'class': 'form-control-file'
                                  }
                              ))

    kind = forms.ChoiceField(label='Аз съм', required=False, choices=choices,
                             widget=forms.Select(
                                 attrs={
                                     'class': 'form-control'
                                 }
                             ))

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'kind', 'avatar',)


class EditProfileForm(forms.ModelForm):
    """
    Same as register but without password
    """
    choices = list(User.ACADEMIC_CHOICES)

    email = forms.EmailField(label='Поща', required=True,
                             validators=[EmailValidator, MaxLengthValidator(50)],
                             widget=forms.EmailInput(
                                 attrs={
                                     'class': 'form-control'
                                 }
                             ))

    first_name = forms.CharField(label='Име', required=False, max_length=32, validators=[MaxLengthValidator(40)],
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': 'form-control'
                                     }
                                 ))

    last_name = forms.CharField(label='Фамилия', required=False, max_length=32, validators=[MaxLengthValidator(40)],
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control'
                                    }
                                ))

    avatar = forms.ImageField(label='Аватар', required=False,
                              widget=forms.FileInput(
                                     attrs={
                                         'class': 'form-control-file',
                                     }
                                 ))

    kind = forms.ChoiceField(label='Аз съм', required=False, choices=choices,
                             widget=forms.Select(
                                 attrs={
                                     'class': 'form-control'
                                 }
                             ))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'kind', 'avatar',)


class LoginForm(AuthenticationForm):
    """
    Extended just to get the 'class': 'form-control'
    attributes of the widget
    """
    username = UsernameField(label='Поща', widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label="Парола", strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
