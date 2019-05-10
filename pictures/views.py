from django.views.generic.edit import FormView
from django.views.generic import CreateView


from .forms import AlbumForm, PictureForm
from .models import Album, Picture

from django.http import HttpResponseRedirect
from django.shortcuts import render


class AlbumCreate(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'add-pictures.html'
    success_url = f'/pictures/add/'
    # get pk and insert into url


    # def post(self, request, *args, **kwargs):
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     album_title = self.get_object().title
    #     files = request.FILES.getlist('file_field')
    #     if form.is_valid():
    #         form.save()
    #         form = PictureForm
    #
    #         for f in files:
    #             form_class = PictureForm
    #             form = PictureForm({'album': album_title,
    #                                 'picture': f})
    #         return self.form_valid(form)
    #
    #     else:
    #         return self.form_invalid(form)

class PictureCreate(CreateView):
    model = Picture
    form_class = PictureForm
    template_name = 'add-pictures.html'
    success_url = '/'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(PictureCreate, self).get_context_data(**kwargs)
    #     context['album'] = Album.objects.all().filter(album=self.get_object())
    #     return context

    # def post(self, request, **kwargs):
    #     url = f'/pictures/add/{self.get_object().id}/'
    #     post_values = self.get_object().id
    #     form = CommentForm(post_values)
    #     user = self.request.user
    #
    #     if form.is_valid() and user.is_authenticated:
    #         post_values['post'] = self.get_object()
    #         comment = Comment(
    #             content=post_values['content'],
    #             post=self.get_object(),
    #             user=self.request.user
    #         )
    #         comment.save()
    #         return HttpResponseRedirect(url)
    #     else:
    #         raise Exception(form.errors)