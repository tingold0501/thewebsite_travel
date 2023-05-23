from django.shortcuts import render

from formsdashboard.models import Restaurant

def gallery(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    name = restaurant.name
    description = restaurant.description

    # Lấy hình ảnh của nhà hàng
    image = restaurant.image
    
    detail1 = restaurant.detail1
    detail2 = restaurant.detail2
    detail3 = restaurant.detail3
    detail4 = restaurant.detail4
    detail5 = restaurant.detail5

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




