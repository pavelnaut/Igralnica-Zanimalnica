from django.urls import path

from . import views

urlpatterns = [path('', views.Application.as_view(), name='application'),
               ]
