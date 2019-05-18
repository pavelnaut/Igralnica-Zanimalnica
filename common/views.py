from django.shortcuts import render
from django.views.generic import CreateView
from django.core.mail import send_mail
from django.conf import settings


from .models import ChildApplication
from .forms import ApplicationForm

from accounts.models import User

def index(request):
    return render(request, 'index.html')


class Application(CreateView):
    model = ChildApplication
    template_name = 'application.html'
    form_class = ApplicationForm
    success_url = '/'
    queryset = User.objects.all()
    # def post(self, request, *args, **kwargs):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         self.object = None
    #         ChildApplication(email=user)
    #         data = request.POST.copy()
    #         subject = f"Имате нова заявка от {data.get('parent')}"
    #         message = (f"Родител: {data.get('parent')}\n"
    #                    f"Дете: {data.get('child')}\n"
    #                    f"Училище: {data.get('school')}\n"
    #                    f"Клас: {data.get('group')}\n"
    #                    f"Период: {data.get('period_from')} - {data.get('period_to')}\n"
    #                    f"Телефон за връзка: {data.get('phone')}\n"
    #                    f"{data.get('extra')}\n")
    #         send_mail(subject=subject, message=message, from_email=user.email, recipient_list=[settings.EMAIL_HOST_USER])
    #         return super().post(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        self.object = None
        user = self.request.user
        data = request.POST.copy()
        subject = f"Имате нова заявка от {data.get('parent')}"
        message = (f"Родител: {data.get('parent')}\n"
                   f"Дете: {data.get('child')}\n"
                   f"Училище: {data.get('school')}\n"
                   f"Клас: {data.get('group')}\n"
                   f"Период: {data.get('period_from')} - {data.get('period_to')}\n"
                   f"Телефон за връзка: {data.get('phone')}\n"
                   f"{data.get('extra')}\n")
        ChildApplication(user=user)

        form = self.get_form()

        if form.is_valid() and user.is_authenticated:
            send_mail(subject=subject, message=message, from_email=user.email,
                      recipient_list=[settings.EMAIL_HOST_USER])
            return super().post(request, *args, **kwargs)
