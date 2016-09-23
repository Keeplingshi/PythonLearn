# coding=utf-8

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from polls.models import Questionnaire


# 验证登录
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/polls/admin')
        else:
            print("Your account has been disabled!")
    else:
        # 如果存在用户名密码，但不正确，则提示
        if username is not None and password is not None:
            context = {'isSuccess': 1}
            return render(request, 'polls/login.html', context)

        return render(request, 'polls/login.html')


# 退出登录
def logout(request):
  auth.logout(request)
  return HttpResponseRedirect("/polls/login")


# 修改密码页面
@login_required
def modify_password_view(request):
    user = auth.get_user(request)
    context = {'user': user}
    return render(request, 'polls/modifyPasswordView.html', context)


# 修改密码
@login_required
def modify_password(request):
    user = auth.get_user(request)
    old_password = request.POST.get('old_password')
    new_password = request.POST.get('password')
    if User.check_password(user, old_password):
        User.set_password(user, new_password)
        User.save(user)
        # 重新登录
        auth.login(request, user)
        return HttpResponse("success")

    return HttpResponse("error")


# 账号管理页面
@csrf_exempt
def user_list(request):
    search_text = request.POST.get('searchText')
    if search_text is not None:
        users = User.objects.all().filter(username__contains=search_text)
    else:
        users = User.objects.all()
    paginator = Paginator(users, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(1)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'polls/user/userList.html', {'userList': users, 'searchText': search_text})
