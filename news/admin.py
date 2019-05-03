from django.contrib import admin
from .models import Post, Comment
from django.contrib.auth.models import User, Group

admin.site.register(Post)
admin.site.register(Comment)
admin.site.unregister(User)
admin.site.unregister(Group)


