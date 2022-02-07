from django.shortcuts import render
import datetime


# Create your views here.
def home(request):
    return render(request, 'base.html')


def other(request):
    return render(request, 'others.html')


def about(request):
    time = datetime.datetime.now()
    return render(request, 'about.html', {'time': time})
