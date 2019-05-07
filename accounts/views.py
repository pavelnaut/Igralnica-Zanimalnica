from django.contrib.auth import get_user_model
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm

from .forms import SignUpForm, EditProfileForm
from .models import User

# do I need this?
def redirect_to_user_details(request):
    if request.user.is_authenticated:
        url = f"/accounts/profile/{request.user.pk}/"
        return HttpResponseRedirect(redirect_to=url)


# TODO fix authentication
class UserEdit(UpdateView):
    model = User
    template_name = 'user-edit.html'
    context_object_name = 'user'
    form_class = SignUpForm
    success_url = '/'



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
