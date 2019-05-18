from django.contrib.auth import get_user_model
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.detail import DetailView


from .forms import SignUpForm, EditProfileForm
from .models import User

# do I need this?
def redirect_to_user_details(request):
    if request.user.is_authenticated:
        url = f"{request.user.pk}/"
        return HttpResponseRedirect(redirect_to=url)
    return HttpResponseRedirect(redirect_to="/")


class UserEdit(UpdateView):
    model = User
    template_name = 'user-edit.html'
    context_object_name = 'user'
    form_class = EditProfileForm
    success_url = '/accounts/profile/'


class UserDetails(DetailView):
    model = User
    template_name = 'user-details.html'
    context_object_name = 'user'


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/'
    template_name = 'signup.html'


class LogIn(LoginView):
    model = User
    form_class = AuthenticationForm
    success_url = '/'
    template_name = 'login.html'
