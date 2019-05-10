from django.contrib import admin

from .models import Album, Picture, PictureComment


admin.site.register(Album)
admin.site.register(Picture)
admin.site.register(PictureComment)