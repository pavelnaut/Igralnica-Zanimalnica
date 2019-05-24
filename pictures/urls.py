from django.urls import path

from . import views


urlpatterns = [path('', views.AlbumList.as_view(), name='gallery'),
               path('album/add/', views.AlbumCreate.as_view(), name='create_album'),
               path('album/edit/<pk>/', views.AlbumEdit.as_view(), name='edit_album'),
               path('album/<pk>/', views.AlbumDetail.as_view(), name='album'),
               path('delete/picture/<pk>/', views.PictureDelete.as_view(), name='delete_picture'),
               path('delete/album/<pk>/', views.AlbumDelete.as_view(), name='delete_album'),
               ]