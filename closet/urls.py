from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# Create your views here.

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('users/<int:pk>/', views.users_detail, name='users_detail'),
    path('clothes/new/', views.clothes_new, name='clothes_new'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='closet/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('clothes/<int:pk>', views.clothes_detail, name='clothes_detail'),
    path('clothes/<int:pk>/delete', views.clothes_delete, name='clothes_delete'),
    path('users/<int:pk>/<str:category>', views.users_clothes_category, name='users_clothes_category'),
    ]
