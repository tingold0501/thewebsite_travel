from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rigister.models import User
from .models import TourBooking


@login_required
def bookingdetail(request):
    user_id = request.user.id  # Lấy ID của người dùng đã xác thực từ session

    try:
        # Truy vấn đối tượng người dùng từ database bằng ID
        user = User.objects.get(id=user_id)
        user_email = user.email  # Lấy email của người dùng

        if request.method == 'POST':
            check_in_date = request.POST.get('check_in_date')
            check_out_date = request.POST.get('check_out_date')
            room_quantity = request.POST.get('room_quantity')
            adults = request.POST.get('adults')
            children = request.POST.get('children')

            tour = TourBooking()
            tour.check_in_date = check_in_date
            tour.check_out_date = check_out_date
            tour.number_of_rooms = room_quantity
            tour.number_of_adults = adults
            tour.number_of_children = children
            tour.user = user  # Gán đối tượng User cho trường user của đối tượng TourBooking
            # Lưu đối tượng vào database
            tour.save()

            # In ra thông tin
            print("Email:", user_email)
            print("Check-in Date:", check_in_date)
            print("Check-out Date:", check_out_date)
            print("Room Quantity:", room_quantity)
            print("Adults:", adults)
            print("Children:", children)

        # Lấy danh sách booking của người dùng
        user_bookings = TourBooking.objects.filter(user=user)

        return render(request, 'indexBookingDetail.html', {'user_bookings': user_bookings})

    except User.DoesNotExist:
        # Xử lý khi không tìm thấy người dùng
        return render(request, 'indexBookingDetail.html', {'error': 'User does not exist'})
