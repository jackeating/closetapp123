from django.forms import ModelForm
from .models import Clothes
from django import forms

class ClothesForm(ModelForm):
    class Meta:
        model = Clothes
        fields = ['title', 'comment', 'image', 'category', 'date_of_purchase']
