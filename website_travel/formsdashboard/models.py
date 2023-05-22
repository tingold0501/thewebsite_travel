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




# style="background-image: url(/home/img/slide/{{slide.image.url}});"
# <img src = "home/img/slide/ {{slide.img}}">