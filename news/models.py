from django.db import models

class Post(models.Model):
    title = models.CharField('заглавие', max_length=50, default='No title')
    pub_date = models.DateField('дата на публикуване', auto_now_add=True)
    content = models.TextField('съдържание', default='No content')

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'

    def short_content(self):
        return f"{self.content:.500}..."

    def __str__(self):
        return f"{self.title:.20}..."

