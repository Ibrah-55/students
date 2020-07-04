from django.urls import path, include
from .views import *

urlpatterns = [
    path('about/', about, name='about'),
    path('', regform, name='registration form'),
]
