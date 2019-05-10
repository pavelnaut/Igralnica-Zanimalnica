from django.db import models

from imagekit.models import ProcessedImageField

from accounts.models import User


class Album(models.Model):
    title = models.CharField(verbose_name='заглавие', max_length=100)
    pub_date = models.DateField(verbose_name='дата на създаване', auto_now_add=True)
    is_visible = models.BooleanField(verbose_name='публичен', default=True)

    class Meta:
        verbose_name = 'албум'
        verbose_name_plural = 'албуми'

    def __str__(self):
        return str(self.title)


class Picture(models.Model):
    album = models.ForeignKey(Album, verbose_name='албум', on_delete=models.CASCADE, related_name='pictures')
    picture = ProcessedImageField(verbose_name='снимка', upload_to='gallery/', blank=True, null=True)
    pub_date = models.DateField('дата на качване', auto_now_add=True)

    class Meta:
        verbose_name = 'снимка'
        verbose_name_plural = 'снимки'

    def __str__(self):
        return f'{self.album} - {str(self.picture)}'


class PictureComment(models.Model):
    '''
    Only registered users should be able to comment.
    Admins can delete them. Users can edit and delete
    their own posts.
    '''
    user = models.ForeignKey(User, verbose_name='потребител', on_delete=models.CASCADE, related_name='picture_comments')
    post = models.ForeignKey(Picture, verbose_name='снимка', on_delete=models.CASCADE, related_name='picture_comments')
    content = models.TextField('съдържание', max_length=640)
    pub_date = models.DateTimeField('дата на създаване', auto_now=True)

    class Meta:
        verbose_name = 'коментар'
        verbose_name_plural = 'коментари'

    def __str__(self):
        return f'{self.post} - {self.content:.30}'