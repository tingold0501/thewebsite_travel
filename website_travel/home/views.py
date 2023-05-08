
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
# Create your views here.
def home(request):
    
    return render(request, 'home.html')


# views.py
def send_email_view(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    date = request.POST.get('date')
    time = request.POST.get('time')
    people = request.POST.get('people')
    message = request.POST.get('message')

    subject = 'New Booking Request'
    email_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nDate: {date}\nTime: {time}\nNumber of People: {people}\nMessage: {message}"

    # Gửi email
    send_mail(subject, email_message, email, ['admin@example.com'])

    # Trả về JSON response để xác nhận email đã được gửi thành công
    return JsonResponse({'success': True})
