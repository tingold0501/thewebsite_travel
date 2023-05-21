from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('send-email/',views.home, name='send_email'),
    
]
