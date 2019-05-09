from django.urls import path

from . import views


urlpatterns = [path('add/', views.AlbumCreateView.as_view(), name='add_pictures'),
               ]