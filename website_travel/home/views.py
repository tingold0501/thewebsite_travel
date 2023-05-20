
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        people = int(request.POST.get('people'))
        message = request.POST.get('message')
        
        # Gửi email đến admin
        send_mail(
            subject='New Booking Request',
            message=f'Name: {name}\nEmail: {email}\nPhone: {phone}\nDate: {date}\nTime: {time}\nNumber of People: {people}\nMessage: {message}',
            from_email=email,
            recipient_list=['phamtin050120@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'home.html', {'success_message': 'Email sent successfully!'})
    return render(request, 'home.html')






