from django.shortcuts import render

# Create your views here.
def booking(request):
    return render(request,'indexBooking.html')