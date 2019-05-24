from django.apps import AppConfig


class NewsConfig(AppConfig):
    name = 'news'
    verbose_name = 'Новини'  # had to add a line in __init__ to work
