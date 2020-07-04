from django.shortcuts import render

from . import forms
import datetime
def about(request):
    time = datetime.datetime.now()
    return render(request, 'registration/about.html',{'time': time})

def regform(request):
    form=forms.Signup()
    if request.method == 'POST':
        form=forms.Signup(request.POST)
        html='Form received again'
        if form.is_valid():
            html=html +'A valid form'
    else:
        html='Welcome'

    return render(request, 'registration/signup.html', {'html':html, 'form':form})

