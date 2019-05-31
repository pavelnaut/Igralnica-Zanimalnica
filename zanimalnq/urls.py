from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
    path('pictures/', include('pictures.urls')),
    path('application/', include('applications.urls')),
    path('', include('cms.urls')),
]

admin.site.site_header = "Административен павел"  # it's a pun
admin.site.site_title = "Админ панел"
admin.site.index_title = "Игралница-Занималница"
