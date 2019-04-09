from django.conf.urls import url
from .views import create_view
from django import forms

urlpatterns = [
    url(r'^create/', create_view, name='create')
]
