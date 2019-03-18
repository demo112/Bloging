from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegisterForm


# Create your views here.
def user_login(request):
    if request.method == "POST":
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            # .cleaned_data 清洗出合法数据
            data = user_login_form.cleaned_data
            # 检验账号、密码是否正确匹配数据库中的某个用户
            # 如果均匹配则返回这个 user 对象
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                # 将用户数据保存在 session 中，即实现了登录动作
                login(request, user)
                return redirect("article:article_list")
            else:
                # todo 使用ajax实现页面内校验, 返回来时页面
                return redirect('article:article_list')
    elif request.method == "GET":
        if request.session:
            return redirect('article:article_list')
        else:
            user_login_form = UserLoginForm()
            context = {'form': user_login_form}
            return render(request, 'userprofile/login.html', context)
    else:
        return redirect('err/err_method')


def user_logout(request):
    logout(request)
    return redirect("article:article_list")


def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            new_user.set_password(user_register_form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            # todo 返回来源页面
            return redirect('article:article_list')
        else:
            # todo Ajax动态加载
            return HttpResponse("注册表单输入有误。请重新输入~")
    elif request.method == 'GET':
        user_register_form = UserRegisterForm()
        context = {'user_register_form': user_register_form}
        return render(request, 'userprofile/register.html', context)
    else:
        return redirect('err/err_method')


@login_required(login_url='/userprofile/login/')
def user_delete(request, user_id):
    """高危操作谨慎使用"""
    user = User.objects.get(id=user_id)
    if request.user == user:
        logout(request)
        # todo 此处可以设置为用户状态改变
        user.delete()
        return redirect('article:article_list')
    else:
        return redirect("err:no_right")
