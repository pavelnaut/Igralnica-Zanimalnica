from django.shortcuts import render
from django.contrib.auth import views
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.http import HttpResponseRedirect, HttpResponse

from .models import Post, Comment
from .forms import CommentForm, PostForm

from accounts.models import User


# so far don't need this?
def has_access_to_modify(current_user, comment):
    if current_user.is_superuser:
        return True
    elif current_user.id == comment.user.id:
        return True
    return False


class NewsList(ListView):
    model = Post
    template_name = 'news-list.html'
    context_object_name = 'posts'
    paginate_by = 3

    # Newest at the top, but if two are on the same day, look at pk
    def get_queryset(self):
        return Post.objects.all().order_by('-pub_date', '-pk')


class NewsDetail(DetailView):
    '''
    Not only does it show the full Post, but also shows all
    the comments belonging to it. Content is public, but only
    registered users can add new comments. Each user can edit/delete
    their own comment. Admins can delete every comment but can't
    and shouldn't edit them(that would be voice manipulation).
    '''
    model = Post
    template_name = 'news-details.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsDetail, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.all().filter(post=self.get_object())
        context['form'] = CommentForm()
        return context

    def post(self, request, pk):
        url = f'/news/details/{self.get_object().id}/'
        post_values = request.POST.copy()
        form = CommentForm(post_values)
        user = self.request.user

        if form.is_valid() and user.is_authenticated:
            post_values['post'] = self.get_object()
            comment = Comment(
                content=post_values['content'],
                post=self.get_object(),
                user=self.request.user
            )
            comment.save()
            return HttpResponseRedirect(url)
        else:
            raise Exception(form.errors)


class CommentEdit(UpdateView):
    model = Comment
    form_class = CommentForm
    success_url = "/"
    template_name = 'news-details.html'
    # redirect to post?


class CommentDelete(DeleteView):
    model = Comment
    success_url = '/'
    template_name = 'news-delete.html'


# Only Admins have permission for rest of the views
class NewsEdit(UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/'
    template_name = 'news-edit.html'


class NewsDelete(DeleteView):
    model = Post
    success_url = '/'
    template_name = 'news-delete.html'


class NewsCreate(CreateView):
    model = Post
    form_class = PostForm
    success_url = '/'
    template_name = 'news-edit.html'