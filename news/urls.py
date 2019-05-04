from django.urls import path
from . import views

urlpatterns = [path('', views.NewsList.as_view(), name='index'),
               path('news/details/<pk>/', views.NewsDetail.as_view(), name='details'),
               path('news/create/', views.NewsCreate.as_view(), name='create'),
               path('news/edit/<pk>/', views.NewsEdit.as_view(), name='edit'),
               path('news/delete/<pk>/', views.NewsDelete.as_view(), name='delete'),
               ]