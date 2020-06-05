# Generated by Django 2.2.1 on 2019-05-09 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20190509_0354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='album',
        ),
        migrations.RemoveField(
            model_name='post',
            name='picture',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default='No content', verbose_name='съдържание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='No title', max_length=50, verbose_name='заглавие'),
        ),
    ]