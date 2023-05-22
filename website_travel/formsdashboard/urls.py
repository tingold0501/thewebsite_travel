from django.urls import path
from . import views

urlpatterns = [
    path('', views.formsdashboard, name='formsdashboard'),
]