from django import forms
from django.db import models

class Slide(models.Model):
    image = models.ImageField(upload_to='../img/slide/', null= True)
    field1 = models.CharField(max_length=100)
    field2 = models.TextField()



class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        fields = ['image','field1', 'field2']

