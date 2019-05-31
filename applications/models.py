from django.db import models
from cms.models import CMSPlugin

from phonenumber_field.modelfields import PhoneNumberField


class ChildApplication(models.Model):
    GROUP_CHOICES = (
        ('1', 'Първи клас'),
        ('2', 'Втори клас'),
        ('3', 'Трети клас'),
        ('4', 'Четвърти клас'),
        ('P', 'Предучилищна'),
    )

    # if it's summer show diff options
    TYPE_CHOICES = (
        ('I', 'Лятна Игралница'),
        ('Z', 'Лятна Занималница'),
        ('B', 'Игралница-Занималница'),
    )

    parent = models.CharField(verbose_name='родител', max_length=30)
    child = models.CharField(verbose_name='дете', max_length=30)
    school = models.CharField(verbose_name='училище', max_length=50)
    group = models.CharField(verbose_name='клас', max_length=1, choices=GROUP_CHOICES)
    type = models.CharField(verbose_name='тип', max_length=1, choices=TYPE_CHOICES, default='B')
    period_from = models.DateField(verbose_name='от')
    period_to = models.DateField(verbose_name='до')
    phone = PhoneNumberField(verbose_name='телефон')
    email = models.EmailField(verbose_name='поща')
    extra = models.TextField(verbose_name='допълнително', blank=True, null=True)

    def __str__(self):
        return f"{self.parent}: {self.child}"

    class Meta:
        verbose_name = 'заявление'
        verbose_name_plural = 'заявления'


class ChildApplicationPluginModel(CMSPlugin):
    application = models.ForeignKey(ChildApplication, on_delete=models.CASCADE)

    def __str__(self):
        return self.application