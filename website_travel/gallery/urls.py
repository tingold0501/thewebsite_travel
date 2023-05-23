from django.urls import path
from . import views

urlpatterns = [
    path('gallery/<int:restaurant_id>/', views.gallery, name='gallery'),
]