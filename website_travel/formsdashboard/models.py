from django import forms
from django.db import models

class Slide(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.TextField()



class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        fields = ['field1', 'field2']

