from django.shortcuts import render
from django.http import HttpResponseRedirect

from .services import final_data
from .models import *
from .forms import AppointmentForm

def demobook(request):

    details= Appointment.objects.all()
    if request.method == "POST":
        form = AppointmentForm(request.POST, None)
        if form.is_valid():
            newform = form.save()
            return HttpResponseRedirect('/confirmation')

            
    return render(request, 'book_demo.html', {"data":final_data, "details":details})


def confirmation(request):
    data = Appointment.objects.last()  
    spl_word = "2020"
    course= data.course_time_date.partition(spl_word)[0] 
    time=data.course_time_date[-5:]
    date=data.course_time_date[-14:-5]


    return render(request, "thanks.html", {'data':data,'time':time, 'date':date, 'course':course})
