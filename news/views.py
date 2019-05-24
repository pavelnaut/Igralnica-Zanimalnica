from django.shortcuts import render
from django.contrib.auth import views
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.http import HttpResponseRedirect, HttpResponse

from .models import Post, Comment
from .forms import CommentForm, PostForm


# how to make this work?
def redirect_to_commented_post(request):
    if request.user.is_authenticated:
        url = f"/news/details/{request.post.id}/"
        return HttpResponseRedirect(redirect_to=url)


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
    Not only does it show the full NewsPost, but also shows all
    the comments belonging to it. Content is public, but only
    registered users can add new comments. Each user can edit/delete
    their own comment. Admins can do whatever they want.
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
        data = request.POST.copy()
        form = CommentForm(data)
        user = self.request.user

        if form.is_valid() and user.is_authenticated:
            data['post'] = self.get_object()
            comment = Comment(
                content=data['content'],
                post=self.get_object(),
                user=self.request.user
            )
            comment.save()
            return HttpResponseRedirect(url)
        else:
            raise Exception(form.errors)


class CommentEdit(UpdateView):
    """
    Comment owners can edit their comments.
    Admins can edit all comments.
    """
    model = Comment
    form_class = CommentForm
    success_url = "/"
    template_name = 'news-details.html'
    # redirect to post?


class CommentDelete(DeleteView):
    """
    Comment owners can delete their comments.
    Admins can delete all comments.
    """
    model = Comment
    success_url = '/'
    template_name = 'news-delete.html'

    def post(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_superuser or user == self.get_object().user:
            return self.delete(request, *args, **kwargs)
        return HttpResponseRedirect('/')


# Only Admins have permission for rest of the views
class NewsEdit(UpdateView):
    model = Post
    context_object_name = 'comment'
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
