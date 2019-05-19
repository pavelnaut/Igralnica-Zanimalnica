from django import forms

from .models import ChildApplication
from accounts.models import User

from phonenumber_field.formfields import PhoneNumberField
from bootstrap_datepicker_plus import DatePickerInput


class ApplicationForm(forms.ModelForm):

    parent = forms.CharField(label='Родител', required=True,
                             max_length=50,
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control'
                                    }
                                ))

    child = forms.CharField(label='Дете', required=True,
                            max_length=50,
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control'
                                    }
                                ))

    school = forms.CharField(label='Училище', required=True,
                             max_length=50,
                             widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control'
                                    }
                                ))
    group = forms.ChoiceField(label='Клас/група', required=True, choices=ChildApplication.GROUP_CHOICES,
                                widget=forms.Select(
                                    attrs={
                                        'class': 'form-control'
                                    }
                                ))

    period_from = forms.DateField(label='В периода от', required=True,
                                widget=DatePickerInput(options={"locale": "bg",}))

    period_to = forms.DateField(label='до', required=True,
                                widget=DatePickerInput(options={"locale": "bg",}))

    phone = PhoneNumberField(label='Телефон за връзка', required=True, max_length=20,
                             widget=forms.TextInput(attrs={
                                        'class': 'form-control'
                                    }))

    extra = forms.CharField(label='Допълнителна информация', required=False,
                            max_length=500,
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control'
                                    }
                                ))

    class Meta:
        model = ChildApplication
        fields = ('__all__')
