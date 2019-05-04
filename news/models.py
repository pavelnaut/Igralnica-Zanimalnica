from django.db import models
from django.conf import settings
from accounts.models import User


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='потребител', on_delete=models.CASCADE, related_name='user')
    content = models.TextField('съдържание', max_length=640)
    pub_date = models.DateTimeField('дата на създаване', auto_now=True)

    class Meta:
        verbose_name = 'коментар'
        verbose_name_plural = 'коментари'

    def __str__(self):
        return f'{self.user}\n{self.content:.30}'


# TODO fix relations
class Post(models.Model):
    title = models.CharField('заглавие', max_length=50)
    pub_date = models.DateField('дата на публикуване', auto_now_add=True)
    content = models.TextField('съдържание')
    comments = models.OneToOneField(Comment, verbose_name='коментари', on_delete=models.CASCADE, related_name='posts', blank=True, null=True)

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'

    def short_content(self):
        return f"{self.content:.50}..."

    def __str__(self):
        return f"{self.title:.20}..."

