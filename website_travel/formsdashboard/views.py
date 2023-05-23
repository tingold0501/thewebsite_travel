from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import SlideForm 
from .models import RestaurantForm


def create_forms(request):
    slide_form = SlideForm()
    restaurant_form = RestaurantForm()
    
    if request.method == 'POST':
        if 'slide_form_submit' in request.POST:
            slide_form = SlideForm(request.POST, request.FILES)
            if slide_form.is_valid():
                slide = slide_form.save()
                # Perform any additional operations with the slide object
                
        elif 'restaurant_form_submit' in request.POST:
            restaurant_form = RestaurantForm(request.POST, request.FILES)
            if restaurant_form.is_valid():
                restaurant = restaurant_form.save()
                # Perform any additional operations with the restaurant object

    return render(request, 'indexFormsDashboard.html', {'slide_form': slide_form, 'restaurant_form': restaurant_form})
