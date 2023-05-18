
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        people = request.POST['people']
        message = request.POST['message']
        
        # Gửi email đến admin
        send_mail(
            subject='New Booking Request',
            message=f'Name: {name}\nEmail: {email}\nPhone: {phone}\nDate: {date}\nTime: {time}\nNumber of People: {people}\nMessage: {message}',
            from_email=email,
            recipient_list=['huynhtin0501@gmail.com'],
            fail_silently=False,
        )
        return JsonResponse({'status': 'success'})
    return render(request, 'home.html')






