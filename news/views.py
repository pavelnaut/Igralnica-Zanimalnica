from django.shortcuts import render
from django.contrib.auth import views
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Post


class NewsList(ListView):
    model = Post
    template_name = 'news-list.html'
    context_object_name = 'posts'
    paginate_by = 3


class NewsDetail(DetailView):
    model = Post
    template_name = 'news-details.html'


class NewsEdit(UpdateView):
    model = Post
    success_url = '/'
    template_name = 'details.html'


class NewsDelete(DeleteView):
    model = Post
    success_url = '/'
    template_name = 'delete.html'


class NewsCreate(CreateView):
    model = Post
    success_url = '/'