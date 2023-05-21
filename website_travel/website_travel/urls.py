
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('login/', include('login.urls')),
    path('account/', include('account.urls')),
    path('booking/', include('booking.urls')),
    path('gallery/', include('gallery.urls')),
 

]
