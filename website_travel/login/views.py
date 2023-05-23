
from django.shortcuts import render, redirect
from bookingdetail.models import TourBooking
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            users = User.objects.filter(email=email, password=password)
            if users.exists():
                # Lấy đối tượng User đầu tiên trong danh sách
                user = users.first()
                # Lưu email vào session
                request.session['user_email'] = user.email

                # Thực hiện các hành động sau khi đăng nhập thành công
                print("Login Success")
                return redirect('bookingdetail')  # Chuyển hướng đến trang bookingdetail sau khi đăng nhập thành công
            else:
                # Xử lý khi thông tin đăng nhập không khớp
                print("Not Login")
                return render(request, 'login.html', {'error': 'Invalid email or password'})
        except User.DoesNotExist:
            # Xử lý khi không tìm thấy User
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    else:
        return render(request, 'login.html')











