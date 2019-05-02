from django.db import models


class Post(models.Model):
    title = models.CharField('Заглавие', max_length=50)
    pub_date = models.DateField('Дата на публикуване', auto_now_add=True)
    content = models.TextField('Съдържание')

    def short_content(self):
        return f"{self.content:.50}..."

    def __str__(self):
        return f"{self.title:.20}..."
