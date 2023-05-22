from django.shortcuts import render, redirect
from .models import User

def rigister(request):
    if request.method == 'POST':
        # Lấy dữ liệu từ request.POST
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Kiểm tra xem password và confirm_password có khớp không
        if password == confirm_password:
            # Tạo một đối tượng User và lưu vào cơ sở dữ liệu
            user = User(first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()
            
            all_users = User.objects.all()
            
            for user in all_users:
                print(f"User ID: {user.id}")
                print(f"First Name: {user.first_name}")
                print(f"Last Name: {user.last_name}")
                print(f"Email: {user.email}")
                print(f"Password: {user.password}")
                print(f"Confirm Password: {user.confirm_password}")
                print("-----------")
        
            # Chuyển hướng người dùng đến trang thành công hoặc trang chính
            return redirect('login')  # thay 'success' bằng tên view/template tương ứng
        else:
            # Xử lý lỗi nếu password và confirm_password không khớp
            return render(request, 'rigister.html', {'error': "Password and Confirm Password do not match."})
    else:
        # Xử lý khi request.method là GET (truy cập trang đăng ký lần đầu)
        return render(request, 'rigister.html')



