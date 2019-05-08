from django.db import models

from accounts.models import User


class Post(models.Model):
    '''
    Only admins should be able to CRUD posts.
    '''
    title = models.CharField('заглавие', max_length=50)
    pub_date = models.DateField('дата на публикуване', auto_now_add=True)
    content = models.TextField('съдържание')

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'

    def short_content(self):
        return f"{self.content:.500}..."

    def __str__(self):
        return f"{self.title:.20}..."


class Comment(models.Model):
    '''
    Only registered users should be able to comment.
    Admins can delete them. Users can edit and delete
    their own posts.
    '''
    user = models.ForeignKey(User, verbose_name='потребител', on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, verbose_name='публикация', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField('съдържание', max_length=640)
    pub_date = models.DateTimeField('дата на създаване', auto_now=True)

    class Meta:
        verbose_name = 'коментар'
        verbose_name_plural = 'коментари'

    def __str__(self):
        return f'{self.post} - {self.content:.30}'

