from django.forms import ModelForm
from .models import Clothes
from django import forms
from cloudinary.forms import CloudinaryFileField

class ClothesForm(ModelForm):
    class Meta:
        model = Clothes
        fields = ['title', 'comment', 'image', 'category', 'date_of_purchase']
        widgets = {
        'date_of_purchase' : forms.SelectDateWidget
        }
        # image = CloudinaryFileField(
        #     options={'folder': 'media/Model_image', 'tags': 'Model_name'})
