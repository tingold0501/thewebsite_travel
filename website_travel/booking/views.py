from django.shortcuts import render
from .models import Restaurant

def booking(request):
    restaurant_list = Restaurant.objects.all()
    return render(request, 'indexBooking.html', {'indexBooking': restaurant_list})
