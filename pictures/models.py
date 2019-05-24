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

    # Returns the first picture of the album
    def cover(self):
        try:
            picture = Picture.objects.all().filter(album=self)[0].pic_source()
            return picture
        except:
            return "gallery/default.jpg"    # Do NOT delete default picture.

    # Returns string instead of boolean value
    def public(self):
        if self.is_visible:
            return 'Публичен'
        return 'Частен'


class Picture(models.Model):
    album = models.ForeignKey(Album, verbose_name='албум', on_delete=models.CASCADE, related_name='pictures')
    picture = models.ImageField(verbose_name='снимка', upload_to='common/static/gallery/', blank=True, null=True)
    pub_date = models.DateField('дата на качване', auto_now_add=True)

    class Meta:
        verbose_name = 'снимка'
        verbose_name_plural = 'снимки'

    def pic_source(self):
        image_name = str(self.picture).split('/')[3]
        return f"gallery/{image_name}"

    def __str__(self):
        return f'{self.album} - {str(self.picture)}'
