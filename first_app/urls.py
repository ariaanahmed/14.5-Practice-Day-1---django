from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('model_form', views.model_form, name='model_form'),
]
