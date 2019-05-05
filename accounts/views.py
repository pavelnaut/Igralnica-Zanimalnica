from django.contrib.auth import get_user_model
from django.views.generic import DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.http import HttpResponseRedirect


from .forms import SignUpForm, LogInForm


def redirect_to_user_details(request):
    if request.user.is_authenticated:
        url = f"{request.user.pk}/"
        return HttpResponseRedirect(redirect_to=url)


class UserDetails(DetailView):
    model = settings.AUTH_USER_MODEL
    template_name = 'user-details.html'
    context_object_name = 'user'


class SignUp(CreateView):
    model = get_user_model
    form_class = SignUpForm
    success_url = '/'
    template_name = 'signup.html'


class LogIn(LoginView):
    model = get_user_model
    form_class = LogInForm
    success_url = '/'
    template_name = 'login.html'