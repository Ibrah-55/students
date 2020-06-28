from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
path('', views.student_show, name = 'student_show'),
    path('tutorial/', RedirectView.as_view(url = 'https://data-flair.training/blogs/category/django/')),

]