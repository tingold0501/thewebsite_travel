from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery')
    # Thêm các trường dữ liệu khác tương ứng với thông tin của nhà hàng

    def __str__(self):
        return self.name

