from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from rigister.models import User

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            users = User.objects.filter(email=email, password=password)
            if users.exists():
                # Lấy đối tượng User đầu tiên trong danh sách
                user = users.first()
                # Thực hiện các hành động sau khi đăng nhập thành công
                print("Login Success")
                return redirect('bookingdetail')  # Chuyển hướng đến trang chủ sau khi đăng nhập thành công
            else:
                # Xử lý khi thông tin đăng nhập không khớp
                print("Not Login")
                return render(request, 'login.html', {'error': 'Invalid email or password'})
        except User.DoesNotExist:
        # Xử lý khi không tìm thấy User
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    else:
        return render(request, 'login.html')

