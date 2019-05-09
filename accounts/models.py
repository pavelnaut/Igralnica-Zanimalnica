from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    '''
    Avatar field is using django-imagekit in order to strip image's
    metadata and to resize it to a smaller size. Jpeg format is shit,
    that's why we use png, even though it's larger in size.
    '''
    ACADEMIC_CHOICES = (
        ('P', 'Родител'),
        ('S', 'Ученик'),
        ('T', 'Учител'),
        ('G', 'Гост'),
    )
    email = models.EmailField(verbose_name='поща', unique=True)
    first_name = models.CharField(verbose_name='име', max_length=30, blank=True)
    last_name = models.CharField(verbose_name='фамилия', max_length=30, blank=True)
    date_joined = models.DateTimeField(verbose_name='дата на създаване', auto_now_add=True)
    avatar = ProcessedImageField(verbose_name='аватар',
                                 upload_to='common/static/avatars/',
                                 processors=[ResizeToFill(140, 140)],
                                 format='PNG',
                                 default='common/static/avatars/default.png')
    kind = models.CharField(verbose_name='аз съм', max_length=1, choices=ACADEMIC_CHOICES, default='G')
    is_active = models.BooleanField(verbose_name='активен', default=True)
    is_staff = models.BooleanField(verbose_name='служител', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'потребител'
        verbose_name_plural = 'потребители'

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

    def avatar_source(self):
        return f"/avatars/{str(self.avatar).split('/')[3]}"
