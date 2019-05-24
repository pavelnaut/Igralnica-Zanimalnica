from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [path('', views.Application.as_view(), name='application'),
               path('invalid/', TemplateView.as_view(template_name='invalid.html'), name='invalid'),
               ]
