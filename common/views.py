from django.shortcuts import render
from django.views.generic import CreateView
from django.core.mail import send_mail, mail_admins
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponseForbidden

from .models import ChildApplication
from .forms import ApplicationForm
from django.forms.forms import ValidationError


class Application(CreateView):
    """
    Only registered users can post. Sends email with form
    info to page mail account.
    """
    model = ChildApplication
    template_name = 'application.html'
    form_class = ApplicationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        self.object = None
        try:
            user = self.request.user
        except:
            return HttpResponseRedirect('/')

        data = request.POST.copy()

        subject = f"Имате нова заявка от {data.get('parent')}"
        message = (f"Родител: {data.get('parent')}\n"
                   f"Дете: {data.get('child')}\n"
                   f"Училище: {data.get('school')}\n"
                   f"Клас: {data.get('group')}\n"
                   f"Период: {data.get('period_from')} - {data.get('period_to')}\n"
                   f"Телефон за връзка: {data.get('phone')}\n"
                   f"Поща: {user.email}\n"
                   f"{data.get('extra')}\n")
        form = ApplicationForm(data)

        if not form.is_valid():
            raise ValidationError('Неправилно попълнен телефонен номер.')
        # +359 works 0888 works, but 555555 doesn't

        if form.is_valid() and user.is_authenticated:
            form.save()
            send_mail(subject=subject, message=message, from_email=user.email,
                      recipient_list=[settings.EMAIL_HOST_USER], fail_silently=False)
            # mail_admins(subject=subject, message=message) if admins have real mail
            return super().post(data, *args, **kwargs)
        return HttpResponseRedirect('/')
