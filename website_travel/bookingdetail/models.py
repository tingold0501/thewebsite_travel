from django.db import models
from rigister.models import User

class TourBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True, blank= True)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_rooms = models.PositiveIntegerField()
    number_of_adults = models.PositiveIntegerField()
    number_of_children = models.PositiveIntegerField()

    def __str__(self):
        return f"Booking {self.id}"


from django import forms
from .models import TourBooking

class TourBookingForm(forms.ModelForm):
    class Meta:
        model = TourBooking
        fields = ['check_in_date', 'check_out_date', 'number_of_rooms', 'number_of_adults', 'number_of_children']
