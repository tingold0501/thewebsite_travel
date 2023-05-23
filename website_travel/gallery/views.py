from django.shortcuts import render

from formsdashboard.models import Restaurant, RestaurantDetail

def gallery(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    restaurant_detail = RestaurantDetail.objects.get(restaurant=restaurant)
    name = restaurant.name
    description = restaurant_detail.description

    # Lấy hình ảnh của nhà hàng
    image = restaurant.image
    
    detail1 = restaurant_detail.detail1
    detail2 = restaurant_detail.detail2
    detail3 = restaurant_detail.detail3
    detail4 = restaurant_detail.detail4
    detail5 = restaurant_detail.detail5

    return render(request, 'gallery.html', {
        'name': name,
        'description': description,
        'image': image,
        'detail1': detail1,
        'detail2': detail2,
        'detail3': detail3,
        'detail4': detail4,
        'detail5': detail5
    })




