from django import forms
from django.core.validators import MaxLengthValidator

from .models import Post


class PostForm(forms.ModelForm):

    title = forms.CharField(label='Заглавие', required=True, validators=[MaxLengthValidator(50)],
                            max_length=50,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control'
                                      }

                              ))

    content = forms.CharField(label='Съдържание', required=True,
                              widget=forms.Textarea(
                                attrs={
                                    'class': 'form-control'
                                      }

                              ))

    class Meta:
        model = Post
        fields = ('title', 'content',)
