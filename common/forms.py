from django import forms
from django.core.validators import MaxLengthValidator

from .models import ChildApplication


from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from bootstrap_datepicker_plus import DatePickerInput


class ApplicationForm(forms.ModelForm):
    """
    Uses bootstrap_datepicker_plus for dates and phonenumber_field
    for phone field. Sends email with info to page mail account.
    """

    parent = forms.CharField(label='Родител', required=True, validators=[MaxLengthValidator(40)],
                             max_length=50,
                             widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control'
                                    }
                                ))

    child = forms.CharField(label='Дете', required=True, validators=[MaxLengthValidator(40)],
                            max_length=50,
                            widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control'
                                    }
                                ))

    school = forms.CharField(label='Училище', required=True, validators=[MaxLengthValidator(70)],
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
                             widget=PhoneNumberInternationalFallbackWidget(attrs={
                                 'class': 'form-control'
                             }))

    extra = forms.CharField(label='Допълнителна информация', required=False,  validators=[MaxLengthValidator(1000)],
                            max_length=1000,
                            widget=forms.Textarea(
                                    attrs={
                                        'class': 'form-control'
                                    }
                            ))

    class Meta:
        model = ChildApplication
        fields = '__all__'

