
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


# TODO maybe add username
class User(AbstractBaseUser, PermissionsMixin):
    ACADEMIC_CHOICES = (
        ('P', 'Родител'),
        ('S', 'Ученик'),
        ('T', 'Учител'),
        ('G', 'Гост'),
    )

    email = models.EmailField(verbose_name='поща', unique=True)
    first_name = models.CharField(_('име'), max_length=30, blank=True)
    last_name = models.CharField(_('фамилия'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('дата на създаване'), auto_now_add=True)
    avatar = models.ImageField(_('аватар'), upload_to='avatars/', null=True, blank=True)
    kind = models.CharField(_('аз съм'), max_length=1, choices=ACADEMIC_CHOICES, default='G')
    is_active = models.BooleanField(_('активен'), default=True)
    is_staff = models.BooleanField(_('служител'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('потребител')
        verbose_name_plural = _('потребители')

    def public_title(self):
        '''
        Returns the first_name plus the last_name plus the title, with a space in between.
        '''
        full_title = '%s %s' % (self.get_full_name(), self.get_kind_display())
        return full_title.strip()

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
