from django.urls import path
from . import views

urlpatterns = [path('', views.NewsList.as_view(), name='index'),
               path('details/<pk>/', views.NewsDetail.as_view(), name='details'),
               path('create/', views.NewsCreate.as_view(), name='create'),
               path('edit/<pk>/', views.NewsEdit.as_view(), name='edit'),
               path('delete/<pk>/', views.NewsDelete.as_view(), name='delete'),
               ]