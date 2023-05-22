
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


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
    path('account/', include('account.urls')),
 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
