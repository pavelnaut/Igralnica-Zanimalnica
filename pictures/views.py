from django.views.generic.edit import FormView
from django.views.generic import CreateView, ListView, DetailView


from .forms import AlbumForm, PictureForm
from .models import Album, Picture

from django.http import HttpResponseRedirect
from django.shortcuts import render


class AlbumCreate(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'add-pictures.html'
    success_url = f'/pictures/gallery/'


class AlbumList(ListView):
    model = Album
    template_name = 'gallery.html'
    context_object_name = 'albums'


class PictureCreate(CreateView):
    model = Picture
    form_class = PictureForm
    template_name = 'add-pictures.html'
    success_url = '/'


class AlbumDetail(DetailView):
    model = Album
    template_name = 'album.html'
    context_object_name = 'album'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        context['pictures'] = Picture.objects.all().filter(album=self.get_object())
        return context