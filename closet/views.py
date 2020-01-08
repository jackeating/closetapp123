from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required # 追加
from django.contrib import messages
from .forms import ClothesForm
from django.views.decorators.http import require_POST
from .models import Clothes, Category
from django.http import HttpResponse
from django.core.paginator import Paginator


def index(request):
    return render(request, 'closet/index.html')

@login_required
def users_detail(request, pk):
    cate = Category.objects.all()
    user = get_object_or_404(User, pk=pk)
    clothess = user.clothes_set.all().order_by('-date_of_purchase')
    paginator = Paginator(clothess, 30)
    p = request.GET.get("p")
    clothess = paginator.get_page(p)
    return render(request, 'closet/users_detail.html', {'user': user, 'clothess': clothess, 'cate':cate})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # ユーザーインスタンスを作成
        if form.is_valid():
            new_user = form.save() # ユーザーインスタンスを保存
            input_username = form.cleaned_data['username']
            input_password = form.cleaned_data['password1']
            # フォームの入力値で認証できればユーザーオブジェクト、できなければNoneを返す
            new_user = authenticate(username=input_username, password=input_password)
            # 認証成功時のみ、ユーザーをログインさせる
            if new_user is not None:
                # loginメソッドは、認証ができてなくてもログインさせることができる。→上のauthenticateで認証を実行する
                login(request, new_user)
                return redirect('app:users_detail', pk=new_user.pk)
    else:
        form = UserCreationForm()
    return render(request, 'closet/signup.html', {'form': form})

@login_required
def clothes_new(request):
    if request.method == "POST":
        form = ClothesForm(request.POST, request.FILES)  # ②
        if form.is_valid():
            clothes = form.save(commit=False)  # ③
            clothes.user = request.user# ④
            clothes.save()  # ⑤
            messages.success(request, "投稿が完了しました！")
        return redirect('app:users_detail', pk=request.user.pk)
    else:
        form = ClothesForm()
    return render(request, 'closet/clothes_new.html', {'form': form})

def clothes_detail(request, pk):
    clothes = get_object_or_404(Clothes, pk=pk)
    return render(request, 'closet/clothes_detail.html', {'clothes': clothes})

@require_POST
def clothes_delete(request, pk):
    clothes = get_object_or_404(Clothes, pk=pk)
    clothes.delete()
    return redirect('app:users_detail', request.user.id)

@login_required
def users_clothes_category(request, pk, category):
    cate = Category.objects.all()
    user = get_object_or_404(User, pk=pk)
    category = Category.objects.get(title=category)
    clothess = user.clothes_set.all().filter(category=category).order_by('-date_of_purchase')
    return render(request, 'closet/users_detail.html', {'user': user, 'clothess': clothess, 'category':category,'cate':cate})
