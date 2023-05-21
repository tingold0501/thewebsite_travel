from django.shortcuts import render

# Create your views here.

def bookingdetail(request):
    return render(request, 'indexBookingDetail.html')
