from django import forms
from django.db import models


class Slide(models.Model):
    image = models.ImageField(upload_to='images/',blank=True, null= True)
    field1 = models.CharField(max_length=100)
    field2 = models.TextField()



class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        fields = ['image','field1', 'field2']



class Restaurant(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400, default='Default description')
    detail1 = models.TextField(default='') # Thêm giá trị mặc định là ''
    detail2 = models.TextField(default='')
    detail3 = models.TextField(default='')
    detail4 = models.TextField(default='')
    detail5 = models.TextField(default='')


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['image', 'name', 'description', 'detail1', 'detail2', 'detail3', 'detail4', 'detail5']

