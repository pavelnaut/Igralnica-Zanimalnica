from django.db import models


class Album(models.Model):
    title = models.CharField(verbose_name='заглавие', max_length=100)
    pub_date = models.DateField(verbose_name='дата на създаване', auto_now_add=True)
    is_visible = models.BooleanField(verbose_name='публичен', default=True)

    class Meta:
        verbose_name = 'албум'
        verbose_name_plural = 'албуми'

    def __str__(self):
        return str(self.title).replace(" ", "_")

