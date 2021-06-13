from django.shortcuts import render,get_object_or_404, redirect
from .models import Meeting,Room
from django.forms import modelform_factory
# Create your views here.

def detail(request,id):
    meeting = get_object_or_404(Meeting,pk=id)
    return render(request,"meetings/detail.html",{"meeting":meeting})

def room_list(request):
    return render(request,"meetings/rooms_list.html",
                  {"rooms":Room.objects.all()})

MeetingForm = modelform_factory(Meeting,exclude=[])

def new(request):
    if request.method == "POST":
        #Form has been submitted, process data
        form=MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        #Has not submitted yet, the form is to be rendered
        form=MeetingForm()
    return render(request,"meetings/new.html",{"form": form})