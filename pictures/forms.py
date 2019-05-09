from django import forms

from multiupload.fields import MultiImageField

from .models import Album
from news.models import Post


class AlbumForm(forms.ModelForm):

    title = forms.CharField(label='Заглавие', required=True, max_length=100,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control'
                                      }

                              ))

    files = MultiImageField(min_num=1, max_num=50, label='Снимки', required=True,
                                 widget=forms.FileInput(
                                     attrs={
                                         'class': 'form-control-file',

                                     }
                                 ))

    is_visible = forms.CheckboxInput()



    class Meta:
        model = Album
        fields = ['title', 'is_visible']

    #files = MultiImageField(min_num=1, max_num=50, max_file_size=1024*1024*5)

    def save(self, commit=True):
        instance = super(AlbumForm, self).save(commit)
        for each in self.cleaned_data['files']:
            Post.objects.create(picture=each, album=instance)
        return instance