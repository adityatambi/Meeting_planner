from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting
# Create your views here.
def welcome(request):
    return render (request, "website/welcome.html",
                   {"meetings":Meeting.objects.all()})

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

def about(request):
    return HttpResponse("This page is developed by Aditya Tambi. \n"
                        "This is not the first webpage of my life\n"
                        "Anyways. Have a good day!")