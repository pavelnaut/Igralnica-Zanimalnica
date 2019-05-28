from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [path('', views.NewsList.as_view(), name='index'),
               path('news/details/<pk>/', views.NewsDetail.as_view(), name='details'),
               path('news/create/', views.NewsCreate.as_view(), name='create'),
               path('news/edit/<pk>/', views.NewsEdit.as_view(), name='edit'),
               path('news/delete/<pk>/', views.NewsDelete.as_view(), name='delete'),
               path('news/comment/', views.CreateView.as_view(), name='comment'),
               path('about/', TemplateView.as_view(template_name='about.html'),
                    name='about'),
               ]