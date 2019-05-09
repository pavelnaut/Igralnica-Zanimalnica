from django.views.generic.edit import FormView
from django.views.generic import CreateView

from .forms import AlbumForm
from .models import Album


class AlbumCreateView(FormView):
    model = Album
    form_class = AlbumForm
    template_name = 'add-pictures.html'
    success_url = '/'
