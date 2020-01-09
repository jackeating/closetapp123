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
    # indexが呼び出されたらindex.htmlを返す

@login_required
# デコレータでviewをログインユーザーのみに表示
def users_detail(request, pk):
    cate = Category.objects.all()
    # category項目の全部を取得
    user = get_object_or_404(User, pk=pk)
    # pkに紐づいたuserを取得。なければHttp404を送出
    clothess = user.clothes_set.all().order_by('-date_of_purchase')
    # userに紐づいたclothesをdate_of_purchase順に全部を取得
    paginator = Paginator(clothess, 30)
    # 30項目毎でclothesを表示する
    p = request.GET.get("p")
    # 閲覧ページを取得
    clothess = paginator.get_page(p)
    # 閲覧ページに合わせてclothesを取得
    return render(request, 'closet/users_detail.html', {'user': user, 'clothess': clothess, 'cate':cate})
    # users_detailが呼び出されたらuser、clothes、cateを載せてusers_detail.htmlを返す

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) 
        # userインスタンスを作成
        if form.is_valid():
            new_user = form.save() 
            # userインスタンスを保存
            input_username = form.cleaned_data['username']
            input_password = form.cleaned_data['password1']
            # フォームの入力値で認証できればユーザーオブジェクト、できなければNoneを返す
            new_user = authenticate(username=input_username, password=input_password)
            # 認証成功時のみ、ユーザーをログインさせる
            if new_user is not None:
                # loginメソッドは、認証ができてなくてもログインさせることができる。→上のauthenticateで認証を実行する
                login(request, new_user)
                return redirect('app:users_detail', pk=new_user.pk)
                # requestがpostの場合、pkに紐づいたusers_detailへリダイレクトする
    else:
        form = UserCreationForm()
        # requestがpostでない場合、新規ユーザー登録フォームインスタンスを作成
    return render(request, 'closet/signup.html', {'form': form})
    # signupが呼び出されてrequestがpostでない場合はformを載せてsignup.htmlを返す

@login_required
# デコレータでviewをログインユーザーのみに表示
def clothes_new(request):
    if request.method == "POST":
        form = ClothesForm(request.POST, request.FILES)
        # clothesインスタンスをフォームから作成
        if form.is_valid():
            clothes = form.save(commit=False)
            # clothesインスタンスを作成。保存はせず
            clothes.user = request.user
            # requestしたuserをclothesのuserとする
            clothes.save()
            # インスタンスを保存
            messages.success(request, "投稿が完了しました！")
            #　保存が成功した時にmessageを画面に表示
        return redirect('app:users_detail', pk=request.user.pk)
        # requestがpostの場合、pkに紐づいたusers_detailへリダイレクトする
    else:
        form = ClothesForm()
        # requestがpostでない場合にclothesフォームインスタンスを作成
    return render(request, 'closet/clothes_new.html', {'form': form})
    # clothes_newが呼び出されてrequestがpostでない場合にformインスタンスを載せてclothes_new.htmlを返す

def clothes_detail(request, pk):
    clothes = get_object_or_404(Clothes, pk=pk)
    return render(request, 'closet/clothes_detail.html', {'clothes': clothes})

@require_POST
# postのみrequestとして許可
def clothes_delete(request, pk):
    clothes = get_object_or_404(Clothes, pk=pk)
    # pkに紐づいたclothesを取得。なければHttp404を送出
    clothes.delete()
    # clothesを削除
    return redirect('app:users_detail', request.user.id)
    # clothes_deleteが呼び出されたらuser.idに紐づいたusers_detailにリダイレクトする

@login_required
# デコレータでviewをログインユーザーのみに表示
def users_clothes_category(request, pk, category):
    cate = Category.objects.all()
    # category項目を全部取得
    user = get_object_or_404(User, pk=pk)
    # pkに紐づいたuserを取得。なければHttp404を送出
    category = Category.objects.get(title=category)
    # categoryからtitleを取得
    clothess = user.clothes_set.all().filter(category=category).order_by('-date_of_purchase')
    # userに紐づいているclothesをcategoryでfilterかけてdate_of_purchase順に並び替え
    return render(request, 'closet/users_detail.html', {'user': user, 'clothess': clothess, 'category':category,'cate':cate})
    # users_clothes_categoryが呼び出された場合、user, clothess, category, cateを載せてusers_detail.htmlを返す
