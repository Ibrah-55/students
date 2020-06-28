from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpRequest, HttpResponseNotFound, HttpResponseServerError
from . models import Student
from django.views.generic.base import RedirectView

def student_show(request):
    student= Student.objects.order_by('roll_no')
    return render(request, 'show.html', {'student': student})