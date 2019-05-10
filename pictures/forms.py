from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile
from django.forms import formset_factory

from multiupload.fields import MultiUploadMetaField
from multiupload.fields import MultiImageField

from .models import Album, Picture

class PictureForm(forms.ModelForm):

    picture = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control-file'}))

    class Meta:
        model = Picture
        fields = ['album', 'picture',]


#AlbumFormSet = formset_factory(AlbumForm)


class AlbumForm(forms.ModelForm):

    title = forms.CharField(label='Заглавие', required=True, max_length=100,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control'
                                      }

                              ))


    is_visible = forms.CheckboxInput()

    #pictures = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control-file'}))

    class Meta:
        model = Album
        fields = ['title', 'is_visible',]

