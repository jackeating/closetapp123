from django.forms import ModelForm
from .models import Clothes
from django import forms
from cloudinary.forms import CloudinaryFileField


class ClothesForm(ModelForm):
    # 洋服を登録する為のフォーム
    class Meta:
        model = Clothes
        fields = ['title', 'comment', 'image', 'category', 'date_of_purchase']
        widgets = {'date_of_purchase': forms.SelectDateWidget(years=[x for x in range(1990, 2030)])}
