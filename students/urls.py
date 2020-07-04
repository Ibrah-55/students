from django.urls import path
from . import views
from django.views.generic.base import RedirectView
from django.views.decorators.cache import cache_page

urlpatterns = [
path('', views.student_show, name = 'student_show'),
path('tutorial/', RedirectView.as_view(url = 'https://data-flair.training/blogs/category/django/')),
path('cookie/', views.setcookie, name='cookie'),
path('showcookie/', views.showcookie, name='showcookie'),
path('student_show/', cache_page(300)),
]