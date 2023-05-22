from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Kiểm tra nếu confirm_password được cung cấp và không rỗng
        if self.confirm_password:
            self.password = self.confirm_password
        super().save(*args, **kwargs)   
