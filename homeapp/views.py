from django.shortcuts import render
from . models import Department,Doctors
from . forms import BookingForm



# Create your views here.
def index(request):
    return render (request,'index.html')
def about(request):
    return render (request,'about.html')
def booking(request):
      form=BookingForm()
      if request.POST:
         form =BookingForm(request.POST)
         if form.is_valid():
             form.save()
             return render(request,'confirmation.html')
         form = BookingForm()
         

      return render (request,'booking.html',{'form':form})
def doctors(request):
    doct=Doctors.objects.all()
    return render (request,'doctors.html',{'doct':doct})
def contact(request):
    return render (request,'contact.html')
def department(request):
    depart=Department.objects.all()
    return render (request,'department.html',{'depart':depart})



