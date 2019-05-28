from django.shortcuts import render
from django.views.generic import CreateView
from django.core.mail import send_mail, mail_admins
from django.conf import settings

from .models import ChildApplication
from .forms import ApplicationForm


class Application(CreateView):
    """
    Sends email with form
    info to page mail account.
    """
    model = ChildApplication
    template_name = 'application.html'
    form_class = ApplicationForm
    success_url = '/'
    choices = ChildApplication.TYPE_CHOICES
    tuple2dict_group = {a: b for a, b in ChildApplication.GROUP_CHOICES}
    tuple2dict_type = {a: b for a, b in ChildApplication.TYPE_CHOICES}

    def post(self, request, *args, **kwargs):

        self.object = None
        data = request.POST.copy()
        subject = f"Имате нова заявка от {data.get('parent')}"
        message = (f"Родител: {data.get('parent')}\n"
                   f"Дете: {data.get('child')}\n"
                   f"Училище: {data.get('school')}\n"
                   f"Клас: {self.tuple2dict_group[data.get('group')]}\n"
                   f"Тип: {self.tuple2dict_type[data.get('type')]}\n"
                   f"Период: {data.get('period_from')} - {data.get('period_to')}\n"
                   f"Телефон за връзка: {data.get('phone')}\n"
                   f"Поща: {data.get('email')}\n"
                   f"{data.get('extra')}\n")
        form = ApplicationForm(data)
        if form.is_valid():
            send_mail(subject=subject, message=message, from_email=data.get('email'),
                      recipient_list=[settings.EMAIL_HOST_USER], fail_silently=False)
            # mail_admins(subject=subject, message=message) if admins have real mail
            return super().post(data, *args, **kwargs)

