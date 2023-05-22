
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('login/', include('login.urls')),
    path('booking/', include('booking.urls')),
    path('gallery/', include('gallery.urls')),
    path('rigister/', include('rigister.urls')),
    path('bookingdetail/', include('bookingdetail.urls')),
    path('formsdashboard/', include('formsdashboard.urls')),
 

]
