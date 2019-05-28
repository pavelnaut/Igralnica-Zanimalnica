from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.http import HttpResponseRedirect

from .models import Post
from .forms import PostForm


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
