from django.views.generic import DetailView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


def redirect_to_user_details(request):
    if request.user.is_authenticated:
        url = f"{request.user.pk}/"
        return HttpResponseRedirect(redirect_to=url)


class UserDetails(DetailView):
    model = User
    template_name = 'user-details.html'
    context_object_name = 'user'


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = '/accounts/login/'
    template_name = 'signup.html'
