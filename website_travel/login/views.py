from rigister.models import User
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            # Xác thực người dùng
            user = User.objects.get(email=email, password=password)
            
            # Lưu thông tin người dùng vào session
            request.session['user_email'] = user.email
            
            # Thực hiện các hành động sau khi đăng nhập thành công
            print("Login Success")
            return redirect('bookingdetail')  # Chuyển hướng đến trang bookingdetail sau khi đăng nhập thành công
        except User.DoesNotExist:
            # Xử lý khi không tìm thấy User hoặc thông tin đăng nhập không khớp
            print("Not Login")
            return render(request, 'loginus.html', {'error': 'Invalid email or password'})
    else:
        return render(request, 'loginus.html')












