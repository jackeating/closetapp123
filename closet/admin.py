from django.contrib import admin
from .models import Clothes, Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    # category項目の追加、削除を行う為に管理サイトにCategory項目を追加
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class ClothesAdmin(admin.ModelAdmin):
    # clothes項目の追加、削除を行う為に管理サイトにClothes項目を追加
    list_display = ('id', 'title', 'user')
    list_display_links = ('id', 'title')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Clothes, ClothesAdmin)
