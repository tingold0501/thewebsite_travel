from django.core.mail import send_mail
from django.http import HttpResponse

def send_email_view(request):
    # Lấy thông tin từ người dùng (ví dụ: tiêu đề và nội dung email)
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    
    # Gửi email cho admin
    send_mail(subject, message, 'sender@example.com', ['admin@example.com'])
    
    return HttpResponse('Email sent to admin.')
