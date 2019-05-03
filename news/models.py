from django.db import models
from django.contrib.auth.models import User, Group



class Comment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user', verbose_name='потребител')
    content = models.TextField('съдържание', max_length=640)
    pub_date = models.DateTimeField('дата на създаване', auto_now=True)

    class Meta:
        verbose_name = 'коментар'
        verbose_name_plural = 'коментари'

    def __str__(self):
        return f'{self.user}\n{self.content:.30}'


class Post(models.Model):
    title = models.CharField('заглавие', max_length=50)
    pub_date = models.DateField('дата на публикуване', auto_now_add=True)
    content = models.TextField('съдържание')
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='posts', blank=True, null=True, verbose_name='коментари')

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'

    def short_content(self):
        return f"{self.content:.50}..."

    def __str__(self):
        return f"{self.title:.20}..."

