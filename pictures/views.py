from django.views.generic.edit import FormView
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.http import HttpResponseRedirect, HttpResponseBadRequest

from .forms import AlbumForm, PictureForm
from .models import Album, Picture


class AlbumCreate(CreateView):
    model = Album
    form_class = AlbumForm
    success_url = '/pictures/'
    template_name = 'add-pictures.html'


class PictureCreate(FormView):
    form_class = PictureForm
    model = Picture
    template_name = 'add-pictures.html'
    success_url = '/pictures/'


class AlbumDelete(DeleteView):
    model = Album
    success_url = '/pictures/'
    template_name = 'pictures-delete.html'


class PictureDelete(DeleteView):
    model = Picture
    success_url = '/pictures/'
    template_name = 'pictures-delete.html'


class AlbumEdit(UpdateView):
    model = Album
    form_class = AlbumForm
    success_url = '/pictures/'
    template_name = 'add-album.html'


class AlbumList(ListView):
    model = Album
    template_name = 'gallery.html'
    context_object_name = 'albums'

    # public albums visible to all,
    # hidden albums visible to admins only
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Album.objects.all().order_by('-pub_date', '-pk')
        return Album.objects.all().order_by('-pub_date', '-pk').filter(is_visible=True)


class AlbumDetail(DetailView):
    model = Album
    template_name = 'album.html'
    context_object_name = 'album'
    form_class = PictureForm

    def get_context_data(self, *, object_list=None, **kwargs):
        if self.get_object().is_visible or self.request.user.is_superuser:
            context = super(AlbumDetail, self).get_context_data(**kwargs)
            context['pictures'] = Picture.objects.all().filter(album=self.get_object())
            context['form'] = PictureForm()
            return context

    def post(self, request, pk):
        url = f'/pictures/album/{self.get_object().id}/'
        files = request.FILES.getlist('picture')
        album = self.get_object()
        user = self.request.user
        if files and user.is_superuser:
            for pic in files:
                # to do: validate
                picture = Picture(
                    album=album,
                    picture=pic,
                )
                picture.save()
            return HttpResponseRedirect(url)
        else:
            return HttpResponseBadRequest()
