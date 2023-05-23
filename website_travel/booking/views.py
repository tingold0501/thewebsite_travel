from django.shortcuts import render
from formsdashboard.models import Restaurant
# 


def booking(request):
    restaurant_list = Restaurant.objects.all()
    print(restaurant_list)
    return render(request, 'indexBooking.html', {'restaurant_list': restaurant_list})


