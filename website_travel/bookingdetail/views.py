from django.shortcuts import render, redirect
from rigister.models import User
from .models import TourBooking


def bookingdetail(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
            user_email = user.email

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
            tour.user = user
            tour.save()

            # In ra thông tin
            print("Email:", user_email)
            print("Check-in Date:", check_in_date)
            print("Check-out Date:", check_out_date)
            print("Room Quantity:", room_quantity)
            print("Adults:", adults)
            print("Children:", children)

            return redirect('bookingdetail')
        else:
            # Xử lý khi người dùng chưa đăng nhập
            return render(request, 'indexBookingDetail.html', {'error': 'Please login to continue.'})

    # Lấy danh sách booking của người dùng hiện tại
    if request.user.is_authenticated:
        user = request.user
        user_bookings = TourBooking.objects.filter(user=user)
        return render(request, 'indexBookingDetail.html', {'user_bookings': user_bookings})
    else:
        # Xử lý khi người dùng chưa đăng nhập
        return render(request, 'indexBookingDetail.html', {'error': 'Please login to continue.'})

