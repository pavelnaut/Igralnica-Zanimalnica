from django.urls import path

from . import views


urlpatterns = [path('add/', views.AlbumCreate.as_view(), name='add_album'),
               path('add/<pk>/', views.PictureCreate.as_view(), name='add_pictures'),
               path('', views.AlbumList.as_view(), name='gallery'),
               path('album/<pk>/', views.AlbumDetail.as_view(), name='album'),
               ]