from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# Create your views here.

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    # welcome to closetのpath
    path('users/<int:pk>/', views.users_detail, name='users_detail'),
    # マイページのpath
    path('clothes/new/', views.clothes_new, name='clothes_new'),
    # 登録画面のpath
    path('signup/', views.signup, name='signup'),
    # signup画面のpath
    path('login/', auth_views.LoginView.as_view(template_name='closet/login.html'), name='login'),
    # login画面のpath
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # logout画面のpath
    path('clothes/<int:pk>', views.clothes_detail, name='clothes_detail'),
    # clothes詳細画面のpath
    path('clothes/<int:pk>/delete', views.clothes_delete, name='clothes_delete'),
    # clothes削除画面のpath
    path('users/<int:pk>/<str:category>', views.users_clothes_category, name='users_clothes_category'),
    # category選択された画面のpath
    ]
