from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookingdetail, name= 'bookingdetail'),
   
    
]